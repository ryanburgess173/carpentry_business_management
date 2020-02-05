CREATE PROCEDURE InsertNewInventoryItem
    @ItemName varchar(50),
    @ItemDescription varchar(255),
    @ItemPrice FLOAT,
    @ItemCostToUs FLOAT
AS
INSERT INTO Inventory
    (
    ItemName,
    ItemDescription,
    ItemPrice,
    ItemCostToUs)
VALUES(
        @ItemName,
        @ItemDescription,
        @ItemPrice,
        @ItemCostToUs
);
GO;