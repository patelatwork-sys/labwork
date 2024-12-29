from apim import GeminiAI

def main():
    ai = GeminiAI('gemini-1.5-flash',use_azure=True) # With Azure APIM
    response = ai.generate_response("What is Python?")
    print(response)
    print("----------------------------------------------")
    ai = GeminiAI('gemini-1.5-flash') # Without Azure APIM
    response = ai.generate_response("What is Python?")
    print(response)

if __name__ == "__main__":
    main()