-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- 主机: localhost
-- 生成日期: 2017-03-31 21:18:11
-- 服务器版本: 5.5.49-0ubuntu0.14.04.1-log
-- PHP 版本: 5.5.9-1ubuntu4.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 数据库: `savannah_gnu`
--

-- --------------------------------------------------------

--
-- 表的结构 `GNA_projects`
--

CREATE TABLE IF NOT EXISTS `GNA_projects` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pj_name` text NOT NULL,
  `pj_desc` text NOT NULL,
  `pj_status` text NOT NULL,
  `pj_date` text NOT NULL,
  `pj_license` text NOT NULL,
  `md5` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=63 ;

--
-- 转存表中的数据 `GNA_projects`
--

INSERT INTO `GNA_projects` (`id`, `pj_name`, `pj_desc`, `pj_status`, `pj_date`, `pj_license`, `md5`) VALUES
(53, 'aml', '-- This project has been moved to  --\r\nThis library is mostly a C++ portable layer over SDL and some other multimedia libraries (to come). The aim is to have a common interface to the different libraries out there somebody might want to use to make portable games. People should be able to use it simply and have at least a "default consistent behaviour". This default behaviour must balance efficiency, usability and nice end-user experience.\r\nThe main features are :\r\n- A simple interface to graphics libraries ( using an abstract model of a graphic engine for games )\r\n- A simple interface to input libraries\r\n- A simple interface to audio libraries ( using an abstract model of           \r\nan audio engine for games )\r\n- A simple interface to video libraries\r\n- A simple interface to operating system related functions.\r\n    (timer, thread, etc.).\r\n- A common set of useful "management" components.\r\nThe main component is right now SDLut, a C++ wrapper over SDL 1.2\r\nDocumentation available at : \nRegistration Date:  Sun 25 Sep 2005 01:50:27 AM UTC\nLicense: Development Status:  3 - Alpha\n', 'Development Status:  3 - Alpha\n', 'Registration Date:  Sun 25 Sep 2005 01:50:27 AM UTC\n', 'Modified BSD License', '8dee0dc8789a1bd60d0f6701b27b30b3'),
(55, 'agt', 'This project has not yet submitted a short description. You can  now.Registration Date:  Sun 14 May 2006 03:34:16 PM UTC\nLicense: Development Status:  0 - Undefined\n', 'Development Status:  0 - Undefined\n', 'Registration Date:  Sun 14 May 2006 03:34:16 PM UTC\n', 'GNU General Public License V2 or later', 'd6094a52d3c90723c55f8639664fae22'),
(57, 'abelha', 'The Abelha project is an manufacturing monitoring software.Registration Date:  Tue 06 Mar 2012 08:43:52 PM UTC\nLicense: Development Status:  3 - Alpha\n', 'Development Status:  3 - Alpha\n', 'Registration Date:  Tue 06 Mar 2012 08:43:52 PM UTC\n', 'GNU General Public License V3 or later', '12ac82bbfd7158c62be769bcb8ef9e58'),
(59, 'aae', 'Aae is an game engine written in C++, which uses lua for scripting, Ogre3d for rendering, Bullet for physicsRegistration Date:  Mon 09 Jul 2007 06:23:45 PM UTC\nLicense: Development Status:  0 - Undefined\n', 'Development Status:  0 - Undefined\n', 'Registration Date:  Mon 09 Jul 2007 06:23:45 PM UTC\n', 'GNU General Public License V2 or later', '06bd9a7e117ed922d71e4bce4960443f'),
(61, 'a2jmidid', 'Daemon for exposing legacy ALSA sequencer applications in JACK MIDI system.Registration Date:  Sun 26 Aug 2007 03:35:36 PM UTC\nLicense: Development Status:  5 - Production/Stable\n', 'Stable\n', 'Registration Date:  Sun 26 Aug 2007 03:35:36 PM UTC\n', 'GNU General Public License V2 or later', '6036498b50af03e021d9bf4493ad00b9');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
