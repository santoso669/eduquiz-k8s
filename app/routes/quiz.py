from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.models.models import Soal, Hasil

quiz_bp = Blueprint('quiz', __name__, url_prefix='/quiz')

@quiz_bp.route('/')
@login_required
def index():
    soals = Soal.query.all()
    return render_template('quiz.html', soals=soals)

@quiz_bp.route('/submit', methods=['POST'])
@login_required
def submit():
    soals = Soal.query.all()
    if not soals:
        flash('Belum ada soal untuk dikerjakan.', 'warning')
        return redirect(url_for('quiz.index'))
    benar = 0
    for s in soals:
        jawaban_user = request.form.get(f'soal_{s.id}')
        if jawaban_user == s.jawaban:
            benar += 1
    total = len(soals)
    skor  = int((benar / total) * 100) if total > 0 else 0
    hasil = Hasil(user_id=current_user.id, skor=skor, total_soal=total, benar=benar)
    db.session.add(hasil)
    db.session.commit()
    flash(f'Quiz selesai! Skor kamu: {skor} ({benar}/{total} benar)', 'success')
    return redirect(url_for('quiz.riwayat'))

@quiz_bp.route('/riwayat')
@login_required
def riwayat():
    if current_user.role == 'guru':
        hasils = Hasil.query.order_by(Hasil.created_at.desc()).all()
    else:
        hasils = Hasil.query.filter_by(user_id=current_user.id)\
                            .order_by(Hasil.created_at.desc()).all()
    return render_template('riwayat.html', hasils=hasils)
