def main():
    ### Reading and Preprocessing Input"
    with open("input.txt", "r") as f:
        raw_inputs = f.readlines()
        raw_inputs = [i.strip() for i in raw_inputs]
        raw_inputs = [i.split("x") for i in raw_inputs]


    wrap_dimensions = []
    for raw_inp in raw_inputs:
        processed_input = [int(i) for i in raw_inp]
        wrap_dimensions.append(sorted(processed_input))


    ### Part 1
    ANS1 = 0

    for dims in wrap_dimensions:
        area = 2*dims[0]*dims[1] + 2*dims[1]*dims[2] \
                + 2*dims[2]*dims[0] + dims[0]*dims[1]
        ANS1 += area


    ### Part 2
    ANS2 = 0

    for dims in wrap_dimensions:
        ribbon_length = dims[0]*dims[1]*dims[2] + 2*(dims[0]+dims[1])
        ANS2 += ribbon_length

    return ANS1, ANS2



if __name__ == "__main__":
    ANS1, ANS2 = main()

    print(f"Answer to Part 1: {ANS1}")
    print(f"Answer to Part 2: {ANS2}")
