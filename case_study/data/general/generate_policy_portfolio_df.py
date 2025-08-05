#!/usr/bin/env python3
"""
Improved Azure AI Inference-powered dataset generation script using pandas DataFrame.
This approach accumulates all data in memory before writing to avoid duplicate headers.
"""

# Azure AI Inference Client setup
import os
import pandas as pd
import numpy as np
from dotenv import load_dotenv
from azure.ai.inference import ChatCompletionsClient  # type: ignore
from azure.ai.inference.models import SystemMessage, UserMessage  # type: ignore
from azure.core.credentials import AzureKeyCredential

# Load environment variables from .env file
load_dotenv()

print("Azure AI Inference Setup (DataFrame Version)")
print("=" * 60)

# Configuration for Azure AI Inference
endpoint = os.getenv("AZURE_AI_INFERENCE_ENDPOINT")
api_key = os.getenv("AZURE_AI_INFERENCE_KEY")
model_name = os.getenv("AZURE_AI_INFERENCE_MODEL", "Phi-4")

print(f"Endpoint: {endpoint}")
print(f"Model: {model_name}")
print(f"API Key: {'*' * (len(api_key) - 8) + api_key[-8:] if api_key else 'Not found'}")
print()

# Instantiate Azure ChatCompletionsClient
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(api_key),
    api_version="2024-05-01-preview"
)

print("Azure AI Inference client initialized successfully")
print()

# Enhanced Schema for policy_portfolio.csv
schema = [
    # Core policy information
    "policy_id", "occupation", "age", "coverage_amount", "premium", "policy_type",
    "issue_date", "risk_rating", "medical_exam_required", "state", "annual_income",
    "health_status", "smoking_status", "beneficiary_relationship", "payment_frequency",
    
    # Enhanced analytics fields for workshop demonstrations
    "policy_status", "underwriter_id", "agent_id", "last_premium_paid_date",
    "policy_value", "region", "application_channel", "explanation"
]

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
You are a data generation assistant. Using the following comprehensive underwriting guidelines, generate realistic policy records in CSV format (no extra commentary).

Schema columns: {', '.join(schema)}

