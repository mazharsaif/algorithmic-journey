def main():
### Reading and processing Input"
    input_string = "1321131112"

### Part 1
    def look_and_say(string:str) -> str:
        
        seqs = [string[0]]


        for i in range(1, len(string)):
            if string[i] == seqs[-1][0]:
                seqs[-1] = seqs[-1]+string[i]
            else:
                seqs.append(string[i])
            

        output = "".join([f"{len(i)}{i[0]}" for i in seqs])
        return output
    
    ANS1 = input_string
    for i in range(40):
        ANS1 =  look_and_say(ANS1)

    ANS1 = len(ANS1)


### Part 2 # Time To Calculate-Approx=10s
    ANS2 = input_string
    for i in range(50):
        ANS2 =  look_and_say(ANS2)

    ANS2 = len(ANS2) 

    
    return ANS1, ANS2



if __name__ == "__main__":
    ANS1, ANS2 = main()

    print(f"Answer to Part 1: {ANS1}")
    print(f"Answer to Part 2: {ANS2}")
