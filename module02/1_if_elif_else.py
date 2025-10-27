a = -5
print("Variable a: ", a)  # print variable

# variable|comparison operators|objects|logical operators|var|comparison operators|     objects(numberic(int,float,complex),string,bool,None,list,tuple,set,dict,frozenset)     |
#    a    |(==,<,>,<=,>=,!=)   |   0   |    and/or/not   | a |   ==,<,>,<=,>=,!=  | 3,0.5,5+2j,"Sam",True/False,None,["Sam"],("Sam",),{"Sam"},{"name":"Sam"},frozenset({"Sam"}) |                            |
# -------------------------------------------------------------------------logical expressions-----------------------------------------------------------------------------------

# if condition: -> conditional statement / if statement
# elif condition: -> conditional statement / elif statement
# else condition: -> else statement

if (
    a > 0
):  # if block, if True -> block instructions; if False -> outside of block instructions -> elif statements
    print("a is positive")  # |--> block instructions
elif (
    a < 0
):  # elif -> else if block, # if True -> block instructions; if False -> outside of block instructions -> else statement
    print("a is negative")  # |--> block instructions
else:  # else block, in other cases -> only block instructions -> than other instructions outside if-elif-else statements
    print("a is zero")  # |--> block instructions
print("fin")


b = -20
if b > 0:  # check on first step
    print("b is positive", b)
elif (
    b < -10
):  # check on second step (!!!! Very important order logical expressions in if-elif-elif-else statements, because interpritator go from up to down)
    print("b is less than -10: ", b)
elif b < 0:  # check on third step
    print("b is negative: ", b)
else:  # do only if 1,2,3 steps result == False
    print("b is zero", b)
print("fin")
