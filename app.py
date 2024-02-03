from flask import Flask, redirect, render_template, url_for, request



app = Flask(__name__)

@app.route('/home')
def index():
		# Precisamos da função redirect para navegar para o endpoint "/home"
    return redirect('/') 

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/contato', methods=['POST'])
def menssagem_contato():
    remetente = request.form.get('remetente')
    assunto =  request.form.get('assunto')
    resposta = f'Obrigado {remetente} por entrar em contato'
    return render_template('index.html', mensagem=resposta)


    



    


if __name__ == '__main__':
    app.run(debug=True)
        