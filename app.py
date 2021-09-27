from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://tdwzapbpreouha:6abe57e54679ef8cc6150bdf2f32940ad4da79d70d34e09badbe08edd5677768@ec2-3-225-204-194.compute-1.amazonaws.com:5432/d7lbdirc0htgu1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

database = SQLAlchemy(app)

from models.usuario import Usuario

@app.route("/")
def hello():
    correos = ''
    usuarios =Usuario.get_all()
    for user in usuarios:
        correos += user.email + ' '
        print(user.email)
    return correos
    