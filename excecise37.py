and      Logical and                                True and False == False
as       Part of the with-as statement              with X as Y: pass
assert   Assert(ensure)that something is true       assert False, "Error!"
break    Stop this loop right now                   while True: break
class    Define a class                             class Person(object)
continue Don't process more of the loop, do it again while True: contunue
def      define a function                          def X(): pass
del      Delete from dictionary                     del X[Y]
elif     Else if condition                          if: X; elif: Y; else: J
else     Else conditon                              if: X; elif: Y; else: J
exec  Run a string as python                     exec 'print "Hello!"'
finally  Exceptions or not, finally do this no matter what   finally: pass
for      Loop over a collection of things           for X in Y: pass
from     Importing specific parts of a module       import X from Y
global   Declare that you want a global variable    global X
if       If conditon                                
import   Import a modle into this one to use        import os'
in       Part of for-loops Also a test of X in Y    for X in Y: pass
lambla   Create a short anonymous fuction           s = lambla y: y ** y; s(3)
not      logical not                                not True == False
or       Logical or         
pass     This block is empty
print    Pritn this string
raise    Raise an exception when things go wrong   raise ValueError("No")
return   Exit the fuction with a return value
try      while loop, and if exception, go to except  try: pass
while    while loop
with     With an expression as a value do           with X as Y: pass
yield    Pause here and return to caller            def X(): yield Y; X().next()





True  
False
None     Represents "nothing" or "no value"        x = None
strings  Stores textual information                x = "Hello"
numbers   Stores integers                          i = 100
floats   Stores decimals                           i = 10.98
lists    Stores a list of things                   j = [1, 2, 3, 4]
dicts   Stores a key = value maping of things      e = ['x':1, 'y':2 ]




\\  Backsplash
\'  Single-quote
\''  Double-quote
\a   Bell
\b  Backspace
\f   Foemfeed
\n   Newline
\r   Carriage
\t   Tab
\v   Vertical tab




%d Decimal integers(not floating point)     "%d" % 45 == '45'
%i Same as %d                                "%i" % 45 == '45'
%o   Octal number                             "%o" % 1000 == '1750'
%u   Unsigned decimnal                       "%u" % -1000 == '-1000[A
%x   Heximal lowercase                       "%x" %1000 == '3e8'
%X   Hexadecimal upercase                    "%X" %1000 == '3E8'
%e   Exponential notation, lowercase 'e'      "%e" % 1000 == '1.000000e+03'
%E   Exponential notation, uppercase 'E'      "%E" % 1000 == '1.000000E+03'
%f   Floating point real number                "%f" % 10.34 == '10.340000'
%F   Same as %f
%g   Either %f or %e, whichever is shorter     "%f" % 10.34 == '10.34'
%G   Same as %g but uppercase                  "%G" % 10.34 == '10.34'
%c   Character format                          "%c" % int == "<type 'int'>"
%s   String format                             "%s there" % 'hi' == 'hi there' 
%%   A percent sign                             "%g%%" % 10.34 == '10.34%'



+   Additon       2+4==6
-   Subtraction   2-4==-2
*  Multiplication   2*4==8
** power of      2 ** 4 = 16
/ Division       2 / 4.0 == 0.5
//   Floor division   2 // 4.0 == 0.0
%  String interpolate  modulus     2 % 4 == 2
<   Less than     4 < 4 == False
>   Greater than   4 > 4 == False
<=  Less than equal   4<=4 == True
>=   Greater than equal   4>=4 == True
== equal
!=  Not equal
<>  Not equal
()  Parenthesis
[]  Lists bracket
{}   Dict curly braces
@   At(decorators)
,   comma
: Colon
.  Dot
= Assign equal 
; sime-colon
+=   Add and assign
-=   Subtract and assign
*= Multiply and assign
/=  Divide and assign
%= Modulus assign
**= Power assign
