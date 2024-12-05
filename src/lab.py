from llm_style_console import LLMStyleConsole

def main():
    print("Como posso ajudar?")

    # Criando uma instância com callback
    console = LLMStyleConsole(callback=handle_response)

    # Exemplo de texto para testar
    texto_exemplo = """Olá! Eu sou um assistente virtual.
    Como posso ajudar você hoje?"""
    
    # Exibindo o texto e obtendo resposta
    response = console.display_and_get_response(texto_exemplo)

def handle_response(response: str):
    print("ok")

if __name__ == "__main__":
    main()