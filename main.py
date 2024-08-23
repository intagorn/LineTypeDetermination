x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
output = ""
if (x1 == x2) or (y1 == y2):
    #special case
    if x1 == x2 and y1 == y2:
        output="Single Point"
    elif x1 == x2:
        output="Vertical Line"
    elif y1 == y2:
        output="Horizontal Line"

else:
    slope = (y2-y1)/(x2-x1)
    #normal case
    if slope > 0:
        output="Positive Slope"
    else:
        output="Negative Slope"

print(output)