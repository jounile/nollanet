import os
from datetime import datetime

from app import app, db
from app.models import Links, LinkCategories, StoryType, MediaType, Country, Genre, Media, MapType, MapCountry, MapTown, MapSpot, User, Uploads, Story
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
        db.session.add(Links(id=7, name="Link 7", url="http://example.com", category=3, user_id=1, create_time=datetime.now()))
        db.session.add(Links(id=8, name="Link 8", url="http://example.com", category=3, user_id=1, create_time=datetime.now()))
        db.session.add(Links(id=9, name="Link 9", url="http://example.com", category=3, user_id=1, create_time=datetime.now()))

        # Genre
        db.session.add(Genre(id=1, type_name='skateboarding'))
        db.session.add(Genre(id=2, type_name='snowboarding'))
        db.session.add(Genre(id=3, type_name='nollagang'))
        db.session.add(Genre(id=4, type_name='snowskate'))

        # MediaType
        db.session.add(MediaType(id=1, type_name='photo'))
        db.session.add(MediaType(id=2, type_name='mediatype2'))
        db.session.add(MediaType(id=3, type_name='music'))
        db.session.add(MediaType(id=4, type_name='movies'))
        db.session.add(MediaType(id=5, type_name='stories')) # interviews, reviews
        db.session.add(MediaType(id=6, type_name='video'))

        # Photo (skateboarding)
        db.session.add(Media(id=1, media_topic="Skateboading photo 1", media_desc="desc", media_text="text", mediatype_id=1, genre_id=1, storytype_id=1, create_time=datetime.now(), owner="", lang_id=2, country_id=1, hidden=0))
        db.session.add(Media(id=2, media_topic="Skateboading photo 2", media_desc="desc", media_text="text", mediatype_id=1, genre_id=1, storytype_id=1, create_time=datetime.now(), owner="", lang_id=2, country_id=1, hidden=0))
        db.session.add(Media(id=3, media_topic="Skateboading photo 3", media_desc="desc", media_text="text", mediatype_id=1, genre_id=1, storytype_id=1, create_time=datetime.now(), owner="", lang_id=2, country_id=1, hidden=0))
        db.session.add(Media(id=4, media_topic="Skateboading photo 4", media_desc="desc", media_text="text", mediatype_id=1, genre_id=1, storytype_id=1, create_time=datetime.now(), owner="", lang_id=2, country_id=1, hidden=0))

        # Photo (snowboarding)
        db.session.add(Media(id=5, media_topic="Snowboading photo 1", media_desc="desc", media_text="text", mediatype_id=1, genre_id=2, storytype_id=1, create_time=datetime.now(), owner="", lang_id=2, country_id=1, hidden=0))
        db.session.add(Media(id=6, media_topic="Snowboading photo 2", media_desc="desc", media_text="text", mediatype_id=1, genre_id=2, storytype_id=1, create_time=datetime.now(), owner="", lang_id=2, country_id=1, hidden=0))
        db.session.add(Media(id=7, media_topic="Snowboading photo 3", media_desc="desc", media_text="text", mediatype_id=1, genre_id=2, storytype_id=1, create_time=datetime.now(), owner="", lang_id=2, country_id=1, hidden=0))
        db.session.add(Media(id=8, media_topic="Snowboading photo 4", media_desc="desc", media_text="text", mediatype_id=1, genre_id=2, storytype_id=1, create_time=datetime.now(), owner="", lang_id=2, country_id=1, hidden=0))

        # Video (skateboarding)
        db.session.add(Media(id=9, media_topic="Skateboading video 1", media_desc="desc", media_text="text", mediatype_id=6, genre_id=1, storytype_id=1, create_time=datetime.now(), owner="", lang_id=2, country_id=1, hidden=0))
        db.session.add(Media(id=10, media_topic="Skateboading video 2", media_desc="desc", media_text="text", mediatype_id=6, genre_id=1, storytype_id=1, create_time=datetime.now(), owner="", lang_id=2, country_id=1, hidden=0))
        db.session.add(Media(id=11, media_topic="Skateboading video 3", media_desc="desc", media_text="text", mediatype_id=6, genre_id=1, storytype_id=1, create_time=datetime.now(), owner="", lang_id=2, country_id=1, hidden=0))
        db.session.add(Media(id=12, media_topic="Skateboading video 4", media_desc="desc", media_text="text", mediatype_id=6, genre_id=1, storytype_id=1, create_time=datetime.now(), owner="", lang_id=2, country_id=1, hidden=0))

        # Video (snowboarding)
        db.session.add(Media(id=13, media_topic="Snowboading video 1", media_desc="desc", media_text="text", mediatype_id=6, genre_id=2, storytype_id=1, create_time=datetime.now(), owner="", lang_id=2, country_id=1, hidden=0))
        db.session.add(Media(id=14, media_topic="Snowboading video 2", media_desc="desc", media_text="text", mediatype_id=6, genre_id=2, storytype_id=1, create_time=datetime.now(), owner="", lang_id=2, country_id=1, hidden=0))
        db.session.add(Media(id=15, media_topic="Snowboading video 3", media_desc="desc", media_text="text", mediatype_id=6, genre_id=2, storytype_id=1, create_time=datetime.now(), owner="", lang_id=2, country_id=1, hidden=0))
        db.session.add(Media(id=16, media_topic="Snowboading video 4", media_desc="desc", media_text="text", mediatype_id=6, genre_id=2, storytype_id=1, create_time=datetime.now(), owner="", lang_id=2, country_id=1, hidden=0))

        # Reviews
        db.session.add(Story(id=17, media_topic="Review 1", media_desc="desc", media_text="text", mediatype_id=5, genre_id=1, storytype_id=2, create_time=datetime.now(), owner="", lang_id=2, country_id=1, hidden=0))
        db.session.add(Story(id=18, media_topic="Review 2", media_desc="desc", media_text="text", mediatype_id=5, genre_id=2, storytype_id=2, create_time=datetime.now(), owner="", lang_id=2, country_id=1, hidden=0))
        db.session.add(Story(id=19, media_topic="Review 3", media_desc="desc", media_text="text", mediatype_id=5, genre_id=3, storytype_id=2, create_time=datetime.now(), owner="", lang_id=2, country_id=1, hidden=0))
        db.session.add(Story(id=20, media_topic="Review 4", media_desc="desc", media_text="text", mediatype_id=5, genre_id=4, storytype_id=2, create_time=datetime.now(), owner="", lang_id=2, country_id=1, hidden=0))

        # Interviews
        db.session.add(Story(id=21, media_topic="Interview 1", media_desc="desc", media_text="text", mediatype_id=5, genre_id=1, storytype_id=3, create_time=datetime.now(), owner="", lang_id=2, country_id=1, hidden=0))
        db.session.add(Story(id=22, media_topic="Interview 2", media_desc="desc", media_text="text", mediatype_id=5, genre_id=1, storytype_id=3, create_time=datetime.now(), owner="", lang_id=2, country_id=1, hidden=0))
        db.session.add(Story(id=23, media_topic="Interview 3", media_desc="desc", media_text="text", mediatype_id=5, genre_id=1, storytype_id=3, create_time=datetime.now(), owner="", lang_id=2, country_id=1, hidden=0))
        db.session.add(Story(id=24, media_topic="Interview 4", media_desc="desc", media_text="text", mediatype_id=5, genre_id=1, storytype_id=3, create_time=datetime.now(), owner="", lang_id=2, country_id=1, hidden=0))

        # News
        db.session.add(Story(id=25, media_topic="News 1", media_desc="desc", media_text="text", mediatype_id=5, genre_id=1, storytype_id=4, create_time=datetime.now(), owner="", lang_id=2, country_id=1, hidden=0))
        db.session.add(Story(id=26, media_topic="News 2", media_desc="desc", media_text="text", mediatype_id=5, genre_id=1, storytype_id=4, create_time=datetime.now(), owner="", lang_id=2, country_id=1, hidden=0))
        db.session.add(Story(id=27, media_topic="News 3", media_desc="desc", media_text="text", mediatype_id=5, genre_id=1, storytype_id=4, create_time=datetime.now(), owner="", lang_id=2, country_id=1, hidden=0))
        db.session.add(Story(id=28, media_topic="News 4", media_desc="desc", media_text="text", mediatype_id=5, genre_id=1, storytype_id=4, create_time=datetime.now(), owner="", lang_id=2, country_id=1, hidden=0))

        # StoryType
        db.session.add(StoryType(id=1, type_name='general'))
        db.session.add(StoryType(id=2, type_name='reviews'))
        db.session.add(StoryType(id=3, type_name='interviews'))
        db.session.add(StoryType(id=4, type_name='news'))
        db.session.add(StoryType(id=5, type_name='other'))

        # Country
        db.session.add(Country(id=1, country_code='fi', country_name='Finland'))
        db.session.add(Country(id=2, country_code='se', country_name='Sweden'))
        db.session.add(Country(id=3, country_code='ee', country_name='Estonia'))
        db.session.add(Country(id=4, country_code='dk', country_name='Denmark'))
        db.session.add(Country(id=5, country_code='de', country_name='Germany'))

        # MapType
        db.session.add(MapType(id=1, name="Outdoor"))
        db.session.add(MapType(id=2, name="Indoor"))
        db.session.add(MapType(id=3, name="Handrail"))
        db.session.add(MapType(id=4, name="Shop"))

        # MapCountry 
        db.session.add(MapCountry(id=1, maa="Finland", lat="61.938205", lon="26.315953", koodi=""))
        db.session.add(MapCountry(id=2, maa="Sweden", lat="62.905199", lon="17.051174", koodi=""))
        db.session.add(MapCountry(id=3, maa="USA", lat="39.607428", lon="-99.134190", koodi=""))
        db.session.add(MapCountry(id=4, maa="Germany", lat="51.076102", lon="10.252248", koodi=""))

        # MapTown (country 1)
        db.session.add(MapTown(id=1, paikkakunta="Helsinki", maa_id=1, lat="60.186427", lon="24.933512"))
        db.session.add(MapTown(id=2, paikkakunta="Paikkakunta 2", maa_id=1, lat="", lon=""))
        db.session.add(MapTown(id=3, paikkakunta="Paikkakunta 3", maa_id=1, lat="", lon=""))
        db.session.add(MapTown(id=4, paikkakunta="Paikkakunta 4", maa_id=1, lat="", lon=""))

        # MapTown (country 2)
        db.session.add(MapTown(id=5, paikkakunta="Stockholm", maa_id=2, lat="59.339025", lon="18.068564"))
        db.session.add(MapTown(id=6, paikkakunta="Paikkakunta 6", maa_id=2, lat="", lon=""))
        db.session.add(MapTown(id=7, paikkakunta="Paikkakunta 7", maa_id=2, lat="", lon=""))
        db.session.add(MapTown(id=8, paikkakunta="Paikkakunta 8", maa_id=2, lat="", lon=""))

        # MapTown (country 3)
        db.session.add(MapTown(id=9, paikkakunta="San Francisco", maa_id=3, lat="37.774235", lon="-122.409450"))
        db.session.add(MapTown(id=10, paikkakunta="Paikkakunta 10", maa_id=3, lat="", lon=""))
        db.session.add(MapTown(id=11, paikkakunta="Paikkakunta 11", maa_id=3, lat="", lon=""))
        db.session.add(MapTown(id=12, paikkakunta="Paikkakunta 12", maa_id=3, lat="", lon=""))

        # MapTown (country 4)
        db.session.add(MapTown(id=13, paikkakunta="Paikkakunta 13", maa_id=4, lat="", lon=""))
        db.session.add(MapTown(id=14, paikkakunta="Paikkakunta 14", maa_id=4, lat="", lon=""))
        db.session.add(MapTown(id=15, paikkakunta="Paikkakunta 15", maa_id=4, lat="", lon=""))
        db.session.add(MapTown(id=16, paikkakunta="Paikkakunta 16", maa_id=4, lat="", lon=""))

        # Spots
        db.session.add(MapSpot(kartta_id=1, paikkakunta_id=1, user_id=1, nimi="Country 1, Town 1, Type 1, Spot 1", info="Micropolis Skateboard Park", tyyppi=1, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=1, latlon="60.193521, 24.928171"))
        db.session.add(MapSpot(kartta_id=2, paikkakunta_id=1, user_id=1, nimi="Country 1, Town 1, Type 2, Spot 2", info="Kontulan skeittihalli", tyyppi=2, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=1, latlon="60.236949, 25.086057"))
        db.session.add(MapSpot(kartta_id=3, paikkakunta_id=1, user_id=1, nimi="Country 1, Town 1, Type 3, Spot 3", info="Kaivopuiston hänkkä", tyyppi=3, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=1, latlon="60.156616, 24.957480"))
        db.session.add(MapSpot(kartta_id=4, paikkakunta_id=1, user_id=1, nimi="Country 1, Town 1, Type 4, Spot 4", info="Ponke's The Shop", tyyppi=4, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=1, latlon="60.169810, 24.937334"))

        db.session.add(MapSpot(kartta_id=5, paikkakunta_id=2, user_id=1, nimi="Country 1, Town 2, Type 1, Spot 5", info="desc", tyyppi=1, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=1, latlon=""))
        db.session.add(MapSpot(kartta_id=6, paikkakunta_id=2, user_id=1, nimi="Country 1, Town 2, Type 2, Spot 6", info="desc", tyyppi=2, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=1, latlon=""))
        db.session.add(MapSpot(kartta_id=7, paikkakunta_id=2, user_id=1, nimi="Country 1, Town 2, Type 3, Spot 7", info="desc", tyyppi=3, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=1, latlon=""))
        db.session.add(MapSpot(kartta_id=8, paikkakunta_id=2, user_id=1, nimi="Country 1, Town 2, Type 4, Spot 8", info="desc", tyyppi=4, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=1, latlon=""))

        db.session.add(MapSpot(kartta_id=9, paikkakunta_id=3, user_id=1, nimi="Country 1, Town 3, Type 1, Spot 9", info="desc", tyyppi=1, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=1, latlon=""))
        db.session.add(MapSpot(kartta_id=10, paikkakunta_id=3, user_id=1, nimi="Country 1, Town 3, Type 2, Spot 10", info="desc", tyyppi=2, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=1, latlon=""))
        db.session.add(MapSpot(kartta_id=11, paikkakunta_id=3, user_id=1, nimi="Country 1, Town 3, Type 3, Spot 11", info="desc", tyyppi=3, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=1, latlon=""))
        db.session.add(MapSpot(kartta_id=12, paikkakunta_id=3, user_id=1, nimi="Country 1, Town 3, Type 4, Spot 12", info="desc", tyyppi=4, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=1, latlon=""))

        db.session.add(MapSpot(kartta_id=13, paikkakunta_id=4, user_id=1, nimi="Country 1, Town 4, Type 1, Spot 13", info="desc", tyyppi=1, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=1, latlon=""))
        db.session.add(MapSpot(kartta_id=14, paikkakunta_id=4, user_id=1, nimi="Country 1, Town 4, Type 2, Spot 14", info="desc", tyyppi=2, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=1, latlon=""))
        db.session.add(MapSpot(kartta_id=15, paikkakunta_id=4, user_id=1, nimi="Country 1, Town 4, Type 3, Spot 15", info="desc", tyyppi=3, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=1, latlon=""))
        db.session.add(MapSpot(kartta_id=16, paikkakunta_id=4, user_id=1, nimi="Country 1, Town 4, Type 4, Spot 16", info="desc", tyyppi=4, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=1, latlon=""))

        db.session.add(MapSpot(kartta_id=17, paikkakunta_id=5, user_id=1, nimi="Country 2, Town 5, Type 1, Spot 17", info="desc", tyyppi=1, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=2, latlon=""))
        db.session.add(MapSpot(kartta_id=18, paikkakunta_id=5, user_id=1, nimi="Country 2, Town 5, Type 2, Spot 18", info="desc", tyyppi=2, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=2, latlon=""))
        db.session.add(MapSpot(kartta_id=19, paikkakunta_id=5, user_id=1, nimi="Country 2, Town 5, Type 3, Spot 19", info="desc", tyyppi=3, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=2, latlon=""))
        db.session.add(MapSpot(kartta_id=20, paikkakunta_id=5, user_id=1, nimi="Country 2, Town 5, Type 4, Spot 20", info="desc", tyyppi=4, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=2, latlon=""))

        db.session.add(MapSpot(kartta_id=21, paikkakunta_id=6, user_id=1, nimi="Country 2, Town 6, Type 1, Spot 21", info="desc", tyyppi=1, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=2, latlon=""))
        db.session.add(MapSpot(kartta_id=22, paikkakunta_id=6, user_id=1, nimi="Country 2, Town 6, Type 2, Spot 22", info="desc", tyyppi=2, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=2, latlon=""))
        db.session.add(MapSpot(kartta_id=23, paikkakunta_id=6, user_id=1, nimi="Country 2, Town 6, Type 3, Spot 23", info="desc", tyyppi=3, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=2, latlon=""))
        db.session.add(MapSpot(kartta_id=24, paikkakunta_id=6, user_id=1, nimi="Country 2, Town 6, Type 4, Spot 24", info="desc", tyyppi=4, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=2, latlon=""))

        db.session.add(MapSpot(kartta_id=25, paikkakunta_id=7, user_id=1, nimi="Country 2, Town 7, Type 1, Spot 25", info="desc", tyyppi=1, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=2, latlon=""))
        db.session.add(MapSpot(kartta_id=26, paikkakunta_id=7, user_id=1, nimi="Country 2, Town 7, Type 2, Spot 26", info="desc", tyyppi=2, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=2, latlon=""))
        db.session.add(MapSpot(kartta_id=27, paikkakunta_id=7, user_id=1, nimi="Country 2, Town 7, Type 3, Spot 27", info="desc", tyyppi=3, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=2, latlon=""))
        db.session.add(MapSpot(kartta_id=28, paikkakunta_id=7, user_id=1, nimi="Country 2, Town 7, Type 4, Spot 28", info="desc", tyyppi=4, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=2, latlon=""))

        db.session.add(MapSpot(kartta_id=29, paikkakunta_id=8, user_id=1, nimi="Country 2, Town 8, Type 1, Spot 29", info="desc", tyyppi=1, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=2, latlon=""))
        db.session.add(MapSpot(kartta_id=30, paikkakunta_id=8, user_id=1, nimi="Country 2, Town 8, Type 2, Spot 30", info="desc", tyyppi=2, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=2, latlon=""))
        db.session.add(MapSpot(kartta_id=31, paikkakunta_id=8, user_id=1, nimi="Country 2, Town 8, Type 3, Spot 31", info="desc", tyyppi=3, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=2, latlon=""))
        db.session.add(MapSpot(kartta_id=32, paikkakunta_id=8, user_id=1, nimi="Country 2, Town 8, Type 4, Spot 32", info="desc", tyyppi=4, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=2, latlon=""))

        db.session.add(MapSpot(kartta_id=33, paikkakunta_id=9, user_id=1, nimi="Country 3, Town 9, Type 1, Spot 33", info="desc", tyyppi=1, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=3, latlon=""))
        db.session.add(MapSpot(kartta_id=34, paikkakunta_id=9, user_id=1, nimi="Country 3, Town 9, Type 2, Spot 34", info="desc", tyyppi=2, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=3, latlon=""))
        db.session.add(MapSpot(kartta_id=35, paikkakunta_id=9, user_id=1, nimi="Country 3, Town 9, Type 3, Spot 35", info="desc", tyyppi=3, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=3, latlon=""))
        db.session.add(MapSpot(kartta_id=36, paikkakunta_id=9, user_id=1, nimi="Country 3, Town 9, Type 4, Spot 36", info="desc", tyyppi=4, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=3, latlon=""))

        db.session.add(MapSpot(kartta_id=37, paikkakunta_id=10, user_id=1, nimi="Country 3, Town 10, Type 1, Spot 37", info="desc", tyyppi=1, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=3, latlon=""))
        db.session.add(MapSpot(kartta_id=38, paikkakunta_id=10, user_id=1, nimi="Country 3, Town 10, Type 2, Spot 38", info="desc", tyyppi=2, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=3, latlon=""))
        db.session.add(MapSpot(kartta_id=39, paikkakunta_id=10, user_id=1, nimi="Country 3, Town 10, Type 3, Spot 39", info="desc", tyyppi=3, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=3, latlon=""))
        db.session.add(MapSpot(kartta_id=40, paikkakunta_id=10, user_id=1, nimi="Country 3, Town 10, Type 4, Spot 40", info="desc", tyyppi=4, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=3, latlon=""))

        db.session.add(MapSpot(kartta_id=41, paikkakunta_id=11, user_id=1, nimi="Country 3, Town 11, Type 1, Spot 41", info="desc", tyyppi=1, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=3, latlon=""))
        db.session.add(MapSpot(kartta_id=42, paikkakunta_id=11, user_id=1, nimi="Country 3, Town 11, Type 2, Spot 42", info="desc", tyyppi=2, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=3, latlon=""))
        db.session.add(MapSpot(kartta_id=43, paikkakunta_id=11, user_id=1, nimi="Country 3, Town 11, Type 3, Spot 43", info="desc", tyyppi=3, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=3, latlon=""))
        db.session.add(MapSpot(kartta_id=44, paikkakunta_id=11, user_id=1, nimi="Country 3, Town 11, Type 4, Spot 44", info="desc", tyyppi=4, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=3, latlon=""))

        db.session.add(MapSpot(kartta_id=45, paikkakunta_id=12, user_id=1, nimi="Country 3, Town 12, Type 1, Spot 45", info="desc", tyyppi=1, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=3, latlon=""))
        db.session.add(MapSpot(kartta_id=46, paikkakunta_id=12, user_id=1, nimi="Country 3, Town 12, Type 2, Spot 46", info="desc", tyyppi=2, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=3, latlon=""))
        db.session.add(MapSpot(kartta_id=47, paikkakunta_id=12, user_id=1, nimi="Country 3, Town 12, Type 3, Spot 47", info="desc", tyyppi=3, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=3, latlon=""))
        db.session.add(MapSpot(kartta_id=48, paikkakunta_id=12, user_id=1, nimi="Country 3, Town 12, Type 4, Spot 48", info="desc", tyyppi=4, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=3, latlon=""))

        db.session.add(MapSpot(kartta_id=49, paikkakunta_id=13, user_id=1, nimi="Country 4, Town 13, Type 1, Spot 49", info="desc", tyyppi=1, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=4, latlon=""))
        db.session.add(MapSpot(kartta_id=50, paikkakunta_id=13, user_id=1, nimi="Country 4, Town 13, Type 2, Spot 50", info="desc", tyyppi=2, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=4, latlon=""))
        db.session.add(MapSpot(kartta_id=51, paikkakunta_id=13, user_id=1, nimi="Country 4, Town 13, Type 3, Spot 51", info="desc", tyyppi=3, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=4, latlon=""))
        db.session.add(MapSpot(kartta_id=52, paikkakunta_id=13, user_id=1, nimi="Country 4, Town 13, Type 4, Spot 52", info="desc", tyyppi=4, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=4, latlon=""))

        db.session.add(MapSpot(kartta_id=53, paikkakunta_id=14, user_id=1, nimi="Country 4, Town 14, Type 1, Spot 53", info="desc", tyyppi=1, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=4, latlon=""))
        db.session.add(MapSpot(kartta_id=54, paikkakunta_id=14, user_id=1, nimi="Country 4, Town 14, Type 2, Spot 54", info="desc", tyyppi=2, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=4, latlon=""))
        db.session.add(MapSpot(kartta_id=55, paikkakunta_id=14, user_id=1, nimi="Country 4, Town 14, Type 3, Spot 55", info="desc", tyyppi=3, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=4, latlon=""))
        db.session.add(MapSpot(kartta_id=56, paikkakunta_id=14, user_id=1, nimi="Country 4, Town 14, Type 4, Spot 56", info="desc", tyyppi=4, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=4, latlon=""))

        db.session.add(MapSpot(kartta_id=57, paikkakunta_id=15, user_id=1, nimi="Country 4, Town 15, Type 1, Spot 57", info="desc", tyyppi=1, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=4, latlon=""))
        db.session.add(MapSpot(kartta_id=58, paikkakunta_id=15, user_id=1, nimi="Country 4, Town 15, Type 2, Spot 58", info="desc", tyyppi=2, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=4, latlon=""))
        db.session.add(MapSpot(kartta_id=59, paikkakunta_id=15, user_id=1, nimi="Country 4, Town 15, Type 3, Spot 59", info="desc", tyyppi=3, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=4, latlon=""))
        db.session.add(MapSpot(kartta_id=60, paikkakunta_id=15, user_id=1, nimi="Country 4, Town 15, Type 4, Spot 60", info="desc", tyyppi=4, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=4, latlon=""))

        db.session.add(MapSpot(kartta_id=61, paikkakunta_id=16, user_id=1, nimi="Country 4, Town 12, Type 1, Spot 61", info="desc", tyyppi=1, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=4, latlon=""))
        db.session.add(MapSpot(kartta_id=62, paikkakunta_id=16, user_id=1, nimi="Country 4, Town 12, Type 2, Spot 62", info="desc", tyyppi=2, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=4, latlon=""))
        db.session.add(MapSpot(kartta_id=63, paikkakunta_id=16, user_id=1, nimi="Country 4, Town 12, Type 3, Spot 63", info="desc", tyyppi=3, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=4, latlon=""))
        db.session.add(MapSpot(kartta_id=64, paikkakunta_id=16, user_id=1, nimi="Country 4, Town 12, Type 4, Spot 64", info="desc", tyyppi=4, temp=0, paivays=datetime.now(), karttalinkki="", maa_id=4, latlon=""))

        # Users
        db.session.add(User(user_id=1, level=1, username="admin", password=bcrypt.generate_password_hash("admin"), name="Admin Tester", bornyear=2010, email="admin@example.com", email2="", info="", location="", date=datetime.now(), hobbies="", open=1, extrainfo="", sukupuoli=1, icq="", apulainen=1, last_login=datetime.now(), chat=1, oikeus=1, lang_id=1, login_count=1, lastloginip="", lastloginclient="", address="", postnumber="", emails=1, puhelin="", kantaasiakasnro="", lamina_lisatieto="", blogs=1, user_showid=1, blog_level=1, last_login2=datetime.now(), messenger="", myspace="", rss="", youtube="", ircgalleria="", last_profile_update=datetime.now(), avatar="", flickr_username=""))
        db.session.add(User(user_id=2, level=0, username="tester", password=bcrypt.generate_password_hash("tester"), name="User Tester", bornyear=2010, email="tester@example.com", email2="", info="", location="", date=datetime.now(), hobbies="", open=1, extrainfo="", sukupuoli=1, icq="", apulainen=1, last_login=datetime.now(), chat=1, oikeus=1, lang_id=1, login_count=1, lastloginip="", lastloginclient="", address="", postnumber="", emails=1, puhelin="", kantaasiakasnro="", lamina_lisatieto="", blogs=1, user_showid=1, blog_level=1, last_login2=datetime.now(), messenger="", myspace="", rss="", youtube="", ircgalleria="", last_profile_update=datetime.now(), avatar="", flickr_username=""))

        # Uploads
        db.session.add(Uploads(id=1, user_id=2 ,create_time=datetime.now(), path="21-04-2020_10-43-32_venice_skatepark_covid.png"))

        db.session.commit()
        print("Inserting example data finished")

if __name__ == "__main__":
    if(os.getenv('MYSQL_HOST') == "db"): # localhost
        create_db()
        seed_db()
    else:
        print("Don´t want to override production database!")