def badfun(n):
    try:
        return n/0
    except:
        print("No está ok bro")
        raise
try:
    badfun(0)
except ArithmeticError:
    print("I know")
print("...")
