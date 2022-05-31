-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Mar 10, 2022 at 05:52 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `face_recognizer`
--

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `fname` varchar(255) NOT NULL,
  `lname` varchar(255) NOT NULL,
  `contact` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `securityq` varchar(255) NOT NULL,
  `securitya` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`fname`, `lname`, `contact`, `email`, `securityq`, `securitya`, `password`) VALUES
('Gaurav', 'Nandankar', '7698218655', 'hearmegaurav@gmail.com', 'Your Collage Name', 'Vimal Tormal Poddar', '123');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `Department` varchar(255) NOT NULL,
  `Course` varchar(255) NOT NULL,
  `Year` varchar(255) NOT NULL,
  `Semester` varchar(255) NOT NULL,
  `Id` varchar(255) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Division` varchar(255) NOT NULL,
  `D.O.B` varchar(255) NOT NULL,
  `Mobile` varchar(12) NOT NULL,
  `E-mail` varchar(255) NOT NULL,
  `Address` varchar(255) NOT NULL,
  `Gender` varchar(255) NOT NULL,
  `Photo` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`Department`, `Course`, `Year`, `Semester`, `Id`, `Name`, `Division`, `D.O.B`, `Mobile`, `E-mail`, `Address`, `Gender`, `Photo`) VALUES
('I.T', 'BCA', '2021-2022', 'Semester-6', '1', 'Gaurav', 'A', '03/09/2001', '7698218655', 'hearmegaurav@gmail.com', 'Surat', 'Male', 'Yes'),
('Financal', 'B.Com', '2021-2022', 'Semester-6', '2', 'Vinit', 'A', '01/05/2001', '8128145324', 'vinit@gmail.com', 'Surat', 'Male', 'Yes');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `register`
--
ALTER TABLE `register`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`Id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
