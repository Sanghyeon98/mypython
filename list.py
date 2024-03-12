# 컬렉션 - 데이터를 수집

#알고리즘 :  문제를 해결하기 위한 순서 또는 절차.

#                 빵집
#                 반죽 - > 발효 - > 굽기 - > 데코 - > 포장 - > 판매

#자료구조 :  의미없는 데이터가 자료 구조를 통과하는 순간 하나의 정보가 된다. 

#------------------------------------------------------------------------------------------------

# list
# 1. 변수를 여러번 선언하지 않고 여러 칸 list를 한 번만 선언하기 위해서 사용. 
#   변수를 선언하면, 값이 한개만 담기고 , 이름도 반드시 붙여야한다.
#   여러 변수를 선언하면 이름도 많아져서 관리하기 불편하다.
#   따라서 list는 이름 하나고 각 값을 방번호(인덱스)로 접근하기 때문에
#   값을 관리하기 훨씬 편하고 쉽다.

# 2.  규칙성이 없는 값에 규칙성을 부여하기 위해서
#  "박상현" " 지우개" "마우스" "핫도그" "배고파" "맛있다"
#       0                 1               2                 3             4                   5

#list 선언 대괄호 보면 list다.!
# list명 = [값1,값2, ....]
# list명 = [값] * 칸수
# list명 =[]

#list 길이 len(list명)

#list 사용 
        # dataList =[1,2,3]
# 값 넣기
        # (추가)
        # dataList.append(4)
        # 결과:[1,2,3,4]

        # (삽입)
        # dataList.insert(인덱스번호,값)
        # dataList.insert(1,1.5)
        # 결과 : [1, 1.5, 2, 3]

# 값 삭제
        # dataList.remove(값)
        # [1,2,3,1].remove(1)
        # 결과: [2,3,1]

        # del dataList[인덱스번호]
        # del dataList[1]
        # 결과 : [1,3]

        # dataList.clear()
        # 모든 값 삭제

# 값 검색
        # dataList.index(값)
        # dataList.index(3)
        # 결과: 2
        # 중복 시 좌에서 우방향으로 가장 먼저 만난 값의 인덱스 번호를 가져온다.

# 값 수정
        # dataList[인덱스 번호] = 새로운값
        # dataList[0] = 10
        # 결과 : [10,2,3]
        
# for문 사용
          #   0, ?, 1 --> ? 로 사용 가능
          # for i in range(len(list명)):
          #   list명[i]   리스트의 각요소
                    
#빠른 for문(향상된 for문, forEach문)
          # for i in list명:            i 리스트의 각 요소        
          
#값의 유무 확인 
          # 값 in list명 : 조건식(참 또는 거짓의 값) list안에 값이 있으면 True!
          # 값 not in list먕 : list안에 값이 없으면 True!           
          
          
dataList = [2,4,5,6]
print(len(dataList))
print(dataList[2])
print(dataList)



dataList.append(7)
print(dataList)

dataList.insert(1,3)
print(dataList)

print(dataList.index(7))
if(-100 in dataList) :
  print(dataList.index(-100))
else:
  print ("해당 값은 리스트에 없습니다.")

dataList.remove(4)    
print(dataList)

del dataList[4]
print(dataList)

dataList[0] = 20
print(dataList)

print(dataList[0:3])

#-------------------------------------------

dataList2= [0]* 100
for i in dataList2:
  print(i)
  
# cnt =1 
# for i in dataList2:
#   i = cnt
#   cnt += 1
# print(dataList2)     

for i in range(len(dataList2)):
  dataList2[i] = i+1
  print(dataList2[i]) 