#!/usr/bin/env python3
from openai import OpenAI
import os
import sys
import json
from datetime import datetime

def list_models(api_key=None):
    # Get API key from argument or environment
    api_key = api_key or os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        print("Error: OpenAI API key not found!")
        print("Please either:")
        print("1. Set the OPENAI_API_KEY environment variable")
        print("2. Pass the API key as an argument: ./list_models.py YOUR_API_KEY")
        sys.exit(1)
    
    try:
        client = OpenAI(api_key=api_key)
        models = client.models.list()
        
        # Sort models by ID for easier reading
        sorted_models = sorted(models.data, key=lambda x: x.id)
        
        # Print models in a formatted way
        print("\nAvailable OpenAI Models:")
        print("=" * 80)
        print(f"{'Model ID':<40} {'Created':<20} {'Owner':<20}")
        print("=" * 80)
        
        gpt_models = []
        for model in sorted_models:
            created = datetime.fromtimestamp(model.created).strftime('%Y-%m-%d')
            if model.id.startswith('gpt'):
                gpt_models.append(model)
            print(f"{model.id:<40} {created:<20} {model.owned_by:<20}")
        
        print("\nGPT Models Available:")
        print("=" * 80)
        for model in sorted(gpt_models, key=lambda x: x.id):
            created = datetime.fromtimestamp(model.created).strftime('%Y-%m-%d')
            print(f"{model.id:<40} {created:<20} {model.owned_by:<20}")
            
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    api_key = sys.argv[1] if len(sys.argv) > 1 else None
    list_models(api_key)
