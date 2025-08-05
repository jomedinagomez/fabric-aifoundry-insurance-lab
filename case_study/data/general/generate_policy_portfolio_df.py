#!/usr/bin/env python3
"""
Production-Scale Azure AI Foundry Structured Output Insurance Policy Dataset Generation
=====================================================================================

This script generates a comprehensive 750-record insurance policy portfolio using 
Azure AI Foundry's structured output with Pydantic models for type-safe, reproducible data generation.

Key Features:
- Azure AI Foundry Structured Output: Uses Pydantic models for type-safe, reproducible data generation
- Claims-Aware Generation: Policies generated with characteristics that support 
  realistic future claims analysis
- Production Scale: 750 policies for enterprise-level analytics demonstrations
- Real-time Distribution Control: Feedback system ensures 80%+ target compliance
- Enhanced Analytics Schema: 23 fields supporting comprehensive business scenarios
- Status Correlation Logic: Policy characteristics align with current status 
  (lapsed/terminated policies have claim-predictive attributes)
"""

# OpenAI SDK setup with Pydantic structured output and Entra ID authentication
import os
import pandas as pd
import numpy as np
import json
from typing import List, Optional, Literal
from datetime import datetime, date
from pydantic import BaseModel, Field, field_validator
from dotenv import load_dotenv
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

# Load environment variables from .env file
load_dotenv()

# Pydantic models for structured output with integrated requirements
class PolicyRecord(BaseModel):
    """Pydantic model for a single insurance policy record with validation."""
    
    # Core policy information
    policy_id: str = Field(..., description="Policy ID in format LIF-####", pattern=r"^LIF-\d{4}$")
    occupation: str = Field(..., description="Policyholder occupation (exclude law enforcement/military)")
    age: int = Field(..., ge=18, le=80, description="Policyholder age between 18-80")
    coverage_amount: float = Field(..., ge=25000, le=15000000, description="Coverage amount between $25K-$15M")
    premium: float = Field(..., gt=0, description="Annual premium amount")
    policy_type: Literal["Term Life", "Whole Life", "Universal Life"] = Field(..., description="Type of life insurance policy")
    issue_date: str = Field(..., description="Policy issue date in YYYY-MM-DD format", pattern=r"^\d{4}-\d{2}-\d{2}$")
    risk_rating: Literal["A", "B", "C", "D", "E"] = Field(..., description="Risk rating from A (lowest) to E (highest)")
    medical_exam_required: Literal["Yes", "No"] = Field(..., description="Yes when coverage_amount >= $500,000")
    state: str = Field(..., min_length=2, max_length=2, description="US state abbreviation")
    annual_income: float = Field(..., ge=30000, le=2000000, description="Annual income between $30K-$2M")
    health_status: Literal["Excellent", "Good", "Fair", "Poor"] = Field(..., description="Health status")
    smoking_status: Literal["Smoker", "Non-Smoker"] = Field(..., description="Smoking status")
    beneficiary_relationship: Literal["Spouse", "Child", "Parent", "Other"] = Field(..., description="Relationship to beneficiary")
    payment_frequency: Literal["Monthly", "Quarterly", "Annual"] = Field(..., description="Premium payment frequency")
    
    # Enhanced analytics fields  
    policy_status: Literal["Active", "Lapsed", "Terminated", "Suspended"] = Field(..., description="Current policy status")
    underwriter_id: str = Field(..., description="Underwriter ID in format UW## (e.g., UW01, UW02, UW15)", pattern=r"^UW\d{2}$")
    agent_id: str = Field(..., description="Agent ID in format AGT## (e.g., AGT01, AGT02, AGT30)", pattern=r"^AGT\d{2}$")
    last_premium_paid_date: str = Field(..., description="Last premium payment date", pattern=r"^\d{4}-\d{2}-\d{2}$")
    policy_value: float = Field(..., ge=0, description="Current policy cash value (0 for term life)")
    region: Literal["Northeast", "Southeast", "Midwest", "Southwest", "West"] = Field(..., description="Geographic region based on state")
    application_channel: Literal["Agent", "Online", "Broker", "Direct Mail", "Phone"] = Field(..., description="Application channel")
    explanation: Optional[str] = Field(default="", description="Explanation for notable cases (usually empty)")

    @field_validator('policy_id')
    @classmethod
    def validate_policy_id(cls, v):
        # Check format: LIF-#### (should be exactly 8 characters)
        if not v.startswith('LIF-') or len(v) != 8:
            raise ValueError('Policy ID must be in format LIF-####')
        # Check that the ending is 4 digits
        if not v[4:].isdigit():
            raise ValueError('Policy ID must be in format LIF-####')
        return v

    @field_validator('underwriter_id')
    @classmethod
    def validate_underwriter_id(cls, v):
        # Must be exactly UW## format (4 characters total)
        if not v.startswith('UW') or len(v) != 4 or not v[2:].isdigit():
            raise ValueError('Underwriter ID must be UW## (e.g., UW01, UW15)')
        # Check range 01-15
        num = int(v[2:])
        if num < 1 or num > 15:
            raise ValueError('Underwriter ID must be UW01-UW15')
        return v

    @field_validator('agent_id')
    @classmethod
    def validate_agent_id(cls, v):
        # Must be exactly AGT## format (5 characters total)
        if not v.startswith('AGT') or len(v) != 5 or not v[3:].isdigit():
            raise ValueError('Agent ID must be AGT## (e.g., AGT01, AGT30)')
        # Check range 01-30
        num = int(v[3:])
        if num < 1 or num > 30:
            raise ValueError('Agent ID must be AGT01-AGT30')
        return v

