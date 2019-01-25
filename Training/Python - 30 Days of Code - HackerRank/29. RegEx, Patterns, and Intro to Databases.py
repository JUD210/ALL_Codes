# https://www.hackerrank.com/challenges/30-regex-patterns/problem


# Inputs
standard_input = """30
riya riya@gmail.com
julia julia@julia.me
julia sjulia@gmail.com
julia julia@gmail.com
samantha samantha@gmail.com
tanya tanya@gmail.com
riya ariya@gmail.com
julia bjulia@julia.me
julia csjulia@gmail.com
julia djulia@gmail.com
samantha esamantha@gmail.com
tanya ftanya@gmail.com
riya riya@live.com
julia julia@live.com
julia sjulia@live.com
julia julia@live.com
samantha samantha@live.com
tanya tanya@live.com
riya ariya@live.com
julia bjulia@live.com
julia csjulia@live.com
julia djulia@live.com
samantha esamantha@live.com
tanya ftanya@live.com
riya gmail@riya.com
priya priya@gmail.com
preeti preeti@gmail.com
alice alice@alicegmail.com
alice alice@gmail.com
alice gmail.alice@gmail.com"""


import re

names = []
for _ in range(int(input())):
    name, email = input().split()
    try:
        assert re.match(r"[a-z]{1,20}", name)
        assert re.match(r"[a-z@.]{1,40}@gmail\.com", email)
    except:
        continue
    else:
        names.append(name)

print(*sorted(names), sep="\n")
# alice
# alice
# julia
# julia
# julia
# julia
# preeti
# priya
# riya
# riya
# samantha
# samantha
# tanya
# tanya
