from llm_service import recommend_books

print("📚 AI Book Recommender")

while True:

    genre = input("\nEnter genre (or 'exit'): ")
    if genre.lower() == "exit":
        break

    mood = input("Enter mood: ")
    goal = input("Reading goal: ")

    result = recommend_books(genre, mood, goal)

    print("\n📖 Recommended Books:\n")
    print(result)