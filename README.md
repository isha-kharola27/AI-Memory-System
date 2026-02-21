# TASK 1 – AI Memory Retrieval System

This project implements a simple AI memory system that can:

- Store user memories
- Convert memories into embeddings
- Retrieve the most relevant memory when a query is asked
- Evaluate performance using Top-K metrics
- Simulate how a conversational AI remembers past information and retrieves it when needed


## Architecture

The system consists of four main components:


### 1. Memory Storage

- Each memory is converted into an embedding using the Gemini API.
- The embedding is stored together with the original text.
- Memories are saved locally using a JSON file.


### 2. Embedding Generation

- Whenever a memory or query is added, a vector embedding is generated using the Gemini embedding model.
- Embeddings convert text into numerical vectors.
- Texts with similar meanings produce similar vector representations.


### 3. Memory Retrieval

When a user asks a question:

- The query is converted into an embedding.
- Cosine similarity is calculated between the query embedding and stored memory embeddings.
- Memories are ranked based on similarity scores.
- The top_k most similar memories are returned.

Cosine similarity was chosen because it is simple, efficient, and widely used for comparing vectors.


## Tradeoffs Made


### Simple Local Storage

We used local JSON storage instead of a vector database such as FAISS.

**Tradeoff:**

- Easy to implement
- Suitable for small projects
- Not scalable for large datasets


### Cosine Similarity Only

We used cosine similarity without any reranking mechanism.

**Tradeoff:**

- Simple and fast
- May not perform well for complex semantic queries
- No contextual reranking


### Small Dataset

The system was tested on a small set of memories.

**Tradeoff:**

- Easier to achieve high accuracy
- Does not reflect real-world scale
- Performance may decrease with larger datasets


## What I Would Improve With More Time

If given more time, I would:

1. Use a real vector database (FAISS or Chroma) for better scalability.
2. Add reranking using a cross-encoder model.
3. Improve evaluation with more challenging and diverse queries.
4. Add memory updating and deletion functionality.


## Conclusion

This project demonstrates a basic yet functional AI memory retrieval system using embeddings and similarity search.

Although simple, it illustrates how conversational AI systems can store, retrieve, and evaluate information effectively using vector-based representations.



# TASK 2 – Memory Quality Evaluation

The goal of Task 2 is to measure how effectively the memory system retrieves the correct information when given a query.

An evaluation script (evaluator.py) was built to automatically test the system using predefined memories and queries.


## Test Dataset

The evaluation dataset includes:

- 10 stored memories (facts)
- 10 test queries
- Each query mapped to the correct memory using an ID

Example:

Memory:
My favourite food is pasta

Query:
Which food do I like most?

Expected Result:
My favourite food is pasta


## How Evaluation Works

For each query:

- The query is converted into an embedding.
- The system retrieves the top_k most similar memories.
- The retrieved results are compared with the expected correct memory.
- Scores are calculated.
- Results are printed in the console.


## Metrics Used


### Top-1 Accuracy

Checks whether the correct memory is ranked first.

Formula:

Accuracy = Correct Top-1 Predictions / Total Queries

Why chosen:

- It measures strict retrieval performance.
- If the correct memory appears first, the system is highly accurate.


### Top-K Hit Rate (K = 3)

Checks whether the correct memory appears anywhere in the top 3 results.

Formula:

Top-K Hit Rate = Queries where correct memory appears in Top 3 / Total Queries

Why chosen:

- In real systems, the correct answer does not always need to be first.
- Being in the top few results is still useful.


## Results

Example output:

Top-1 Accuracy: 0.90  
Top-3 Hit Rate: 1.00


## What Worked Well

- Direct factual queries worked very well.
- Cosine similarity correctly matched related sentences.
- Small dataset made retrieval precise.


## Limitations

- The system works best when queries are similar to stored memory wording.
- Small dataset makes evaluation easier.
- No advanced reranking model.
- No handling of ambiguous queries.
- Performance may drop with larger datasets.