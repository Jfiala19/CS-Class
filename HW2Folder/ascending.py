import sys
x = float(sys.argv[1])
y = float(sys.argv[2])
z = float(sys.argv[3])
result = x<y<z or x>y>z
print(result)