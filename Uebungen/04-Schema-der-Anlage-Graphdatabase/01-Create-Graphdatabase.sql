-- Create a graph demo database
IF NOT EXISTS (SELECT * FROM sys.databases WHERE NAME = 'graphdemo')
	CREATE DATABASE GraphDemo;
GO

USE GraphDemo;
GO