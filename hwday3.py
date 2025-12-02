is_logged_in = True
is_subscribed = False
user_credit = 100
max_credits = 200
min_credits = 50
credits_valid = user_credit >= min_credits and user_credit<= max_credits and user_credit != min_credits

bonus_eligible = is_subscribed or not (user_credit <= min_credits)

user_credit += 50
user_credit -= 20
user_credit *= 2
user_credit %= 150

power_result = user_credit **2

full_access = is_logged_in and is_subscribed

is_true_login = is_logged_in is True

access_result = is_logged_in or is_subscribed and False

print("Is logged in :" ,is_logged_in)
print("Is subscribed :", is_subscribed)
print("credits valid :",credits_valid)
print("Is Bonus eligible :", bonus_eligible)
print("User credits =", user_credit)
print("Power result = ", power_result)
print("Full access  : ",full_access)
print("Is true login  :", is_true_login)
print("Access result  : ", access_result)