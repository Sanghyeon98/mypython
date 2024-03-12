#기타 제어문
# break : 인터프리터가 break를 만나자마자 반복문 탈출
# continue : 아래 문장을 하지 않고 다음 반복

#1 ~10 까지 중 4까지만 출력

for i in range(10):
  print(i+1)
  if(i ==3):
    break

for i in range(10):
  print(i+1)
  if(i ==3):
    continue