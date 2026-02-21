#TASK 1
##AI Memory Retrieval System
  
This project implements a simple AI memory system that can:

1:Store user memories
2:Convert memories into embeddings
3:Retrieve the most relevant memory when a query is asked
4:Evaluate performance using Top-K metrics
5:The system simulates how a conversational AI remembers past information and retrieves it when needed.

 Architecture:

The system has four main components:

1️: Memory Storage
-Each memory is converted into an embedding using Gemini API.
-The embedding is stored together with the original text.
-Memories are saved locally (using JSON file).

2️:Embedding Generation
-When a memory or query is added, we generate a vector embedding using the Gemini embedding model.
-Embeddings convert text into numerical vectors.
-Similar meanings produce similar vectors.

3️:Memory Retrieval
-When a user asks a question:
-The query is converted into an embedding.
-Cosine similarity is calculated between the query and stored memories.
-Memories are ranked by similarity score.
-The top_k most similar memories are returned.
-We use cosine similarity because it is simple and effective for comparing vectors.

 Tradeoffs Made:
   Simple Local Storage
-We used local JSON storage instead of a vector database (like FAISS).

Tradeoff:
-Easy to implement
-Not scalable for large datasets

 Cosine Similarity Only
-We used cosine similarity without reranking.

Tradeoff:
-Simple and fast
-May not perform well for complex semantic queries

 Small Dataset
-We tested on a small set of memories.

Tradeoff:
-Easier to achieve high accuracy
-Does not reflect real-world scale

What I Would Improve With More Time

If given more time, I would:
1:Use a real vector database (FAISS or Chroma) for scalability.
2:Add re-ranking using a cross-encoder model.
3:Improve evaluation with more challenging queries.
4:Add memory updating and deletion features.

 Conclusion:
This project demonstrates a basic but functional AI memory retrieval system using embeddings and similarity search. While simple, it shows how conversational AI systems can store and recall information effectively.

#TASK 2- Memory Quality Evaluation

The goal of Task 2 is to measure how well the memory system retrieves the correct information when given a query.
We built an evaluation script (evaluator.py) that automatically tests the system using predefined memories and queries.

Test Dataset

We created:
10 stored memories (facts)
10 test queries
Each query is mapped to the correct memory using an ID.
Example:
Memory:My favourite food is pasta
Query: Which food i like most?
Expected result: My favourite food is pasta.

How Evaluation Works

For each query:
-The query is converted into an embedding.
-The system retrieves the top_k most similar memories.
-The retrieved results are compared with the expected correct memory.
-Scores are calculated.
-Results are printed in the console for each query.

Metrics Used
1️: Top-1 Accuracy
Checks whether the correct memory is the first result returned.
Formula:
Accuracy = Correct Top-1 Predictions / Total Queries
Why chosen:
-It measures strict retrieval performance.
-If the correct answer is ranked first, the system is highly accurate.

2️:Top-K Hit Rate (K = 3)
Checks whether the correct memory appears anywhere in the top 3 results.
Formula:
Top-K Hit Rate = Queries where correct memory is in top K / Total Queries
Why chosen:
-In real systems, the correct memory does not always need to be first.
-Being in the top few results is still useful.

Results

Example output:
Top-1 Accuracy:0.90
Top-3 Hit Rate:1.00

What Worked Well:
1:Direct factual queries worked very well.
2:Cosine similarity correctly matched related sentences.
3:Small dataset made retrieval precise.

 What Failed / Limitations
1:System works best when queries are similar to stored memory wording.
2:Small dataset makes evaluation easier.
3:No advanced reranking model.
4:No handling of ambiguous queries.
5:Performance may drop with larger datasets.