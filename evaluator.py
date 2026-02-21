from memory_utils import store_memory, retrieve_memories
from test_data import test_memories, test_queries

from google import genai
from dotenv import load_dotenv
import os


load_dotenv()


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def run_evaluation(top_k=3):

    print("----- STORING TEST MEMORIES -----")

    for memory in test_memories:
        store_memory(client, memory["text"])

    correct_top1 = 0
    correct_topk = 0
    total = len(test_queries)

    print("\n----- EVALUATION START -----")

    for test in test_queries:
        query = test["query"]
        expected_id = test["expected_id"]

       
        expected_text = next(
            m["text"] for m in test_memories if m["id"] == expected_id
        )

      
        results = retrieve_memories(client, query, top_k=top_k)
        


        if not isinstance(results, list):
            results = [results]

        
        if results and results[0] == expected_text:
            correct_top1 += 1

      
        if expected_text in results:
            correct_topk += 1

        print(f"\nQuery: {query}")
        print(f"Expected: {expected_text}")
        print(f"Retrieved: {results}")

    
    top1_accuracy = correct_top1 / total
    topk_accuracy = correct_topk / total

    print("\n----- FINAL RESULTS -----")
    print(f"Top-1 Accuracy: {top1_accuracy:.2f}")
    print(f"Top-{top_k} Hit Rate: {topk_accuracy:.2f}")


if __name__ == "__main__":
    run_evaluation(top_k=3)
