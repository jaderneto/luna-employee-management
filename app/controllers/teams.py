def create_team(data):
    from app import db
    from app.teams.models import Teams

    new_team = Teams(
        name=data['name']
    )

    try:
        db.session.add(new_team)
        db.session.commit()
        return {"message": "Team created successfully!"}, 201
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 500
