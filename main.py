# def numberofBits(n):
#     ones= 0
#     zeros=0
#     while(n):
#         if (n & 1==1):
#             ones +=1
#         else :
#             zeros+= 1
#         n >>= 1
#     print("number of ones ===" , ones , "number of zeros" , zeros)
# number=int(input("input the number"))
# numberofBits(number)

#program to check if bit is int or not

def setbit(number, n):
    if number &(1<<(n-1)):
        print("set")
    else:
        print("not set")
number= int (input("enter number"))
n= int(input("enter a Bit number"))
setbit(number, n)