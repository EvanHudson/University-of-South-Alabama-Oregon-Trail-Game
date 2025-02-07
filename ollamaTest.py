
import ollama
"""
response = ollama.generate(
    model="deepseek-r1:1.5b",
    prompt="Respond with a sentence describing a scenario under 10 words",
    stream=False, 
    max_new_tokens = 10
)
print(response["response"])
"""
import ollama

#model = "deepseek-r1:1.5b"
model = "llama3.2:1b"
messages = []
while True:

    user_input = input("You: ")
    # Exit Condition
    if user_input.lower() == "exit":
        break
    # Response Initialization
    response = [
        {'role': 'user',
         'content': user_input},
        {'role': 'assistant',
         'content': ""},
    ]
    # Generating AI Responses
    for part in ollama.chat(model=model, messages=messages + [
        {"role": "user", "content": user_input}
    ], stream=True):
        # Processing AI Response
        print(part["message"]["content"], end='', flush=True)
        response[1]["content"] += part.message.content

    print()
    # Add the response to the messages to maintain the history
    messages += response
