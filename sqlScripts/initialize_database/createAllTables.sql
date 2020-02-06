DELIMITER $$
CREATE PROCEDURE CreateAllTables()
BEGIN
    CREATE TABLE Transactions
    (
        TransactionID int IDENTITY NOT NULL PRIMARY KEY,
        TransactionName varchar
    (50),
        OrderID int NOT NULL,
        Subtotal FLOAT NOT NULL,
        Tax FLOAT NOT NULL,
        Total FLOAT NOT NULL
    );

    CREATE TABLE Orders
    (
        OrderID int IDENTITY NOT NULL PRIMARY KEY,
        OrderDescription varchar(2500) NOT NULL,
        CustomerID int NOT NULL,
        OrderNotes varchar(2500),
        InitialEstimatedCost FLOAT NOT NULL,
        ProjectLog varchar(2500),
        HalftimeEstimatedCost FLOAT,
        FinalCostOfProject FLOAT
    );
END$$
DELIMITER ;