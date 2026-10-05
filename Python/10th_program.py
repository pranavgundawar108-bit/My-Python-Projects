#program to find forth vertex of a rectangle if 3 are given:
#A(1,4),B(1,6),C(7,4)

(x1,y1) = (1,4)
(x2,y2) = (1,6)
(x3,y3) = (7,4)

x4 = (x2 + (x3-x1))
y4 = (y2 + (y3-y1))
print("(x4,y4)=",(x4,y4))