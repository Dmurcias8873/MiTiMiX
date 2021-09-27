from app import database

class Usuario(database.Model):

    __tablename_ = 'usuarios'

    id = database.Column(database.Integer, primary_key=True)
    email = database.Column(database.String, nullable=False)
    password = database.Column(database.String, nullable=False)

    @staticmethod
    def get_all():
        return Usuario.query.all()