-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Oct 19, 2022 at 12:33 PM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flask`
--

-- --------------------------------------------------------

--
-- Table structure for table `chuck`
--

CREATE TABLE `chuck` (
  `id` int(11) NOT NULL,
  `value` text NOT NULL,
  `dataTime` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `chuck`
--

INSERT INTO `chuck` (`id`, `value`, `dataTime`) VALUES
(1, 'One of the main reasons there are so many mean fifth graders in the world today is because Chuck Norris stopped punching bad guys in the dick a decade ago.', '19/10/2022, 05:32:30'),
(2, 'A girl asked Chuck Norris to shave his beard. Chuck Norris roundhouse kicked her, and she grew taller and her hair grew shorter. That girl is now Justin Bieber.', '19/10/2022, 05:32:39');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `chuck`
--
ALTER TABLE `chuck`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `chuck`
--
ALTER TABLE `chuck`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
