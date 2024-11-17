from app import db


class Organization(db.Model):
    organization_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=True)
    email = db.Column(db.String(120), nullable=True)
    cnpj = db.Column(db.String(18), unique=True, nullable=False)

    # Relationships
    work_relationships = db.relationship('WorkRelationship', back_populates='organization')
