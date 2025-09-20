# chat_ollama_app

Este projeto é um chat simples utilizando o modelo Ollama (phi3:mini) via LangChain.

## Requisitos
- Python 3.13+
- Pacote `langchain-community`

## Instalação

1. Clone o repositório:
	```powershell
	git clone https://github.com/LuisFacunde/chat_ollama_app.git
	cd chat_ollama_app
	```

2. Instale as dependências:
	```powershell
	pip install langchain-community
	```

## Execução

Execute o arquivo principal:
```powershell
C:/Users/luis.silva/AppData/Local/Programs/Python/Python313/python.exe src/main.py
```

## Uso
- Digite sua mensagem e pressione Enter para conversar com o modelo.
- Para encerrar, digite `sair`.

## Configuração do modelo
O modelo está configurado para acessar o Ollama em:
```
http://ollama.eastus.cloudapp.azure.com:11434
```

Você pode alterar o endereço e o modelo editando o arquivo `src/main.py`.

---

LuisFacunde - 2025