Comprehensive Underwriting Guidelines:
{guidelines}
"""

# Configure batch generation
total_records = 50  # Quick test run (was 750)
batch_size = 25  # records per batch - smaller for test
all_dataframes = []  # Store DataFrames instead of raw text

print("Generation Configuration")
print("=" * 60)
print(f"Total records to generate: {total_records}")
print(f"Batch size: {batch_size}")
print(f"Number of batches: {(total_records + batch_size - 1) // batch_size}")
print(f"Estimated generation time: ~2-3 minutes")
print(f"Using DataFrame approach for clean CSV output")
print()

# Build requirement template
requirements_template = (
    "Requirements:\n"
    "- Generate {rows} rows covering ages 18-80, occupations across professional, management, skilled, service, high-risk classes.\n"
    "- EXCLUDE law enforcement (police, sheriff, security), military, and defense-related occupations.\n"
    "- Use realistic policy_id format: 'LIF-YYYYMMDD-######' (e.g., LIF-20230615-123456).\n"
    "- Coverage amounts between $25,000 and $15,000,000.\n"
    "- Issue dates between 2018-01-01 and 2024-12-31.\n"
    "- Apply age factors, occupation multipliers, and comprehensive risk assessment from guidelines.\n"
    "- Include medical_exam_required as Yes when coverage_amount >= $500,000.\n"
    "- Include state (US states), annual_income ($30K-$2M), health_status (Excellent/Good/Fair/Poor).\n"
    "- Include smoking_status (Smoker/Non-Smoker), beneficiary_relationship (Spouse/Child/Parent/Other).\n"
    "- Include payment_frequency (Monthly/Quarterly/Annual).\n"
    "- Enhanced Analytics Fields:\n"
    "  * policy_status: 85% Active, 10% Lapsed, 3% Terminated, 2% Suspended\n"
    "  * underwriter_id: Distribute across UW001-UW015 (15 underwriters)\n"
    "  * agent_id: Distribute across AGT001-AGT030 (30 agents)\n"
    "  * last_premium_paid_date: Recent dates for Active policies, older for Lapsed/Terminated\n"
    "  * policy_value: $0 for Term Life, realistic cash values for Whole/Universal Life\n"
    "  * region: Northeast/Southeast/Midwest/Southwest/West based on state\n"
    "  * application_channel: 40% Agent, 25% Online, 20% Broker, 10% Direct Mail, 5% Phone\n"
    "- For 'explanation' field: Most records should be empty. Only provide explanations for notable cases.\n"
    "- OUTPUT FORMAT: Return ONLY clean CSV data with comma-separated values. NO markdown, NO code blocks.\n"
    "- First row must be data (not header), as header will be handled separately.\n"
)

def clean_csv_response(response_content):
    """Clean the API response to extract valid CSV lines."""
    print(f"  Raw API response preview: {response_content[:200]}...")
    
    # Remove markdown code blocks if present
    if response_content.startswith("```"):
        first_newline = response_content.find('\n')
        if first_newline != -1:
            response_content = response_content[first_newline + 1:]
        if response_content.endswith("```"):
            response_content = response_content[:-3].strip()
    
    # Filter out any remaining markdown artifacts or empty lines
    lines = []
    for line in response_content.splitlines():
        line = line.strip()
        print(f"  Checking line: {line[:50]}...")
        
        # More permissive filtering - accept lines that look like CSV data
        if (line and 
            not line.startswith("```") and 
            not line.startswith("#") and
            not line == "csv" and
            not line.startswith('"policy_id"') and  # Skip any headers
            not line.startswith('policy_id') and
            "," in line):  # Just need commas for CSV
            
            # Check if it looks like a policy record
            if ("LIF-" in line or len(line.split(",")) >= 20):  # Either has policy ID or enough columns
                lines.append(line)
                print(f"  Accepted line")
            else:
                print(f"  Rejected - doesn't look like policy data")
        else:
            print(f"  Rejected - basic filters")
    
    return lines

def parse_csv_lines_to_dataframe(lines, schema):
    """Parse CSV lines into a pandas DataFrame with proper column types."""
    import io
    import csv
    
    # Create a StringIO object to simulate file reading
    csv_data = '\n'.join(lines)
    csv_buffer = io.StringIO(csv_data)
    
    try:
        # Read CSV data
        reader = csv.reader(csv_buffer)
        rows = list(reader)
        
        # Create DataFrame
        df = pd.DataFrame(rows, columns=schema)
        
        # Basic data type conversions and validation
        if not df.empty:
            # Convert numeric columns
            numeric_columns = ['age', 'coverage_amount', 'premium', 'annual_income', 'policy_value']
            for col in numeric_columns:
                if col in df.columns:
                    df[col] = pd.to_numeric(df[col], errors='coerce')
            
            # Remove rows with critical missing data
            df = df.dropna(subset=['policy_id', 'occupation', 'age'])
            
            # Data quality checks
            df = df[df['age'].between(18, 80)]  # Reasonable age range
            df = df[df['coverage_amount'] > 0]  # Positive coverage
            
        return df
    
    except Exception as e:
        print(f"  Error parsing CSV data: {e}")
        return pd.DataFrame(columns=schema)

# Batch loop for API calls
print("Starting Data Generation (DataFrame Method)")
print("=" * 60)

for start in range(0, total_records, batch_size):
    rows = min(batch_size, total_records - start)
    batch_num = (start // batch_size) + 1
    total_batches = (total_records + batch_size - 1) // batch_size
    
    print(f"Batch {batch_num}/{total_batches}: Generating {rows} records (rows {start+1}-{start+rows})")
    progress_percent = (batch_num / total_batches) * 100
    print(f"  Progress: {progress_percent:.1f}% complete")
    
    batch_prompt = prompt + "\n" + requirements_template.format(rows=rows)
    
    try:
        print(f"  Calling Azure AI Inference API...")
        response = client.complete(
            messages=[
                SystemMessage(content="You are a CSV data generator. Always respond with pure CSV format only - no markdown, no code blocks, no headers, no explanations. Generate realistic insurance policy data according to the provided schema and guidelines."),
                UserMessage(content=batch_prompt)
            ],
            model=model_name,
            temperature=0.7,
            max_tokens=8000,
            top_p=0.95
        )
        
        # Clean the response content
        response_content = response.choices[0].message.content.strip()
        clean_lines = clean_csv_response(response_content)
        
        print(f"  Received {len(clean_lines)} clean CSV lines from API")
        
        # Parse into DataFrame
        batch_df = parse_csv_lines_to_dataframe(clean_lines, schema)
        
        if not batch_df.empty:
            all_dataframes.append(batch_df)
            print(f"  Added {len(batch_df)} valid records to DataFrame collection")
        else:
            print(f"  No valid records parsed from this batch")
        
        print(f"  Total DataFrames collected: {len(all_dataframes)}")
        
    except Exception as e:
        print(f"  Error in batch {batch_num}: {e}")
    
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
    
    # Dataset summary
    print(f"\nDataset Summary:")
    print(f"   Records: {len(final_df)}")
    print(f"   Unique occupations: {final_df['occupation'].nunique()}")
    print(f"   Age range: {final_df['age'].min():.0f}-{final_df['age'].max():.0f}")
    print(f"   Coverage range: ${final_df['coverage_amount'].min():,.0f}-${final_df['coverage_amount'].max():,.0f}")
    print(f"   Policy status distribution:")
    for status, count in final_df['policy_status'].value_counts().head().items():
        percentage = (count / len(final_df)) * 100
        print(f"     {status}: {count} ({percentage:.1f}%)")
    
else:
    print("No valid data generated. Please check API configuration and guidelines.")

print("=" * 60)
print("Generation complete!")
