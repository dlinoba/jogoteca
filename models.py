from jogoteca import db

class jogos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(40), nullable=False)
    console = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name
      
class usuarios(db.Model):
    nickname = db.Column(db.String(8), primary_key=True)
    nome = db.Column(db.String(20), nullable=False)
    senha = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name
    
class CLIENTE(db.Model):
    ID_CLIENTE = db.Column(db.Integer, primary_key=True, autoincrement=True)
    NM_CLIENTE = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name

class TELEFONE(db.Model):
    __tablename__ = 'TELEFONE'
    ID_TELEFONE = db.Column(db.Integer, primary_key=True, autoincrement=True)
    CD_DDD = db.Column(db.String(2), nullable=False)
    NR_TELEFONE = db.Column(db.String(10), nullable=False)
    ID_CLIENTE = db.Column(db.Integer, db.ForeignKey(CLIENTE.ID_CLIENTE))
    CLIENTE = db.relationship(CLIENTE, backref='TELEFONES',primaryjoin='TELEFONE.ID_CLIENTE == CLIENTE.ID_CLIENTE', 
        foreign_keys=ID_CLIENTE)
    
    def __repr__(self):
        return '<Name %r>' % self.name

#TELEFONE.ID_CLIENTE = db.relationship("TELEFONE", order_by=TELEFONE.ID_TELEFONE, back_populates="CLIENTE")

class PRODUTO(db.Model):
    ID_PRODUTO = db.Column(db.Integer, primary_key=True, autoincrement=True)
    CD_PRODUTO = db.Column(db.String(45), nullable=False)
    NM_PRODUTO = db.Column(db.String(4000), nullable=False)
    IN_ATIVO = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return '<Name %r>' % self.name
    