class PolicyBatch(BaseModel):
    """Pydantic model for a batch of policy records."""
    policies: List[PolicyRecord] = Field(
        ..., 
        description="""
List of insurance policy records that must follow these GENERATION REQUIREMENTS:

CORE REQUIREMENTS:
- Ages 18-80, occupations across professional, management, skilled, service, high-risk classes
- EXCLUDE law enforcement (police, sheriff, security), military, and defense-related occupations
- Policy IDs in format: 'LIF-####' (e.g., LIF-1001, LIF-2342)
- Coverage amounts between $25,000 and $15,000,000
- Issue dates between 2018-01-01 and 2024-12-31 (prioritize 60% older policies 2018-2021)
- Medical exam required when coverage_amount >= $500,000
- Include state (US states), annual_income ($30K-$2M), health_status (Excellent/Good/Fair/Poor)
- Include smoking_status (Smoker/Non-Smoker), beneficiary_relationship (Spouse/Child/Parent/Other)
- Include payment_frequency (Monthly/Quarterly/Annual)

CLAIMS-AWARE POLICY GENERATION:
- Lapsed Policies (~10%): Generate with higher-risk characteristics (occupations D-E, older ages, payment gaps)
- Terminated Policies (~3%): Include medical conditions or high-risk activities that justify termination
- Suspended Policies (~2%): Generate with payment compliance issues or recent premium gaps
- Active Policies (~85%): Mix of risk profiles with current payment activity patterns

ENHANCED ANALYTICS FIELDS:
- policy_status: 85% Active, 10% Lapsed, 3% Terminated, 2% Suspended
- underwriter_id: Distribute across UW01-UW15 (15 underwriters) - EXACTLY UW01, UW02, UW03... UW15 format
- agent_id: Distribute across AGT01-AGT30 (30 agents) - EXACTLY AGT01, AGT02, AGT03... AGT30 format
- last_premium_paid_date: Recent dates for Active policies, older for Lapsed/Terminated
- policy_value: $0 for Term Life, realistic cash values for Whole/Universal Life
- region: Northeast/Southeast/Midwest/Southwest/West based on state
- application_channel: 40% Agent, 25% Online, 20% Broker, 10% Direct Mail, 5% Phone

CRITICAL FORMAT REQUIREMENTS:
- policy_id: MUST be LIF-#### (exactly 4 digits after dash, e.g., LIF-1001, LIF-2342)
- All dates: MUST be YYYY-MM-DD format
- underwriter_id: MUST be exactly 4 characters like UW01, UW02, UW03, etc.
- agent_id: MUST be exactly 5 characters like AGT01, AGT02, AGT03, etc.

RISK STRATIFICATION for Future Claims Analysis:
- Ensure sufficient high-risk occupations (classes D-E) for realistic claim generation
- Include older policies with appropriate aging for natural claim patterns
- Align premium payment patterns with policy status for logical claim correlation
        """
    )

print("OpenAI Azure SDK with Entra ID Authentication Setup")
print("=" * 60)

# Configuration for Azure OpenAI with Entra ID authentication
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
model_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4o-mini")

print(f"Endpoint: {endpoint}")
print(f"Model: {model_name}")
print(f"Authentication: Entra ID (DefaultAzureCredential)")
print()

# Set up Entra ID token provider
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
)

# Instantiate Azure OpenAI client with Entra ID authentication
client = AzureOpenAI(
    azure_endpoint=endpoint,
    azure_ad_token_provider=token_provider,
    api_version="2024-10-21"
)

print("Azure OpenAI client initialized successfully with Entra ID authentication")
print()

