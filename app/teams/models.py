from app import db


class Teams(db.Model):
    team_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    # Relationships
    assignments = db.relationship('Assignment', back_populates='teams')

