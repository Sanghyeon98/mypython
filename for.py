# for 변수명 in range(초기값, 끝값, 증감값):
#      반복할 문장  

# range( 초기값 , 끝값 , 증감값)
# 초기값이 0일 때 생략이 가능하다.
# 증감값이 1일 때에는 생략이 가능하다.

# for i in range(0,10,1) :
#     print("%d. 박상현" %(i+1))

# for i in range(10,0,-1) :
#     print("%d. 박상현" %i)
    
#0부터 1씩 증가시키는 for문을 작성한다(10번 반복)
#단, 10~1까지 출력한다.
# for i in range(0, 10 , 1):
#     print(10-i)
    
 #%% for task 
 # 반복문 시작값을 무조건 0으로 고정
#  1~100까지 출력
# 100~1까지 출력
# 1~100까지 중 짝수만 출력
# A~F까지 출력
# A~F까지 중 c제외 하고 출력
# aBcDeFgHiJKkLmNoPqRsTuVwXyZ 출력

# for i in range(0, 100, 1):
#     print(i+1)

# for i in range(0, 100, 1):
#     print(100-i);

# for i in range(0, 100, 2):
#     print(i+2)
    
# for i in range(0,6,1):
#     if (i +65) != 67 :
#         print(chr(i+65))
        
# print(chr(97))
 
for i in range(26):
    if(i % 2==0):
         print(chr(i+65+32))
    else:
        print(chr(i+65))