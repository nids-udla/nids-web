-- MariaDB dump 10.19  Distrib 10.9.3-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: nids
-- ------------------------------------------------------
-- Server version	10.9.3-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add area',7,'add_area'),
(26,'Can change area',7,'change_area'),
(27,'Can delete area',7,'delete_area'),
(28,'Can view area',7,'view_area'),
(29,'Can add diploma',8,'add_diploma'),
(30,'Can change diploma',8,'change_diploma'),
(31,'Can delete diploma',8,'delete_diploma'),
(32,'Can view diploma',8,'view_diploma'),
(33,'Can add estadisticas',9,'add_estadisticas'),
(34,'Can change estadisticas',9,'change_estadisticas'),
(35,'Can delete estadisticas',9,'delete_estadisticas'),
(36,'Can view estadisticas',9,'view_estadisticas'),
(37,'Can add noticia',10,'add_noticia'),
(38,'Can change noticia',10,'change_noticia'),
(39,'Can delete noticia',10,'delete_noticia'),
(40,'Can view noticia',10,'view_noticia'),
(41,'Can add proyecto',11,'add_proyecto'),
(42,'Can change proyecto',11,'change_proyecto'),
(43,'Can delete proyecto',11,'delete_proyecto'),
(44,'Can view proyecto',11,'view_proyecto'),
(45,'Can add rol',12,'add_rol'),
(46,'Can change rol',12,'change_rol'),
(47,'Can delete rol',12,'delete_rol'),
(48,'Can view rol',12,'view_rol'),
(49,'Can add tarea',13,'add_tarea'),
(50,'Can change tarea',13,'change_tarea'),
(51,'Can delete tarea',13,'delete_tarea'),
(52,'Can view tarea',13,'view_tarea'),
(53,'Can add usuario',14,'add_usuario'),
(54,'Can change usuario',14,'change_usuario'),
(55,'Can delete usuario',14,'delete_usuario'),
(56,'Can view usuario',14,'view_usuario'),
(57,'Can add investigacion',15,'add_investigacion'),
(58,'Can change investigacion',15,'change_investigacion'),
(59,'Can delete investigacion',15,'delete_investigacion'),
(60,'Can view investigacion',15,'view_investigacion'),
(61,'Can add graduado',16,'add_graduado'),
(62,'Can change graduado',16,'change_graduado'),
(63,'Can delete graduado',16,'delete_graduado'),
(64,'Can view graduado',16,'view_graduado'),
(65,'Can add funcion',17,'add_funcion'),
(66,'Can change funcion',17,'change_funcion'),
(67,'Can delete funcion',17,'delete_funcion'),
(68,'Can view funcion',17,'view_funcion'),
(69,'Can add autor',18,'add_autor'),
(70,'Can change autor',18,'change_autor'),
(71,'Can delete autor',18,'delete_autor'),
(72,'Can view autor',18,'view_autor'),
(73,'Can add asignado',19,'add_asignado'),
(74,'Can change asignado',19,'change_asignado'),
(75,'Can delete asignado',19,'delete_asignado'),
(76,'Can view asignado',19,'view_asignado');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(7,'index','area'),
(19,'index','asignado'),
(18,'index','autor'),
(8,'index','diploma'),
(9,'index','estadisticas'),
(17,'index','funcion'),
(16,'index','graduado'),
(15,'index','investigacion'),
(10,'index','noticia'),
(11,'index','proyecto'),
(12,'index','rol'),
(13,'index','tarea'),
(14,'index','usuario'),
(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES
(1,'contenttypes','0001_initial','2023-06-19 15:18:45.234118'),
(2,'auth','0001_initial','2023-06-19 15:18:46.050226'),
(3,'admin','0001_initial','2023-06-19 15:18:46.211395'),
(4,'admin','0002_logentry_remove_auto_add','2023-06-19 15:18:46.226803'),
(5,'admin','0003_logentry_add_action_flag_choices','2023-06-19 15:18:46.235661'),
(6,'contenttypes','0002_remove_content_type_name','2023-06-19 15:18:46.351636'),
(7,'auth','0002_alter_permission_name_max_length','2023-06-19 15:18:46.428384'),
(8,'auth','0003_alter_user_email_max_length','2023-06-19 15:18:46.479494'),
(9,'auth','0004_alter_user_username_opts','2023-06-19 15:18:46.488138'),
(10,'auth','0005_alter_user_last_login_null','2023-06-19 15:18:46.555312'),
(11,'auth','0006_require_contenttypes_0002','2023-06-19 15:18:46.560990'),
(12,'auth','0007_alter_validators_add_error_messages','2023-06-19 15:18:46.570483'),
(13,'auth','0008_alter_user_username_max_length','2023-06-19 15:18:46.621681'),
(14,'auth','0009_alter_user_last_name_max_length','2023-06-19 15:18:46.670610'),
(15,'auth','0010_alter_group_name_max_length','2023-06-19 15:18:46.716953'),
(16,'auth','0011_update_proxy_permissions','2023-06-19 15:18:46.727514'),
(17,'auth','0012_alter_user_first_name_max_length','2023-06-19 15:18:46.774108'),
(18,'index','0001_initial','2023-06-19 15:18:48.221402'),
(19,'sessions','0001_initial','2023-06-19 15:18:48.303325'),
(20,'index','0002_remove_usuario_extra_rrss_tarea_completado_and_more','2023-07-07 20:19:58.391552');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES
('kenj136clt6214zkm4eq77jxkstdact7','.eJxtzrsOwjAMBdBfiTKjdu_Ea2RkR2ljWkNiV4lDQYh_x60YOrBeH9v3bTFfHi6gdwLeNpIKbGzJkMhFsI09wyszmSOD3ViIDoOGNx6o8gxbeLo4Bqg6jjp2LRfR8YkTRINjLtF4DpxMRjF6TypViecTOx-R5p0EbnnTDaS0f2mWuUMX8k7zQWTMTV1P01QFpDt4pPlbPVfwS6mf3q90jzKU9r87rNyq_goKBLgysUJiAvv5AvM7ZRw:1qIdwQ:HMbwHrKsxfDWKGUJ1q_kht8L7GhXRlYBhqhywu-phqM','2023-07-23 23:35:46.858682');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `index_area`
--

DROP TABLE IF EXISTS `index_area`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `index_area` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `index_area`
--

LOCK TABLES `index_area` WRITE;
/*!40000 ALTER TABLE `index_area` DISABLE KEYS */;
INSERT INTO `index_area` VALUES
(1,'Technology'),
(2,'Marketing');
/*!40000 ALTER TABLE `index_area` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `index_asignado`
--

DROP TABLE IF EXISTS `index_asignado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `index_asignado` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `id_proyecto_id` bigint(20) NOT NULL,
  `id_tarea_id` bigint(20) NOT NULL,
  `id_usuario_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `index_asignado_id_proyecto_id_8e121095_fk_index_proyecto_id` (`id_proyecto_id`),
  KEY `index_asignado_id_tarea_id_24de23bf_fk_index_tarea_id` (`id_tarea_id`),
  KEY `index_asignado_id_usuario_id_b790ee50_fk_index_usuario_id` (`id_usuario_id`),
  CONSTRAINT `index_asignado_id_proyecto_id_8e121095_fk_index_proyecto_id` FOREIGN KEY (`id_proyecto_id`) REFERENCES `index_proyecto` (`id`),
  CONSTRAINT `index_asignado_id_tarea_id_24de23bf_fk_index_tarea_id` FOREIGN KEY (`id_tarea_id`) REFERENCES `index_tarea` (`id`),
  CONSTRAINT `index_asignado_id_usuario_id_b790ee50_fk_index_usuario_id` FOREIGN KEY (`id_usuario_id`) REFERENCES `index_usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `index_asignado`
--

LOCK TABLES `index_asignado` WRITE;
/*!40000 ALTER TABLE `index_asignado` DISABLE KEYS */;
INSERT INTO `index_asignado` VALUES
(1,1,1,1),
(2,2,2,2),
(3,1,2,2),
(4,2,3,1),
(5,2,4,2),
(6,2,4,2);
/*!40000 ALTER TABLE `index_asignado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `index_autor`
--

DROP TABLE IF EXISTS `index_autor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `index_autor` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `id_noticia_id` bigint(20) NOT NULL,
  `id_usuario_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `index_autor_id_noticia_id_17afee7e_fk_index_noticia_id` (`id_noticia_id`),
  KEY `index_autor_id_usuario_id_0487a9b2_fk_index_usuario_id` (`id_usuario_id`),
  CONSTRAINT `index_autor_id_noticia_id_17afee7e_fk_index_noticia_id` FOREIGN KEY (`id_noticia_id`) REFERENCES `index_noticia` (`id`),
  CONSTRAINT `index_autor_id_usuario_id_0487a9b2_fk_index_usuario_id` FOREIGN KEY (`id_usuario_id`) REFERENCES `index_usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `index_autor`
--

LOCK TABLES `index_autor` WRITE;
/*!40000 ALTER TABLE `index_autor` DISABLE KEYS */;
INSERT INTO `index_autor` VALUES
(1,1,1),
(2,2,2);
/*!40000 ALTER TABLE `index_autor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `index_diploma`
--

DROP TABLE IF EXISTS `index_diploma`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `index_diploma` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `tipo` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `index_diploma`
--

LOCK TABLES `index_diploma` WRITE;
/*!40000 ALTER TABLE `index_diploma` DISABLE KEYS */;
INSERT INTO `index_diploma` VALUES
(1,'Bachelor','Science'),
(2,'Master','Arts');
/*!40000 ALTER TABLE `index_diploma` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `index_estadisticas`
--

DROP TABLE IF EXISTS `index_estadisticas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `index_estadisticas` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(100) NOT NULL,
  `valor` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `index_estadisticas`
--

LOCK TABLES `index_estadisticas` WRITE;
/*!40000 ALTER TABLE `index_estadisticas` DISABLE KEYS */;
INSERT INTO `index_estadisticas` VALUES
(1,'Visitors',1000),
(2,'Sales',500);
/*!40000 ALTER TABLE `index_estadisticas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `index_funcion`
--

DROP TABLE IF EXISTS `index_funcion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `index_funcion` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `id_rol_id` bigint(20) NOT NULL,
  `id_usuario_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `index_funcion_id_rol_id_c2ca8b24_fk_index_rol_id` (`id_rol_id`),
  KEY `index_funcion_id_usuario_id_0f36f43d_fk_index_usuario_id` (`id_usuario_id`),
  CONSTRAINT `index_funcion_id_rol_id_c2ca8b24_fk_index_rol_id` FOREIGN KEY (`id_rol_id`) REFERENCES `index_rol` (`id`),
  CONSTRAINT `index_funcion_id_usuario_id_0f36f43d_fk_index_usuario_id` FOREIGN KEY (`id_usuario_id`) REFERENCES `index_usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `index_funcion`
--

LOCK TABLES `index_funcion` WRITE;
/*!40000 ALTER TABLE `index_funcion` DISABLE KEYS */;
INSERT INTO `index_funcion` VALUES
(1,1,1),
(2,2,2);
/*!40000 ALTER TABLE `index_funcion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `index_graduado`
--

DROP TABLE IF EXISTS `index_graduado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `index_graduado` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `id_diploma_id` bigint(20) NOT NULL,
  `id_usuario_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `index_graduado_id_diploma_id_277511f8_fk_index_diploma_id` (`id_diploma_id`),
  KEY `index_graduado_id_usuario_id_2b8c735f_fk_index_usuario_id` (`id_usuario_id`),
  CONSTRAINT `index_graduado_id_diploma_id_277511f8_fk_index_diploma_id` FOREIGN KEY (`id_diploma_id`) REFERENCES `index_diploma` (`id`),
  CONSTRAINT `index_graduado_id_usuario_id_2b8c735f_fk_index_usuario_id` FOREIGN KEY (`id_usuario_id`) REFERENCES `index_usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `index_graduado`
--

LOCK TABLES `index_graduado` WRITE;
/*!40000 ALTER TABLE `index_graduado` DISABLE KEYS */;
INSERT INTO `index_graduado` VALUES
(1,1,1),
(2,2,2);
/*!40000 ALTER TABLE `index_graduado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `index_investigacion`
--

DROP TABLE IF EXISTS `index_investigacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `index_investigacion` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `id_area_id` bigint(20) NOT NULL,
  `id_usuario_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `index_investigacion_id_area_id_072b4efd_fk_index_area_id` (`id_area_id`),
  KEY `index_investigacion_id_usuario_id_59a5a1a6_fk_index_usuario_id` (`id_usuario_id`),
  CONSTRAINT `index_investigacion_id_area_id_072b4efd_fk_index_area_id` FOREIGN KEY (`id_area_id`) REFERENCES `index_area` (`id`),
  CONSTRAINT `index_investigacion_id_usuario_id_59a5a1a6_fk_index_usuario_id` FOREIGN KEY (`id_usuario_id`) REFERENCES `index_usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `index_investigacion`
--

LOCK TABLES `index_investigacion` WRITE;
/*!40000 ALTER TABLE `index_investigacion` DISABLE KEYS */;
INSERT INTO `index_investigacion` VALUES
(1,1,1),
(2,2,2);
/*!40000 ALTER TABLE `index_investigacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `index_noticia`
--

DROP TABLE IF EXISTS `index_noticia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `index_noticia` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(100) NOT NULL,
  `palabra_clave` varchar(100) NOT NULL,
  `descripcion` varchar(300) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `index_noticia`
--

LOCK TABLES `index_noticia` WRITE;
/*!40000 ALTER TABLE `index_noticia` DISABLE KEYS */;
INSERT INTO `index_noticia` VALUES
(1,'News 1','Lorem','Lorem ipsum dolor sit amet.'),
(2,'News 2','Ipsum','Lorem ipsum dolor sit amet.');
/*!40000 ALTER TABLE `index_noticia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `index_proyecto`
--

DROP TABLE IF EXISTS `index_proyecto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `index_proyecto` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(100) NOT NULL,
  `descripcion` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `index_proyecto`
--

LOCK TABLES `index_proyecto` WRITE;
/*!40000 ALTER TABLE `index_proyecto` DISABLE KEYS */;
INSERT INTO `index_proyecto` VALUES
(1,'Project 1','Lorem ipsum dolor sit amet.'),
(2,'Project 2','Lorem ipsum dolor sit amet.'),
(3,'Proyecto A','Descripción del Proyecto A'),
(4,'Proyecto B','Descripción del Proyecto B');
/*!40000 ALTER TABLE `index_proyecto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `index_rol`
--

DROP TABLE IF EXISTS `index_rol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `index_rol` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `index_rol`
--

LOCK TABLES `index_rol` WRITE;
/*!40000 ALTER TABLE `index_rol` DISABLE KEYS */;
INSERT INTO `index_rol` VALUES
(1,'Admin'),
(2,'User');
/*!40000 ALTER TABLE `index_rol` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `index_tarea`
--

DROP TABLE IF EXISTS `index_tarea`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `index_tarea` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(100) NOT NULL,
  `descripcion` varchar(100) NOT NULL,
  `completado` tinyint(1) NOT NULL,
  `fecha_inicio` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `index_tarea`
--

LOCK TABLES `index_tarea` WRITE;
/*!40000 ALTER TABLE `index_tarea` DISABLE KEYS */;
INSERT INTO `index_tarea` VALUES
(1,'Task 1','Lorem ipsum dolor sit amet.',1,'0000-00-00'),
(2,'Task 2','Lorem ipsum dolor sit amet.',1,'0000-00-00'),
(3,'Tarea 1','Descripción de la Tarea 1',1,'2023-07-03'),
(4,'Tarea 2','Descripción de la Tarea 2',0,'2023-07-04'),
(5,'Tarea 3','Descripción de la Tarea 3',0,'2023-07-05');
/*!40000 ALTER TABLE `index_tarea` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `index_usuario`
--

DROP TABLE IF EXISTS `index_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `index_usuario` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nombre_completo` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `password` varchar(300) NOT NULL,
  `descripcion` varchar(100) NOT NULL,
  `linkedin` varchar(200) NOT NULL,
  `github` varchar(200) NOT NULL,
  `telefono` varchar(300) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `index_usuario`
--

LOCK TABLES `index_usuario` WRITE;
/*!40000 ALTER TABLE `index_usuario` DISABLE KEYS */;
INSERT INTO `index_usuario` VALUES
(1,'Teyson Doe','john.doe@example.com','89e01536ac207279409d4de1e5253e01f4a1769e696db0d6062ca9b8f56767c8','Lorem ipsum dolor sit amet.','https://www.linkedin.com/johndoe','https://github.com/johndoe','none'),
(2,'Jane Smith','jane.smith@example.com','16472b57e17a8a0eafd5d6811cf5b182f6b4e2812e322d5fc33b0d1f19fb5832','Lorem ipsum dolor sit amet.','https://www.linkedin.com/janesmith','https://github.com/janesmith','none');
/*!40000 ALTER TABLE `index_usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-09 20:49:54
