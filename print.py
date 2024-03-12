#%% (1) test
# 제어 문자
# 반드시 따옴표 안에서 사용한다.
#   \n : 줄바꿈, 개행 문자 (new line);
#   \t : 위 아래 줄 간격 맞춰 띄기(tab);
#   \\  : \사용
#   \"  : "사용
#    \'  : '사용

# 인터프리터에서 해석 방향 
# 위에서 아래로 좌에서 우로

print("자기소개 : ", end='←0')
print("이름 ; ")
print("박상현/n나이: 10살")


#서식 문자(format)
# 반드시 따옴표 안에서 작성한다.
# %d : decimal 정수 (10진수)
# %o : octal(8진수);
# %x : hexadecimal 정수(16진수)
# %f : float 실수;
# %c : character 문자
# %s : string 문자열 