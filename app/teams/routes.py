from flask import Blueprint
from flask import request, jsonify, render_template, redirect, url_for, flash
from app.controllers import teams

bp = Blueprint('teams', __name__)


@bp.route('/create', methods=['GET', 'POST'])
def create_team_page():
    if request.method == 'POST':
        data = {
            'name': request.form['name']
        }
        result, status = teams.create_team(data=data)
        if status == 201:
            flash('Team created successfully!', 'success')
            return redirect(url_for('teams.create_team_page'))
        else:
            flash(f'Error: {result["error"]}', 'danger')
    return render_template('teams/create_team.html')
