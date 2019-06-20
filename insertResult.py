import pymysql.cursors

conn = pymysql.connect(
        host='*',
        user='*',
        password='*',
        db='*',
        charset='utf8mb4'
        )


def insertResult(result):
    classID = result[0]
    classNum = result[1]
    className = result[2]
    classTime = result[3]
    split = result[4]
    if len(split) == 5:
        day = split[0]
        start = split[1]
        lasting = str(split[2])
        building = split[3]
        room = split[4]
        with conn.cursor() as cursor:
            sql = "INSERT INTO ClassInfo (classID, classNum, className, day,starttime, lastingtime, building, room) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) "
            cursor.execute(sql,(classID,classNum,className,day,start,lasting,building,room))
        conn.commit()
    
    if len(split) == 8:
        day = [split[0], split[3]]
        start = [split[1], split[4]]
        lasting = [str(split[2]), str(split[5])]
        building = split[6]
        room = split[7]
        with conn.cursor() as cursor:
            sql = "INSERT INTO ClassInfo (classID, classNum, className, day,starttime, lastingtime, building, room) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) "
            cursor.execute(sql,(classID,classNum,className,day[0],start[0],lasting[0],building,room))
        conn.commit()
        with conn.cursor() as cursor:
            sql = "INSERT INTO ClassInfo (classID, classNum, className, day,starttime, lastingtime, building, room) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) "
            cursor.execute(sql,(classID,classNum,className,day[1],start[1],lasting[1],building,room))
        conn.commit()

    elif len(split) == 9 :
        day = [split[0], split[3]]
        start = [split[1], split[4]]
        lasting = [str(split[2]), str(split[5])]
        building = split[6]
        room = [split[7],split[8]]
        with conn.cursor() as cursor:
            sql = "INSERT INTO ClassInfo (classID, classNum, className, day,starttime, lastingtime, building, room) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) "
            cursor.execute(sql,(classID,classNum,className,day[0],start[0],lasting[0],building,room[0]))
        conn.commit()
        with conn.cursor() as cursor:
            sql = "INSERT INTO ClassInfo (classID, classNum, className, day,starttime, lastingtime, building, room) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) "
            cursor.execute(sql,(classID,classNum,className,day[1],start[1],lasting[1],building,room[1]))
        conn.commit()     

    elif len(split) == 10:
        day = [split[0], split[3]]
        start = [split[1], split[4]]
        lasting = [str(split[2]), str(split[5])]       
        building = [split[6],split[8]]
        room = [split[7], split[9]]

        if building[0][len(building[0])-1].isdecimal == True:

            with conn.cursor() as cursor:
                sql = "INSERT INTO ClassInfo (classID, classNum, className, day,starttime, lastingtime, building, room) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) "
                cursor.execute(sql,(classID,classNum,className,day[0],start[0],lasting[0],building[0],room[0]))
            conn.commit()
            with conn.cursor() as cursor:
                sql = "INSERT INTO ClassInfo (classID, classNum, className, day,starttime, lastingtime, building, room) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) "
                cursor.execute(sql,(classID,classNum,className,day[1],start[1],lasting[1],building[1],room[1]))
            conn.commit()
    #print (result)
    #print (classID+"-"+classNum+" is inserted in DB")

    
#result = ['12345','12','hello','3-3',['mon','09',3,'310','210']]
#insertResult(result)
