# test_data.py

test_memories = [
    {"id": 1, "text": "My favorite food is pasta."},
    {"id": 2, "text": "I live in New York."},
    {"id": 3, "text": "My dog's name is Bruno."},
    {"id": 4, "text": "I work as a software engineer."},
    {"id": 5, "text": "I love playing football."},
    {"id": 6, "text": "My birthday is on July 10."},
    {"id": 7, "text": "I prefer coffee over tea."},
    {"id": 8, "text": "My favorite color is blue."},
    {"id": 9, "text": "I travel to Paris every summer."},
    {"id": 10, "text": "I enjoy watching sci-fi movies."},
]

test_queries = [
    {"query": "If I’m choosing dinner, what cuisine would suit me?", "expected_id": 1},
    {"query": "Where do I live?", "expected_id": 2},
    {"query": "What is my dog's name?", "expected_id": 3},
    {"query": "What is my profession?", "expected_id": 4},
    {"query": "What physical activity do I enjoy most?", "expected_id": 5},
    {"query": "When is my birthday?", "expected_id": 6},
    {"query": "Do I prefer coffee or tea?", "expected_id": 7},
    {"query": "What is my favorite color?", "expected_id": 8},
    {"query": "Where do I travel in summer?", "expected_id": 9},
    {"query": "What kind of movies do I enjoy?", "expected_id": 10},
]
