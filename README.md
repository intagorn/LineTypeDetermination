#  LineTypeDetermination
จงเขียนโปรแกรมเพื่อคำนวณหาประเภทของเส้นตรงจากจุดสองจุด (x<sub>1</sub>, y<sub>1</sub>) และ (x<sub>2</sub>, y<sub>2</sub>) 

โปรแกรมจะแสดงผลลัพธ์เป็นหนึ่งในห้าประเภทด้านล่าง:
* Positive Slope
* Negative Slope
* Horizontal Line
* Vertical Line
* Single Point

##  Input
รับข้อมูลเป็นจำนวนจริง (float ) 4 ค่า x<sub>1</sub>, y<sub>1</sub>, x<sub>2</sub>, y<sub>2</sub>

##  Ouputput
ผลลัพธ์ของโปรแกรมจะเป็นข้อความ (string) แสดงประเภทของเส้นตรง

## การคำนวณหาความชัน (slope) ของเส้นตรง
การคำนวณหาความชันของเส้นตรงจากจุดสองจุด ให้ใช้สมการด้านล่าง :

slope = (y2 - y1) / (x2 - x1)

Hint: ควรระวังการหารด้วย 0 ในการคำนวณ slope
## เงื่อนไขและผลลัพธ์
ตารางด้านล่างสรุปเงื่อนไขของการหาประเภทของเส้นตรงจากจุดสองจุด

| เงื่อนไข | คำอธิบาย | ผลลัพธ์ |
|-----------|-------------|--------|
| x1==x2 และ y1==y2 | ทั้งสองจุดเป็นจุดเดียวกัน | Single Point |
| y1==y2  | เส้นตรงขนานกับแกน x | Horizontal Line |
| x1==x2    | เส้นตรงขนานกับแกน y  | Vertical Line |
| slope > 0| เส้นตรงมีความชันเป็นบวก | Positive Slope |
| slope < 0 | เส้นตรงมีความชันเป็นลบ | Negative Slope |


**ตัวอย่างที่ 1:**

**Input:** `x1=2`,  `y1=3`,`x2=2`,  `y2=3` โดยโปรแกรมจะถาม `x1`, `y1`,`x2`, `y2`  ตามลำดับ
```
2
3
2
3
```
**Expected output:** หลังจากโปรแกรมคำนวณแล้ว โปรแกรมควรแสดงผลลัพธ์เป็น
```
Single Point
```

**ตัวอย่างที่ 2:**

**Input:** `x1=1`,  `y1=4`,`x2=1`,  `y2=7` โดยโปรแกรมจะถาม `x1`, `y1`,`x2`, `y2`  ตามลำดับ
```
1
4
1
7
```
**Expected output:** หลังจากโปรแกรมคำนวณแล้ว โปรแกรมควรแสดงผลลัพธ์เป็น
```
Vertical Line
```

**ตัวอย่างที่ 3:**

**Input:** `x1=0`,  `y1=5`,`x2=10`,  `y2=5` โดยโปรแกรมจะถาม `x1`, `y1`,`x2`, `y2`  ตามลำดับ
```
0
5
10
5
```
**Expected output:** หลังจากโปรแกรมคำนวณแล้ว โปรแกรมควรแสดงผลลัพธ์เป็น
```
Horizontal Line
```

**ตัวอย่างที่ 4:**

**Input:** `x1=1`,  `y1=2`,`x2=4`,  `y2=6` โดยโปรแกรมจะถาม `x1`, `y1`,`x2`, `y2`  ตามลำดับ
```
1
2
4
6
```
**Expected output:** หลังจากโปรแกรมคำนวณแล้ว โปรแกรมควรแสดงผลลัพธ์เป็น
```
Positive Slope
```

**ตัวอย่างที่ 5:**

**Input:** `x1=3`,  `y1=5`,`x2=6`,  `y2=2` โดยโปรแกรมจะถาม `x1`, `y1`,`x2`, `y2`  ตามลำดับ
```
3
5
6
2
```
**Expected output:** หลังจากโปรแกรมคำนวณแล้ว โปรแกรมควรแสดงผลลัพธ์เป็น
```
Negative Slope
```
