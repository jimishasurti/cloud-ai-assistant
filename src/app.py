from prompt import SYSTEM_PROMPT
from ai_client import get_ai_response

def main():
    print("☁️ Cloud Infrastructure AI Assistant")
    print("Type 'exit' to quit\n")

    while True:
        question = input("Ask a cloud question: ")

        if question.lower() == "exit":
            break

        answer = get_ai_response(SYSTEM_PROMPT, question)
        print("\nAI Response:\n")
        print(answer)
        print("-" * 50)

if __name__ == "__main__":
    main()
