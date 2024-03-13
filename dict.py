#dict 
# 한쌍으로 저장되어 관리한다.
# len()를 사용하면 한 쌍을 1로 카운트한다.
# 키 값은 중복이 될수 없으며, 값은 중복이 가능하다.
# 키 값을 주면 그 키의 짝꿍 값을 가지고 온다.

# dict명 = {키 : 값, 키 : 값, ...}

#dict 사용
# 추가(키 값이 없을때)
#         dict명[키] =값
# 수정(키 값이 있을때)
#         dict명[키] = 값
# 삭제(한 쌍이 삭제 된다.)
#         del dict명[키]
# 검색
#         키 in dict명 : 키 값이 있으면 참
#         키 not in dict명 : 키 값이 없으면 참

# Key 분리 
#     list(dict명.keys())
# Value 분리
#       dict명.values()    

중국집 = {"자장면" : 1500, "짬뽕" : 2500}
print(len(중국집))
print(중국집["자장면"])

if "자장면" in 중국집 :
  중국집["자장면"] = 4000
print(중국집["자장면"])  

if "탕수육"not in 중국집 :
  중국집["탕수육"] = 9000
print(중국집)  

for i in 중국집.keys():
  print(i)
  
for i in range(len(중국집)):
  print(str(i+1)+ "."+list(중국집.keys())[i])
  
print(중국집.values())
print(중국집.get("탕수육"))