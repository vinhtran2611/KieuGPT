# KieuGPT


## Result

### Char level
```
After traning 3000 iter: train loss down from 4.90732 to 0.45013
Input:"Trăm năm "
Sample:
iter_dt 110.47ms; iter 3000: 
Trăm năm mà mặc muối mơn sang
Lần làm gươn chước chia pha thế này!
Sân Lồng thương cách hồng quầy
Từ rằng: Ph
Expect:
1. Trăm năm trong cõi người ta
Chữ tài chữ mệnh khéo là ghét nhau
or
2. Trăm năm biết có duyên gì hay không?
Ngổn ngang trăm mối bên lòng
```

### Word level
```
After traning 5000 iter: train loss down from 7.7963 to 0.46276
Input:"Trăm năm "
Sample:
trăm năm tính cuộc vuông tròn 
phải dò cho đến ngọn nguồn lạch sông 
nàng rằng muôn đội ơn lòng 
chút e bên thú bên tòng dễ đâu 
giận duyên tủi phận bời bời 
Expect:
1. Trăm năm trong cõi người ta
Chữ tài chữ mệnh khéo là ghét nhau
or
2. Trăm năm biết có duyên gì hay không?
Ngổn ngang trăm mối bên lòng

Now it learn format 6 8 6 8, :D!!!!
```