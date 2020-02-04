CREATE PROCEDURE InsertNewTransaction
    @TransactionName nvarchar(30)
AS
INSERT INTO Transactions
    (TransactionName)
VALUES(
        @TransactionName
);
GO;