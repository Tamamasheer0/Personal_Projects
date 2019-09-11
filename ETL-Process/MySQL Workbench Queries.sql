/*************************************************************************************** 
						Group Project #2 - Extract, Transform, Load (ETL)
						Automated ETL Process - MySQL Database

Created: On: 05/22/2019									Last Modified: 06/17/2019

[Description]
	Objective: Design & Build a Fully Automated ETL Process Capable of Achieving the 
    Following:
		1. Extracting Data From an Online Web Source.
        2. Cleaning & Transforming the Raw Extracted Data Into a More Standardized,
		   Workable Structure.
		3. Loading the Cleaned Data Into Either a MySQL or MongoDB Database.
        **<Manual> Query Database Once Data Has Been Loaded Using the ETL Process.

[Employed Technologies]
    - Python <SQLAlchemy>: Automated Table Creation
    - Python <BeautifulSoup>: Automated Data Aggregation
    - Python <Pandas>: Automated Data Transformation & Loading to MySQL Database
    - MySQL Workbench: SQL Queries >> Data Exploration & Management
***************************************************************************************/
USE moneyball_db;
SELECT * FROM mlb_players_2019;

-- Query All Los Angeles Dodgers --
SELECT fname, lname, age, birthday, team
FROM mlb_players_2019
WHERE team = "Los Angeles Dodgers";

/*************************************************************************************** 

						RESET -- DELETE DATABASE -- moneyball_db 

***************************************************************************************/
DROP DATABASE IF EXISTS moneyball_db;