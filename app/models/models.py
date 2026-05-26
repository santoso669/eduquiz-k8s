from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id         = db.Column(db.Integer, primary_key=True)
    nama       = db.Column(db.String(100), nullable=False)
    email      = db.Column(db.String(120), unique=True, nullable=False)
    password   = db.Column(db.String(255), nullable=False)
    role       = db.Column(db.String(20), default='siswa')  # siswa / guru
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    hasils     = db.relationship('Hasil', backref='user', lazy=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Soal(db.Model):
    __tablename__ = 'soals'
    id          = db.Column(db.Integer, primary_key=True)
    pertanyaan  = db.Column(db.Text, nullable=False)
    pilihan_a   = db.Column(db.String(200), nullable=False)
    pilihan_b   = db.Column(db.String(200), nullable=False)
    pilihan_c   = db.Column(db.String(200), nullable=False)
    pilihan_d   = db.Column(db.String(200), nullable=False)
    jawaban     = db.Column(db.String(1), nullable=False)  # a/b/c/d
    kategori    = db.Column(db.String(100), default='Umum')
    created_at  = db.Column(db.DateTime, default=datetime.utcnow)


class Hasil(db.Model):
    __tablename__ = 'hasils'
    id          = db.Column(db.Integer, primary_key=True)
    user_id     = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    skor        = db.Column(db.Integer, nullable=False)
    total_soal  = db.Column(db.Integer, nullable=False)
    benar       = db.Column(db.Integer, nullable=False)
    created_at  = db.Column(db.DateTime, default=datetime.utcnow)
