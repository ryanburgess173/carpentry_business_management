CREATE PROCEDURE InsertNewOrder
    @OrderDescription varchar(250),
    @CustomerID int,
    @OrderNotes varchar(2500),
    @InitialEstimatedCost FLOAT,
    @ProjectLog varchar(2500),
    @HalftimeEstimatedCost FLOAT,
    @FinalCostOfProject FLOAT
AS
INSERT INTO Orders
    (
    OrderDescription,
    CustomerID,
    OrderNotes,
    InitialEstimatedCost,
    ProjectLog,
    HalftimeEstimatedCost,
    FinalCostOfProject
    )
VALUES(
        @OrderDescription,
        @CustomerID,
        @OrderNotes,
        @InitialEstimatedCost,
        @ProjectLog,
        @HalftimeEstimatedCost,
        @FinalCostOfProject
);
GO;