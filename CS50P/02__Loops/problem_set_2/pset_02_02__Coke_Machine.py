# write sum that needs to be paid
# accept only chosen coins, one at a time
# end when sum=0
# if sum <0 write change that will be returned by machine

accepted_coins = [5, 10, 25]
sum = 50


while sum > 0:
    payment = int(input(f"Money to be paid: {sum}\n"))

    if payment in accepted_coins:
        sum -= payment
    else:
        print("We accept 5, 10, 25 only.")


if sum < 0:
    print(f"Here's your change: {-sum}")

print("Thank you!")
