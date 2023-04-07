from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from txlink.auth import login_required
from txlink.db import get_db

bp = Blueprint('cust', __name__)

@bp.route('/')
def index():
    db = get_db()

    return render_template('cust/index.html')

@bp.route('/cust_list', methods=('GET', 'POST'))
@login_required
def cust_list():
    db = get_db()

    if request.method == 'GET':
        custs = db.execute(
        "SELECT id, customer_name, company_addr, site_addr, Email, Note "
        "FROM customer where user_id =?",
        f"{g.user['id']}"
        ).fetchall()
        return render_template('cust/cust_list.html', custs=custs)
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        id = db.execute(
        "SELECT id "
        "FROM customer where customer_name == ? ",
        customer_name
        ).fetchone()
        return redirect(url_for("cust.edit_cust"), id=id)

@bp.route('/add_cust', methods=('GET', 'POST'))
@login_required
def add_cust():
    if request.method == 'POST':
        
        customer_name = request.form['customer_name']
        company_addr = request.form['company_addr']
        site_addr = request.form['site_addr']
        Email = request.form['Email']
        Note = request.form['Note']
        db = get_db()
        error = None

        if error is None:
            try:
                db.execute(
                    "INSERT INTO customer (user_id, customer_name, company_addr, site_addr, Email, Note) VALUES (?, ?,?,?,?,?)",
                    (f"{g.user['id']}", customer_name, company_addr, site_addr, Email, Note)
                )
                db.commit()
            except db.IntegrityError:
                error = f"看看什么错."
            else:
                return redirect(url_for("cust.cust_list"))
        flash(error)

    return render_template('cust/add_cust.html')

@bp.route('/edit_cust/<int:id>', methods=('GET', 'POST'))
def edit_cust(id):

    db = get_db()
    error = None
    if request.method=='POST':
        if request.form['action'] =='save':
            customer_name = request.form['customer_name']
            company_addr = request.form['company_addr']
            site_addr = request.form['site_addr']
            Email = request.form['Email']
            Note = request.form['Note']
            id = request.form['id']
            if error is None:
                try:
                    db.execute(
                        "update customer set customer_name=?, company_addr=?, site_addr=?, Email=?, Note=? "
                        "where id = ? and user_id=?",
                        (customer_name, company_addr, site_addr, Email, Note, f"{id}", f"{g.user['id']}")
                    )
                    db.commit()
                    # error = request.form['save']
                    # print(f"e:{error}")
                except db.IntegrityError:
                    error = f"{customer_name}."
            flash(error)

        if request.form['action'] =='delete':
            db.execute(
            "delete FROM customer where id =? and user_id =?", (f"{id}", f"{g.user['id']}" ) )
            db.commit()
            return redirect(url_for("cust.cust_list"))

    cust = db.execute(
        "SELECT id, customer_name, company_addr, site_addr, Email, Note "
        "FROM customer where id =? and user_id =?", (f"{id}", f"{g.user['id']}" ) ).fetchone()
  
    return render_template('cust/edit_cust.html', cust=cust)