# https://www.hackerrank.com/challenges/the-minion-game/problem


class Player:
    def __init__(self, name, word_type):
        self.name = name
        self.word_type = word_type
        self.score = 0


def init_char_checker(word_type):
    vowels = ["A", "E", "I", "O", "U"]
    consonants = [
        chr(code_num)
        for code_num in range(ord("A"), ord("Z") + 1)
        if chr(code_num) not in vowels
    ]

    if word_type == "vowels":
        return vowels
    elif word_type == "consonants":
        return consonants
    else:
        raise Exception("Player's word_type is set wrong!")


def value_score(Player, string):

    char_checker = init_char_checker(Player.word_type)
    score = 0

    # ex) string: "BANANA"
    for i in range(len(string)):

        if string[i] not in char_checker:
            continue
        else:
            score += len(string) - i
            # i:0 j:0~5 -> score += 6 (B, BA, BAN, BANA, BANAN, BANANA)
            # i:1 j:1~5 -> continue
            # i:2 j:2~5 -> score += 4 (N, NA, NAN, NANA)

    """ Terminated due to timeout :(

    # ex) String: "BANANA"
    for i in range(1, len(string) + 1):
    # i:1~6 -> 1, 2, 3, 4, 5, 6 chars

        for j in range(len(string) - i + 1):
        # i:1 j:0~5 -> B, A, N, A, N, A
        # i:2 j:0~4 -> BA, AN, NA, AN, NA
        # i:6 j:0   -> BANANA

            word = string[j : j + i]

            if word[0] in char_checker:
                score += 1
    """

    return score


def check_winner(p_v, p_c):
    if p_v.score > p_c.score:
        return "{} {}".format(p_v.name, p_v.score)
    elif p_v.score < p_c.score:
        return "{} {}".format(p_c.name, p_c.score)
    else:
        return "Draw"


def minion_game(string):

    p_v = Player("Kevin", "vowels")
    p_c = Player("Stuart", "consonants")

    p_v.score = value_score(p_v, string)
    p_c.score = value_score(p_c, string)

    result = check_winner(p_v, p_c)

    print(result)
    # Stuart 12


if __name__ == "__main__":
    s = input()
    # BANANA

    minion_game(s)
    # Stuart 12
