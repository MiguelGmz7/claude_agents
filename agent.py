from connection import openai_client

def run_agent(query="What is an LLM?"):
    """Run the agent with a query using OpenAI client."""
    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful searching assistant. Provide accurate answers to questions."
            },
            {
                "role": "user",
                "content": query
            }
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    result = run_agent("What is an LLM?")
    print(result)
