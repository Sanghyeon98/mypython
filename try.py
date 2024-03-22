#예외 처리
#             에러 : 심각한 오류
#             예외 : 덜 심각한 오류
            
# try : 
#             오류가 발생할 수 있는 문장
# except 오류 이름 as 객체:  // alias : 별칭
#             오류 발생 시 실행할 문장
            
# 모든 예외 클래스의 부모 클래스는 Exception이다.
# 어떤 오류든지 상관없이 except로 처리할 때에는
# "오류 이름" 자리에 에외의 최상위 부모인 Exception을 작성한다.

try:
    int(input("정수 입력 : "))
except Exception as e:
    print("정수만 입력하세요")
print("반드시 실행되어야 할 문장")

try:
    print(10/0)
except Exception as e:
    print("0으로 나눌 수 없습니다.")