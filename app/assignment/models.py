from app import db


class Assignment(db.Model):
    assignment_id = db.Column(db.Integer, primary_key=True)
    # This foreign Key indicates that assignments is 'the many side' of the relationship one-to-many
    work_relationship_id = db.Column(db.Integer, db.ForeignKey('work_relationship.work_relationship_id'), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=True)
    status = db.Column(db.String(10), nullable=False, default='active')
    job_title = db.Column(db.String(100), nullable=False)
    shift = db.Column(db.String(20), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.team_id'), nullable=False)

    # Relationship
    work_relationship = db.relationship('WorkRelationship', back_populates='assignments')
    teams = db.relationship('Teams', back_populates='assignments')
