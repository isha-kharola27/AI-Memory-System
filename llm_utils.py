def extract_memory(client, user_input):
    prompt = f"""
    Extract important long-term facts about the user from this message.
    Only return short factual memory statements.
    If nothing important, return NONE.

    Message: {user_input}
    """

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    result = response.text.strip()

    if result.upper() == "NONE":
        return []

    memories = [line.strip("- ").strip() for line in result.split("\n") if line.strip()]
    return memories


def generate_response(client, user_input, retrieved_memories):
    memory_text = "\n".join(retrieved_memories) if retrieved_memories else "No past memories."

    prompt = f"""
    You are a helpful AI assistant.

    Relevant past memories about the user:
    {memory_text}

    User question:
    {user_input}

    Use the memories if relevant to personalize the response.
    """

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    return response.text
