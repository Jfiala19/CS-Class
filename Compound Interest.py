import math
import sys
Pnot = float(sys.argv[1])
r = float(sys.argv[2])
r = r*0.01
t = float(sys.argv[3])
Pf = (Pnot)*((math.e)**(r*t))
print(str(Pf))
