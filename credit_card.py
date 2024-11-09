# Python Credit card validator Program

sum_odd_digits = 0
sum_even_digits = 0
total = 0

# STEP 1 - Remove "-" or " "

card_no = input("Enter a credit card #:  ")
card_no = card_no.replace("-","")
card_no = card_no.replace(" ","")
card_no = card_no[::-1]


# STEP 2 - Add all digits in the odd places from right to left

for x in card_no[::2]:
    sum_odd_digits += int(x)

#STEP 3 - Double every second digit from right to left
# (IF result is a two digit number then add the two digit num to get the single digit number )

for x in card_no[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_even_digits += (1+(x%10))
    else:
        sum_even_digits += x

# STEP 7- Add sum od odd digits and sum of even digitd

total = sum_odd_digits + sum_even_digits

# STEP 6 - if % 10 then its valid- Checking condition

if total % 10 == 0:
    print("Its a VALID Credit Card!!")
else:
    print("Its a INVALID Credit Card!!")









