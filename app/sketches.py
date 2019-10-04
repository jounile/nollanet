

"""

# NollaNet TV jaksot
select media_id, media_topic, media_desc, owner from media_table where media_type =6 and lang_id=2 and media_topic like '%Nolla.net TV%' order by create_time desc;

# Haetaan HYLÄTTY sähköpostin tekstit tietokannasta
select otsikko, teksti1 from yleiset where yleiset_id=9

# Haetaan HYVÄKSYTYN sähköpostin tekstit tietokannasta. 
select otsikko, teksti1 from yleiset where yleiset_id=1

# Hakemukset (level=99)
select username,name,sukupuoli,bornyear,email,homepage,location,info,hobbies,open,extrainfo,user_id from users where level = 99 and lang_id = 2 order by user_id

# Hylätyt (level=100)
select username, name from users where level = 100;

# Käyttäjä hyväksytään
update users set level = 5 where user_id = %s and level = 99;

# Muutetaan ruksitut käyttäjät
update users set level = 5 where user_id in ($hyvaksytyt) and level = 99;

# Siirretään hylätyt käyttäjät varastoon levelille 100
update users set level = 100, password='hylätty_23.123f5M6', username = concat('hylätty_',username) where user_id in ($hylatyt) and level = 99;

# List story types
select type, teksti from story_type order by type;

# Sinulla on oikeudet syöttää sisältää mutta et pysty sitä hyväksymään näytettäväksi. Näet vain omistamasi sisältötiedot.
if (userlevel > 3)

# Chat count
select count(*) from chat where type = 1 and userkey is not null;

# List chats
select username, chattime_id, text, iplog, userlevel, private from chat where type in (0,9) order by chattime_id desc;

# Get all email addresses which are wrong 
select username,name,user_id,bornyear,email,homepage,location,last_login,hobbies,open,extrainfo from users where level < 10;

# Lamina -kaupan  ylläpitotyökalut
select * from navigointi_admin where tila = 2 order by otsikko;

# Profile images
select media_file,media_file_type from naama_photos where media_id=1;

# Kuvan tiedot muutettu.
UPDATE naama_photos SET media_topic='$media_topic', media_desc='$media_desc', media_genre='$media_genre' WHERE media_id=$media_id;

# Poista naamakuva 
DELETE FROM naama_photos WHERE media_id=$media_id LIMIT 1;

# Naamagallerian kuvaehdotusten hyväksyminen
SELECT media_id,media_topic,media_desc,media_file_size,media_file_type,create_time,owner,moved,media_genre FROM naama_photos WHERE media_genre=".$genre." and media_type='1' ORDER BY create_time;

# Spotmap
SELECT kartta_id,paikkakunta_id,user_id,nimi,info,tyyppi,temp,karttalinkki,paivays,paikkakunta_text,maa_id,maa_text FROM kartta_ehdotus WHERE maa_id=$country ORDER BY paivays;

# Delete from spotmap
DELETE FROM kartta_ehdotus WHERE kartta_id=$id LIMIT 1;

# Listaa maat
select id,maa from kartta_maa;

# Syötä spotti ehdotus
insert into kartta_tieto ( paikkakunta_id,user_id,nimi,info,tyyppi,temp,karttalinkki,paivays,maa_id ) values ( '$pk_id','$spotti[1]','$spotti[2]','$spotti[3]','$spotti[4]','$spotti[5]','$spotti[6]','$spotti[7]','$maa_id' )

# Päivitä temp-kenttä 0->1 (hyväksytty)
UPDATE kartta_ehdotus SET temp=1 where kartta_id=$id;

# Syötä uusi kaupunki
insert into kartta_paikkakunta ( paikkakunta, maa_id ) values ( '$spotti[8]', '$ins_maa_id' );

# Eri käyttäjien loggauksia toissapäivänä yhteensä: ".$tiedot[0]." kappaletta
select count(*) from users   WHERE TO_DAYS(NOW())-2 = TO_DAYS(last_login);

# different menu depending on userlevel
userlevel = 1
levels = get_levels(userlevel)

# admins (levels 1-4)
def get_levels(userlevel):
    if userlevel == 1:
        levels = "(5,4,3,2,1)"
    elif userlevel == 4:
        levels = "(5,4)"
    elif userlevel == 3:
        levels = "(5,4,3)"
    else :
        levels = "(5)"
    return levels

@app.route('/api/mainmenu')
@auto.doc()
def get_mainmenu():
    sql = "SELECT * FROM departments WHERE type=1 AND alavalikko=0 AND lang_id=2 AND paavalikko IN {0} ORDER BY paavalikko".format(levels)


@app.route('/api/submenu0')
@auto.doc()
def get_submenu0():
    sql = "SELECT name, url, information, logo, paavalikko, alavalikko, level FROM departments WHERE type=1 AND alavalikko=0 AND lang_id=2 AND level IN {0} ORDER BY paavalikko".format(levels)


@app.route('/api/submenu4')
@auto.doc()
def get_submenu4():
    sql = "SELECT name, url, information, logo, paavalikko, alavalikko, level FROM departments WHERE type=1 AND alavalikko=4 AND lang_id=2 AND level IN {0} ORDER BY paavalikko".format(levels)


@app.route('/api/submenu5')
@auto.doc()
def get_submenu5():
    sql = "SELECT name, url, information, logo, paavalikko, alavalikko, level FROM departments WHERE type=1 AND alavalikko=5 AND lang_id=2 AND level IN {0} ORDER BY paavalikko".format(levels)


@app.route('/api/submenu99')
@auto.doc()
def get_submenu99():
    sql = "SELECT name, url, information, logo FROM departments WHERE type=1 AND alavalikko=99 AND lang_id=2 AND level IN {0} ORDER BY paavalikko".format(levels)


@app.route('/api/submenu100')
@auto.doc()
def get_submenu100():
    sql = "SELECT name, url, information, logo FROM departments WHERE type=1 AND alavalikko=100 AND lang_id=2 AND level IN {0} ORDER BY paavalikko".format(levels)


@app.route('/users', methods=['GET'])
def view_users(): 
    if not session.get('logged_in'):
        flash('You are not logged in')
        return render_template('auth/login.html')
    else:
        response = requests.get(url=request.url_root + "api/users")
        users = response.json()
        return render_template('views/users.html', users=users)

@app.route("/api/media/insertfile")
@auto.doc()
def insert_media_with_file():
    media_type = "media_type"
    media_genre = "media_genre"
    story_type = "story_type"
    media_topic = "media_topic"
    media_desc = "media_desc"
    username = "owner"
    create_time = get_now()
    media_file = "media_file"
    media_file_size = "media_file_size"
    media_file_type = "media_file_type"
    lang_id = "2"
    sql= "INSERT INTO media_table (media_type, media_genre, story_type, media_topic, media_desc, owner, create_time, media_file, media_file_size, media_file_type, lang_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor = db.connection.cursor()
    cursor.execute(sql, (media_type, media_genre, story_type, media_topic, media_desc, username, create_time, media_file, media_file_size, media_file_type, lang_id))
    print ("Insert file done")
    return render_template("views/about.html")

@app.route("/api/media/updatefile")
@auto.doc()
def update_media_with_file():
    media_type = "5"
    media_genre = "4"
    story_type = "1"
    media_topic = "media_topic"
    media_desc = "media_desc"
    create_time = get_now()
    media_file = "media_file"
    media_file_size = "media_file_size"
    media_file_type = "media_file_type"
    lang_id = "2"

    media_id = "6334"
    owner = "owner"

    sql = "UPDATE media_table SET media_type=%s, media_genre=%s, story_type=%s, media_topic=%s, media_desc=%s, create_time=%s, media_file=%s, media_file_size=%s, media_file_type=%s, lang_id=%s WHERE media_id=%s AND owner=%s"
    cursor = db.connection.cursor()
    cursor.execute(sql, (media_type, media_genre, story_type, media_topic, media_desc, create_time, media_file, media_file_size, media_file_type, lang_id, media_id, owner))
    print ("Update file done")
    return render_template("views/about.html")
"""