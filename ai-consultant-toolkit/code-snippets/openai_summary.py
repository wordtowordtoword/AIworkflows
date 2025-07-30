import openai

openai.api_key = "your-api-key"

def summarize_text(text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Summarize the following:\n{text}"}]
    )
    return response.choices[0].message["content"]

# Example
print(summarize_text("Your long business document text goes here."))
