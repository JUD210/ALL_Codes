# https://www.hackerrank.com/challenges/the-minion-game/problem?h_r=next-challenge&h_v=zen


class Player:
    
    def __init__(self, name):
        self.name = name
        self.score = 0

    def value_score(self, string):
        vowels = ["A", "E", "I", "O", "U"]
        consonants = [
            chr(code_num)
            for code_num in range(ord("A"), ord("Z") + 1)
            if chr(code_num) not in vowels
        ]

        return ""


def minion_game(string):

    p_v = Player("KEVIN")  # Player: Vowels side
    p_c = Player("STUART")  # Player: Consonants side




if __name__ == "__main__":
    s = input()
    # BANANA

    minion_game(s)
    # Stuart 12