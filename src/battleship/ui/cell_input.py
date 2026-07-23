

class CellInput:
    def __init__(self, letters: list[str], numbers: list[str]) -> None:
        self.letters = letters
        self.numbers = numbers

    def take_input(self) -> tuple[int, int]:    
            while True:
                cell_code = input("Input Cell: ")
    
                if self.validate_input_cell(cell_code):
                    break
    
                print("Sorry, try again!")
    
            return self.parse_input_cell(cell_code) 

    def validate_input_cell(self, cell_code: str) -> bool:
        if not cell_code:
            return False

        letter_valid = cell_code[0].upper() in self.letters
        number_valid = cell_code[1:] in self.numbers
        
        return letter_valid and number_valid

    def parse_input_cell(self, cell_code: str) -> tuple[int, int]:
        let_str = cell_code[0].upper()
        num_str = cell_code[1:]

        row = self.letters.index(let_str)
        col = self.numbers.index(num_str)

        return (row, col)
