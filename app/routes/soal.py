from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.models.models import Soal

soal_bp = Blueprint('soal', __name__, url_prefix='/soal')

@soal_bp.route('/')
@login_required
def index():
    soals = Soal.query.order_by(Soal.created_at.desc()).all()
    return render_template('soal.html', soals=soals)

@soal_bp.route('/tambah', methods=['POST'])
@login_required
def tambah():
    if current_user.role != 'guru':
        flash('Hanya guru yang dapat menambah soal.', 'danger')
        return redirect(url_for('soal.index'))
    s = Soal(
        pertanyaan = request.form.get('pertanyaan'),
        pilihan_a  = request.form.get('pilihan_a'),
        pilihan_b  = request.form.get('pilihan_b'),
        pilihan_c  = request.form.get('pilihan_c'),
        pilihan_d  = request.form.get('pilihan_d'),
        jawaban    = request.form.get('jawaban'),
        kategori   = request.form.get('kategori', 'Umum'),
    )
    db.session.add(s)
    db.session.commit()
    flash('Soal berhasil ditambahkan.', 'success')
    return redirect(url_for('soal.index'))

@soal_bp.route('/hapus/<int:id>', methods=['POST'])
@login_required
def hapus(id):
    if current_user.role != 'guru':
        flash('Akses ditolak.', 'danger')
        return redirect(url_for('soal.index'))
    s = Soal.query.get_or_404(id)
    db.session.delete(s)
    db.session.commit()
    flash('Soal dihapus.', 'info')
    return redirect(url_for('soal.index'))
