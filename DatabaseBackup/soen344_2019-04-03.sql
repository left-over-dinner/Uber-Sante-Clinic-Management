# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: room3.mysql.database.azure.com (MySQL 5.6.39.0)
# Database: soen344
# Generation Time: 2019-04-04 02:31:43 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table alembic_version
# ------------------------------------------------------------

DROP TABLE IF EXISTS `alembic_version`;

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;

INSERT INTO `alembic_version` (`version_num`)
VALUES
	('aafceb3e7794');

/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table appointment
# ------------------------------------------------------------

DROP TABLE IF EXISTS `appointment`;

CREATE TABLE `appointment` (
  `appointment_id` int(11) NOT NULL AUTO_INCREMENT,
  `patient_card_number` varchar(250) NOT NULL,
  `doctor_permit_number` varchar(250) NOT NULL,
  `date` date NOT NULL,
  `slots` json NOT NULL,
  `appointment_type` varchar(250) NOT NULL,
  PRIMARY KEY (`appointment_id`),
  KEY `doctor_permit_number` (`doctor_permit_number`),
  KEY `patient_card_number` (`patient_card_number`),
  CONSTRAINT `appointment_ibfk_1` FOREIGN KEY (`doctor_permit_number`) REFERENCES `doctor` (`permit_number`) ON DELETE CASCADE,
  CONSTRAINT `appointment_ibfk_2` FOREIGN KEY (`patient_card_number`) REFERENCES `patient` (`card_number`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `appointment` WRITE;
/*!40000 ALTER TABLE `appointment` DISABLE KEYS */;

INSERT INTO `appointment` (`appointment_id`, `patient_card_number`, `doctor_permit_number`, `date`, `slots`, `appointment_type`)
VALUES
	(63,'45678','12345','2019-09-07',X'5B325D','Walk-In'),
	(85,'KEPE28428429','12345','2019-03-21',X'5B315D','Walk-In'),
	(88,'MArc24149149','1222345688','2019-03-22',X'5B385D','Walk-In'),
	(89,'KEPE28428429','12345','2019-09-07',X'5B345D','Walk-In');

/*!40000 ALTER TABLE `appointment` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table availability
# ------------------------------------------------------------

DROP TABLE IF EXISTS `availability`;

CREATE TABLE `availability` (
  `availability_id` int(11) NOT NULL AUTO_INCREMENT,
  `doctor_permit_number` varchar(250) NOT NULL,
  `date` date NOT NULL,
  `slots` json NOT NULL,
  PRIMARY KEY (`availability_id`),
  KEY `doctor_permit_number` (`doctor_permit_number`),
  CONSTRAINT `availability_ibfk_1` FOREIGN KEY (`doctor_permit_number`) REFERENCES `doctor` (`permit_number`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `availability` WRITE;
/*!40000 ALTER TABLE `availability` DISABLE KEYS */;

INSERT INTO `availability` (`availability_id`, `doctor_permit_number`, `date`, `slots`)
VALUES
	(35,'1222345688','2019-09-10',X'5B322C20342C20362C2031302C2031352C2031362C2031375D'),
	(42,'1222345688','2019-03-22',X'5B392C2031302C2031312C2031322C2031332C2031342C2033312C2033322C2033335D'),
	(30000,'12345','2019-09-07',X'5B312C20332C20355D'),
	(100031,'12345','2019-03-21',X'5B322C20332C20342C20355D'),
	(100033,'1222345688','2019-03-30',X'5B342C20352C20362C20372C20382C2031312C2031322C2031332C2031342C2031352C2031362C2031372C2031382C2031392C2032302C2032322C2032332C2032342C2032352C2032362C2032382C2032392C2033302C2033312C2033322C2033335D'),
	(100059,'1222345688','2019-04-01',X'5B312C20322C20332C20342C20352C20362C20372C20382C20392C2031302C2031312C2031322C2031332C2031342C2031352C2031362C2031372C2031382C2031392C2032302C2032312C2032322C2032332C2032342C2032352C2032362C2032372C2032382C2032392C2033302C2033312C2033322C2033335D'),
	(100070,'123123123','2019-03-27',X'5B312C20322C20332C20342C20352C20362C20372C20382C20392C2031302C2031312C2031322C2031332C2031342C2031352C2031362C2031372C2031382C2031392C2032302C2032312C2032322C2032332C2032342C2032352C2032362C2032372C2032382C2032392C2033302C2033315D'),
	(100071,'123123123','2019-03-29',X'5B312C20322C20332C20342C20352C20362C20375D'),
	(100072,'12345','2018-08-12',X'5B312C20342C20355D'),
	(100073,'12345','2018-08-12',X'5B312C20342C20355D'),
	(100074,'12345','2018-08-12',X'5B312C20342C20355D'),
	(100075,'12345','2018-08-12',X'5B312C20342C20355D');

/*!40000 ALTER TABLE `availability` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table clinics
# ------------------------------------------------------------

DROP TABLE IF EXISTS `clinics`;

CREATE TABLE `clinics` (
  `clinic_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(250) NOT NULL,
  `no_doctors` int(11) NOT NULL,
  `no_nurses` int(11) NOT NULL,
  `no_rooms` int(11) NOT NULL,
  `schedule` varchar(250) NOT NULL,
  PRIMARY KEY (`clinic_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `clinics` WRITE;
/*!40000 ALTER TABLE `clinics` DISABLE KEYS */;

INSERT INTO `clinics` (`clinic_id`, `name`, `no_doctors`, `no_nurses`, `no_rooms`, `schedule`)
VALUES
	(1,'Soen',9,9,7,'Mon-Frid 24h');

/*!40000 ALTER TABLE `clinics` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table doctor
# ------------------------------------------------------------

DROP TABLE IF EXISTS `doctor`;

CREATE TABLE `doctor` (
  `permit_number` varchar(250) NOT NULL,
  `last_name` varchar(250) NOT NULL,
  `first_name` varchar(250) NOT NULL,
  `specialty` varchar(250) NOT NULL,
  `location` varchar(250) NOT NULL,
  `email` varchar(250) NOT NULL,
  `password` varchar(250) NOT NULL,
  `clinic_id` int(11) NOT NULL,
  PRIMARY KEY (`permit_number`),
  KEY `clinic_id` (`clinic_id`),
  CONSTRAINT `doctor_ibfk_1` FOREIGN KEY (`clinic_id`) REFERENCES `clinics` (`clinic_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `doctor` WRITE;
/*!40000 ALTER TABLE `doctor` DISABLE KEYS */;

INSERT INTO `doctor` (`permit_number`, `last_name`, `first_name`, `specialty`, `location`, `email`, `password`, `clinic_id`)
VALUES
	('1222345688','jakarta','yesName','YALLHA','city','me@you.com','pass',1),
	('123123123','hello','hello','Nothing','HERE','abc@cde.xyz','hello',1),
	('12345','Paul','Bob','speciality','Montreal','email@you','password',1),
	('12345688','jakarta','yesName','','city','me@yous.com','pass',1),
	('123908','Singh','Manpreet','special','Montreal','m@com','pass',1),
	('436545','Nickel','Peck','HELLO','987654','me@you','you@pass',1),
	('438946','Line','Ghanem','HELLO','65767','me@you','you@pass',1),
	('516765','Nickel','Peck','legs','Montreal','me@you','you@pass',1),
	('56765','Nickel','Peck','legs','Montreal','me@you','you@pass',1);

/*!40000 ALTER TABLE `doctor` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table nurse
# ------------------------------------------------------------

DROP TABLE IF EXISTS `nurse`;

CREATE TABLE `nurse` (
  `access_id` varchar(250) NOT NULL,
  `password` varchar(250) NOT NULL,
  `last_name` varchar(250) NOT NULL,
  `first_name` varchar(250) NOT NULL,
  `email` varchar(250) NOT NULL,
  `clinic_id` int(11) NOT NULL,
  PRIMARY KEY (`access_id`),
  KEY `clinic_id` (`clinic_id`),
  CONSTRAINT `nurse_ibfk_1` FOREIGN KEY (`clinic_id`) REFERENCES `clinics` (`clinic_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `nurse` WRITE;
/*!40000 ALTER TABLE `nurse` DISABLE KEYS */;

INSERT INTO `nurse` (`access_id`, `password`, `last_name`, `first_name`, `email`, `clinic_id`)
VALUES
	('1234','sample31','YOLO1','YOU31','sample31',1),
	('14141840','pass','Cecaj','Eglen','eglen@co.ca',1),
	('3434','sample3','YOLO','YOU3','sample3',1),
	('343430','sample3','YOLO','YOU3','sample3',1),
	('41414','pass','salib','Mike','mike@david.com',1),
	('67TYU5','456789','YOU','ELMO','you@you',1),
	('sample3','sample31','YOLO1','YOU31','sample31',1);

/*!40000 ALTER TABLE `nurse` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table patient
# ------------------------------------------------------------

DROP TABLE IF EXISTS `patient`;

CREATE TABLE `patient` (
  `card_number` varchar(250) NOT NULL,
  `birth_day` date NOT NULL,
  `gender` varchar(250) NOT NULL,
  `phone_number` varchar(250) NOT NULL,
  `address` varchar(250) NOT NULL,
  `email` varchar(250) NOT NULL,
  `last_name` varchar(250) NOT NULL,
  `first_name` varchar(250) NOT NULL,
  `password` varchar(250) NOT NULL,
  PRIMARY KEY (`card_number`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `patient` WRITE;
/*!40000 ALTER TABLE `patient` DISABLE KEYS */;

INSERT INTO `patient` (`card_number`, `birth_day`, `gender`, `phone_number`, `address`, `email`, `last_name`, `first_name`, `password`)
VALUES
	('123123123','2019-09-19','Male','41231231231','here','a@b.com','Guy','Some','hello'),
	('12E2T395','1998-09-08','Male','514-5141-1717','room 3','me@me1.ca','Kong','NAMEFIRST','pass'),
	('12ET395','1998-09-08','Male','514-5141-1717','room 3','me@me1.ca','Kong','NAMEFIRST','pass'),
	('45678','2002-02-02','Male','5147895678','1234 Some Str','peter@rigby.com','Rigby','Peter','1234'),
	('5678TY','1991-09-08','Male','514-5141-1717','room 3','me@meh.ca','','NAMEFIRST','cass'),
	('5678TYYU','1991-09-08','Male','514-5141-1717','room 3','me@me.ca','','NAMEFIRST','pass'),
	('72868372872','0001-03-02','Male','5141222333','5 street','marc@noon.com','Noon','Marc','pass'),
	('98989','1997-09-16','sample2','sample2','sample2','sample2','OKOKOK','sample2','sample2'),
	('989898','1997-09-16','sample2','sample2','sample2','sample2','Jess','sample2','sample2'),
	('KEPE28428429','1994-03-10','Male','5149230424','1200 Rue Guy','erdem@co.ca','Kepenek','Erdem','pass'),
	('krdfvtghujikol','2019-12-20','both','1231231234','here','a@b.ca','hi','hi','hello'),
	('MArc24149149','1952-02-03','MAle','514924202','1200 Rue Guy','marc@henry.com','Henry','MArc','pass');

/*!40000 ALTER TABLE `patient` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
