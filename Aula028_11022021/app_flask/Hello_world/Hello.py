from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/haha')
def haha():
    return "hahaha"
    
@app.route('/confirmacao')
def confirmation():
    return render_template('confirmation.html')

if __name__ == '__main__':
    app.run()