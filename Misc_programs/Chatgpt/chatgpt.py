import openai
import time

openai.api_key = ''

question = input("Ques:  ")

response = openai.Completion.create(
    model = 'text-davinci-003',
    prompt = question,
    temperature = 0.1,
    max_tokens = 512,
    top_p = 1,
    frequency_penalty = 0.0,
    presence_penalty = 0.4,
)

message = response['choices'][0]['text']

for char in message:
    print(char, end='', flush=True)
    time.sleep(0.02)