
class Elevator:

    def __init__(self, onFloor, canMoveUp, canMoveDown, status) -> None:
        self.canMoveUp = canMoveUp
        self.canMoveDown = canMoveDown
        self.onFloor = onFloor
        self.status = status

class ElevatorSystem:

    def __init__(self, NoOfElevators, NoOfFloors) -> None:
        self.NoOfElevators = NoOfElevators
        self.NoOfFloors = NoOfFloors

    def state(self, UserInputs):
        ...
    



