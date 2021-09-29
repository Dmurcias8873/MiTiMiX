from app import database

class Artistas(database.Model):

    __tablename_ = 'artistas'

    idartista = database.Column(database.Integer, primary_key=True)
    nombre = database.Column(database.String, nullable=False)
    idcanciones = database.Column(database.Integer, database.ForeignKey("canciones.idcanciones"))

    def __str__(self):
        return f"<Artista {self.idartista} {self.nombre} {self.idcanciones}>"

    @staticmethod
    def get_all():
        return Artistas.query.all()
    