from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        # Captura os dados enviados pela Maytapi API
        data = request.json
        
        # Validação básica
        if not data:
            return jsonify({"status": "Nenhum dado recebido"}), 400

        # Extraindo informações da mensagem com fallback
        mensagem = data.get('message', 'Mensagem não disponível')
        remetente = data.get('from', 'Remetente não identificado')
        grupo = data.get('group_name', 'Grupo não identificado')

        # Log no terminal
        print(f"Mensagem recebida de {remetente} no grupo {grupo}: {mensagem}")
        
        # Resposta ao webhook
        return jsonify({"status": "Mensagem processada"}), 200
    
    except Exception as e:
        print(f"Erro no processamento: {e}")
        return jsonify({"status": "Erro no processamento", "error": str(e)}), 500

# app.run é removido em produção

