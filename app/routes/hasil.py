from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models.models import Hasil

hasil_bp = Blueprint('hasil', __name__, url_prefix='/hasil')

@hasil_bp.route('/')
@login_required
def index():
    if current_user.role == 'guru':
        hasils = Hasil.query.order_by(Hasil.created_at.desc()).all()
    else:
        hasils = Hasil.query.filter_by(siswa_id=current_user.id)\
                            .order_by(Hasil.created_at.desc()).all()
    return render_template('hasil.html', hasils=hasils)
