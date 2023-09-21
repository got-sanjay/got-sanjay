def fact_rec(num):
  if num == 0 or num == 1:
    return 1
  else:
    return num * fact_rec(num - 1)


number = int(input("enter the value:"))
ex = fact_rec(number)

print("The factorial of {} is {}.".format(number, ex))
