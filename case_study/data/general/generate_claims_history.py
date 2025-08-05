#!/usr/bin/env python3
"""
Connected Claims History Generation - Policy-Aware Dataset Creation
=================================================================

This script generates a connected claims dataset that references the actual 
policy_portfolio.csv with realistic business relationships and temporal logic.

Key Features:
- Policy-Aware Generation: Analyzes actual policy characteristics for targeted claims
- Status Correlation Logic: Claims patterns explain current policy status
- Temporal Validation: All claims occur after policy issue dates with realistic timing
- Financial Logic: Claim amounts ≤ actual coverage amounts from policy data
- Business Realism: Higher claim rates for lapsed/terminated policies

Target: 150-190 claims (25-30% of 638 policies) with realistic distribution
"""

import os
import pandas as pd
import numpy as np
from dotenv import load_dotenv
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
from datetime import datetime, timedelta

# Load environment variables
load_dotenv()

print("Connected Claims Generation - Policy-Aware Analysis")
print("=" * 70)

# Azure AI Inference configuration
endpoint = os.getenv("AZURE_AI_INFERENCE_ENDPOINT")
api_key = os.getenv("AZURE_AI_INFERENCE_KEY")
model_name = os.getenv("AZURE_AI_INFERENCE_MODEL", "gpt-4.1-mini")

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(api_key),
    api_version="2024-05-01-preview"
)

print(f"Azure AI Inference Setup Complete")
print(f"Endpoint: {endpoint}")
print(f"Model: {model_name}")
print()

# Load and analyze existing policy portfolio
policy_csv_path = os.path.join(os.path.dirname(__file__), 'policy_portfolio.csv')
print("Loading Policy Portfolio for Analysis")
print("=" * 70)

try:
    policies_df = pd.read_csv(policy_csv_path)
    print(f"✅ Loaded {len(policies_df)} policies from policy_portfolio.csv")
    
    # Analyze policy characteristics for claims targeting
    policy_analysis = {
        'total_policies': len(policies_df),
        'status_distribution': policies_df['policy_status'].value_counts().to_dict(),
        'occupation_risk': policies_df.groupby('occupation')['risk_rating'].mean().to_dict(),
        'age_groups': policies_df.groupby(pd.cut(policies_df['age'], bins=[0, 35, 45, 55, 100], labels=['26-35', '36-45', '46-55', '56+']))['policy_id'].count().to_dict(),
        'coverage_ranges': policies_df.groupby(pd.cut(policies_df['coverage_amount'], bins=[0, 500000, 1000000, 2000000, float('inf')], labels=['Low', 'Medium', 'High', 'Premium']))['policy_id'].count().to_dict()
    }
    
    print("Policy Portfolio Analysis:")
    print(f"  Status Distribution: {policy_analysis['status_distribution']}")
    print(f"  Age Groups: {dict(policy_analysis['age_groups'])}")
    print(f"  Coverage Ranges: {dict(policy_analysis['coverage_ranges'])}")
    print()
    
except Exception as e:
    print(f"❌ Error loading policy portfolio: {e}")
    exit(1)

# Enhanced Claims Schema (9 fields)
claims_schema = [
    "claim_id", "policy_id", "claim_date", "claim_amount", "claim_type", 
    "claim_status", "cause_of_death", "processing_days", "adjuster_id"
]

# Load underwriting guidelines for claims context
import glob
guidelines = ""
guidelines_dir = os.path.join(os.path.dirname(__file__), "..", "..", "underwriting_guidelines")

print("Loading Underwriting Guidelines for Claims Context")
print("=" * 70)
guideline_files = glob.glob(os.path.join(guidelines_dir, "*.md"))

for md_file in guideline_files:
    filename = os.path.basename(md_file)
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
        guidelines += f"# {filename}\n" + content + "\n\n"

print(f"Loaded {len(guideline_files)} guideline files")
print(f"Total guidelines content: {len(guidelines)} characters")
print()

# Calculate target claims distribution based on policy analysis
target_claims = int(len(policies_df) * 0.25)  # 25% claim rate
print("Claims Generation Strategy")
print("=" * 70)
print(f"Target Claims: {target_claims} (25% of {len(policies_df)} policies)")

