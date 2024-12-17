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

        # Extraindo dados de forma segura
        mensagem = data.get('message', '')
        tipo = data.get('type', 'texto')
        remetente = data.get('from', 'Remetente não identificado')
        grupo = data.get('group_name', 'Grupo não identificado')

        # Log para diferentes tipos de mensagens
        if tipo == 'sticker':
            url_sticker = data.get('url', 'URL não disponível')
            print(f"Sticker recebido no grupo {grupo} de {remetente}: {url_sticker}")
        elif tipo == 'image':
            url_imagem = data.get('url', 'URL não disponível')
            print(f"Imagem recebida no grupo {grupo} de {remetente}: {url_imagem}")
        else:
            print(f"Mensagem de texto recebida de {remetente} no grupo {grupo}: {mensagem}")

        return jsonify({"status": "Mensagem processada"}), 200
    
    except Exception as e:
        print(f"Erro no processamento: {e}")
        return jsonify({"status": "Erro no processamento", "error": str(e)}), 500

if __name__ == '__main__':
    app.run()
