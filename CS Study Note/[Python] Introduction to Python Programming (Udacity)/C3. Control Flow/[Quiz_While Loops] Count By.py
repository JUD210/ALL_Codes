""" Quiz: Count By

Suppose you want to count from some number start_num by another number count_by until you hit a final number end_num. Use break_num as the variable that you'll change each time through the loop. For simplicity, assume that end_num is always larger than start_num and count_by is always positive.

Before the loop, what do you want to set break_num equal to? How do you want to change break_num each time through the loop? What condition will you use to see when it's time to stop looping?

After the loop is done, print out break_num, showing the value that indicated it was time to stop looping. It is the case that break_num should be a number that is the first number larger than end_num. 

    +Quiz: Count By Check

Now in addition, address what would happen if someone gives a start_num that is greater than end_num. If this is the case, set result to "Oops! Looks like your start value is greater than the end value. Please try again." Otherwise, set result to the value of break_num.


start_num = #provide some start number
end_num = #provide some end number that you stop when you hit
count_by = #provide some number to count by 

# write a condition to check that end_num is larger than start_num before looping
# write a while loop that uses break_num as the ongoing number to 
#   check against end_num


print(result)

"""

start_num = 10  # provide some start number
end_num = 100  # provide some end number that you stop when you hit
count_by = 5  # provide some number to count by

# write a while loop that uses break_num as the ongoing number to
#   check against end_num

if start_num > end_num:
    result = "Oops! Looks like your start value is greater than the end value. Please try again."

else:
    break_num = start_num
    while break_num < end_num:
        break_num += count_by

    result = break_num

print(result)
