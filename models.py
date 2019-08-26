from database import db

class Organization(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(240), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
    
    def __repr__(self):
        return '<Organization %r' % self.name

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True)
    role = db.Column(db.String(80))

    def __init__(self, username, password, email, role):
        self.username = username
        self.email = email
        self.password = password
        self.role = role

    def __repr__(self):
        return '<User %r>' % self.username

if __name__ == '__main__':
    db.create_all()
    db.session.commit()