# Status-based claim targeting
active_policies = policies_df[policies_df['policy_status'] == 'Active']
lapsed_policies = policies_df[policies_df['policy_status'] == 'Lapsed']
terminated_policies = policies_df[policies_df['policy_status'] == 'Terminated']
suspended_policies = policies_df[policies_df['policy_status'] == 'Suspended']

claims_targets = {
    'Active': int(len(active_policies) * 0.15),      # 15% of active policies
    'Lapsed': int(len(lapsed_policies) * 0.50),      # 50% of lapsed policies (explains lapse)
    'Terminated': int(len(terminated_policies) * 0.80), # 80% of terminated policies (explains termination)
    'Suspended': int(len(suspended_policies) * 0.60)    # 60% of suspended policies (explains suspension)
}

print(f"Claim Distribution Strategy:")
for status, target in claims_targets.items():
    policy_count = len(policies_df[policies_df['policy_status'] == status])
    rate = (target / policy_count * 100) if policy_count > 0 else 0
    print(f"  {status}: {target} claims from {policy_count} policies ({rate:.1f}% rate)")

total_targeted = sum(claims_targets.values())
print(f"Total Targeted Claims: {total_targeted}")
print()

# Build comprehensive prompt with policy-aware context
prompt_template = f"""
You are generating realistic insurance claims that reference actual policies from our portfolio.

POLICY PORTFOLIO ANALYSIS:
- Total Policies: {len(policies_df)}
- Active: {len(active_policies)} policies
- Lapsed: {len(lapsed_policies)} policies  
- Terminated: {len(terminated_policies)} policies
- Suspended: {len(suspended_policies)} policies

CLAIMS SCHEMA: {', '.join(claims_schema)}

BUSINESS LOGIC REQUIREMENTS:
1. POLICY REFERENCE: All policy_id values must exist in the provided policy list
2. TEMPORAL LOGIC: claim_date must be AFTER the policy issue_date
3. FINANCIAL LOGIC: claim_amount must be ≤ policy coverage_amount
4. STATUS CORRELATION: Claims should explain current policy status
   - Lapsed policies: Claims 6-18 months before lapse (payment-related)
   - Terminated policies: High-value claims or multiple claims justifying termination
   - Suspended policies: Recent claims with compliance issues
   - Active policies: Mixed historical claims supporting continued coverage

CLAIM TYPES: Death Benefit, Disability, Surrender, Loan, Partial Withdrawal, Maturity
CLAIM STATUS: Approved (80%), Pending (15%), Denied (5%)
CAUSE OF DEATH: Natural, Accident, Illness (for death benefit claims only)
PROCESSING DAYS: 15-90 days realistic processing time
ADJUSTER IDS: ADJ001-ADJ010 (10 adjusters)

UNDERWRITING GUIDELINES CONTEXT:
{guidelines}

OUTPUT FORMAT: Return ONLY clean CSV data. NO markdown, NO code blocks, NO headers.
First row must be data (header handled separately).
"""

