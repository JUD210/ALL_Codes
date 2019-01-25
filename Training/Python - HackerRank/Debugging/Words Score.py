# https://www.hackerrank.com/challenges/words-score/problem


# Inputs
standard_input = """3
programming is awesome"""


def is_vowel(letter):
    return letter in ["a", "e", "i", "o", "u", "y"]


def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            # Edit THIS!
            # ++score
            score += 1
    return score


n = int(input())
# 3
words = input().split()
# programming is awesome

print(score_words(words))
# 4
