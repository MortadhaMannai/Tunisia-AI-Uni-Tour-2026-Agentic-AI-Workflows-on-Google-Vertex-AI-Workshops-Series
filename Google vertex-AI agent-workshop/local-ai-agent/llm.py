import ollama

def call_llm(prompt):
    """
    This function sends a prompt to the local LLM and returns the output.
    """
    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response["message"]["content"]
