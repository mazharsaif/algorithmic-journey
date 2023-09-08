def main():
    ### Imports
    import json

    ### Reading and Preprocessing Input"
    with open("input.json", "r") as f:
        jstring = json.load(f)

    ### Part 1
    def num_sum(node):
        if isinstance(node, int):
            return node

        elif isinstance(node, str):
            return 0

        elif isinstance(node, list):
            return sum([num_sum(n) for n in node])

        elif isinstance(node, dict):
            return sum([num_sum(n) for n in node.values()])

        else:
            raise ValueError()

            
    ANS1 = num_sum(jstring)


    ### Part 2
    def num_sum_skipred(node):
        if isinstance(node, int):
            return node

        elif isinstance(node, str):
            return 0

        elif isinstance(node, list):
            return sum([num_sum_skipred(n) for n in node])

        elif isinstance(node, dict):
            values = node.values()
            if "red" in values:
                return 0

            
            return sum([num_sum_skipred(n) for n in values])

        else:
            raise ValueError()

            
    ANS2 = num_sum_skipred(jstring)


    
    return ANS1, ANS2



if __name__ == "__main__":
    ANS1, ANS2 = main()

    print(f"Answer to Part 1: {ANS1}")
    print(f"Answer to Part 2: {ANS2}")
