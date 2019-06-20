
def IDtoTime(string):
    start_time = ""
    result = []
#mon1
#mon1,2
#mon10,2,3
#mon10:30
#tue(11:30
    if string[1].isdecimal() == True:
        start_time = string[1]
        if len(string) >=3 :    
            if string[2].isdecimal() == True:
                start_time = string[1:3]
                if len(string) >=4:
                    if string[3] == ',':
                        start_time = change24(start_time)    
            elif string[2] == ',':
                start_time = string[1]
                start_time = change24(start_time)
        else :
            start_time = change24(start_time)
    elif string[1] == '(':
        start_time = string[2:4]

    time_lasting = 0; 
    if string.count(',') >= 0:
        time_lasting = string.count(',')+1
        if string[len(string)-1] == ',':
            time_lasting = string.count(',')
    if string.count(':') > 0:
        time_lasting = 1.5
        if start_time == "10" or start_time == "13" or start_time == "16" or start_time== "19":
            start_time = start_time+".5"
    tmp = [daytoenglish(string[0]), start_time, time_lasting]
    return tmp

def change24(time_to):
    time_ = 0
    if time_to == '0':
        time_ = '08'
    if time_to == '1':
        time_ = '09'
    if time_to == '2':
        time_ = '10'
    if time_to == '3':
        time_ = '11'
    if time_to == '4':
        time_ = '12'
    if time_to == '5':
        time_ = '13'
    if time_to == '6':
        time_ = '14'
    if time_to == '7':
        time_ = '15'
    if time_to == '8':
        time_ = '16'
    if time_to == '9':
        time_ = '17'
    if time_to == '10':
        time_ = '18'
    if time_to == '11':
        time_ = '19'
    if time_to == '12':
        time_ = '20'
    if time_to == '13':
        time_ = '21'
    return time_
    
def daytoenglish(value):
    if value == '월':
        return 'mon'
    if value == '화':
        return 'tues'
    if value == '수':
        return 'wed'
    if value == '목':
        return 'thurs'
    if value == '금':
        return 'fri'
    if value == '토':
        return 'sat'
    if value == '일':
        return 'sun'





def classify(arr): 
    day = ['월','화','수','목','금','토','일']
    building = '관'
    room = '호'

    check = 0
    tmp = []
    result = []
    for index in range(len(arr)):
        for index2 in range(len(day)):
            if len(arr[index])>0 : 
                idx = arr[index][0].find(day[index2])
                if idx != -1:
                    check = 1
        if check == 1:
            tmp = IDtoTime(arr[index])
            for n in range(len(tmp)):
                if tmp[1] != '' and tmp[2] != 0:
                    result.append(tmp[n])
            check = 0
        idx = arr[index].find(building)
        if idx != -1:
            if arr[index][idx-1].isdecimal() == True:
                result.append(arr[index][0:idx])
        idx = arr[index].find(room)
        if idx != -1:
            if arr[index][idx-1].isdecimal() == True: 
                result.append(arr[index][0:idx])
    return result


stringsplit = ['화(16:30~17:15)', '/', '목(15:00~16:15)', '/','화요일에하는', '인생경험', '월월월', '권력의', '203관(서라벌홀)', '607호', '310관(서라벌홀)', '728호', '<강의실>']
stringsplit1 = ['화10', '/', '목0,1', '/','화요일에하는', '인생경험', '월월월', '권력의', '203관(서라벌홀)', '607호', '310관(서라벌홀)', '728호', '<강의실>']
stringsplit2 = ['화1,2,3', '/', '목4', '/','화요일에하는', '인생경험', '월월월', '권력의', '203관(서라벌홀)', '607호', '310관(서라벌홀)', '728호', '<강의실>']
result = classify(stringsplit)
print(result)
result = classify(stringsplit1)
print(result)
result = classify(stringsplit2)
print(result)
