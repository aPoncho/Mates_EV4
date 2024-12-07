-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 07-12-2024 a las 20:52:52
-- Versión del servidor: 8.3.0
-- Versión de PHP: 8.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `appdb`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `gastos`
--

DROP TABLE IF EXISTS `gastos`;
CREATE TABLE IF NOT EXISTS `gastos` (
  `id_gasto` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int DEFAULT NULL,
  `monto_gasto` int DEFAULT NULL,
  `fecha_gasto` datetime DEFAULT NULL,
  `descripcion` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id_gasto`),
  KEY `fk_gastos` (`id_usuario`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `gastos`
--

INSERT INTO `gastos` (`id_gasto`, `id_usuario`, `monto_gasto`, `fecha_gasto`, `descripcion`) VALUES
(3, 2, 50000, '2024-12-02 00:00:00', 'cuaderno'),
(2, 2, 20000, '2024-12-05 00:00:00', 'testing'),
(4, 2, 43000, '2024-12-01 00:00:00', 'lapiz');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ingresos`
--

DROP TABLE IF EXISTS `ingresos`;
CREATE TABLE IF NOT EXISTS `ingresos` (
  `id_ingreso` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int DEFAULT NULL,
  `monto_ingreso` int DEFAULT NULL,
  `fecha_ingreso` datetime DEFAULT NULL,
  `descripcion` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id_ingreso`),
  KEY `fk_ingresos` (`id_usuario`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `presupuestos`
--

DROP TABLE IF EXISTS `presupuestos`;
CREATE TABLE IF NOT EXISTS `presupuestos` (
  `id_presupuesto` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int DEFAULT NULL,
  `id_gasto` int DEFAULT NULL,
  `id_ingreso` int DEFAULT NULL,
  `ingreso_total` int DEFAULT NULL,
  `estimado_necesidades` int DEFAULT NULL,
  `estimado_deseo` int DEFAULT NULL,
  `estimado_ahorro` int DEFAULT NULL,
  `gastos_necesidades` int DEFAULT NULL,
  `gastos_deseados` int DEFAULT NULL,
  `gastos_ahorro` int DEFAULT NULL,
  PRIMARY KEY (`id_presupuesto`),
  KEY `fk_usuario` (`id_usuario`),
  KEY `fk_gastos_pre` (`id_gasto`),
  KEY `fk_ingresos_pre` (`id_ingreso`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `apellido` varchar(45) DEFAULT NULL,
  `correo` varchar(100) NOT NULL,
  `password` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `fecha_ingreso` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_usuario`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id_usuario`, `nombre`, `apellido`, `correo`, `password`, `fecha_ingreso`) VALUES
(2, 'Francisco', 'Barrios', 'fbarrios@gmail.com', '$2b$12$XjujMGnGOCxPPua3SUzABevFWTiz2mI3DDoxDKDAaa94OmOOuFr6W', '2024-12-06 17:14:18');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
