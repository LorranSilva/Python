from app import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Intenger, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String(120), unique=True)

#  inicializando os campos com __init__

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __repr__(self):
        return "<User %r>" % self.username


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Intenger, primary_key=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Intenger, db.foreignKey('users.id'))
    user = db.relationship('User', foreign_keys=user_id)

    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return "<Post %r>" % self.id


class Follow(db.Model):
    __tablename__ = "follow"
    id = db.Column(db.Intenger, primary_key=True)
    user_id = db.Column(db.Intenger, db.ForeignKey('users.id'))
    follower_id = id.Column(db.Intenger, db.models.ForeignKey('users.id'))
    user = db.relationship('User', foreing_keys=user_id)
    # referencia ao id dos seguidores
    follower = db.relationship('User', foreign_keys=follower_id)
