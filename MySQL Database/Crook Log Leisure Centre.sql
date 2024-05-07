-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: crook_log_leisure_centre_db
-- ------------------------------------------------------
-- Server version	5.5.5-10.1.30-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `live_session`
--

DROP TABLE IF EXISTS `live_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `live_session` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `User_ID` int(5) DEFAULT NULL,
  `Entry_Time` timestamp NULL DEFAULT NULL,
  `Exit_Time` timestamp NULL DEFAULT NULL,
  `Activity_Type` char(10) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Entry_Time_UNIQUE` (`Entry_Time`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `live_session`
--

LOCK TABLES `live_session` WRITE;
/*!40000 ALTER TABLE `live_session` DISABLE KEYS */;
INSERT INTO `live_session` VALUES (1,2,'2018-04-22 17:49:36','2018-04-22 18:05:44','Swimming'),(2,4,'2018-04-22 18:13:44','2018-04-22 18:14:22','Gym');
/*!40000 ALTER TABLE `live_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `logged_in_users`
--

DROP TABLE IF EXISTS `logged_in_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `logged_in_users` (
  `ID` int(4) NOT NULL AUTO_INCREMENT,
  `User_ID` int(4) DEFAULT NULL,
  `Logged_In_Time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `Logged_Out_Time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=62 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `logged_in_users`
--

LOCK TABLES `logged_in_users` WRITE;
/*!40000 ALTER TABLE `logged_in_users` DISABLE KEYS */;
INSERT INTO `logged_in_users` VALUES (1,5,'2018-04-22 11:27:10','2018-04-22 12:14:24'),(2,1,'2018-04-22 11:47:45','2018-04-22 12:14:24'),(3,1,'2018-04-22 11:48:47','2018-04-22 12:14:24'),(4,6,'2018-04-22 16:25:21','2018-04-22 16:25:30'),(5,3,'2018-04-22 16:28:32','2018-04-22 16:28:57'),(6,5,'2018-04-22 16:36:46','2018-04-22 16:36:47'),(7,2,'2018-04-22 16:37:11','2018-04-22 16:37:13'),(8,3,'2018-04-22 16:38:08','2018-04-22 16:38:10'),(9,2,'2018-04-22 16:38:26','2018-04-22 16:38:27'),(10,3,'2018-04-22 16:38:42','2018-04-22 16:38:43'),(11,3,'2018-04-22 16:41:57','2018-04-22 16:41:59'),(12,2,'2018-04-22 16:42:19','2018-04-22 16:42:22'),(13,2,'2018-04-22 16:42:59','2018-04-22 16:43:02'),(14,2,'2018-04-22 16:44:03','2018-04-22 16:44:04'),(15,3,'2018-04-22 16:44:38','2018-04-22 16:44:40'),(16,2,'2018-04-22 16:45:13','2018-04-22 16:45:16'),(17,3,'2018-04-22 16:45:37','2018-04-22 16:45:41'),(18,2,'2018-04-22 16:46:06','2018-04-22 16:46:09'),(19,3,'2018-04-22 16:46:23','2018-04-22 16:46:26'),(20,6,'2018-04-22 16:55:22','2018-04-22 17:32:46'),(21,6,'2018-04-22 17:13:05','2018-04-22 17:32:46'),(22,1,'2018-04-22 17:24:51','2018-04-22 17:32:46'),(23,6,'2018-04-22 17:33:02','2018-04-22 17:45:54'),(24,5,'2018-04-22 17:39:25','2018-04-22 17:45:54'),(25,2,'2018-04-22 17:45:52','2018-04-22 17:45:54'),(26,2,'2018-04-22 17:46:08','2018-04-22 17:46:12'),(27,2,'2018-04-22 17:46:44','2018-04-22 17:46:47'),(28,6,'2018-04-22 17:47:56','2018-04-22 17:47:57'),(29,2,'2018-04-22 17:49:35','2018-04-22 17:49:36'),(30,2,'2018-04-22 18:05:43','2018-04-22 18:05:44'),(31,4,'2018-04-22 18:07:31','2018-04-22 18:07:37'),(32,4,'2018-04-22 18:08:05','2018-04-22 18:08:08'),(33,4,'2018-04-22 18:11:21','2018-04-22 18:11:25'),(34,4,'2018-04-22 18:11:56','2018-04-22 18:11:57'),(35,4,'2018-04-22 18:13:41','2018-04-22 18:13:44'),(36,4,'2018-04-22 18:14:17','2018-04-22 18:14:22'),(37,1,'2018-04-22 19:07:32','2018-04-24 20:22:56'),(38,5,'2018-04-22 19:47:44','2018-04-24 20:22:56'),(39,7,'2018-04-23 18:40:05','2018-04-24 20:22:56'),(40,7,'2018-04-23 18:40:52','2018-04-24 20:22:56'),(41,7,'2018-04-23 18:42:22','2018-04-24 20:22:56'),(42,7,'2018-04-23 18:42:56','2018-04-24 20:22:56'),(43,7,'2018-04-23 18:43:59','2018-04-24 20:22:56'),(44,7,'2018-04-23 18:44:37','2018-04-24 20:22:56'),(45,6,'2018-04-23 21:06:25','2018-04-24 20:22:56'),(46,6,'2018-04-23 21:08:25','2018-04-24 20:22:56'),(47,7,'2018-04-24 20:28:06','2018-05-05 10:40:40'),(48,7,'2018-04-24 20:28:50','2018-05-05 10:40:40'),(49,7,'2018-04-24 20:29:40','2018-05-05 10:40:40'),(50,7,'2018-04-24 20:34:13','2018-05-05 10:40:40'),(51,7,'2018-04-24 20:54:51','2018-05-05 10:40:40'),(52,7,'2018-04-25 09:03:31','2018-05-05 10:40:40'),(53,7,'2018-04-25 09:05:28','2018-05-05 10:40:40'),(54,7,'2018-04-25 09:20:42','2018-05-05 10:40:40'),(55,7,'2018-04-25 09:21:02','2018-05-05 10:40:40'),(56,7,'2018-04-25 09:22:05','2018-05-05 10:40:40'),(57,1,'2018-05-05 10:39:57','2018-05-05 10:40:40'),(58,5,'2018-05-05 10:41:25','2018-05-05 10:46:47'),(59,5,'2018-05-05 10:48:11','2018-05-05 10:48:13'),(60,1,'2018-05-05 10:52:02','2018-05-05 10:54:35'),(61,7,'2018-05-05 10:54:49','2018-05-05 10:55:36');
/*!40000 ALTER TABLE `logged_in_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role_types`
--

DROP TABLE IF EXISTS `role_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `role_types` (
  `Role_Type_ID` int(11) NOT NULL,
  `Role` varchar(45) NOT NULL,
  PRIMARY KEY (`Role_Type_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role_types`
--

LOCK TABLES `role_types` WRITE;
/*!40000 ALTER TABLE `role_types` DISABLE KEYS */;
INSERT INTO `role_types` VALUES (1,'Member'),(2,'Staff'),(3,'Root');
/*!40000 ALTER TABLE `role_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_roles`
--

DROP TABLE IF EXISTS `user_roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_roles` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `User_ID` int(11) DEFAULT NULL,
  `Role_Type_ID` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_roles`
--

LOCK TABLES `user_roles` WRITE;
/*!40000 ALTER TABLE `user_roles` DISABLE KEYS */;
INSERT INTO `user_roles` VALUES (1,1,3),(2,2,1),(3,3,1),(4,4,1),(5,5,1),(6,6,2),(7,7,2);
/*!40000 ALTER TABLE `user_roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `User_ID` int(4) NOT NULL AUTO_INCREMENT,
  `Title` char(5) NOT NULL,
  `First_Name` char(10) NOT NULL,
  `Last_Name` char(10) NOT NULL,
  `DOB` date NOT NULL,
  `Email` varchar(30) NOT NULL,
  `Gender` char(7) NOT NULL,
  `Address` varchar(30) NOT NULL,
  `Post_Code` varchar(10) NOT NULL,
  `City` char(10) NOT NULL,
  `Membership_Type` char(10) NOT NULL,
  `Password` varchar(20) NOT NULL,
  `Status` varchar(45) NOT NULL DEFAULT 'ACTIVE',
  PRIMARY KEY (`User_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Mr','Tony','Lewis','1954-09-04','admin','Male','123 Street','ABC 123','Kent','Gym','admin','ACTIVE'),(2,'Mr','Connor','Pike','1998-11-28','connor.pike@gmail.co.uk','Male','19 Baker Avenue','ZYX CPA','Dartford','Gym','connor','ACTIVE'),(3,'Mr','x','x','0000-00-00','x','x','x','x','x','x','x','INACTIVE'),(4,'Mr','Jack','Robert','1972-06-15','jack.robert@gmail.com','Male','45 Lucton Street','DA4 765','Kent','Gym','jackattack','ACTIVE'),(5,'Mr','Alex','Earl','1983-06-14','alex.earl@hotmail.com','Male','55 Porter Street','DA3 567','Kent','Gym','password','ACTIVE'),(6,'Miss','Lucy','Smith','1986-01-22','staff.smith@crooklog.com','Female','46 Rydal Street','ER5 6YU','Kent','Swim23','password','ACTIVE'),(7,'Miss','Jessica','Lewis','1974-08-12','staff.lewis@crooklog.com','Female','345 Canal Street','DA5 754','Kent','Gym','password','ACTIVE');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-05-10 18:55:13
