def main():
    ### Imports
    from collections import defaultdict

    ### Reading and Preprocessing Input"
    with open("input.txt", "r") as f:
        steps = f.read()


    # Utility Functions
    def get_new_loc(step, prev_location):
        x, y = prev_location
        if step == "^":
            y += 1
        elif step == "v":
            y -= 1

        elif step == "<":
            x -= 1
        
        elif step == ">":
            x += 1

        else:
            raise ValueError(f"Unsupported Step direction {step}")


        return (x, y)
    

    ### Part 1
    visited_hashmap = defaultdict(int)
    visited_hashmap[(0, 0)] = 1


    current_loc = (0, 0)

    for s in steps:
        current_loc = get_new_loc(s, current_loc)
        visited_hashmap[current_loc] += 1
        
    ANS1 = len(visited_hashmap)



    ### Part 2
    visited_hashmap = defaultdict(int)
    visited_hashmap[(0, 0)] = 1


    santa_loc = (0, 0)
    robo_loc = (0, 0)
    for i, s in enumerate(steps):
        if i%2 != 0:
            santa_loc = get_new_loc(s, santa_loc)
            visited_hashmap[santa_loc] += 1
        else:
            robo_loc = get_new_loc(s, robo_loc)
            visited_hashmap[robo_loc] += 1

    ANS2 = len(visited_hashmap)
    
    
    return ANS1, ANS2



if __name__ == "__main__":
    ANS1, ANS2 = main()

    print(f"Answer to Part 1: {ANS1}")
    print(f"Answer to Part 2: {ANS2}")
