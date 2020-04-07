import sqlite3
conn = sqlite3.connect('library.db')


def makeSureNotNull(attribute_name):
    while True:
        attribute = input("Enter "+attribute_name+" : ")
        if(attribute is None):
            print("Attribute "+attribute_name+" cannot be NULL")
        else:
            return attribute

def ifEmptySetToNULL(attribute_name):
    attribute = input("Enter "+attribute_name+" : ")
    if(attribute is None):
        return "NULL"
    else:
        return attribute

def displayHelp ():
    print("/finditem     : find item from the library")
    print("/borrow       : Borrow item from the library")
    print("/return       : Return item to the library")
    print("/donate       : Add item to the library")
    print("/findevent    : Find an event happening in library")
    print("/register     : Register an event in library")
    print("/volunteer    : Add volunteer personel to the library")
    print("/request      : Request for librarian\'s help")

def borrow (cursor):
    item_id = input("Which item to borrow? Specify by item id : ")
    cursor.execute("SELECT * FROM Items WHERE id = " +item_id)
    result = cursor.fetchone()
    print(result)
    if result is None:
        print("Item ID "+item_id+" not found.")
        return
    elif (result[3] != "available"):
        print("The item is not available.")
        return

    user_id = input("Who wants to borrow? Specify by user id : ")
    cursor.execute("SELECT pid FROM Users WHERE pid = "+ user_id)
    result = cursor.fetchone()
    if user_id is None:
        print("User ID "+user_id+" not found.")
        return

    cursor.execute("UPDATE Items SET availability = 'borrowed' WHERE id = "+str(item_id))
    execution = "INSERT INTO Borrowing (id, uid, fine) VALUES ("+str(item_id)+","+str(user_id)+",0)"
    print(execution)
    cursor.execute("INSERT INTO Borrowing (id, uid, fine) VALUES ("+str(item_id)+" ,"+str(user_id)+",0)")
    print("User "+user_id+" has borrowed an item "+item_id)

    conn.commit()

def finditem (cursor):
    # print("Search by title or ID")
    # search_type = input("Enter ID or title : ")
    # if(search_type == "ID"):
    #     id = input("Enter ID of an item : ")
    #     cursor.execute("SELECT * FROM Items WHERE id = "+ id)
    #
    # elif(search_type == "title"):
    #     title = input("Enter title of an item : ")
    #     cursor.execute("SELECT * FROM Items WHERE title LIKE '%"+ title+"%'")
    #
    # else:
    #     print("Invalid search type.")
    #     finditem(cursor)
    #
    # result = cursor.fetchall()
    # if(len(result) == 0):
    #     print("Item not found.")
    # iteration = 1
    # for column in result:
    #     print("Item #"+str(iteration))
    #     print("id :" + str(column[0]))
    #     print("title :" + column[1])
    #     print("release_date :" + str(column[2]))
    #     print("avilability :" + str(column[3]) + "\n")
    #     iteration = iteration + 1

    itemDict = {"1": "CD", "2": "Magazines", "3": "Scientific_Journals", "4": "Books"}
    item = 0
    cursor = conn.cursor()

    with conn:
        while not int(item) in range(1, 4):
            item = input("How can I help you today? Here are the options: \n"
                         "1. CD \n"
                         "2. Magazines \n"
                         "3. Scientific Journals \n"
                         "4. Books \n"
                         "Please enter the number corresponding to the item you want to query. \n")

        detailType = input(
            "What kind of detail do you know about this " + itemDict[item] + "? (author, studio, publisher, etc)\n"
                                                                             "Enter 'None' if you do not know any specific details \n")

        print(type(detailType))

        cur = conn.cursor()

        if item is "1":
            if detailType != "None":
                details = input("What is the value of the detail, " + detailType + "? \n")
                detailDict = {"type": detailType, "value": details}
                print(detailDict)
                findItemQuery = "SELECT * FROM Items NATURAL JOIN CD NATURAL JOIN CD_Detail WHERE " + detailType + "=:value"
                cur.execute(findItemQuery, detailDict)
            else:
                findItemQuery = "SELECT * FROM Items NATURAL JOIN CD NATURAL JOIN CD_Detail"
                cur.execute(findItemQuery)

        elif item is "2":
            if detailType != "None":
                details = input("What is the value of the detail, " + detailType + "? \n")
                detailDict = {"type": detailType, "value": details}
                print(detailDict)
                findItemQuery = "SELECT * FROM Items NATURAL JOIN Magazines NATURAL JOIN Magazine_Detail WHERE " + detailType + "=:value"
                cur.execute(findItemQuery, detailDict)
            else:
                findItemQuery = "SELECT * FROM Items NATURAL JOIN Magazines NATURAL JOIN Magazine_Detail"
                cur.execute(findItemQuery)

        elif item is "3":
            if detailType != "None":
                details = input("What is the value of the detail, " + detailType + "? \n")
                detailDict = {"type": detailType, "value": details}
                print(detailDict)
                findItemQuery = "SELECT * FROM Items NATURAL JOIN Scientific_Journals NATURAL JOIN SJ_Detail WHERE " + detailType + "=:value"
                cur.execute(findItemQuery, detailDict)
            else:
                findItemQuery = "SELECT * FROM Items NATURAL JOIN Scientific_Journals NATURAL JOIN SJ_Detail"
                cur.execute(findItemQuery)

        elif item is "4":
            if detailType != "None":
                details = input("What is the value of the detail, " + detailType + "? \n")
                detailDict = {"type": detailType, "value": details}
                print(detailDict)
                findItemQuery = "SELECT * FROM Items NATURAL JOIN Scientific_Journals NATURAL JOIN SJ_Detail WHERE " + detailType + "=:value"
                cur.execute(findItemQuery, detailDict)
            else:
                findItemQuery = "SELECT * FROM Items NATURAL JOIN Scientific_Journals NATURAL JOIN SJ_Detail"
                cur.execute(findItemQuery)

        rows = cur.fetchall()

        if rows:
            print("We do have the following item")
        else:
            print("Unfortunate we do not have the item")

        print(rows)

    if conn:
        conn.close()
        print('Closed database successfully')


