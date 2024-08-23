#  LineTypeDetermination
This project involves writing a Python program that determines the type of a line based on the coordinates of two points
(x<sub>1</sub>, y<sub>1</sub>) and (x<sub>2</sub>, y<sub>2</sub>) 

The program will classify the line as one of the following types:
* Positive Slope
* Negative Slope
* Horizontal Line (Parallel to the x-axis)
* Vertical Line (Parallel to the y-axis)
* Single Point (No Line)

##  Input
Four real numbers representing the coordinates x<sub>1</sub>, y<sub>1</sub>, x<sub>2</sub>, y<sub>2</sub>

##  Ouputput
The program will output the type of line formed by the two points.

## Slope Equation

To determine the slope of a line between two points, use the following equation:

slope = (y2 - y1) / (x2 - x1)

## Conditions and Output

The table below summarizes the conditions for determining the type of line formed by two points \((x_1, y_1)\) and \((x_2, y_2)\):

| Condition | Description | Output |
|-----------|-------------|--------|
| x1=x2 และ y1=y2 | The two points are identical. | Single Point (No Line) |
| \( x_1 \neq x_2 \) and the slope > 0 | The line has a positive slope. | Positive Slope |
| \( x_1 \neq x_2 \) and the slope < 0 | The line has a negative slope. | Negative Slope |
| \( y_1 = y_2 \) and \( x_1 \neq x_2 \) | The line is parallel to the x-axis. | Horizontal Line |
| \( x_1 = x_2 \) and \( y_1 \neq y_2 \) | The line is parallel to the y-axis. | Vertical Line |

**ตัวอย่างที่ 1:**

**Input:** `month=8`,  `day=4` โดยโปรแกรมจะถาม `month`, `day`  ตามลำดับ
```
8
14
```
**Expected output:** หลังจากโปรแกรมคำนวณแล้ว โปรแกรมควรแสดงผลลัพธ์เป็น
```
Wednesday
```
