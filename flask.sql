-- Active: 1786998924903@@127.0.0.1@3306@flask_project
-- Active: 1786998924903@@127.0.0.1@3306@flask_project
USE flask_project;
SELECT `State`, Category, ROUND(AVG(Unit_Price), 2) AS Average_Unit_Price, SUM(Quantity) AS Total_Quantity
FROM orders_table
GROUP BY `State`, Category
ORDER BY `State` DESC;  