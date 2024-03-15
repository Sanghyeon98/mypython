#5개의 정수 중 최대값과 최소값을 구해주는 메소드

def getMaxAndMin(dataList):
    maxData = dataList[0] 
    minData = dataList[0]
    resultList = []
    
    for i in range(1, len(dataList)):
        if maxData < dataList[i]:
            maxData = dataList[i]
        if minData > dataList[i]:
            minData =dataList[i]
    resultList.append(maxData)
    resultList.append(minData)
    return resultList

# dataList = [ 3, 5 , 7 ,8]

# result=getMaxAndMin(dataList)

# print("최대값 : " + str(result[0]))
# print("최소값 : "+str(result[1]))


#소문자를 대문자로 바꿔주는 메소드
def changeToUpper(string):
    result = ""
    for i in string:
       if ord(i) >= 97 and ord(i) <= 122:
           result += chr(ord(i)-32)
       else :
           result += i
    return result

# print(changeToUpper("ASDdasdasdfASDFfxz"))           

#한글을 정수로 바꿔주는 메소드(일공이사  -> 1024)
def changeToInteger(hangle):
    hangle_org ="공일이삼사오육칠팔구"
    result=""
    for i in hangle:
        result += str(hangle_org.index(i))
    return int(result)   

print(changeToInteger("일공이사"))

def add(num1, num2):
    return num1 +num2

def sub(num1,num2):
    return num1 - num2