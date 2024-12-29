import os
import requests
from dotenv import load_dotenv
import google.generativeai as genai

class GeminiAI:
    def __init__(self, model, use_azure=False):
        # Load environment variables
        load_dotenv()

        #set the model
        self.model = model
        
        # Get API keys and endpoints
        self.api_key = os.getenv('GEMINI_API_KEY')
        self.azure_endpoint = os.getenv('AZURE_APIM_ENDPOINT')
        self.azure_subscription_key = os.getenv('AZURE_APIM_SUBSCRIPTION_KEY')
        
        self.use_azure = use_azure
        
        if not use_azure:
            # Direct Gemini configuration
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel(self.model)
    
    def generate_response(self, prompt):
        """Generate response for given prompt"""
        if self.use_azure:
            return self._generate_via_azure(prompt)
        return self._generate_via_gemini(prompt)
    
    def _generate_via_gemini(self, prompt):
        """Direct Gemini API call"""
        response = self.model.generate_content(prompt)
        return response.text
    
    def _generate_via_azure(self, prompt):
        """Azure APIM call"""
        headers = {
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': self.azure_subscription_key
        }
        
        payload = {
            "contents": [{"parts":[{"text": prompt}]}]
        }
        
        response = requests.post(
            self.azure_endpoint,
            headers=headers,
            json=payload
        )
        
        if response.status_code == 200:
            return response.json()['candidates'][0]['content']['parts'][0]['text']
        else:
            raise Exception(f"Azure APIM request failed: {response.status_code}")