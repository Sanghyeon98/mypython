#학생관리 
# 학생 이름과 학생 점수를 입력받고
# 추가 , 수정, 삭제, 목록

title = "학생 성적 관리 프로그램\n"
msg = "1.추가\n2.수정\n3.삭제\n4.목록\n5.나가기\n"
errMsg = "다시 시도해주세요"

studentDict = {}
subjectList = ["국어", "영어","수학"]

while True:
  choice = int(input(title + msg))
  
  #추가
  if choice == 1:
    name= input("학생 이름 : ")
    if name not in studentDict:
      studentDict[name] = input("다음과 같이 각 점수를 입력하세요.\n예)국어,영어,수학\n").split(",")
      
    else :
      print("이미 등록된 학생입니다.") 
    print(studentDict)
  #수정
  elif choice == 2:
    choice = int(input("1.학생명\n2.점수\n"))
    name = input("수정할 학생명 : ")
    if choice ==1:
      if name in studentDict:
        new = input("새로운 학생명")
          #기전 학생을 삭제하기 전
          #점수를 임시로 담아 놓는다.
        scoreList = studentDict[name]
        
        del studentDict[name]
        studentDict[new] = scoreList
      else :
        print("존재하지 않는 학생입니다.")
    elif choice ==2:
      choice = int(input("1.국어점수\n2.영어점수\n3.수학점수\n"))
      studentDict[name][choice-1]=int(input("새로운 점수 : "))
  #삭제           
  elif choice == 3:
    name = input("삭제할 학생명 : ")
    if name in studentDict:
      del studentDict[name]
    else:
      print("존재하지않는 학생입니다.")
  
  #목록      
  elif choice == 4:
    for i in studentDict.keys():
      print("["+i+"]")
      cnt=0
      for j in studentDict[i]:
        print(subjectList[cnt]+ " : "+str(j)+"점")
        cnt +=1
  elif choice == 5:
    break
  else :
    print(errMsg)  