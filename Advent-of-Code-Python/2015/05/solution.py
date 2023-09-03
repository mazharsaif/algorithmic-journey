def main():
    ### Imports: None

    ### Reading and Preprocessing Input"
    with open("input.txt", "r") as f:
        raw_inputs = f.read()
        strings = raw_inputs.split()


    ### Part 1
    nice_str_indices = []

    for idx, s in enumerate(strings):
        
        num_vowels = 0
        twice = False
        flag = False
        if s[0] in "aeiou":
            num_vowels += 1
        for i, char in enumerate(s[1:], start=1):
            if char == s[i-1]:
                twice = True

            if char in "aeiou":
                num_vowels +=1
            

            if char in "bdqy":
                if s[i-1] == "acpx"["bdqy".index(char)]:
                    flag = True
                    break

        if not flag:
            if twice and num_vowels>=3:
                nice_str_indices.append(idx)

    ANS1 = len(nice_str_indices)


    ### Part 2
    nice_str_indices = []
    c2 = []
    c1 = []

    for idx, s in enumerate(strings):
        C2 = False
        l, r = 0, 2
        while r < len(s):
            # window = s[l:r]

            if s[l] == s[r]:
                C2 = True
                break

            l += 1
            r += 1

        c2.append(C2)




        C1 = False
        char_pairs:dict[str, int] = {} # "ad":index of d

        for i in range(1, len(s)):
            pair = s[i-1:i+1]
            if pair not in char_pairs:
                char_pairs[pair] = i

            # elif s[i] != s[i-1]:
            elif char_pairs[pair] != i-1:
                C1 = True

        c1.append(C1)

    ANS2 = 0
    for idx, (c1_, c2_) in enumerate(zip(c1, c2)):
        if c1_ and c2_:
            ANS2 += 1
            
    return ANS1, ANS2



if __name__ == "__main__":
    ANS1, ANS2 = main()

    print(f"Answer to Part 1: {ANS1}")
    print(f"Answer to Part 2: {ANS2}")
