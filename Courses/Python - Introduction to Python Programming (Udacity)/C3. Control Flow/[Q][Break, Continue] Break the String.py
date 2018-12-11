""" Quiz: Break the String

Write a loop with a break statement to create a string, news_ticker, that is exactly 140 characters long. You should create the news ticker by adding headlines from the headlines list, inserting a space in between each headline. If necessary, truncate the last headline in the middle so that news_ticker is exactly 140 characters long.

Remember that break works in both for and while loops. Use whichever loop seems most appropriate. Consider adding print statements to your code to help you resolve bugs. 
"""


# HINT: modify the headlines list to verify your loop works with different inputs

"""  [Solution] is more efficient way """

headlines = [
    "Local Bear Eaten by Man",
    "Legislature Announces New Laws",
    "Peasant Discovers Violence Inherent in System",
    "Cat Rescues Fireman Stuck in Tree",
    "Brave Knight Runs Away",
    "Papperbok Review: Totally Triffic",
]

news_ticker = ""

for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break

print(news_ticker)


""" [My Answer] """

# headlines = [
#     "Local Bear Eaten by Man",
#     "Legislature Announces New Laws",
#     "Peasant Discovers Violence Inherent in System",
#     "Cat Rescues Fireman Stuck in Tree",
#     "Brave Knight Runs Away",
#     "Papperbok Review: Totally Triffic",
# ]

# news_ticker = ""
# # write your loop here
# for headline in headlines:

#     if len(news_ticker) == 140:
#         print("Length of news_ticker: {}".format(len(news_ticker)))
#         break

#     elif len(news_ticker) > 140:
#         print("ERROR! Something's Wrong!")
#         break

#     elif len(news_ticker) + len(headline) <= 140:
#         news_ticker += headline

#     elif len(news_ticker) + len(headline) > 140:
#         for text in headline:
#             if len(news_ticker) < 140:
#                 news_ticker += text
#             else:
#                 break
#         break

#     news_ticker += "\n"

# print(news_ticker)
# print(len(news_ticker))