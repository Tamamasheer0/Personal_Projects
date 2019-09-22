CREATE DATABASE IF NOT EXISTS stock_data;
use stock_data;


/*	Initialize 'stock_data' table */
CREATE TABLE closing_prices (
    id INT NOT NULL AUTO_INCREMENT,
   Date VARCHAR(30) NULL,
    JPM DECIMAL(10, 5) NULL,
    WFC DECIMAL(10, 5) NULL,
    AMZN DECIMAL(10, 5) NULL,
    C DECIMAL(10, 5) NULL,
    BAC DECIMAL(10, 5) NULL,
    MSFT DECIMAL(10, 5) NULL,
    PG DECIMAL(10, 5) NULL,
    DIS DECIMAL(10, 5) NULL,
    T DECIMAL(10, 5) NULL,
    CVX DECIMAL(10, 5) NULL,
    VZ DECIMAL(10, 5) NULL,
    CSCO DECIMAL(10, 5) NULL,
    KO DECIMAL(10, 5) NULL,
    PFE DECIMAL(10, 5) NULL,
    ORCL DECIMAL(10, 5) NULL,
    PM DECIMAL(10, 5) NULL,
    IBM DECIMAL(10, 5) NULL,
    NKE DECIMAL(10, 5) NULL,
    MO DECIMAL(10, 5) NULL,
    USB DECIMAL(10, 5) NULL,
    TXN DECIMAL(10, 5) NULL,
    GM DECIMAL(10, 5) NULL,
    TSLA DECIMAL(10, 5) NULL,
    F DECIMAL(10, 5) NULL,
    HAL DECIMAL(10, 5) NULL,
    S DECIMAL(10, 5) NULL,
    GLW DECIMAL(10, 5) NULL,
    MGM DECIMAL(10, 5) NULL,
    DVA DECIMAL(10, 5) NULL,
    X DECIMAL(10, 5) NULL,
    CMCSA DECIMAL(10, 5) NULL,
   PRIMARY KEY (id)
);

/*	Import CSV Stock Data to 'stock_data' Table */
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/stock_data.csv'
INTO TABLE closing_prices
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;