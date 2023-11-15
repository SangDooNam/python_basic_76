
#Type your answer below (pick the correct line).

a=5
b=0
try:
    result=a/b
except ZeroDivisionError:
    result="You can't divide by 0"
    print(result)



a="Hello World!"
try:
    a + 10
except BaseException:
    msg="You can't add int to string"
    print(msg)






lst=[5, 10, 20]

try:
    print(lst[5])
except IndexError:
    msg="You're out of list range"
    print(msg)

