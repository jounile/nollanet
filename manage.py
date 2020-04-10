from flask_cli import FlaskCLI
from datetime import datetime

from app import app, db
from app.models import Links, LinkCategories

FlaskCLI(app)

@app.cli.command("create_db")
def create_db():
    print("Creating database tables...")
    db.drop_all()
    db.create_all()
    db.session.commit()
    print("Creating database tables finished")

    print("Inserting example data...")
    db.session.add(LinkCategories(id=1, name="Link category 1", user_id=1, create_time=datetime.now()))
    db.session.add(Links(id=1, name="Link 1", url="http://example.com", category=1, user_id=1, create_time=datetime.now()))
    db.session.commit()
    print("Inserting example data finished")

if __name__ == "__main__":
    create_db()