# https://www.hackerrank.com/challenges/merge-the-tools/problem


def merge_the_tools(string, k):
    # ex) string: AABCAAADA

    segments = [string[s : s + k] for s in range(0, len(string), k)]
    # ['AAB', 'CAA', 'ADA']


    for i in range(len(segments)):
        subsegment = ""

        for j in segments[i]:
            if j not in subsegment:
                subsegment += j

        print(subsegment)
    # AB
    # CA
    # AD



if __name__ == "__main__":
    string, k = input(), int(input())
    # AABCAAADA, 3

    merge_the_tools(string, k)
    # AB
    # CA
    # AD
