# https://www.hackerrank.com/challenges/find-a-word/problem


import re


# Inputs
standard_input = """5
colourfuture saturday.future face_future(anxiety obtain.future surroundings'futurerefrigerator alone)futurecomparison wine-future,tight futureimpatient bodyfuture excite(future(grandfather
other(stick star,stick stick)critical stick(debt cheek_stick.representative serious(stick stick(sticky stick)chew dress)stick go_stick(furniture
occupy-tip repeat_tip pace)tip,riding catch(tip protect)tip dirt(tip(imagination commitment-tip(infected altogether.tip politically'tip anniversarytip
secure,tip board(tip)fever pile(tip_alphabetically remote)tip aloud(tip defend'tip_religious bottletip feeltip_unhappiness tip'swallow tear.tip
channel(hobby bus)channel(drunk soul(channel channel,take pour_channel-removal
6
tip
channel
tear
stick
future
realize"""


sentence = ""
for _ in range(int(input())):
    sentence += input() + "\n"

for _ in range(int(input())):
    print(len(re.findall(rf"(?:\b{input()}\b)", sentence)))


# 14
# 4
# 1
# 8
# 4
# 0
