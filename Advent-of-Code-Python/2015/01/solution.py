def main():
    ### Reading and Preprocessing Input"
    with open("input.txt", "r") as f:
        inputs = f.read()

    ### Part 1
    plus1 = minus1 = 0
    for char in inputs:
        if char == "(":
            plus1 +=1
        else:
            minus1 +=1

    ANS1 = (plus1 - minus1)

    print(f"Answer to Part 1: {ANS1}")


    ### Part 2
    current_floor = 0
    for i, step in enumerate(inputs):
        if step == "(":
            current_floor +=1
        else:
            current_floor -=1

        if current_floor == -1:
            ANS2 = i + 1
            break

    print(f"Answer to Part 2: {ANS2}")

if __name__ == "__main__":
    main()