import os
from datetime import datetime

from app import app, db
from app.models import Links, LinkCategories, StoryType, MediaType, Country, Genre, Media, MapSpot, User
from app.mod_auth import bcrypt

def create_db():

        print("Creating database tables...")
        db.drop_all()
        db.create_all()
        db.session.commit()
        print("Creating database tables finished")

def seed_db():
        print("Inserting example data...")

        # LinkCategories
        db.session.add(LinkCategories(id=1, name="Link category 1", user_id=1, create_time=datetime.now()))
        db.session.add(LinkCategories(id=2, name="Link category 2", user_id=1, create_time=datetime.now()))
        db.session.add(LinkCategories(id=3, name="Link category 3", user_id=1, create_time=datetime.now()))

        # Links
        db.session.add(Links(id=1, name="Link 1", url="http://example.com", category=1, user_id=1, create_time=datetime.now()))
        db.session.add(Links(id=2, name="Link 2", url="http://example.com", category=1, user_id=1, create_time=datetime.now()))
        db.session.add(Links(id=3, name="Link 3", url="http://example.com", category=1, user_id=1, create_time=datetime.now()))
        db.session.add(Links(id=4, name="Link 4", url="http://example.com", category=2, user_id=1, create_time=datetime.now()))
        db.session.add(Links(id=5, name="Link 5", url="http://example.com", category=2, user_id=1, create_time=datetime.now()))
        db.session.add(Links(id=6, name="Link 6", url="http://example.com", category=2, user_id=1, create_time=datetime.now()))

        # Genre
        db.session.add(Genre(id=1, type_id=1, type_name='skateboarding'))
        db.session.add(Genre(id=2, type_id=2, type_name='snowboarding'))
        db.session.add(Genre(id=3, type_id=3, type_name='nollagang'))
        db.session.add(Genre(id=4, type_id=4, type_name='snowskate'))

        # MediaType
        db.session.add(MediaType(id=1, type_id=1, type_name='photo'))
        db.session.add(MediaType(id=2, type_id=2, type_name='mediatype2'))
        db.session.add(MediaType(id=3, type_id=3, type_name='music'))
        db.session.add(MediaType(id=4, type_id=4, type_name='movies'))
        db.session.add(MediaType(id=5, type_id=5, type_name='stories')) # interviews, reviews
        db.session.add(MediaType(id=6, type_id=6, type_name='video'))

        # Photo (skateboarding)
        db.session.add(Media(media_id=1, media_topic="Photo 1", media_desc="desc", media_text="text", media_type=1, media_genre=1, story_type=1, create_time=datetime.now(), owner="", lang_id=1, country_id=1, hidden=0))
        db.session.add(Media(media_id=2, media_topic="Photo 2", media_desc="desc", media_text="text", media_type=1, media_genre=1, story_type=1, create_time=datetime.now(), owner="", lang_id=1, country_id=1, hidden=0))
        db.session.add(Media(media_id=3, media_topic="Photo 3", media_desc="desc", media_text="text", media_type=1, media_genre=1, story_type=1, create_time=datetime.now(), owner="", lang_id=1, country_id=1, hidden=0))
        db.session.add(Media(media_id=4, media_topic="Photo 4", media_desc="desc", media_text="text", media_type=1, media_genre=1, story_type=1, create_time=datetime.now(), owner="", lang_id=1, country_id=1, hidden=0))

        # Photo (snowboarding)
        db.session.add(Media(media_id=5, media_topic="Photo 1", media_desc="desc", media_text="text", media_type=1, media_genre=2, story_type=1, create_time=datetime.now(), owner="", lang_id=1, country_id=1, hidden=0))
        db.session.add(Media(media_id=6, media_topic="Photo 2", media_desc="desc", media_text="text", media_type=1, media_genre=2, story_type=1, create_time=datetime.now(), owner="", lang_id=1, country_id=1, hidden=0))
        db.session.add(Media(media_id=7, media_topic="Photo 3", media_desc="desc", media_text="text", media_type=1, media_genre=2, story_type=1, create_time=datetime.now(), owner="", lang_id=1, country_id=1, hidden=0))
        db.session.add(Media(media_id=8, media_topic="Photo 4", media_desc="desc", media_text="text", media_type=1, media_genre=2, story_type=1, create_time=datetime.now(), owner="", lang_id=1, country_id=1, hidden=0))

        # Reviews
        db.session.add(Media(media_id=9, media_topic="Review 1", media_desc="desc", media_text="text", media_type=5, media_genre=1, story_type=2, create_time=datetime.now(), owner="", lang_id=1, country_id=1, hidden=0))
        db.session.add(Media(media_id=10, media_topic="Review 2", media_desc="desc", media_text="text", media_type=5, media_genre=2, story_type=2, create_time=datetime.now(), owner="", lang_id=1, country_id=1, hidden=0))
        db.session.add(Media(media_id=11, media_topic="Review 3", media_desc="desc", media_text="text", media_type=5, media_genre=3, story_type=2, create_time=datetime.now(), owner="", lang_id=1, country_id=1, hidden=0))
        db.session.add(Media(media_id=12, media_topic="Review 4", media_desc="desc", media_text="text", media_type=5, media_genre=4, story_type=2, create_time=datetime.now(), owner="", lang_id=1, country_id=1, hidden=0))

        # Interviews
        db.session.add(Media(media_id=13, media_topic="Interview 1", media_desc="desc", media_text="text", media_type=5, media_genre=1, story_type=3, create_time=datetime.now(), owner="", lang_id=1, country_id=1, hidden=0))
        db.session.add(Media(media_id=14, media_topic="Interview 2", media_desc="desc", media_text="text", media_type=5, media_genre=1, story_type=3, create_time=datetime.now(), owner="", lang_id=1, country_id=1, hidden=0))
        db.session.add(Media(media_id=15, media_topic="Interview 3", media_desc="desc", media_text="text", media_type=5, media_genre=1, story_type=3, create_time=datetime.now(), owner="", lang_id=1, country_id=1, hidden=0))
        db.session.add(Media(media_id=16, media_topic="Interview 4", media_desc="desc", media_text="text", media_type=5, media_genre=1, story_type=3, create_time=datetime.now(), owner="", lang_id=1, country_id=1, hidden=0))

        # News
        db.session.add(Media(media_id=17, media_topic="News 1", media_desc="desc", media_text="text", media_type=4, media_genre=1, story_type=4, create_time=datetime.now(), owner="", lang_id=1, country_id=1, hidden=0))
        db.session.add(Media(media_id=18, media_topic="News 2", media_desc="desc", media_text="text", media_type=4, media_genre=1, story_type=4, create_time=datetime.now(), owner="", lang_id=1, country_id=1, hidden=0))
        db.session.add(Media(media_id=19, media_topic="News 3", media_desc="desc", media_text="text", media_type=4, media_genre=1, story_type=4, create_time=datetime.now(), owner="", lang_id=1, country_id=1, hidden=0))
        db.session.add(Media(media_id=20, media_topic="News 4", media_desc="desc", media_text="text", media_type=4, media_genre=1, story_type=4, create_time=datetime.now(), owner="", lang_id=1, country_id=1, hidden=0))

        # StoryType
        db.session.add(StoryType(id=1, type_id=1, type_name='general'))
        db.session.add(StoryType(id=2, type_id=2, type_name='reviews'))
        db.session.add(StoryType(id=3, type_id=3, type_name='interviews'))
        db.session.add(StoryType(id=4, type_id=4, type_name='news'))
        db.session.add(StoryType(id=5, type_id=99, type_name='other'))

        # Country
        db.session.add(Country(id=1, country_code='fi', country_name='Finland'))
        db.session.add(Country(id=2, country_code='se', country_name='Sweden'))
        db.session.add(Country(id=3, country_code='ee', country_name='Estonia'))
        db.session.add(Country(id=4, country_code='dk', country_name='Denmark'))
        db.session.add(Country(id=5, country_code='de', country_name='Germany'))

        # Spots
        db.session.add(MapSpot(kartta_id=1, paikkakunta_id=1, user_id=1, nimi="Spot 1", info="desc", tyyppi=1, temp=1, paivays=datetime.now(), karttalinkki="", maa_id=1, latlon=1))
        db.session.add(MapSpot(kartta_id=2, paikkakunta_id=1, user_id=1, nimi="Spot 2", info="desc", tyyppi=1, temp=2, paivays=datetime.now(), karttalinkki="", maa_id=1, latlon=1))
        db.session.add(MapSpot(kartta_id=3, paikkakunta_id=1, user_id=1, nimi="Spot 3", info="desc", tyyppi=1, temp=3, paivays=datetime.now(), karttalinkki="", maa_id=1, latlon=1))
        db.session.add(MapSpot(kartta_id=4, paikkakunta_id=1, user_id=1, nimi="Spot 4", info="desc", tyyppi=1, temp=4, paivays=datetime.now(), karttalinkki="", maa_id=1, latlon=1))

        # Users
        db.session.add(User(user_id=1, level=1, username="tester", password=bcrypt.generate_password_hash("tester"), name="Sir Tester", bornyear=2010, email="tester@example.com", email2="", info="", location="", date=datetime.now(), hobbies="", open=1, extrainfo="", sukupuoli=1, icq="", apulainen=1, last_login=datetime.now(), chat=1, oikeus=1, lang_id=1, login_count=1, lastloginip="", lastloginclient="", address="", postnumber="", emails=1, puhelin="", kantaasiakasnro="", lamina_lisatieto="", blogs=1, user_showid=1, blog_level=1, last_login2=datetime.now(), messenger="", myspace="", rss="", youtube="", ircgalleria="", last_profile_update=datetime.now(), avatar="", flickr_username=""))

        db.session.commit()
        print("Inserting example data finished")

if __name__ == "__main__":
    if(os.getenv('MYSQL_HOST') == "db"): # localhost
        create_db()
        seed_db()
    else:
        print("Don´t want to override production database!")