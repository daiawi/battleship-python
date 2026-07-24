from battleship.core.actions import Orientation, Placement, Shot


class CellInput:
    def __init__(self, letters: list[str], numbers: list[str]) -> None:
        self.letters = letters
        self.numbers = numbers

    def take_placement(self) -> Placement:    
        cell_input = self.prompt_for_cell()
        orient_input = self.prompt_for_orientation()
        placement = Placement(cell=cell_input, orientation=orient_input)

        return placement

    def take_shot(self) -> Shot:
        cell_input = self.prompt_for_cell()
        shot = Shot(cell=cell_input)

        return shot

    def prompt_for_cell(self) -> tuple[int, int]:
        while True:
            cell_code = input("Input Cell: ")

            if self.validate_input_cell(cell_code):
                break

            print("Sorry, try again!")
    
        return self.parse_input_cell(cell_code) 

    # TODO: Finish Orientation Prompt
    def prompt_for_orientation(self) -> Orientation:
        return Orientation.HORIZONTAL

    def validate_input_cell(self, input_cell: str) -> bool:
        cell_code = input_cell.strip()

        if not cell_code:
            return False

        letter_valid = cell_code[0].upper() in self.letters
        number_valid = cell_code[1:] in self.numbers
        
        return letter_valid and number_valid

    def parse_input_cell(self, input_cell: str) -> tuple[int, int]:
        cell_code = input_cell.strip()
        
        let_str = cell_code[0].upper()
        num_str = cell_code[1:]

        row = self.letters.index(let_str)
        col = self.numbers.index(num_str)

        return (row, col)
