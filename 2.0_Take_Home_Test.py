'''
HONOR CODE: I solemnly promise that while taking this test I will only use PyCharm or the Internet,
but I will definitely not ask another person except the instructor. Signed: Eddie H. Agic

1.) How do you enter a single line comment in a program?

#Use a pound like this (except this is all a comment anyways so it doesn't really do anything).

INCORRECT: You are getting floor (//) mixed up with modulus (%). Try it out.
2.) What do the following lines of code output? ALSO: Why do they give a different answer?
2 / 3 .6 Repeating, just a normal division problem.
2 // 3 0, this is a 'floor' and will come up with the remainder.  CORRECTION:  It cuts off everything after the decimal.
3/2 1.5, regular division.
3//2 1, remainder.  CORRECTION:  It cuts off everything after the decimal.





3.) What happens when you try this and why?
A = 22
b = 13
c = a+b

It won't work because we set CAPITAL A to 22 and not LOWERCASE a to 22, so it either won't know what to add or
if you have 'a' set to something you will most likely get the wrong answer.



4.) All of the variable names below can be used. But which ONE of these is the better variable name to use?
a
A
Area
AREA
area
area_of_rectangle - This one because it does not contain any capital letters and is specific.
Area_Of_Rectangle





5.) Which of these variables names are NOT allowed in Python? 
Test them if you aren't sure.

apple
Apple
APPLE
Apple2
1Apple - This one
account number - This one
account_number
account.number - This one
accountNumber
account# - This one
pi
PI
fred
Fred
GreatBigVariable
greatBigVariable
great_big_variable
great.big.variable - This one
2x - This one
x2x
total% - This one
#left - This one






6.) Predict the output of (a) and its type and then test it?
a =2 - Output 2 (I was correct)
a*=10 - Multiplies the variable by what you set it to (I think I was correct)
a/=2 - Divides the variable by what you set it to (I think I was correct)
a+=12 - Adds to the variable what you set it to (Okay by now I'm sure I'm correct on these)
a-=7 - Subtracts from the variable what you set it to (Absolutely correct)
a - 15
type(a) - The console says <class 'float'>







7.) This program runs, but the code still could be better. How?
radius = 10
x = 3.14
pi = x
area = pi  * radius ** 2
area

Instead of setting x to 3.14 and creating unnecessary variables, you could just set pi to 3.14.




8.) What is the ouput of each of these?
type(42) <class 'int'>
type(42.0) <class 'float'>
type("C3PO") <class 'str'>
type(True) <class 'bool'>






yes, that would work but 3*(x+y) would also work.
9.) Fix the mistake in the following code:
x = 4
y = 5
a = 3(x + y)
a = 3*x+3*y is the correct way to write this.  CORRECTION: 3*(x+9) would be more efficient than 3*x+3*y, though they
retrieve the same result.




SO...correct the code.
10.)Why does this code not calculate the average?
x,y,z =(3,4,5)
ave = x+y+z/3
ave

Because it is doing of order of operations.  So instead of finding the average, its dividing 'z' by 3 and adding 7.
CORRECTION: (x+y+z)/3


'''
