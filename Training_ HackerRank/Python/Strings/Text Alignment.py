# https://www.hackerrank.com/challenges/text-alignment/problem


# Replace all ______ with rjust, ljust or center.

thickness = int(input())  # This must be an odd number
# 5

c = "H"


# Top Cone
for i in range(thickness):
    print((c * (i * 2 + 1)).center(thickness * 2))
    # print((c*i).______(thickness-1)+c+(c*i).______(thickness-1))

#     H
#    HHH
#   HHHHH
#  HHHHHHH
# HHHHHHHHH


# Top Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH


# #Middle Belt
for i in range((thickness + 1) // 2):
    print((c * thickness * 5).center(thickness * 6))

#   HHHHHHHHHHHHHHHHHHHHHHHHH
#   HHHHHHHHHHHHHHHHHHHHHHHHH
#   HHHHHHHHHHHHHHHHHHHHHHHHH
#   HHHHHHHHHHHHHHHHHHHHHHHHH


# #Bottom Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH


# #Bottom Cone
for i in range(thickness):
    print(
        (
            (c * (thickness - i - 1)).rjust(thickness)
            + c
            + (c * (thickness - i - 1)).ljust(thickness)
        ).rjust(thickness * 6)
    )

#                     HHHHHHHHH
#                      HHHHHHH
#                       HHHHH
#                        HHH
#                         H


#     H
#    HHH
#   HHHHH
#  HHHHHHH
# HHHHHHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHHHHHHHHHHHHHHHHHHHHHH
#   HHHHHHHHHHHHHHHHHHHHHHHHH
#   HHHHHHHHHHHHHHHHHHHHHHHHH
#   HHHHHHHHHHHHHHHHHHHHHHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#                     HHHHHHHHH
#                      HHHHHHH
#                       HHHHH
#                        HHH
#                         H

