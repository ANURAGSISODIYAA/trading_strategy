CREATE DATABASE trading_data;

USE trading_data;

CREATE TABLE stock_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    datetime DATETIME,
    open DECIMAL(10, 2),
    high DECIMAL(10, 2),
    low DECIMAL(10, 2),
    close DECIMAL(10, 2),
    volume INT,
    instrument VARCHAR(50)
);
