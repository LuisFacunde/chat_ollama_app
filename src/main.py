from langchain_community.llms import Ollama

def main():
    llm = Ollama(
        base_url="http://ollama.eastus.cloudapp.azure.com:11434", 
        model="phi3:mini"
    )

    print("=== Chat com Ollama (phi3:mini) ===")
    print("Digite 'sair' para encerrar.\n")

    while True:
        prompt = input("Você: ")
        if prompt.lower() in ["sair", "exit", "quit"]:
            print("Encerrando...")
            break

        resposta = llm.invoke(prompt)

        print(f"Ollama: {resposta}\n")

if __name__ == "__main__":
    main()
