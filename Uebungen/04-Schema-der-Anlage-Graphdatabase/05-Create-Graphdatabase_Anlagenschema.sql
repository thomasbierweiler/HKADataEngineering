-- Create a graph demo database
IF NOT EXISTS (SELECT * FROM sys.databases WHERE NAME = 'HSKAGraphAnlagenschema')
	CREATE DATABASE HSKAGraphAnlagenschema;
GO

USE HSKAGraphAnlagenschema;
GO