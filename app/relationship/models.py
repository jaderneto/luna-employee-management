from app import db


class WorkRelationship(db.Model):
    work_relationship_id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.employee_id'), nullable=False)
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.organization_id'), nullable=False)
    status = db.Column(db.String(10), nullable=False, default='active')
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=True)

    # Relationships
    employee = db.relationship('Employees', back_populates='work_relationships')
    organization = db.relationship('Organization', back_populates='work_relationships')
    assignments = db.relationship('Assignment', back_populates='work_relationship', cascade="all, delete-orphan")
