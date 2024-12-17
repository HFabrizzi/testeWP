from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Captura os dados enviados pela Maytapi API
    data = request.json

    # Extraindo informações da mensagem
    mensagem = data.get('message')  # Conteúdo da mensagem
    remetente = data.get('from')  # Número do remetente
    grupo = data.get('group_name')  # Nome do grupo (se aplicável)

    # Log no terminal
    print(f"Mensagem recebida de {remetente} no grupo {grupo}: {mensagem}")
    
    # Enviar resposta ao Maytapi (se necessário)
    return jsonify({"status": "Mensagem processada"}), 200

"if __name__ == '__main__':
    app.run(port=5000)"