# Enhanced Schema for policy_portfolio.csv - derived from Pydantic model
schema = [
    # Core policy information
    "policy_id", "occupation", "age", "coverage_amount", "premium", "policy_type",
    "issue_date", "risk_rating", "medical_exam_required", "state", "annual_income",
    "health_status", "smoking_status", "beneficiary_relationship", "payment_frequency",
    
    # Enhanced analytics fields for workshop demonstrations
    "policy_status", "underwriter_id", "agent_id", "last_premium_paid_date",
    "policy_value", "region", "application_channel", "explanation"
]

def pydantic_to_dataframe(policy_batch: PolicyBatch) -> pd.DataFrame:
    """Convert a PolicyBatch Pydantic model to a pandas DataFrame."""
    records = []
    for policy in policy_batch.policies:
        record = {
            'policy_id': policy.policy_id,
            'occupation': policy.occupation,
            'age': policy.age,
            'coverage_amount': policy.coverage_amount,
            'premium': policy.premium,
            'policy_type': policy.policy_type,
            'issue_date': policy.issue_date,
            'risk_rating': policy.risk_rating,
            'medical_exam_required': policy.medical_exam_required,
            'state': policy.state,
            'annual_income': policy.annual_income,
            'health_status': policy.health_status,
            'smoking_status': policy.smoking_status,
            'beneficiary_relationship': policy.beneficiary_relationship,
            'payment_frequency': policy.payment_frequency,
            'policy_status': policy.policy_status,
            'underwriter_id': policy.underwriter_id,
            'agent_id': policy.agent_id,
            'last_premium_paid_date': policy.last_premium_paid_date,
            'policy_value': policy.policy_value,
            'region': policy.region,
            'application_channel': policy.application_channel,
            'explanation': policy.explanation or ""
        }
        records.append(record)
    
    return pd.DataFrame(records)

# Load underwriting guidelines
import glob
guidelines = ""
guidelines_dir = os.path.join(os.path.dirname(__file__), "..", "..", "underwriting_guidelines")

print("Loading Underwriting Guidelines")
print("=" * 60)
guideline_files = glob.glob(os.path.join(guidelines_dir, "*.md"))
print(f"Found {len(guideline_files)} guideline files:")

for md_file in guideline_files:
    filename = os.path.basename(md_file)
    print(f"  {filename}")
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
        guidelines += f"# {filename}\n" + content + "\n\n"
        print(f"    Loaded {len(content.splitlines())} lines")

print(f"Total guidelines content: {len(guidelines)} characters")
print()

# Build prompt using the comprehensive guidelines
prompt = f"""
You are a data generation assistant. Using the following comprehensive underwriting guidelines, generate realistic policy records following the PolicyBatch schema requirements.

Comprehensive Underwriting Guidelines:
{guidelines}

The PolicyBatch model contains all generation requirements in the policies field description. Follow these requirements precisely for realistic insurance policy generation.
"""

# Configure batch generation - PRODUCTION SCALE
total_records = 750  # Production-scale dataset for enterprise-level analytics
batch_size = 25  # Optimized batch size for efficient generation
all_dataframes = []  # Store DataFrames converted from Pydantic models
feedback_interval = 1  # Provide distribution feedback every batch (real-time control)

print("Enhanced OpenAI Azure SDK with Entra ID Authentication Configuration (PRODUCTION SCALE)")
print("=" * 70)
print(f"Total records to generate: {total_records}")
print(f"Batch size: {batch_size} (optimized for Azure OpenAI structured output)")
print(f"Number of batches: {(total_records + batch_size - 1) // batch_size}")
print(f"Feedback interval: Every batch (real-time distribution correction)")
print(f"Estimated generation time: ~10-15 minutes")
print(f"Using OpenAI Azure SDK with Entra ID auth and Pydantic structured output")
print()

