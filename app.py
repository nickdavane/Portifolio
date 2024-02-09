from flask import Flask, redirect, render_template



app = Flask(__name__)

@app.route('/')
def index():
		# Precisamos da função redirect para navegar para o endpoint "/home"
    return redirect('/home') 

@app.route('/home', )
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
        