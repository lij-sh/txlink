from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from txlink.auth import login_required
from txlink.db import get_db

bp = Blueprint('prod', __name__, url_prefix='/prod')

@bp.route('/prod_center', methods=('GET', 'POST'))
@login_required
def prod_center():
    db = get_db()

    if request.method == 'GET':
        prods = db.execute(
        "SELECT * "
        "FROM product where user_id =?",
        f"{g.user['id']}"
        ).fetchall()
        return render_template('prod/prod.html', prods=prods)

