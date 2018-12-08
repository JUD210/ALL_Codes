# https://www.hackerrank.com/challenges/30-review-loop/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

result = []
for i in range(int(input())):
    text = input()

    text_even = ""
    text_odd = ""

    for j in range(len(text)):
        if j % 2 == 0:
            text_even += text[j]
        else:
            text_odd += text[j]
        
    result.append(text_even+" "+text_odd)

print("\n".join(result))
# 3
# 3
# Hacker
# Hce akr
# Rank
# Rn ak
# is Goooooood
# i oooo sGoood