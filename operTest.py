# qMsg = "다음 중 프로그래밍 언어가 아닌것은?"
# choiceMsg = "1.JAVA\n2.파이썬\n3.C언어\n4.망둥어\n"
# choice = int(input(qMsg+"\n"+ choiceMsg))
# answer = 4

# result = "정답!" if choice ==answer else "오답.." if choice >= 1 and choice <= 4 else " 잘못입력하셨습니다."
# print(result);

#-------------------------------------------------------------------------------------------------------------------

# %% 혈액형별 성격

qMsg= (("당신의 혈액형은?\n"
                  + "1.A형\n2.B형\n3.O형\n4.AB형"))
choice = int(input(qMsg + "\n"))
answer_a = "세심하고 거짓말을 잘 못한다."
answer_b = "거침없고 추진력이 좋다."
answer_o = " 사교성이 좋다."
answer_ab = "착하다."
errMsg = "다시 입력해주세요"

result = ((answer_a if choice == 1 else 
  answer_b if choice == 2 else
    answer_o  if choice == 3 else
       answer_ab   if choice == 4 else errMsg
  ))

print(result)