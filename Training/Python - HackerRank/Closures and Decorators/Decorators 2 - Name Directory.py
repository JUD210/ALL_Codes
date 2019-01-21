# https://www.hackerrank.com/challenges/decorators-2-name-directory/problem


def person_lister(f):
    def inner(people):
        # print(f"people: {people}")
        # people: [['Mike', 'Thomson', '20', 'M'], ['Robert', 'Bustle', '32', 'M'], ['Andria', 'Bustle', '30', 'F']]

        result = [f(person) for person in sorted(people, key=lambda p: int(p[2]))]
        # result = map(f, sorted(people, key=lambda p: p[2]))

        return result

    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


if __name__ == "__main__":
    people = [input().split() for i in range(int(input()))]
    # 3

    # Mike Thomson 20 M
    # Robert Bustle 32 M
    # Andria Bustle 30 F

    print(*name_format(people), sep="\n")
    # Mr. Mike Thomson
    # Ms. Andria Bustle
    # Mr. Robert Bustle
