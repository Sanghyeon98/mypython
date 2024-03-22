# 파일 입출력
#         파일 객체 = open("경로","목적")
        
#         목적
#         -w : 해당 경로 내용 덮어쓰기(기존 내용 삭제, 해당경로에 파일이 없으면 생성)
#         -a : 해당 경로 내용 추가하기(기존 내용 유지, 해당 경로에 파일이 없으면 생성)
#         -r : 해당 경로 내용 읽기(해당 경로에 파일이 없으면 오류)
        
#         출력하기
#                 파일 객체.write("문자열")
                
#         입력하기
#                 파일 객체.readlines()
                
#         close() : 버퍼를 비워주어야 파일에 적용된다.
#                         반드시 작업이 끝나면 파일 객체명.close()를 사용!

#절대 경로 : 내 위치가 어디든 찾아갈 수 있는 경로
#상대 경로 : 내 위치에 따라 경로가 변경된다.
#       .  : 현재위치
#         . . : 인전 폴더

# name_file = open("names.txt", 'a')
# name_file.write("박상현")
# name_file.close()

name_file = open("names.txt","r")
for i in name_file.readlines():
    print(i, end="")