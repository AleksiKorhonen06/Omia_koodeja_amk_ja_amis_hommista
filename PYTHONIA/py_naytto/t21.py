def greatest_number(num1, num2, num3):
    if num1 <= num2 and num3 <= num2:
        return num2
    elif num2 <= num1 and num3 <= num1:
        return num1
    else:
        return num3
     

greatest = greatest_number(5.5, 4.1, 8.2)
print(greatest)