def returnItem(cursor):
    item_id = input("Enter item ID of the item you are returning : ")
    cursor.execute("SELECT * FROM Items WHERE id = "+item_id)
    result = cursor.fetchone()
    if(result is None):
        print("There is no item with id : "+ item_id)
        return
    elif (result[3] != "borrowed"):
        print("No one is borrowing an item with id : "+item_id)
        return
    result = cursor.execute("SELECT * FROM Borrowing WHERE id = "+item_id)
    if(result is None):
        print("No one is borrowing an item with id : "+item_id)
        return

    cursor.execute("DELETE FROM Borrowing WHERE id = "+item_id)
    cursor.execute("UPDATE Items SET availability = 'available' WHERE id = "+item_id)
    conn.commit()

def findevent(cursor):
    attribute = input("Search by name, eid, type, description, room, audiences or eventDate? : ")
    if(attribute == "name" or attribute == "type" or attribute == "description" or attribute == "audiences" or attribute == "room"):
        search = input("Enter the "+ attribute +" you are searching for :")
        cursor.execute("SELECT * FROM Event_Detail NATURAL JOIN Events WHERE "+attribute+" LIKE '%"+search+"%'")
    elif(attribute == "eid"):
        search = input("Enter the event ID : ")
        cursor.execute("SELECT * FROM Event_Detail NATURAL JOIN Events WHERE eid = "+search)
    elif(attribute == "eventDate"):
        search = input("Enter the date (YYYY-MM-DD) : ")
        cursor.execute("SELECT * FROM Event_Detail NATURAL JOIN Events WHERE eventDate = "+search)
    else:
        print("Invalid attribute name")
        return
    
    result = cursor.fetchall()
    if(len(result) == 0):
        print("Event not found. ")
    for row in result:
        print("ID: "+str(row[5]))
        print("Name: "+str(row[1]))
        print("Type: "+str(row[2]))
        print("Audience: "+str(row[3]))
        print("Description: "+str(row[4]))
        print("Room: "+str(row[6]))
        print("Date: "+str(row[7]))
        print("Time: "+str(row[8]))
        print("--------------------")

def donate(cursor):
    with conn:
        while not int(item) in range(1, 4):
            item = input("How can I help you today? Here are the options: \n"
                                "1. CD \n"
                                "2. Magazines \n"
                                "3. Scientific Journals \n"
                                "4. Books \n"
                                "Please enter the number corresponding to the item you want to donate. \n")

        cursor.execute("SELECT MAX(id) FROM Items")
        new_id = str(cursor.fetchone()+1)
        if (item == 1):
            ISRC = input("Enter ISRC of the CD :")
            cursor.execute("SELECT * FROM CD_Detail WHERE ISRC = "+ISRC)
            ISRC_result = curosr.fetchall()
            
        #     if(len(ISRC_result) != 0):



        # elif(item == 2):
        # elif(item == 3):
        # elif(item == 4):
        
def register(cursor):
    with conn:
        cursor.execute("SELECT MAX(eid) FROM Events")
        new_id = int(cursor.fetchone()[0])
        
        if(new_id is None):
            new_id = 1
        else:
            new_id += 1
        
        event = input("Enter unique event type identification : ")
        cursor.execute("SELECT event FROM Event_Detail WHERE event = "+ event)
        if(cursor.fetchone() is None):
            cursor.execute("SELECT MAX(event) FROM Event_Detail")
            event = cursor.fetchone()
            if(new_id is None):
                event = 1
            else :
                event += 1
            
            name = makeSureNotNull("event name")
            event_type = makeSureNotNull("event type")
            audience = makeSureNotNull("audience")
            description = ifEmptySetToNULL("description")
            cursor.execute("INSERT INTO Event_Detail (event,name,type,audience,description) VALUES ("+str(event)+",'"+name+"','"+event_type+"','"+audience+"','"+description+"')")

        room = makeSureNotNull("room")
        eventDate = ifEmptySetToNULL("event date")
        eventTime = ifEmptySetToNULL("event time")

        cursor.execute("INSERT INTO Events (eid, event, room, eventDate, eventTime) VALUES ("+str(new_id)+","+str(event)+",'"+room+"','"+eventDate+"','"+eventTime+"')")
        print("Event with event id "+str(new_id)+" has been registered.")
        conn.commit()



cursor = conn.cursor()
while 1:
    command = input('Enter command or type /help\n')
    if command == "/help":
        displayHelp()
    elif command == "/borrow":
        borrow (cursor)
    elif command == "/finditem":
        finditem(cursor)
    elif command == "/return":
        returnItem(cursor)
    elif command == "/findevent":
        findevent(cursor)
    elif command == "/register":
        register(cursor)


    # else if command == "/volunteer":

    # else if command == "/request":
