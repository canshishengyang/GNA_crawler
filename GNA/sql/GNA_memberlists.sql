-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- 主机: localhost
-- 生成日期: 2017-03-31 21:18:09
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
-- 表的结构 `GNA_memberlists`
--

CREATE TABLE IF NOT EXISTS `GNA_memberlists` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `members` text NOT NULL,
  `pj_id` int(11) NOT NULL,
  `md5` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=11 ;

--
-- 转存表中的数据 `GNA_memberlists`
--

INSERT INTO `GNA_memberlists` (`id`, `members`, `pj_id`, `md5`) VALUES
(1, 'Alexandre VINCENT <asmodehn>;Lloyd Macrohon <ow3dm>;Decertaines <rico>;Negre Guillaume <straasha>;XorfacX <xorfacx>;', 53, '6b9ceeafb2ed49fdf8bb55b0ce3b2269'),
(3, 'Konstantin Aleksandrov <negus>;Alex <neomind>;', 55, 'ff76d6ef130315042370ec01cd0f8fc3'),
(5, 'Boris BARNIER <bozzo>;', 57, 'd4fcdf772e021bf6a1af831e55b580e6'),
(7, 'EdB <edb>;frédéric Delaunay <xfred>;', 59, 'ea8337295adc846b1fee19ed989c183f'),
(9, 'Nedko Arnaudov <nedko>;', 61, 'c97fd35409bedc6b220f3e3fe1513e62');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
