# https://www.hackerrank.com/challenges/python-mutations/problem


def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    return ''.join(l)


def mutate_string2(string, position, character):
    return string[:position] + character + string[position+1:]

if __name__ == '__main__':
    s = input()
    # abracadabra

    i, c = input().split()
    # 5 k

    s_new = mutate_string2(s, int(i), c)
    print(s_new)
    # abrackdabra