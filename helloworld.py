'''Print hello worlf''' # can be used as multiline comment
# hello WOrld 
print('hello world')


''' inline comment supported
LIST literal: []
TUPLE : ()
DICTIONARY: {}
SET {}
FUNCTION ARG
'''

a= [ 1, #item 1
     2, # item 2
     3, # item 2
    ]

print(a)

def myfunc(a, 
           b, #comment
           c):
           print(a,b,c)

myfunc(10, #comment
       20,
       30)

# on comditional staements
a=6
b=11
c=21
if a > 5 and b > 10 and c > 20:
    print("yes")

    
if a > 3 \
    and b > 5 \
        and c > 7:
        print("YESSSS")