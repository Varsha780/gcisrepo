# take a number from the user
# check if odd or even
# find square  
# find cube
# print the result


"""

read input from user
main funtion
doc strings
comments
proper variable name
push to github

"""

def main(): # defining a function
    num = float(input("Enter a number = ")) # taking a number
    def odd_even():
            if num%2==0:
                print("The number is even")
            else:
                print("The number is odd")
    odd_even()
    def square():
         print("The square of the number = ", num**2)
    square()
    def cube():
         print("The cube of the number = ", num**3)
    cube()     

main()

