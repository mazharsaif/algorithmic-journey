def main():
    ### Imports
    import numpy as np
    import sys
    
    ### Utility Functions
    def process_instruction(raw_instruction:str) -> tuple[bool, int, int, int, int]:
        """returns (switch, x1, y1, x2, y2)"""

        instruc = raw_instruction.split(" ")
        if len(instruc)==5:
            switch = instruc[0] + " " + instruc[1]
            x1, y1 = instruc[2].split(",")
            x2, y2 = instruc[4].split(",")

        elif len(instruc)==4:
            switch = instruc[0]
            x1, y1 = instruc[1].split(",")
            x2, y2 = instruc[3].split(",")
        return switch, int(x1), int(y1), int(x2), int(y2)
    

    ### Reading and Preprocessing Input"
    with open("input.txt", "r") as f:
        raw_instructions = f.readlines()
        raw_instructions = [i.rstrip() for i in raw_instructions]
    
    instructions = [process_instruction(i) for i in raw_instructions]


    ### Part 1
    light_grid = np.zeros((1000,1000), dtype="bool")
    for instruc in  instructions:
        x1, y1, x2, y2 = instruc[1:]
        x2 +=1
        y2 +=1
        x1, x2 = min(x1,x2), max(x1,x2)
        y1, y2 = min(y1,y2), max(y1,y2)

        if instruc[0] == "turn off":
            light_grid[y1:y2, x1:x2] = False
        elif instruc[0] == "turn on":
            light_grid[y1:y2, x1:x2] = True

        elif instruc[0] == "toggle":
            light_grid[y1:y2, x1:x2] = ~light_grid[y1:y2, x1:x2]

        else:
            raise ValueError(f"unsupported step {instruc[0]}")

    ANS1 = np.sum(light_grid)
    
        

    ### Part 2
    light_grid = np.zeros((1000,1000), dtype="int32")
    for instruc in  instructions:
        x1, y1, x2, y2 = instruc[1:]
        x2 +=1
        y2 +=1
        x1, x2 = min(x1,x2), max(x1,x2)
        y1, y2 = min(y1,y2), max(y1,y2)

        if instruc[0] == "turn off":
            light_grid[y1:y2, x1:x2] = np.clip(light_grid[y1:y2, x1:x2] -1,
                                               0,
                                               sys.maxsize
                                               )
        elif instruc[0] == "turn on":
            light_grid[y1:y2, x1:x2] = light_grid[y1:y2, x1:x2] + 1

        elif instruc[0] == "toggle":
            light_grid[y1:y2, x1:x2] = light_grid[y1:y2, x1:x2] + 2

        else:
            raise ValueError(f"unsupported step {instruc[0]}")

    ANS2 = np.sum(light_grid)
    

    return ANS1, ANS2



if __name__ == "__main__":
    ANS1, ANS2 = main()

    print(f"Answer to Part 1: {ANS1}")
    print(f"Answer to Part 2: {ANS2}")
