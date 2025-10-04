from openai import OpenAI

# Create a client (it will read your API key from the environment variable)
client = OpenAI()

# Send a simple request to the ChatGPT model
response = client.chat.completions.create(
    model="gpt-4o-mini",  # you can also use gpt-4.1, gpt-3.5-turbo, etc.
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a short Python hello world program."}
    ]
)

# Print the model's reply
print(response.choices[0].message.content)