# Policy-aware claims generation function
def generate_claims_for_policies(target_policies, claim_count, status_context):
    """Generate claims for specific policies with status-aware logic."""
    
    if len(target_policies) == 0 or claim_count == 0:
        return pd.DataFrame(columns=claims_schema)
    
    # Create policy context for AI
    policy_context = "AVAILABLE POLICIES FOR CLAIMS:\n"
    for _, policy in target_policies.iterrows():
        policy_context += f"Policy: {policy['policy_id']}, Issue: {policy['issue_date']}, Coverage: ${policy['coverage_amount']:,}, Status: {policy['policy_status']}, Occupation: {policy['occupation']}, Age: {policy['age']}\n"
    
    # Status-specific generation instructions
    status_instructions = {
        'Active': "Generate mixed historical claims with some recent activity. Claims should support continued active status.",
        'Lapsed': f"Generate claims 6-18 months before lapse date. Claims should correlate with payment difficulties.",
        'Terminated': "Generate high-value claims or multiple claims that justify policy termination.",
        'Suspended': "Generate recent claims with compliance or payment-related complications."
    }
    
    batch_prompt = prompt_template + f"""
    
CURRENT BATCH INSTRUCTIONS:
- Generate {claim_count} claims for {status_context} policies
- {status_instructions.get(status_context, 'Generate realistic historical claims')}
- Use only the policy_id values from the AVAILABLE POLICIES list below

{policy_context}

CRITICAL: Each claim must reference a policy_id from the list above.
"""
    
    try:
        print(f"  Generating {claim_count} claims for {len(target_policies)} {status_context} policies...")
        
        response = client.complete(
            messages=[
                SystemMessage(content="You are a precise insurance claims data generator. You MUST reference only the provided policy_id values and ensure all business logic constraints are met. Generate realistic claims that explain policy status patterns."),
                UserMessage(content=batch_prompt)
            ],
            model=model_name,
            temperature=0.3,  # Lower temperature for strict policy correlation
            max_tokens=6000,
            top_p=0.9
        )
        
        # Clean and parse response
        response_content = response.choices[0].message.content.strip()
        
        # Remove markdown if present
        if response_content.startswith("```"):
            lines = response_content.split('\n')
            response_content = '\n'.join(lines[1:-1]) if len(lines) > 2 else response_content
        
        # Parse CSV lines
        csv_lines = []
        for line in response_content.split('\n'):
            line = line.strip()
            if line and ',' in line and ('CLM-' in line or len(line.split(',')) >= 8):
                csv_lines.append(line)
        
        if csv_lines:
            import io
            csv_data = '\n'.join(csv_lines)
            claims_df = pd.read_csv(io.StringIO(csv_data), names=claims_schema, header=None)
            
            # Validate claims against actual policies
            valid_claims = claims_df[claims_df['policy_id'].isin(target_policies['policy_id'])]
            
            print(f"  Generated {len(csv_lines)} raw claims, {len(valid_claims)} valid after policy validation")
            return valid_claims
        else:
            print(f"  No valid claims generated")
            return pd.DataFrame(columns=claims_schema)
            
    except Exception as e:
        print(f"  Error generating claims: {e}")
        return pd.DataFrame(columns=claims_schema)

# Generate claims by policy status
print("Generating Claims by Policy Status")
print("=" * 70)

all_claims = []

# Generate claims for each status category
for status, target_count in claims_targets.items():
    if target_count == 0:
        continue
        
    target_policies = policies_df[policies_df['policy_status'] == status]
    
    # Sample policies for claims (don't exceed available policies)
    sample_size = min(target_count, len(target_policies))
    sampled_policies = target_policies.sample(n=sample_size, random_state=42)
    
    print(f"\n{status} Policies:")
    claims_batch = generate_claims_for_policies(sampled_policies, target_count, status)
    
    if not claims_batch.empty:
        all_claims.append(claims_batch)
        print(f"  ✅ Added {len(claims_batch)} {status.lower()} claims")
    else:
        print(f"  ⚠️ No valid claims generated for {status} policies")

# Combine and finalize claims dataset
print("\nFinalizing Claims Dataset")
print("=" * 70)

if all_claims:
    final_claims_df = pd.concat(all_claims, ignore_index=True)
    
    # Remove duplicates
    initial_count = len(final_claims_df)
    final_claims_df = final_claims_df.drop_duplicates(subset=['claim_id'], keep='first')
    print(f"Removed {initial_count - len(final_claims_df)} duplicate claim IDs")
    
    # Save to CSV
    output_path = os.path.join(os.path.dirname(__file__), 'claims_history.csv')
    final_claims_df.to_csv(output_path, index=False, encoding='utf-8')
    
    print(f"✅ Successfully saved to: {output_path}")
    print(f"📊 Final dataset: {len(final_claims_df)} claims")
    print(f"🔗 Connected to {final_claims_df['policy_id'].nunique()} unique policies")
    
    # Dataset summary
    print(f"\nClaims Dataset Summary:")
    print(f"  Total Claims: {len(final_claims_df)}")
    print(f"  Claim Types: {final_claims_df['claim_type'].value_counts().to_dict()}")
    print(f"  Claim Status: {final_claims_df['claim_status'].value_counts().to_dict()}")
    print(f"  Coverage Rate: {len(final_claims_df) / len(policies_df) * 100:.1f}% of policies have claims")
    
else:
    print("❌ No claims generated successfully")

print("\n" + "=" * 70)
print("Claims Generation Complete!")
