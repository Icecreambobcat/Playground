from __future__ import annotations
import typing
# just some standard imports i like to use
from data import convert_dict, operators
# store file

class solution:
    def __init__(self, input_line: str ) -> None:
        self.input_line = input_line
        self.output_line: int | str = self.solve()

    def solve(self) -> int | str:
        inter_list = []

        if not self.input_line:
            return "Please enter a valid input."

        for word in self.input_line.strip().lower().split():
            if word in convert_dict.keys():
                number = str(float(convert_dict[word]))
                number = number.replace(',', '.')  # Replace commas with periods
                inter_list.append(number)
            elif word in operators.keys():
                inter_list.append(operators[word])
            else:
                return "Invalid input. Please try again."

        calc_string = ''.join(inter_list)  # Join without spaces to correctly form the expression

        try:
            out = eval(calc_string)
        except Exception as e:
            return f"An error occurred: {e}"

        return out

def main() -> None:

    prev_calcs = []

    while True:
        print("Please enter a calculation or type 'PREV_SOL' to view previous calculations.")
        input_line = input()

        if input_line == "PREV_SOL":
            print(f"Which index would you like to view? There are currently {len(prev_calcs)} previous calculations.")
            index = int(input())

            if index >= len(prev_calcs):
                print("Index out of range.")
            else:
                print(prev_calcs[index].output_line)
        if input_line == "":
            break

        sol = solution(input_line)
        if sol.output_line != "Invalid input. Please try again.":
            prev_calcs.append(sol)
            print(sol.output_line)
        else:
            print(sol.output_line)


if __name__ == "__main__":
    main()