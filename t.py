import random

#c="ab"
#print(c*4)
#
#a=input("enter a number")
#b=input("enter a number")
#print(int(a)+int(b))
#
#def func():
#    print(1)
#    print(2)
#print(3)
#func()
#
#
#def abs(x):
#    if x>0:
#        return(x) 
#    elif x<0:
#        return x * -1
#    else:
#        return(x)
#print(abs(-875)) 

#x=int(input("enter a number"))
#y=int(input("enter a number"))
#z=int(input("enter a number"))
#def max(x,y,z):
#   if x>=y and x>=z:
#       return x
#   elif y>=x and y>=z:
#       return y
#   else: 
#        return z
#print (max(x,y,z))
  
#list = [[1,2,3],[5,3,5]]
#newlist=[]
#newlist.extend(list[0])
#newlist.extend(list[1])
#print (newlist)

#bicycles = ['trek','cannondale','redline','specialized']
#cars = ['Ford','Honda','Tesla']
#newlist = []
#newlist.extend(bicycles)
#newlist.extend(cars)
#list.sort(newlist)
#print (newlist)

#n = 10
#count = 1
#while count <= n:
    #print('*'*count)
    #count = count + 1

#def convert(kilo):
    #return kilo*.621371

#print(convert(10))

#def distance(x,y,x1,y1):
    #a = (x1-x)**2
    #b = (y1-y)**2
    #return (a+b)**0.5

#print(distance(0,2,8,5))

#members =["Iris","Isabella", "Jeanne", "James", "Young", "Jade"]
#def getTeamLeader(members):
    #return(members[random.randint(0,len(members)-1)])

#print(getTeamLeader(members))

#arr=[10,20]
#temp = arr[1]
#arr[1] = arr[0]
#arr[0] = temp

#print(arr)

#def sigma(min,max): 
    #sum = 0
    #count = min
    #while count<=max:
        #sum=sum+count
        #count=count+1
    #return sum

#print(sigma(1,100))

#def sigma(min,max,interval):
    #sum=0
    #count=min
    #while count<=max:
        #sum=sum+count
        #count=count+interval
    #return sum

#print(sigma(1,9,4))

#x = int(input("enter number"))
#def prime(x):
    #y = 2
    #while y <= x-1:
        #if x%y==0:
            #return False
        #y = y+1
    #return True

#print(prime(x))   

#x="hello"
#y="world"
#s = "{}+{}={}".format(x,y)
#print(s)

#y = "world"
#x ="hello"
#line=""
#line = line + f"{x}+{y}={x+y}"
#print(line)

#Using a while loop, ask the user how long their bus rude was this month until they enter 0
#sum=0
#while True:
    #x = int(input("How long was your bus ride?"))
    #sum=sum+x
    #if x == 0:
        #break
#print(sum)

#sum=0
#count=0
#while True:
    #x = int(input("How long was your bus ride?"))
    #sum=sum+x
    #count=count+1
    #if x == 0:
        #break
#print(sum/count)

#numbers_list = [2,9,100,230,3,6,99]
#min=numbers_list[0]
#max=numbers_list[0]
#for numbers in numbers_list:
    #if min>numbers:
        #min=numbers
    #if max<numbers:
        #max=numbers

#print(min,max)

#numbers_list = [0,3,4,-1,-4,-5]
#zero=0
#zer=0
#neg=0
#pos=0
#for numbers in numbers_list:
    #if zero<numbers:
        #pos=pos+1
    #if zero>numbers:
        #neg=neg+1
    #if zero==numbers:
        #zer=zer+1
#line=""
#line = line + f"The number of positives is {pos}, the number of negatives is {neg}, and the number of zeroes is {zer}"
#print(line)

#numbers =[2,9,100,230,3,6,99]
#numbers=[1,9,8,22]
#numbers.sort()
#if len(numbers)%2==0:
#    x=len(numbers)//2
#    y=x-1
#   median=numbers[x]+numbers[y]
#    median=median/2
#    print(median)
#else:
#    median=len(numbers)//2
#    print(numbers[median])




