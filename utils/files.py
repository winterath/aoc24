from os.path import join

def readlines(inputFile):
    input_dir = '/workspaces/aoc24/input'
    path_to_input = join(input_dir, inputFile)
    try:
        with open(path_to_input) as file:
            lines = [line.rstrip() for line in file]
        return lines
    except FileNotFoundError:
        print(f"{inputFile} not found in {input_dir}")
        return []