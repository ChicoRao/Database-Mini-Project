import sqlite3
from sqlite3 import Error
from datetime import date
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
    print("/finditem     : Find item from the library")
    print("/borrow       : Borrow item from the library")
    print("/return       : Return item to the library")
    print("/donate       : Add item to the library")
    print("/findevent    : Find an event happening in library")
    print("/register     : Register an event in library")
    print("/volunteer    : Add volunteer personnel to the library")
    print("/request      : Request for librarian\'s help")
    print("/quit         : Quit the program")

def finditem (cursor):
    itemDict = {"1": "CD", "2": "Magazines", "3": "Scientific_Journals", "4": "Books"}
    item = 0

    with conn:
        while not int(item) in range(1, 5):
            item = input("Which item are you looking for? Here are the options: \n"
                         "1. CD \n"
                         "2. Magazines \n"
                         "3. Scientific Journals \n"
                         "4. Books \n"
                         "Please enter the number corresponding to the item you want to query. \n")

        if item == "1":

            detailType = input("What kind of detail do you know about this " + itemDict[item] + "? (id,availability,ISRC,title,releaseDate,artist,studio,genre)\n"
                                                                                 "Enter 'None' if you do not know any specific details \n")

            if not detailType:
                detailType = "None"

            if detailType != "None":
                details = input("What is the value of the detail, " + detailType + "? \n")
                findItemQuery = "SELECT * FROM Items NATURAL JOIN CD NATURAL JOIN CD_Detail WHERE " + detailType + " LIKE '%"+details+"%'"
                cursor.execute(findItemQuery)
            else:
                findItemQuery = "SELECT * FROM Items NATURAL JOIN CD NATURAL JOIN CD_Detail"
                cursor.execute(findItemQuery)

            rows = cursor.fetchall()

            if rows:
                print("We do have the following item\n")
                dash = '-' * 95
                print(dash)
                print('{:<4s}{:<13s}{:<20s}{:<12s}{:<12s}{:<15s}{:<12s}{:<12s}'.format("id","availability","ISRC","title","releaseDate","artist","studio","genre"))
                print(dash)
                for row in rows:
                    print('{:<4s}{:<13s}{:<20s}{:<12s}{:<12s}{:<15s}{:<12s}{:<12s}'.format(str(row[0]),row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
            else:
                print("Unfortunately we do not have the item")

        elif item == "2":

            detailType = input("What kind of detail do you know about this " + itemDict[item] + "? (id,availability,ISSN,title,releaseDate,publisher,genre)\n"
                                                                                 "Enter 'None' if you do not know any specific details \n")

            if not detailType:
                detailType = "None"

            if detailType != "None":
                details = input("What is the value of the detail, " + detailType + "? \n")
                findItemQuery = "SELECT * FROM Items NATURAL JOIN Magazines NATURAL JOIN Magazine_Detail WHERE " + detailType + " LIKE '%"+details+"%'"
                cursor.execute(findItemQuery)
            else:
                findItemQuery = "SELECT * FROM Items NATURAL JOIN Magazines NATURAL JOIN Magazine_Detail"
                cursor.execute(findItemQuery)

            rows = cursor.fetchall()

            if rows:
                print("We do have the following item\n")
                dash = '-' * 89
                print(dash)
                print('{:<4s}{:<13s}{:<20s}{:<12s}{:<12s}{:<15s}{:<12s}'.format("id","availability","ISSN","title","releaseDate","publisher","genre"))
                print(dash)
                for row in rows:
                    print('{:<4s}{:<13s}{:<20s}{:<12s}{:<12s}{:<15s}{:<12s}'.format(str(row[0]),row[1],row[2],row[3],row[4],row[5],row[6]))
            else:
                print("Unfortunately we do not have the item")

        elif item == "3":

            detailType = input("What kind of detail do you know about this " + itemDict[item] + "? (id,availability,ISSN,title,releaseDate,field,researcher)\n"
                                                                                 "Enter 'None' if you do not know any specific details \n")

            if not detailType:
                detailType = "None"

            if detailType != "None":
                details = input("What is the value of the detail, " + detailType + "? \n")
                findItemQuery = "SELECT * FROM Items NATURAL JOIN Scientific_Journals NATURAL JOIN SJ_Detail WHERE " + detailType + " LIKE '%"+details+"%'"
                cursor.execute(findItemQuery)
            else:
                findItemQuery = "SELECT * FROM Items NATURAL JOIN Scientific_Journals NATURAL JOIN SJ_Detail"
                cursor.execute(findItemQuery)

            rows = cursor.fetchall()

            if rows:
                print("We do have the following item\n")
                dash = '-' * 96
                print(dash)
                print('{:<4s}{:<13s}{:<13s}{:<23s}{:<15s}{:<13s}{:<12s}'.format("id","availability","ISSN","title","releaseDate","field","researcher"))
                print(dash)
                for row in rows:
                    print('{:<4s}{:<13s}{:<13s}{:<23s}{:<15s}{:<13s}{:<12s}'.format(str(row[0]),row[1],row[2],row[3],row[4],row[5],row[6]))
            else:
                print("Unfortunately we do not have the item")


        elif item == "4":

            detailType = input("What kind of detail do you know about this " + itemDict[item] + "? (id,availability,ISBN,title,releaseDate,author,publisher,genre,type)\n"
                                                                                 "Enter 'None' if you do not know any specific details \n")

            if not detailType:
                detailType = "None"

            if detailType != "None":
                details = input("What is the value of the detail, " + detailType + "? \n")
                findItemQuery = "SELECT * FROM Items NATURAL JOIN Books NATURAL JOIN Book_Detail WHERE " + detailType + " LIKE '%"+details+"%'"
                cursor.execute(findItemQuery)
            else:
                findItemQuery = "SELECT * FROM Items NATURAL JOIN Books NATURAL JOIN Book_Detail"
                cursor.execute(findItemQuery)

            rows = cursor.fetchall()

            if rows:
                print("We do have the following item\n")
                dash = '-' * 110
                print(dash)
                print('{:<4s}{:<13s}{:<20s}{:<12s}{:<12s}{:<16s}{:<13s}{:<12s}{:<9s}'.format("id","availability","ISBN","title","releaseDate","author","publisher","genre","type"))
                print(dash)
                for row in rows:
                    print('{:<4s}{:<13s}{:<20s}{:<12s}{:<12s}{:<16s}{:<13s}{:<12s}{:<9s}'.format(str(row[0]),row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))
            else:
                print("Unfortunately we do not have the item")


def borrow (cursor):

    with conn:
        while(True):
            item_id = input("Which item would you like to borrow? Specify by item id: \n"
                        "If you do not know the item id, type \"Search\" to perform a search to find the id\n")
            if item_id == "Search":
                finditem(cursor)
            elif item_id:
                break

        cursor.execute("SELECT * FROM Items WHERE id=:id",{"id":item_id})

        result = cursor.fetchone()

        if result is None:
            print("Item ID "+item_id+" not found.")
            return
        elif (result[1] != "available"):
            print("The item is not available.")
            return

        cursor.execute("SELECT * FROM Items NATURAL JOIN Books NATURAL JOIN Book_Detail WHERE id=:id",{"id":item_id})
        bookCheckResult = cursor.fetchone()

        if bookCheckResult:
            if bookCheckResult[8] == "online":
                print("Cannot borrow an online book")
                return

        user_id = input("Who wants to borrow? Specify by user id : ")
        cursor.execute("SELECT pid FROM Users WHERE pid=:uid",{"uid":user_id})
        result = cursor.fetchone()
        if user_id is None:
            print("User ID "+user_id+" not found.")
            return

        todayDate = date.today()

        try:
            cursor.execute("UPDATE Items SET availability = 'borrowed' WHERE id=:id",{"id":item_id})
        except Error as e:
            print(e)

        borrowQuery = "INSERT INTO Borrowing (id, uid, dateBorrowed, fine) VALUES (:id,:uid,:dateBorrowed,0)"

        try:
            cursor.execute(borrowQuery,{"id":item_id,"uid":user_id,"dateBorrowed":todayDate})
        except Error as e:
            print(e)

    if conn:
        conn.commit()
        print("User "+user_id+" has borrowed an item "+item_id)


def returnItem(cursor):

    with conn:

        item_id = input("Enter item ID of the item you are returning : ")
        cursor.execute("SELECT * FROM Items WHERE id =:id",{"id":item_id})
        result = cursor.fetchone()

        if(result is None):
            print("There is no item with id : "+ item_id)
            return
        elif (result[1] != "borrowed"):
            print("No one is borrowing an item with id : "+item_id)
            return

        result = cursor.execute("SELECT * FROM Borrowing WHERE id=:id AND dateReturned IS NULL",{"id":item_id})

        if(result is None):
            print("No one is borrowing an item with id: "+item_id)
            return

        todayDate = date.today()

        try:
            cursor.execute("UPDATE Borrowing SET dateReturned=:todayDate WHERE id=:id AND dateReturned IS NULL",{"todayDate":todayDate,"id":item_id})
            cursor.execute("UPDATE Items SET availability = 'available' WHERE id =:id",{"id":item_id})
        except Error as e:
            print(e)

    if conn:
        conn.commit()
        print("You have successfully returned the item")

def donate(cursor):
    with conn:
        item = "0"
        while not int(item) in range(1, 5):
            item = input("How can I help you today? Here are the options: \n"
                                "1. CD \n"
                                "2. Magazines \n"
                                "3. Scientific Journals \n"
                                "4. Books \n"
                                "Please enter the number corresponding to the item you want to donate. \n")

        cursor.execute("SELECT MAX(id) FROM Items")
        new_id = cursor.fetchone()
        if(new_id is None):
            item_id = 1
        else:
            item_id = new_id[0] + 1

        try:
            cursor.execute("INSERT INTO Items(id) VALUES(:id)",{"id":item_id})
        except Error as e:
            print(e)

        if (item == str(1)):
            ISRC = input("Enter ISRC of the CD : ")
            cursor.execute("SELECT * FROM CD_Detail WHERE ISRC =:ISRC",{"ISRC":ISRC})

            if(cursor.fetchone() is None):
                title = makeSureNotNull("title")
                releaseDate = makeSureNotNull("release date(YYYY-MM-DD)")
                artist = makeSureNotNull("artist")
                studio = makeSureNotNull("studio")
                genre = ifEmptySetToNULL("genre")

                try:
                    cursor.execute("INSERT INTO CD_Detail (ISRC, title, releaseDate, artist, studio, genre) VALUES(:ISRC,:title,DATE(:rDate),:artist,:studio,:genre)",{"ISRC":ISRC,"title":title,"rDate":releaseDate,"artist":artist,"studio":studio,"genre":genre})
                    print("Donation complete.")
                except Error as e:
                    print(e)

            try:
                cursor.execute("INSERT INTO CD (id, ISRC) VALUES (:id,:ISRC)",{"id":item_id,"ISRC":ISRC})
            except Error as e:
                print(e)

        elif(item == str(2)):
            ISSN = input("Enter ISSN of the magazine : ")
            cursor.execute("SELECT * FROM Magazine_Detail WHERE ISSN =:ISSN",{"ISSN":ISSN})
            if(cursor.fetchone() is None):
                title = makeSureNotNull("title")
                releaseDate = makeSureNotNull("release date (YYYY-MM-DD)")
                publisher = makeSureNotNull("publisher")
                genre = ifEmptySetToNULL("genre")

                try:
                    cursor.execute("INSERT INTO Magazine_Detail (ISSN, title, releaseDate, publisher, genre) VALUES(:ISSN,:title,DATE(:rDate),:publisher,:genre)",{"ISSN":ISSN,"title":title,"rDate":releaseDate,"publisher":publisher,"genre":genre})
                    print("Donation complete.")
                except Error as e:
                    print(e)

            try:
                cursor.execute("INSERT INTO Magazines(id, ISSN) VALUES (:id,:ISSN)",{"id":item_id,"ISSN":ISSN})
            except Error as e:
                print(e)

        elif(item == str(3)):
            ISSN = input("Enter ISSN of the Scientific Journal : ")
            cursor.execute("SELECT * FROM SJ_Detail WHERE ISSN =:ISSN",{"ISSN":ISSN})
            if(cursor.fetchone() is None):
                title = makeSureNotNull("title")
                releaseDate = makeSureNotNull("release date (YYYY-MM-DD)")
                field = makeSureNotNull("field")
                researcher = makeSureNotNull("genre")

                try:
                    cursor.execute("INSERT INTO SJ_Detail (ISSN, title, releaseDate, field, researcher) VALUES(:ISSN,:title,DATE(:rDate),:field,:researcher)",{"ISSN":ISSN,"title":title,"rDate":releaseDate,"field":field,"reseacher":researcher})
                except Error as e:
                    print(e)

            try:
                cursor.execute("INSERT INTO Scientific_Journals (id, ISSN) VALUES (:id,:ISSN)",{"id":item_id,"ISSN":ISSN})
                print("Donation complete.")
            except Error as e:
                print(e)

        elif(item == str(4)):
            ISBN = input("Enter ISBN of the Book : ")
            cursor.execute("SELECT * FROM Book_Detail WHERE ISBN =:ISBN",{"ISBN":ISBN})
            if(cursor.fetchone() is None):
                title = makeSureNotNull("title")
                author = makeSureNotNull("author")
                releaseDate = makeSureNotNull("release date (YYYY-MM-DD)")
                publisher = makeSureNotNull("publisher")
                genre = ifEmptySetToNULL("genre")
                book_type = "printed"

                try:
                    cursor.execute("INSERT INTO Book_Detail (ISBN, title, releaseDate, author, publisher, genre, type) VALUES(:ISBN,:title,DATE(:rDate),:author,:publisher,:genre,:type)",{"ISBN":ISBN,"title":title,"rDate":releaseDate,"author":author,"publisher":publisher,"genre":genre,"type":book_type})
                except Error as e:
                    print(e)

            try:
                cursor.execute("INSERT INTO Books (id, ISBN) VALUES (:id,:ISBN)",{"id":item_id,"ISBN":ISBN})
                print("Donation complete.")
            except Error as e:
                print(e)

        conn.commit()

def findEvent(cursor):
    with conn:

        attribute = input("Search by eid, name, type, description, room, audiences or eventDate? : ")
        if(attribute == "name" or attribute == "type" or attribute == "description" or attribute == "audiences" or attribute == "room"):
            search = input("Enter the "+ attribute +" you are searching for: ")
            cursor.execute("SELECT * FROM Event_Detail NATURAL JOIN Events WHERE "+attribute+" LIKE '%"+search+"%'")
        elif(attribute == "eid"):
            search = input("Enter the event ID : ")
            cursor.execute("SELECT * FROM Event_Detail NATURAL JOIN Events WHERE eid =:search",{"search":search})
        elif(attribute == "eventDate"):
            search = input("Enter the date (YYYY-MM-DD) : ")
            cursor.execute("SELECT * FROM Event_Detail NATURAL JOIN Events WHERE eventDate =:search",{"search":search})
        else:
            print("Invalid attribute name")
            return

        result = cursor.fetchall()
        if(len(result) == 0):
            print("Event not found. ")
        for row in result:
            print("--------------------")
            print("ID:          "+str(row[5]))
            print("Name:        "+str(row[1]))
            print("Type:        "+str(row[2]))
            print("Audience:    "+str(row[3]))
            print("Description: "+str(row[4]))
            print("Room:        "+str(row[6]))
            print("Date:        "+str(row[7]))
            print("Time:        "+str(row[8]))
            print("--------------------")

def joinEvent(cursor):
    with conn:
        while(True):
            event_id = input("Which event do you want to join? Specify by id. : \n"
                        "If you do not know the event id, type \"Search\" to perform a search to find the id\n")
            if event_id == "Search":
                findEvent(cursor)
            elif event_id:
                break

        cursor.execute("SELECT * FROM Events WHERE eid =:eid",{"eid":event_id})
        result = cursor.fetchone()

        if result is None:
            print("Event ID "+event_id+" not found.")
            return

        user_id = input("Who wants to attend? Specify by user id : \n")
        cursor.execute("SELECT pid FROM People WHERE pid =:pid",{"pid":user_id})
        result = cursor.fetchone()
        if result is None:
            print("User ID "+user_id+" not found.")
            return

        try:
            execution = "INSERT INTO Joining (eid, pid) VALUES (:eid,:pid)"
            cursor.execute(execution,{"eid":event_id,"pid":user_id})
            print("User "+user_id+" has joined an event "+event_id)
        except Error as e:
            print(e)

    if conn:
        conn.commit()

def volunteer(cursor):

    with conn:
        pidInput = input("Please enter your pid. (Enter \"None\" if you do not have a pid)\n")

        if pidInput != "None":
            checkPidQuery = "SELECT * FROM People WHERE pid=:pid"
            cursor.execute(checkPidQuery,{"pid":pidInput})

        rows = cursor.fetchone()

        # Person exists
        if rows:

            checkPersonnelQuery = "SELECT * FROM Personnel WHERE pid=:pid"
            cursor.execute(checkPidQuery,{"pid":pidInput})
            row = cursor.fetchone()

            if row:
                print("Already registered as a personnel, will quit now")
                return

            volunteerQuery = "INSERT INTO Personnels(pid, position, salary) VALUES (:pid, 'Volunteer', 0.00)"

            try:
                cursor.execute(volunteerQuery,{"pid":pidInput})
            except Error as e:
                print(e)

            print("Added new volunteer")

        else:
            firstName, lastName, email, phone, address = input("Please enter your first name, last name, email, phone, and address \n"
                                               "with a \"|\" entered between each field for separation \n").split("|")

            maxIDQuery = "SELECT MAX(pid) FROM People"
            cursor.execute(maxIDQuery)
            maxID = cursor.fetchone()

            pid = 0

            if(maxID is None):
                pid = 1
            else:
                pid = maxID[0] + 1

            try:
                peopleQuery = "INSERT INTO People(pid,firstName,lastName,email,phone,address) VALUES (:pid,:fName,:lName,:email,:phone,:address)"
                cursor.execute(peopleQuery,{"pid":pid,"fName":firstName,"lName":lastName,"email":email,"phone":phone,"address":address})

                volunteerQuery = "INSERT INTO Personnels(pid, position, salary) VALUES (:pid, 'Volunteer', 0.00)"
                cursor.execute(volunteerQuery,{"pid":pid})

                print("Added new volunteer")

            except Error as e:
                print(e)

    if conn:
        conn.commit()


def askForHelp(cursor):
    with conn:
        uidInput = input("Please enter your uid?\n")
        descInput = input("What question do you want to ask our librarian?\n")

        maxRIDQuery = "SELECT MAX(rid) FROM Request"
        cursor.execute(maxRIDQuery)
        maxRID = cursor.fetchone()

        rid = 0

        if(maxRID is None):
            rid = 1
        else:
            rid = maxRID[0] + 1

        try:

            requestQuery = "INSERT INTO Request(rid, description) VALUES (:rid, :description)"
            cursor.execute(requestQuery,{"rid":rid,"description":descInput})

            requestByQuery = "INSERT INTO Request_by(pid, rid) VALUES (:pid, :rid)"
            cursor.execute(requestByQuery,{"pid":uidInput,"rid":rid})

            print("Asking for help")

        except Error as e:
            print(e)

    if conn:
        conn.commit()

while 1:
    cursor = conn.cursor()
    command = input('Enter command or type /help\n')
    if command == "/help":
        displayHelp()
    elif command == "/borrow":
        borrow(cursor)
    elif command == "/finditem":
        finditem(cursor)
    elif command == "/return":
        returnItem(cursor)
    elif command == "/donate":
        donate(cursor)
    elif command == "/findevent":
        findEvent(cursor)
    elif command == "/register":
        joinEvent(cursor)
    elif command == "/volunteer":
        volunteer(cursor)
    elif command == "/request":
        askForHelp(cursor)
    elif command == "/quit":
        if conn:
            conn.close();
            print("Database closed successfully")
        break
