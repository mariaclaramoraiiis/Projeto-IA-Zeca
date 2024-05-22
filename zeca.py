from flask import Flask, request, jsonify
app = Flask(__name__, static_folder='static')

class MathAssistant:
   
    def solve_operation(self, operation):
        operation = operation.strip().lower()
        result = None
        tips = ""
        
        # Verificar o tipo de operação e resolver
        if "+" in operation:
            operands = operation.split("+")
            result = sum(map(int, operands))
            tips = "A Adição é o ato de juntar elementos,uma das quatro operações básicas da aritmética. Toda vez que unimos novos elementos ou valores, estamos adicionando. Em matemática utiliza-se o símbolo + para representar uma adição."
        elif "-" in operation:
            operands = operation.split("-")
            result = int(operands[0]) - int(operands[1])
            tips = "Para subtrair, comece com o primeiro número e tire o segundo!"
        elif "*" in operation:
            operands = operation.split("*")
            result = int(operands[0]) * int(operands[1])
            tips = "Para multiplicar, some o primeiro número repetidas vezes!"
        elif "/" in operation:
            operands = operation.split("/")
            result = int(operands[0]) / int(operands[1])
            tips = "Para dividir, reparta o primeiro número em partes iguais!"
        else:
            return "Operação não reconhecida. Tente novamente com uma operação de adição (+), subtração (-), multiplicação (*) ou divisão (/)."
        
        return f"O resultado de {operation} é {result}. {tips}"
    
app = Flask(__name__)
assistant = MathAssistant()

@app.route('/chat', methods=['POST'])
# Função para interagir com o usuário
def chat():
    assistant = MathAssistant()
    while True:
        operation = input("Olá, eu sou o Zeca! Irei te ajudar com seus problemas matemáticos! Digite a operação matemática (ou 'sair' para encerrar): ")
        if operation.lower() == "sair":
            print("Até logo amigo! Espero ter ajudado.")
            break
        print(assistant.solve_operation(operation))

# Iniciar o chat
chat()

if __name__ == '__main__':
    app.run(debug=True)