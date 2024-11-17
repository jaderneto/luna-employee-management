from flask import Blueprint
from flask import request, jsonify, render_template, redirect, url_for, flash
from app.controllers import employees

bp = Blueprint('employees', __name__)


@bp.route('/', methods=['GET'])
def index():
    return "Employees Home"


@bp.route('/employees', methods=['POST'])
def create_employee():
    data = request.get_json()
    result, status = employees.create_employee(data)
    return jsonify(result), status


@bp.route('/employees', methods=['GET'])
def get_employees():
    result, status = employees.list_employees()
    return jsonify(result), status


@bp.route('/employees/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    result, status = employees.get_employee_by_id(employee_id)
    return jsonify(result), status


@bp.route('/create', methods=['GET', 'POST'])
def create_employee_page():
    if request.method == 'POST':
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'full_name': request.form['full_name'],
            'birth_date': request.form['birth_date'],
            'email': request.form['email'],
            'hire_date': request.form['hire_date']
        }
        result, status = employees.create_employee(data)
        if status == 201:
            flash('Employee created successfully!', 'success')
            return redirect(url_for('employees.create_employee_page'))
        else:
            flash(f'Error: {result["error"]}', 'danger')

    return render_template('employees/create_employee.html')


@bp.route('/search', methods=['GET', 'POST'])
def search_employee_page():
    if request.method == 'POST':
        query = request.form['query']
        search_results, status = employees.search_employee(query)

        if status == 200 and search_results:
            return render_template('employees/search_employee.html', results=search_results)
        else:
            flash(f'No employees found for "{query}".', 'info')
    return render_template('employees/search_employee.html', results=None)
