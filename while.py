# while test
# 반복문 while

# while 조건식 : 
#      반복할 문장

# 조건식이 참이면 반복
# 반복횟수를 모를 때 사용하는 목적
# 무한 반복일 경우 , 특정 조건에 break를 사용해서 탈출

#이름 10번 출력
# cnt =0
# while cnt != 10 :
#   cnt += 1
#   print("{}.박상현".format(cnt))
  
  
qMsg = ("당신의 혈액형은?\n"+"1.A형\n2.B형\n3.O형\n4.AB형\n5.나가기\n") 
answer_a = "세심하고 거짓말을 잘 못한다."
answer_b = "거침없고 추진력이 좋다."
answer_o = " 사교성이 좋다."
answer_ab = "착하다."
errMsg = "다시 입력해주세요"
result =""

while True:
  choice = int(input(qMsg));

  if choice ==1:
    result = answer_a
  elif choice  ==2:
    result = answer_b
  elif choice  ==3:
    result = answer_o
  elif choice  ==4:
    result = answer_ab
  elif choice  ==5:
    break
  else :
    result = errMsg

  print("\n"+result+"\n")   
