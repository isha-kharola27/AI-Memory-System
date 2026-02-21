# TASK 3 – How Should AI Decide What to Remember?

If an AI assistant has limited memory capacity, it cannot store everything forever. Just like humans, it must decide what information is important enough to keep and what should eventually be forgotten.

Some information is useful only for a short time, while other information becomes more valuable over time. Therefore, an intelligent memory system must balance usefulness, relevance, and storage limits.

Below are concrete approaches an AI assistant could use to manage memory intelligently.

---

## 1. Recency-Based Decay

One simple strategy is **recency-based decay**. In this approach, memories lose importance as time passes. The assistant assigns a score to each memory and gradually decreases that score over time. If the score drops below a threshold, the memory is deleted.

### Example:

- “I have a meeting at 3 PM today” → should be forgotten tomorrow  
- “My favorite food is pasta” → should not decay quickly because it remains relevant long-term  

This method works well for short-term or time-sensitive information. It mimics human forgetting. Most people cannot remember what they ate two weeks ago, but they remember their hometown.

### Limitations:

- Some old memories are still important.
- Long-term facts (e.g., medical conditions or core preferences) should not disappear just because time passed.
- Pure recency-based decay may delete valuable long-term information.

While simple and efficient, this strategy cannot be used alone.

---

## 2. Importance Scoring Using an LLM

Another approach is to use a Large Language Model (LLM) to evaluate how important a memory is.

When new information appears, the assistant can ask:

- Is this a long-term preference?
- Is this critical personal information?
- Is this a temporary detail?

Based on the analysis, the system assigns an **importance score**. High-importance memories are stored long-term, while low-importance memories are treated as temporary.

### Example:

- “My birthday is July 20” → High importance  
- “I’m feeling tired today” → Low importance  

This approach is more intelligent because it considers meaning, not just time. It prioritizes identity, preferences, and critical facts.

### Tradeoffs:

- More computationally expensive
- The model may misjudge importance
- Requires careful prompting or training

Despite these challenges, this method enables more human-like memory decisions.

---

## 3. Frequency-Based Retention

Another strategy is **frequency-based retention**.

If a user mentions something repeatedly, it becomes more important over time.

### Example:

- If a user frequently talks about “football,” the assistant learns it is important.
- If something is mentioned only once, it may not deserve long-term storage.

Repetition often signals importance in human behavior. However, rare but critical information (such as allergies) might only be mentioned once. Therefore, frequency alone is insufficient.

---

## Tradeoffs Between Approaches

Each strategy works best in different scenarios:

- **Recency-based decay** → Simple and efficient, but may forget important long-term facts.
- **Importance scoring via LLM** → More intelligent and flexible, but computationally expensive.
- **Frequency-based retention** → Captures habits and interests, but misses rare critical details.

A single method alone is not ideal. A hybrid system combining these approaches would perform better.

---

## Relation to Human Memory

Human memory naturally combines these strategies:

- We forget small daily details (recency decay).
- We remember meaningful life events (importance scoring).
- We strengthen memories through repetition (frequency-based retention).

Human memory is adaptive rather than rigid. Similarly, AI memory systems should be adaptive.

---

## My Opinion: What Would Work Best?

In my opinion, the most effective solution for a conversational AI assistant is a **hybrid system**:

1. Use an LLM to assign an importance score when storing new information.
2. Apply recency-based decay to low-importance memories.
3. Increase importance for memories that are mentioned frequently.

This layered approach balances intelligence and efficiency. It prevents blindly forgetting important facts while still controlling storage size.

---

## Conclusion

Deciding what to remember is one of the most challenging problems in AI memory systems.

A purely time-based system is too simple. A purely intelligence-based system may be expensive or inconsistent. A hybrid approach combining recency, importance, and frequency provides a balanced and practical solution.

Ultimately, intelligent forgetting is just as important as intelligent remembering. A well-designed AI assistant should not attempt to remember everything — it should remember what truly matters.