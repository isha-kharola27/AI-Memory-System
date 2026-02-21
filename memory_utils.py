import numpy as np
import os
import json
from sklearn.metrics.pairwise import cosine_similarity

MEMORY_FILE = "memory.json"

def load_memories():
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_memories(memories):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memories, f)

def get_embedding(client, text):
    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )
    return np.array(response.embeddings[0].values)

def store_memory(client, text):
    memories = load_memories()
    embedding = get_embedding(client, text).tolist()

    memories.append({
        "text": text,
        "embedding": embedding
    })

    save_memories(memories)

def retrieve_memories(client, query, top_k=3):
    memories = load_memories()
    if not memories:
        return []

    query_embedding = get_embedding(client, query).reshape(1, -1)

    scores = []
    for memory in memories:
        mem_embedding = np.array(memory["embedding"]).reshape(1, -1)
        score = cosine_similarity(query_embedding, mem_embedding)[0][0]
        scores.append((score, memory["text"]))

    scores.sort(reverse=True, key=lambda x: x[0])

    return [text for score, text in scores[:top_k] if score > 0.6]
