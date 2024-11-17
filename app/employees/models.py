from app import db


class Employees(db.Model):
    employee_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    hire_date = db.Column(db.Date, nullable=False)

    # Relationships
    work_relationships = db.relationship('WorkRelationship', back_populates='employee')
