from flask_mail import Mail, Message
from flask import Flask 


app =Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'cinthyalins@gmail.com'
app.config['MAIL_PASSWORD'] = 'seViraNos30ParaDescobrirASenha'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
   msg = Message('Hello', sender = 'cinthyalins@gmail.com', recipients = ['cinthyalins@gmail.com'])
   msg.body = "Hello Flask message sent from Flask-Mail"
   mail.send(msg)
   return "Sent"

if __name__ == '__main__':
   app.run(debug = True)


# https://www.google.com/settings/security/lesssecureapps
# pip install --user Flask-Mail