def analyze_current_distributions(dataframes, print_summary=False):
    """Analyze current distributions and return feedback for next batches."""
    if not dataframes:
        return ""
    
    # Combine current data
    current_df = pd.concat(dataframes, ignore_index=True)
    n_records = len(current_df)
    
    # Analyze policy status
    status_counts = current_df['policy_status'].value_counts()
    status_percentages = {status: (count / n_records * 100) for status, count in status_counts.items()}
    
    # Analyze application channel
    channel_counts = current_df['application_channel'].value_counts()
    channel_percentages = {channel: (count / n_records * 100) for channel, count in channel_counts.items()}
    
    # Print summary if requested (for final output)
    if print_summary:
        print(f"   Policy status distribution:")
        for status, count in status_counts.items():
            percentage = (count / n_records) * 100
            print(f"     {status}: {count} ({percentage:.1f}%)")
        
        print(f"   Application channel distribution:")
        for channel, count in channel_counts.items():
            percentage = (count / n_records) * 100
            print(f"     {channel}: {count} ({percentage:.1f}%)")
        return current_df  # Return the combined dataframe for other analyses
    
    # Build feedback for next batches
    feedback = "\n\nCRITICAL DISTRIBUTION ADJUSTMENTS REQUIRED FOR NEXT BATCH:\n"
    feedback += "STRICT COMPLIANCE with target distributions is required:\n\n"
    
    # Policy Status Feedback - More aggressive
    feedback += "Policy Status (MANDATORY ADJUSTMENTS):\n"
    current_active = status_percentages.get('Active', 0)
    current_lapsed = status_percentages.get('Lapsed', 0)
    current_terminated = status_percentages.get('Terminated', 0)
    current_suspended = status_percentages.get('Suspended', 0)
    
    # Calculate exact adjustments needed
    active_diff = 85 - current_active
    lapsed_diff = 10 - current_lapsed
    terminated_diff = 3 - current_terminated
    suspended_diff = 2 - current_suspended
    
    feedback += f"- Active: Currently {current_active:.1f}% (Target: 85%) - ADJUST BY {active_diff:+.1f}% - Generate {'MORE' if active_diff > 0 else 'FEWER'} Active policies\n"
    feedback += f"- Lapsed: Currently {current_lapsed:.1f}% (Target: 10%) - ADJUST BY {lapsed_diff:+.1f}% - Generate {'MORE' if lapsed_diff > 0 else 'FEWER'} Lapsed policies\n"
    feedback += f"- Terminated: Currently {current_terminated:.1f}% (Target: 3%) - ADJUST BY {terminated_diff:+.1f}% - Generate {'MORE' if terminated_diff > 0 else 'FEWER'} Terminated policies\n"
    feedback += f"- Suspended: Currently {current_suspended:.1f}% (Target: 2%) - ADJUST BY {suspended_diff:+.1f}% - Generate {'MORE' if suspended_diff > 0 else 'FEWER'} Suspended policies\n"
    
    # Application Channel Feedback - More specific
    feedback += "\nApplication Channel (MANDATORY ADJUSTMENTS):\n"
    current_agent = channel_percentages.get('Agent', 0)
    current_online = channel_percentages.get('Online', 0)
    current_broker = channel_percentages.get('Broker', 0)
    current_direct_mail = channel_percentages.get('Direct Mail', 0)
    current_phone = channel_percentages.get('Phone', 0)
    
    agent_diff = 40 - current_agent
    online_diff = 25 - current_online
    broker_diff = 20 - current_broker
    direct_mail_diff = 10 - current_direct_mail
    phone_diff = 5 - current_phone
    
    feedback += f"- Agent: Currently {current_agent:.1f}% (Target: 40%) - ADJUST BY {agent_diff:+.1f}%\n"
    feedback += f"- Online: Currently {current_online:.1f}% (Target: 25%) - ADJUST BY {online_diff:+.1f}%\n"
    feedback += f"- Broker: Currently {current_broker:.1f}% (Target: 20%) - ADJUST BY {broker_diff:+.1f}%\n"
    feedback += f"- Direct Mail: Currently {current_direct_mail:.1f}% (Target: 10%) - ADJUST BY {direct_mail_diff:+.1f}%\n"
    feedback += f"- Phone: Currently {current_phone:.1f}% (Target: 5%) - ADJUST BY {phone_diff:+.1f}%\n"
    
    feedback += f"\nIMPERATIVE: In the next {30} records, prioritize generating:\n"
    if active_diff > 5:
        feedback += f"- MAJORITY Active policies (at least {int(30 * 0.85)} out of {30})\n"
    if lapsed_diff < -5:
        feedback += f"- MINIMIZE Lapsed policies (maximum {int(30 * 0.10)} out of {30})\n"
    if agent_diff > 5:
        feedback += f"- MORE Agent channel applications (at least {int(30 * 0.40)} out of {30})\n"
    
    feedback += "\nSTRICT COMPLIANCE: Follow these exact distribution targets in the next batch generation.\n"
    
    return feedback

