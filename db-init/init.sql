CREATE DATABASE IF NOT EXISTS nolla;
USE nolla;
SET SQL_MODE='ALLOW_INVALID_DATES';
--
-- Table structure for table `comment`
--

DROP TABLE IF EXISTS `comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `comment` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) NOT NULL DEFAULT '0',
  `header` varchar(250) DEFAULT NULL,
  `comment` longtext,
  `media_id` bigint(20) DEFAULT NULL,
  `comment_user_id` bigint(20) DEFAULT NULL,
  `youtube_id` bigint(20) DEFAULT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `tapahtuma_id` bigint(20) DEFAULT NULL,
  `diary_id` int(20) DEFAULT NULL,
  `kilpailu_id` int(10) DEFAULT NULL,
  `videoblog_id` int(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_2` (`id`),
  KEY `id` (`id`,`user_id`,`media_id`,`comment_user_id`,`youtube_id`),
  KEY `timestamp` (`timestamp`),
  KEY `diary_id` (`diary_id`),
  KEY `tapahtuma_id` (`tapahtuma_id`),
  KEY `staattinen_id` (`kilpailu_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3255 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `countries`
--

DROP TABLE IF EXISTS `countries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `countries` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `country_code` varchar(50) DEFAULT NULL,
  `country_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `countries`
--

LOCK TABLES `countries` WRITE;
/*!40000 ALTER TABLE `countries` DISABLE KEYS */;
INSERT INTO `countries` VALUES (1,'fi','Finland'),(2,'se','Sweden'),(3,'ee','Estonia'),(4,'dk','Denmark'),(5,'de','Germany');
/*!40000 ALTER TABLE `countries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `genre`
--

DROP TABLE IF EXISTS `genre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `genre` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type_id` int(11) DEFAULT NULL,
  `type_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genre`
--

LOCK TABLES `genre` WRITE;
/*!40000 ALTER TABLE `genre` DISABLE KEYS */;
INSERT INTO `genre` VALUES (1,1,'skateboarding'),(2,2,'snowboarding'),(3,3,'nollagang'),(4,4,'snowskate'),(5,0,'none');
/*!40000 ALTER TABLE `genre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `link_categories`
--

DROP TABLE IF EXISTS `link_categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `link_categories` (
  `id` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `user_id` int(50) DEFAULT NULL,
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `link_categories`
--

LOCK TABLES `link_categories` WRITE;
/*!40000 ALTER TABLE `link_categories` DISABLE KEYS */;
INSERT INTO `link_categories` VALUES (1,'Magazines',61401,'2020-02-21 13:53:11'),(2,'Shops',61401,'2020-02-21 13:59:37'),(18,'Skateboard brands',2115,'2020-02-21 16:16:14'),(19,'Youtube channels',2115,'2020-02-21 16:19:26'),(20,'Skateboarding organizations',2115,'2020-02-21 16:19:49'),(21,'Vimeo channels',2115,'2020-02-21 16:20:17'),(22,'Skateboarding events',2115,'2020-02-21 16:21:38');
/*!40000 ALTER TABLE `link_categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `links`
--

DROP TABLE IF EXISTS `links`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `links` (
  `id` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `url` varchar(255) NOT NULL,
  `category` int(50) NOT NULL,
  `user_id` int(50) DEFAULT NULL,
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `links`
--

LOCK TABLES `links` WRITE;
/*!40000 ALTER TABLE `links` DISABLE KEYS */;
INSERT INTO `links` VALUES (1,'Hangup','http://hangup.fi',1,61401,'2020-02-21 16:37:37'),(2,'Lamina','https://lamina.fi',2,2115,'2020-02-21 16:37:27'),(9,'asteskateboards','https://vimeo.com/asteskateboards',21,2115,'2020-02-21 16:20:27'),(10,'Suomen rullalautaliitto','http://rullalauta.fi/',20,2115,'2020-02-21 16:21:13'),(11,'Helride','http://helride.fi/',22,2115,'2020-02-21 16:22:13'),(12,'happyhourskateboards','http://www.happyhourskateboards.com/',18,2115,'2020-02-21 16:33:16'),(13,'chasingthespot','https://www.chasingthespot.com/',20,2115,'2020-02-21 16:34:50'),(14,'Supla skeittauksesta','https://www.supla.fi/ohjelmat/skeittauksesta',1,2115,'2020-02-21 16:36:49'),(15,'Ponkes','https://www.ponkes.com/',2,2115,'2020-02-21 16:37:11'),(16,'Trelogy','http://trelogy.fi/',22,2115,'2020-02-21 16:39:16'),(17,'Skate SM','http://trelogy.fi/skate-sm/',22,2115,'2020-02-21 16:39:36'),(18,'Manserama','http://trelogy.fi/ohjelma/manserama/',22,2115,'2020-02-21 16:40:01'),(19,'Freeskatemag','https://www.freeskatemag.com/',1,2115,'2020-02-21 16:46:57');
/*!40000 ALTER TABLE `links` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `map_country`
--

DROP TABLE IF EXISTS `map_country`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `map_country` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `maa` varchar(100) NOT NULL DEFAULT '',
  `lat` varchar(50) DEFAULT NULL,
  `lon` varchar(50) DEFAULT NULL,
  `koodi` varchar(2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `map_country`
--

LOCK TABLES `map_country` WRITE;
/*!40000 ALTER TABLE `map_country` DISABLE KEYS */;
INSERT INTO `map_country` VALUES (1,'Suomi',NULL,NULL,'FI'),(2,'Espanja','40.44694705960048','-2.8125','ES'),(3,'Ruotsi','61.14323525084058','15.205078125','SE'),(4,'Norja','61.81466389468391','9.404296875','NO'),(5,'Tanska','55.37911044801047','9.8876953125','DK'),(6,'Ranska','46.61926103617151','2.548828125','FR'),(7,'Saksa','51.06901665960392','10.4150390625','DE'),(8,'Tsekki','49.724479188712984','15.29296875','CZ'),(9,'Itävalta','47.398349200359256','14.0625','AT'),(10,'Englanti','55.05320258537112','-2.6806640625',NULL),(11,'Sveitsi','46.800059446787316','7.998046875',NULL),(12,'Yhdysvallat','41.3108238809182','-100.01953125','US'),(13,'Irlanti','53.12040528310657','-8.0859375',NULL),(14,'Viro',NULL,NULL,NULL),(15,'Belgia',NULL,NULL,NULL),(16,'Hollanti','51.80861475198521','5.6689453125','NL'),(17,'Kanada','57.844750992891','-102.392578125','CA'),(19,'Portugali',NULL,NULL,NULL),(21,'Australia','-25.48295117535531','133.2421875','AU'),(22,'Venäjä',NULL,NULL,NULL),(23,'Italia','43.45291889355465','12.216796875','IT'),(24,'Bulgaria',NULL,NULL,NULL),(25,'Kiina',NULL,NULL,NULL),(26,'Latvia','56.9449741808516','25.9716796875','LV'),(27,'Liettua','55.229023057406344','23.9501953125','LT');
/*!40000 ALTER TABLE `map_country` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `map_spot`
--

DROP TABLE IF EXISTS `map_spot`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `map_spot` (
  `kartta_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `paikkakunta_id` int(10) unsigned NOT NULL DEFAULT '0',
  `user_id` int(10) unsigned NOT NULL DEFAULT '0',
  `nimi` varchar(200) NOT NULL DEFAULT '',
  `info` mediumtext NOT NULL,
  `tyyppi` smallint(5) unsigned NOT NULL DEFAULT '0',
  `temp` tinyint(4) NOT NULL DEFAULT '0',
  `paivays` datetime NOT NULL DEFAULT '0000-00-00',
  `karttalinkki` varchar(200) DEFAULT NULL,
  `maa_id` int(10) unsigned NOT NULL DEFAULT '0',
  `latlon` tinytext,
  PRIMARY KEY (`kartta_id`),
  UNIQUE KEY `kartta_id_2` (`kartta_id`),
  KEY `kartta_id` (`kartta_id`),
  KEY `user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2164 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `map_town`
--

DROP TABLE IF EXISTS `map_town`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `map_town` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `paikkakunta` varchar(40) NOT NULL DEFAULT '',
  `maa_id` int(10) unsigned NOT NULL DEFAULT '0',
  `lat` varchar(50) DEFAULT NULL,
  `lon` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `paikkakunta` (`paikkakunta`),
  KEY `maa_id` (`maa_id`)
) ENGINE=InnoDB AUTO_INCREMENT=325 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `map_type`
--

DROP TABLE IF EXISTS `map_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `map_type` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `map_type`
--

LOCK TABLES `map_type` WRITE;
/*!40000 ALTER TABLE `map_type` DISABLE KEYS */;
INSERT INTO `map_type` VALUES (1,'Outdoor'),(2,'Indoor'),(3,'Handrail'),(4,'Shop');
/*!40000 ALTER TABLE `map_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `media`
--

DROP TABLE IF EXISTS `media`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `media` (
  `media_id` int(11) NOT NULL AUTO_INCREMENT,
  `media_type` tinyint(4) NOT NULL DEFAULT '0',
  `media_genre` tinyint(4) NOT NULL DEFAULT '0',
  `story_type` tinyint(4) DEFAULT NULL,
  `media_topic` tinytext NOT NULL,
  `media_desc` text,
  `media_text` longtext,
  `owner` varchar(20) NOT NULL DEFAULT '',
  `create_time` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `other` tinyint(4) DEFAULT NULL,
  `type` tinyint(4) NOT NULL DEFAULT '0',
  `lyhyt` mediumtext,
  `media_file` longblob,
  `media_file_size` tinytext,
  `media_file_type` tinytext,
  `lyhyt_ok` tinyint(1) DEFAULT '0',
  `lang_id` tinyint(4) NOT NULL DEFAULT '1',
  `country_id` int(11) DEFAULT NULL,
  `hidden` int(11) NOT NULL COMMENT 'Media is hidden when value is 1',
  UNIQUE KEY `media_id_2` (`media_id`),
  KEY `media_type` (`media_type`),
  KEY `media_genre` (`media_genre`),
  KEY `type` (`type`),
  KEY `create_time` (`create_time`)
) ENGINE=InnoDB AUTO_INCREMENT=6355 DEFAULT CHARSET=latin1 PACK_KEYS=1;
/*!40101 SET character_set_client = @saved_cs_client */;


--
-- Table structure for table `media_type`
--

DROP TABLE IF EXISTS `media_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `media_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type_id` int(11) DEFAULT NULL,
  `type_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `media_type`
--

LOCK TABLES `media_type` WRITE;
/*!40000 ALTER TABLE `media_type` DISABLE KEYS */;
INSERT INTO `media_type` VALUES (1,1,'photo'),(2,2,'mediatype2'),(3,3,'music'),(4,4,'movies'),(5,5,'stories'),(6,6,'video'),(7,0,'none');
/*!40000 ALTER TABLE `media_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pwdrecover`
--

DROP TABLE IF EXISTS `pwdrecover`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `pwdrecover` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `token` varchar(255) NOT NULL,
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=83 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `story_type`
--

DROP TABLE IF EXISTS `story_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `story_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type_id` int(11) DEFAULT NULL,
  `type_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `story_type`
--

LOCK TABLES `story_type` WRITE;
/*!40000 ALTER TABLE `story_type` DISABLE KEYS */;
INSERT INTO `story_type` VALUES (1,1,'general'),(2,2,'reviews'),(3,3,'interviews'),(4,4,'news'),(5,99,'other'),(6,5,'spotchecks'),(7,0,'none');
/*!40000 ALTER TABLE `story_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `uploads`
--

DROP TABLE IF EXISTS `uploads`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `uploads` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(255) NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `path` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `level` tinyint(4) NOT NULL DEFAULT '99',
  `username` varchar(20) NOT NULL DEFAULT '',
  `password` varchar(60) DEFAULT NULL,
  `name` tinytext NOT NULL,
  `bornyear` smallint(4) NOT NULL DEFAULT '0',
  `email` tinytext NOT NULL,
  `email2` tinytext,
  `homepage` tinytext,
  `info` longtext,
  `location` tinytext NOT NULL,
  `date` date NOT NULL DEFAULT '0000-00-00',
  `hobbies` text,
  `open` tinyint(1) NOT NULL DEFAULT '1',
  `extrainfo` tinytext,
  `sukupuoli` tinyint(1) NOT NULL DEFAULT '1',
  `icq` varchar(15) DEFAULT NULL,
  `apulainen` tinyint(3) unsigned DEFAULT '0',
  `last_login` datetime DEFAULT NULL,
  `chat` int(4) unsigned DEFAULT NULL,
  `oikeus` tinyint(2) NOT NULL DEFAULT '0',
  `lang_id` tinyint(4) NOT NULL DEFAULT '1',
  `login_count` bigint(20) unsigned DEFAULT NULL,
  `lastloginip` tinytext,
  `lastloginclient` tinytext,
  `address` text NOT NULL,
  `postnumber` tinytext NOT NULL,
  `emails` tinyint(4) DEFAULT '1',
  `puhelin` tinytext,
  `kantaasiakasnro` tinytext,
  `lamina_lisatieto` longtext,
  `blogs` bigint(20) DEFAULT NULL,
  `user_showid` bigint(20) DEFAULT NULL,
  `blog_level` tinyint(4) NOT NULL DEFAULT '5',
  `last_login2` datetime DEFAULT NULL,
  `messenger` varchar(50) DEFAULT NULL,
  `myspace` varchar(50) DEFAULT NULL,
  `rss` varchar(100) DEFAULT NULL,
  `youtube` varchar(50) DEFAULT NULL,
  `ircgalleria` varchar(50) DEFAULT NULL,
  `last_profile_update` timestamp NULL DEFAULT NULL,
  `avatar` varchar(100) DEFAULT NULL,
  `flickr_username` tinytext,
  PRIMARY KEY (`user_id`),
  KEY `password` (`password`),
  KEY `username_2` (`username`),
  KEY `level` (`level`),
  KEY `open` (`open`),
  KEY `last_login2` (`last_login2`),
  FULLTEXT KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=61410 DEFAULT CHARSET=latin1 PACK_KEYS=1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `user_online`
--

CREATE TABLE `user_online` (
  `id` int(11) NOT NULL,
  `user_id` int(128) NOT NULL,
  `username` varchar(256) NOT NULL,
  `created_time` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `user_online`
--
ALTER TABLE `user_online`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `user_online`
--
ALTER TABLE `user_online`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;
