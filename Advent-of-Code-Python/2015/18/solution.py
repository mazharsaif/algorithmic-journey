def main():
    ### Imports
    import numpy as np
    from tqdm import tqdm

    ### Reading and Preprocessing Input"
    with open("input.txt", "r") as f:
        initial_state = f.read()
        initial_state = initial_state.replace("#", "1").replace(".", "0").replace("\n", "")

        initial_state = list(initial_state)
        initial_state = np.array(initial_state).reshape((100,100)).astype("bool")

        initial_state_padded = np.zeros((102, 102), dtype="bool")
        initial_state_padded[1:-1, 1:-1] = initial_state


    ### Part 1
    current_state = np.copy(initial_state_padded)
    new_state = np.copy(initial_state_padded)

    for i in tqdm(range(100)):
        new_state = np.copy(current_state)
        for r in range(1, 101):
            for c in range(1, 101):
                bulb_state = current_state[r, c]

                TOP = current_state[r-1, c]
                BOTTOM = current_state[r+1, c]
                LEFT = current_state[r, c-1]
                RIGHT = current_state[r, c+1]
                TL = current_state[r-1, c-1]
                TR = current_state[r-1, c+1]
                BL = current_state[r+1, c-1]
                BR = current_state[r+1, c+1]

                adjacent_states = [TOP, BOTTOM, LEFT, RIGHT, TL, TR, BL, BR]
                adjacent_states = [1 if i else 0 for i in adjacent_states]
                num_adjacent_ons = sum(adjacent_states)
                
                if bulb_state == True:
                    if not ((num_adjacent_ons == 3) or (num_adjacent_ons == 2)):
                        new_state[r, c] = False
                    
                elif num_adjacent_ons == 3:
                    new_state[r, c] = True
                    
        current_state = np.copy(new_state)

    ANS1 = np.sum(current_state)


    ### Part 2

    ## Set Corner bulbs to True for Initial State
    corner_points = [(1, 1), (1, 100), (100, 1), (100, 100)]

    for (r,c) in corner_points:
        initial_state_padded[r,c]=True


    current_state = np.copy(initial_state_padded)
    new_state = np.copy(initial_state_padded)

    for i in tqdm(range(100)):
        new_state = np.copy(current_state)
        for r in range(1, 101):
            for c in range(1, 101):

                if (r, c) in corner_points:
                    continue # Skip for corner bulbs
                
                bulb_state = current_state[r, c]

                TOP = current_state[r-1, c]
                BOTTOM = current_state[r+1, c]
                LEFT = current_state[r, c-1]
                RIGHT = current_state[r, c+1]
                TL = current_state[r-1, c-1]
                TR = current_state[r-1, c+1]
                BL = current_state[r+1, c-1]
                BR = current_state[r+1, c+1]

                adjacent_states = [TOP, BOTTOM, LEFT, RIGHT, TL, TR, BL, BR]
                adjacent_states = [1 if i else 0 for i in adjacent_states]
                num_adjacent_ons = sum(adjacent_states)
                
                if bulb_state == True:
                    if not ((num_adjacent_ons == 3) or (num_adjacent_ons == 2)):
                        new_state[r, c] = False
                    
                elif num_adjacent_ons == 3:
                    new_state[r, c] = True
                    
        current_state = np.copy(new_state)

    ANS2 = np.sum(current_state)


    return ANS1, ANS2



if __name__ == "__main__":
    ANS1, ANS2 = main()

    print(f"Answer to Part 1: {ANS1}")
    print(f"Answer to Part 2: {ANS2}")
