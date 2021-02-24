from flask import Flask, redirect, url_for, render_template, request
# Initialize the Flask application
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/haha')
def haha():
    return "hahaha"
    
@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')

@app.route('/login',methods = ['POST', 'GET']) 
def login(): 
   if request.method == 'POST':
        if request.form['username'] == 'admin': #loga se o username for igual a 'admin'
            return redirect(url_for('success'))
        else:
            return redirect('https://http.cat/401')
   else:
      return redirect(url_for('index'))

@app.route('/success')
def success():
   return 'logged in successfully'


if __name__ == '__main__':
    app.run(debug = True)