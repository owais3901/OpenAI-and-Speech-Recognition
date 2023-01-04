import os
import openai

openai.api_key = "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"
start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

def chat(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    text = response
    return text["choices"][0]["text"]