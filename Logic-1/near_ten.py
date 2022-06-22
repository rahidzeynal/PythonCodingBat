# My 1st solution
def near_ten(num):
  return 10 - num % 10 in range(0, 3) or num % 10 in range(0, 3)


# My 2nd solution
def near_ten(num):
  return num % 10 >= 8 or num % 10 <= 2
