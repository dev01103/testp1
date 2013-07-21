CREATE DATABASE  IF NOT EXISTS `pyshop` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `pyshop`;
-- MySQL dump 10.13  Distrib 5.5.28, for debian-linux-gnu (x86_64)
--
-- Host: 127.0.0.1    Database: pyshop
-- ------------------------------------------------------
-- Server version	5.5.28-1

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
-- Table structure for table `pyshop_templates`
--

DROP TABLE IF EXISTS `pyshop_templates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pyshop_templates` (
  `template_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `type` enum('FE','BE') DEFAULT NULL,
  `default` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`template_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pyshop_templates`
--

LOCK TABLES `pyshop_templates` WRITE;
/*!40000 ALTER TABLE `pyshop_templates` DISABLE KEYS */;
INSERT INTO `pyshop_templates` VALUES (1,'basic','FE',1),(2,'basicBE','BE',0);
/*!40000 ALTER TABLE `pyshop_templates` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pyshop_menu_item_xref`
--

DROP TABLE IF EXISTS `pyshop_menu_item_xref`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pyshop_menu_item_xref` (
  `menu_ref_id` int(11) NOT NULL AUTO_INCREMENT,
  `menu_id` int(11) NOT NULL,
  `item_id` int(11) NOT NULL,
  PRIMARY KEY (`menu_ref_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pyshop_menu_item_xref`
--

LOCK TABLES `pyshop_menu_item_xref` WRITE;
/*!40000 ALTER TABLE `pyshop_menu_item_xref` DISABLE KEYS */;
/*!40000 ALTER TABLE `pyshop_menu_item_xref` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pyshop_user_group`
--

DROP TABLE IF EXISTS `pyshop_user_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pyshop_user_group` (
  `ug_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(45) NOT NULL,
  `group_id` varchar(45) NOT NULL,
  PRIMARY KEY (`ug_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pyshop_user_group`
--

LOCK TABLES `pyshop_user_group` WRITE;
/*!40000 ALTER TABLE `pyshop_user_group` DISABLE KEYS */;
INSERT INTO `pyshop_user_group` VALUES (1,'2','0'),(2,'1','1');
/*!40000 ALTER TABLE `pyshop_user_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pyshop_parts_acl`
--

DROP TABLE IF EXISTS `pyshop_parts_acl`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pyshop_parts_acl` (
  `acl_id` int(11) NOT NULL AUTO_INCREMENT,
  `part_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`acl_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pyshop_parts_acl`
--

LOCK TABLES `pyshop_parts_acl` WRITE;
/*!40000 ALTER TABLE `pyshop_parts_acl` DISABLE KEYS */;
INSERT INTO `pyshop_parts_acl` VALUES (1,2,2,0);
/*!40000 ALTER TABLE `pyshop_parts_acl` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pyshop_menus`
--

DROP TABLE IF EXISTS `pyshop_menus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pyshop_menus` (
  `menu_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`menu_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pyshop_menus`
--

LOCK TABLES `pyshop_menus` WRITE;
/*!40000 ALTER TABLE `pyshop_menus` DISABLE KEYS */;
/*!40000 ALTER TABLE `pyshop_menus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pyshop_parts`
--

DROP TABLE IF EXISTS `pyshop_parts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pyshop_parts` (
  `part_id` int(11) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `position` varchar(45) DEFAULT NULL,
  `dir_name` varchar(45) CHARACTER SET big5 DEFAULT NULL,
  `published` tinyint(4) DEFAULT '0',
  `ordering` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`part_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pyshop_parts`
--

LOCK TABLES `pyshop_parts` WRITE;
/*!40000 ALTER TABLE `pyshop_parts` DISABLE KEYS */;
INSERT INTO `pyshop_parts` VALUES (0,'debug','debug','debug',1,0),(1,'frontpage','centerpart','frontpage',1,0),(2,'partman','partman','partman',1,0),(3,'backend_main','backend','backend',1,0);
/*!40000 ALTER TABLE `pyshop_parts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pyshop_menu_item`
--

DROP TABLE IF EXISTS `pyshop_menu_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pyshop_menu_item` (
  `item_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(45) NOT NULL,
  `view` varchar(45) NOT NULL COMMENT '* for all',
  PRIMARY KEY (`item_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pyshop_menu_item`
--

LOCK TABLES `pyshop_menu_item` WRITE;
/*!40000 ALTER TABLE `pyshop_menu_item` DISABLE KEYS */;
/*!40000 ALTER TABLE `pyshop_menu_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pyshop_users`
--

DROP TABLE IF EXISTS `pyshop_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pyshop_users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `type` enum('guest','user','admin','root') NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `user_name_UNIQUE` (`user_name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pyshop_users`
--

LOCK TABLES `pyshop_users` WRITE;
/*!40000 ALTER TABLE `pyshop_users` DISABLE KEYS */;
INSERT INTO `pyshop_users` VALUES (1,'guest','guest','guest'),(2,'root','root','root');
/*!40000 ALTER TABLE `pyshop_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pythop_groups`
--

DROP TABLE IF EXISTS `pythop_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pythop_groups` (
  `group_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`group_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pythop_groups`
--

LOCK TABLES `pythop_groups` WRITE;
/*!40000 ALTER TABLE `pythop_groups` DISABLE KEYS */;
INSERT INTO `pythop_groups` VALUES (1,'Guests'),(2,'Root');
/*!40000 ALTER TABLE `pythop_groups` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2013-07-21 17:42:30
