#1~100까지 값 넣고 출력
#1~100까지 중 짝수만 넣고 출력
#A~F까지 넣고 출력
#A~F까지중 C 제외하고 출력
#aBcDeFgHiJkLmNoPqRs..Z넣고 출력
#"ABC"에서 B를 Z로 변경하기

# 자연수를 한글로 변경하기
# 입력 예)1024
# 출력 예)일공이사

#1~100까지 값 넣고 출력

# dataList1= []
# for i in range(100):
#   # dataList1[i] =i+1
#   dataList1.append(i+1)
 
dataList1 =[0]*100
for i in range(100):
  dataList1[i] = i+1  
print(dataList1)  

#================================= 
#1~100까지 중 짝수만 넣고 출력
dataList2 =[0]*50
for i in range(len(dataList2)):
  dataList2[i] = (i+1) * 2
print(dataList2)
 
#================================= 
#A~F까지 넣고 출력
dataList3 =[]
for i in range(6):
      dataList3.append(chr(i+65))
print(dataList3)

#================================= 
#A~F까지중 C 제외하고 출력
dataList4 =[""]*5
temp=0

for i in range(len(dataList4)):
  temp =i
  if temp> 1:
    temp +=1
    dataList4[i] =chr(65 +temp)
print(dataList4)   
          