def generate_policy_batch(client: AzureOpenAI, prompt: str, distribution_feedback: str, rows: int) -> pd.DataFrame:
    """Generate a batch of policies using Azure OpenAI with native structured output."""
    
    full_prompt = f"""
{prompt}

Generate exactly {rows} realistic insurance policy records that follow the underwriting guidelines and PolicyBatch requirements.

{distribution_feedback}

Important: Follow all requirements in the PolicyBatch schema, including distribution targets and claims-aware generation logic.
"""
    
    try:
        completion = client.beta.chat.completions.parse(
            model=model_name,
            messages=[
                {"role": "system", "content": """You are a precise insurance policy data generator. Generate realistic insurance policy data that strictly adheres to the PolicyBatch schema, underwriting guidelines, and distribution requirements. 

CRITICAL FORMAT EXAMPLES YOU MUST FOLLOW EXACTLY:
- policy_id: LIF-1001 (NOT LIF-20230415-123456 or LIF-001)
- underwriter_id: UW01 (NOT UW001 or UW1)  
- agent_id: AGT01 (NOT AGT001 or AGT1)
- All dates: 2023-04-15 (NOT 2023-4-15 or 04/15/2023)

When given distribution feedback, adjust the batch to meet the exact percentage targets specified."""},
                {"role": "user", "content": full_prompt}
            ],
            response_format=PolicyBatch,
        )
        
        # Extract the parsed PolicyBatch directly using the new pattern
        policy_batch = completion.choices[0].message.parsed
        
        if policy_batch and policy_batch.policies:
            return pydantic_to_dataframe(policy_batch)
        else:
            print(f"  Warning: No policies generated in this batch")
            return pd.DataFrame(columns=schema)
            
    except Exception as e:
        print(f"  Error generating batch: {e}")
        return pd.DataFrame(columns=schema)

# Batch loop for API calls with structured output
print("Starting OpenAI Azure SDK Structured Data Generation")
print("=" * 70)

for start in range(0, total_records, batch_size):
    rows = min(batch_size, total_records - start)
    batch_num = (start // batch_size) + 1
    total_batches = (total_records + batch_size - 1) // batch_size
    
    print(f"Batch {batch_num}/{total_batches}: Generating {rows} records (rows {start+1}-{start+rows})")
    progress_percent = (batch_num / total_batches) * 100
    print(f"  Progress: {progress_percent:.1f}% complete")
    
    # Add distribution feedback every batch (starting from batch 2)
    distribution_feedback = ""
    if batch_num > 1 and all_dataframes:  # Have previous data to analyze
        print(f"  Analyzing distributions from previous {batch_num-1} batch(es)...")
        distribution_feedback = analyze_current_distributions(all_dataframes)
        print(f"  Added distribution feedback for this batch")
    
    print(f"  Calling Azure OpenAI structured output API...")
    batch_df = generate_policy_batch(client, prompt, distribution_feedback, rows)
    
    if not batch_df.empty:
        all_dataframes.append(batch_df)
        print(f"  Generated {len(batch_df)} valid records with structured output")
    else:
        print(f"  No valid records generated from this batch")
    
    print(f"  Total DataFrames collected: {len(all_dataframes)}")
    print()

# Combine all DataFrames and save
print("Finalizing Dataset")
print("=" * 60)

if all_dataframes:
    # Combine all DataFrames
    final_df = pd.concat(all_dataframes, ignore_index=True)
    
    # Final data quality checks
    print(f"Combined DataFrame shape: {final_df.shape}")
    print(f"Data quality checks:")
    
    # Remove duplicates based on policy_id
    initial_count = len(final_df)
    final_df = final_df.drop_duplicates(subset=['policy_id'], keep='first')
    print(f"  Removed {initial_count - len(final_df)} duplicate policy IDs")
    
    # Ensure we don't exceed target
    if len(final_df) > total_records:
        final_df = final_df.head(total_records)
        print(f"  Trimmed to target {total_records} records")
    
    # Save to CSV
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'policy_portfolio.csv')
    final_df.to_csv(output_path, index=False, encoding='utf-8')
    
    print(f"Successfully saved to: {output_path}")
    print(f"Final dataset shape: {final_df.shape}")
    print(f"Columns: {list(final_df.columns)}")
    
    # Dataset summary using optimized analysis function
    print(f"\nDataset Summary:")
    print(f"   Records: {len(final_df)}")
    print(f"   Unique occupations: {final_df['occupation'].nunique()}")
    print(f"   Age range: {final_df['age'].min():.0f}-{final_df['age'].max():.0f}")
    print(f"   Coverage range: ${final_df['coverage_amount'].min():,.0f}-${final_df['coverage_amount'].max():,.0f}")
    
    # Use the same analysis function for final summary (avoid duplication)
    analyze_current_distributions([final_df], print_summary=True)
    
else:
    print("No valid data generated. Please check API configuration and guidelines.")

print("=" * 60)
print("Generation complete!")
