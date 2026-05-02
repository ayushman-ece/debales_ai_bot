from graph import app_graph

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    result = app_graph.invoke({
        "question": question
    })

    print("\nBot:", result["answer"])