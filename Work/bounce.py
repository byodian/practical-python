import sys

def sum(a, b):
    print(a + b)

height = 100 # Meters
times = 10
num_bounces = 1

while num_bounces <= times:
    bounce_height = round(height * 3/5, ndigits=4)
    print(num_bounces, bounce_height) 
    height = bounce_height
    num_bounces = num_bounces + 1

sum(1,2)

print('sys.argv:', sys.argv)
print(sys.stdin)
print(sys.stdout)
print(sys.stderr)
