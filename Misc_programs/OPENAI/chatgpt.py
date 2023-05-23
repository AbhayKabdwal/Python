import openai
import time

openai.api_key = '' #Enter your API key here

while True:
    try:
        question = input("Ques: ")

        response = openai.Completion.create(
            model = 'text-davinci-003',
            prompt = question,
            temperature = 0.5,
            max_tokens = 512,
            top_p = 1,
            frequency_penalty = 0.0,
            presence_penalty = 0.0,
        )

        message = response['choices'][0]['text']

        for char in message:
            print(char, end='', flush=True)
            time.sleep(0.02)
        
        print("\n")

        if question == "exit":
            break
    
    #Handle authentication error here, e.g. retry or log
    except openai.error.AuthenticationError as e:
        print(f"OpenAI API authentication failed: {e}")
        pass
    
    #Handle API error here, e.g. retry or log
    except openai.error.APIError as e:
        print(f"OpenAI API returned an API Error: {e}")
        pass
    
    #Handle connection error here
    except openai.error.APIConnectionError as e:
        print(f"Failed to connect to OpenAI API: {e}")
        pass

    #Handle rate limit error (we recommend using exponential backoff)
    except openai.error.RateLimitError as e:
        print(f"OpenAI API request exceeded rate limit: {e}")
        pass