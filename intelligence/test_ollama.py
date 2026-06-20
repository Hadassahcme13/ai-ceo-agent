import ollama

response = ollama.chat(
    model="qwen2.5:3b",
    messages=[
        {
            "role": "user",
            "content": "What are NVIDIA's biggest opportunities?"
        }
    ]
)

print(response["message"]["content"])