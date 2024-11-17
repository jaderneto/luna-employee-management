
def create_employee(data):
    from app import db
    from app.employees.models import Employees

    new_employee = Employees(
        first_name=data['first_name'],
        last_name=data['last_name'],
        full_name=data['full_name'],
        birth_date=data['birth_date'],
        email=data['email'],
        hire_date=data['hire_date']
    )

    try:
        db.session.add(new_employee)
        db.session.commit()
        return {"message": "Employee created successfully!"}, 201
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 500


def list_employees():
    from app.employees.models import Employees

    try:
        employees = Employees.query.all()
        employees_response = []
        for emp in employees:
            dict_emp = {
                "employee_id": emp.employee_id,
                "first_name": emp.first_name,
                "last_name": emp.last_name,
                "full_name": emp.full_name,
                "birth_date": emp.birth_date.strftime('%Y-%m-%d'),
                "email": emp.email,
                "hire_date": emp.hire_date.strftime('%Y-%m-%d')
            }
            employees_response.append(dict_emp)

        return {"employees": employees_response}, 200
    except Exception as e:
        return {"error": str(e)}, 500


def get_employee_by_id(employee_id):
    from app.employees.models import Employees

    try:
        employee = Employees.query.get(employee_id)
        if employee is None:
            return {"error": "Employee not found"}, 404

        employee_data = {
            "employee_id": employee.employee_id,
            "first_name": employee.first_name,
            "last_name": employee.last_name,
            "full_name": employee.full_name,
            "birth_date": employee.birth_date.strftime('%Y-%m-%d'),
            "email": employee.email,
            "hire_date": employee.hire_date.strftime('%Y-%m-%d')
        }
        return {"employee": employee_data}, 200
    except Exception as e:
        return {"error": str(e)}, 500


def search_employee(query):
    from app.employees.models import Employees
    from sqlalchemy import or_

    try:
        search_query = f"%{query}%"
        employees = Employees.query.filter(
            or_(
                Employees.first_name.ilike(search_query),
                Employees.last_name.ilike(search_query)
            )
        ).all()

        if employees:
            response = []
            for employee in employees:
                employee_data = {
                    "employee_id": employee.employee_id,
                    "first_name": employee.first_name,
                    "last_name": employee.last_name,
                    "full_name": employee.full_name,
                    "birth_date": employee.birth_date.strftime('%Y-%m-%d'),
                    "email": employee.email,
                    "hire_date": employee.hire_date.strftime('%Y-%m-%d')
                }
                response.append(employee_data)
            return response, 200
        else:
            return {"error": "No employees found"}, 404
    except Exception as e:
        return {"error": str(e)}, 500
