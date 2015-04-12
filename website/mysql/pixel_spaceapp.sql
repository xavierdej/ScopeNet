-- phpMyAdmin SQL Dump
-- version 3.3.8.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 12, 2015 at 09:49 AM
-- Server version: 5.5.8
-- PHP Version: 5.3.10

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `pixel_spaceapp`
--

-- --------------------------------------------------------

--
-- Table structure for table `bodies`
--

DROP TABLE IF EXISTS `bodies`;
CREATE TABLE IF NOT EXISTS `bodies` (
  `Name` varchar(15) NOT NULL DEFAULT '',
  PRIMARY KEY (`Name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `bodies`
--

INSERT INTO `bodies` (`Name`) VALUES
('Achernar'),
('Adara'),
('Agena'),
('Albereo'),
('Alcaid'),
('Alcor'),
('Alcyone'),
('Aldebaran'),
('Alderamin'),
('Alfirk'),
('Algenib'),
('Algieba'),
('Algol'),
('Alhena'),
('Alioth'),
('Almach'),
('Alnair'),
('Alnilam'),
('Alnitak'),
('Alphard'),
('Alphecca'),
('Alshain'),
('Altair'),
('Antares'),
('Arcturus'),
('Ariel'),
('Arkab Posterior'),
('Arkab Prior'),
('Arneb'),
('Atlas'),
('Bellatrix'),
('Betelgeuse'),
('Callisto'),
('Canopus'),
('Capella'),
('Caph'),
('Castor'),
('Cebalrai'),
('Deimos'),
('Deneb'),
('Denebola'),
('Dione'),
('Dubhe'),
('Electra'),
('Elnath'),
('Enceladus'),
('Enif'),
('Etamin'),
('Europa'),
('Fomalhaut'),
('Ganymede'),
('Gienah Corvi'),
('Hamal'),
('Hyperion'),
('Iapetus'),
('Io'),
('Izar'),
('Jupiter'),
('Kaus Australis'),
('Kochab'),
('Maia'),
('Markab'),
('Mars'),
('Megrez'),
('Menkalinan'),
('Menkar'),
('Merak'),
('Mercury'),
('Merope'),
('Mimas'),
('Mimosa'),
('Minkar'),
('Mintaka'),
('Mirach'),
('Miranda'),
('Mirzam'),
('Mizar'),
('Moon'),
('Naos'),
('Neptune'),
('Nihal'),
('Nunki'),
('Oberon'),
('Peacock'),
('Phecda'),
('Phobos'),
('Pluto'),
('Polaris'),
('Pollux'),
('Procyon'),
('Rasalgethi'),
('Rasalhague'),
('Regulus'),
('Rhea'),
('Rigel'),
('Rukbat'),
('Sadalmelik'),
('Sadr'),
('Saiph'),
('Saturn'),
('Scheat'),
('Schedar'),
('Shaula'),
('Sheliak'),
('Sirius'),
('Sirrah'),
('Spica'),
('Sulafat'),
('Sun'),
('Tarazed'),
('Taygeta'),
('Tethys'),
('Thuban'),
('Titan'),
('Titania'),
('Umbriel'),
('Unukalhai'),
('Uranus'),
('Vega'),
('Venus'),
('Vindemiatrix'),
('Wezen'),
('Zaurak');

-- --------------------------------------------------------

--
-- Table structure for table `requests`
--

DROP TABLE IF EXISTS `requests`;
CREATE TABLE IF NOT EXISTS `requests` (
  `Name` varchar(15) NOT NULL DEFAULT '',
  PRIMARY KEY (`Name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `requests`
--


-- --------------------------------------------------------

--
-- Table structure for table `uploads`
--

DROP TABLE IF EXISTS `uploads`;
CREATE TABLE IF NOT EXISTS `uploads` (
  `UploadTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Name` varchar(15) NOT NULL DEFAULT '',
  `FileName` varchar(64) NOT NULL,
  PRIMARY KEY (`UploadTime`),
  KEY `Name` (`Name`,`UploadTime`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `uploads`
--

