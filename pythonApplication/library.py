import sqlite3
from sqlite3 import Error
from prettytable import PrettyTable
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
    print("/finditem     : find item from the library")
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

        detailType = input("What kind of detail do you know about this " + itemDict[item] + "? (author, studio, publisher, etc)\n"
                                                                             "Enter 'None' if you do not know any specific details \n")

        if not detailType:
            detailType = "None"

        if item is "1":
            if detailType != "None":
                details = input("What is the value of the detail, " + detailType + "? \n")
                detailDict = {"type": detailType, "value": details}
                findItemQuery = "SELECT * FROM Items NATURAL JOIN CD NATURAL JOIN CD_Detail WHERE " + detailType + "=:value"
                cursor.execute(findItemQuery, detailDict)
            elif detailType == "" or detailType == "None":
                findItemQuery = "SELECT * FROM Items NATURAL JOIN CD NATURAL JOIN CD_Detail"
                cursor.execute(findItemQuery)

            rows = cursor.fetchall()

            if rows:
                print("We do have the following item")
                x = PrettyTable(["id","availability","ISRC","title","releaseDate","artist","studio","genre"])
                for row in rows:
                    x.add_row(row)
                print(x)
            else:
                print("Unfortunately we do not have the item")

        elif item is "2":
            if detailType != "None":
                details = input("What is the value of the detail, " + detailType + "? \n")
                detailDict = {"type": detailType, "value": details}
                print(detailDict)
                findItemQuery = "SELECT * FROM Items NATURAL JOIN Magazines NATURAL JOIN Magazine_Detail WHERE " + detailType + "=:value"
                cursor.execute(findItemQuery, detailDict)
            elif detailType == "" or detailType == "None":
                findItemQuery = "SELECT * FROM Items NATURAL JOIN Magazines NATURAL JOIN Magazine_Detail"
                cursor.execute(findItemQuery)

            rows = cursor.fetchall()

            if rows:
                print("We do have the following item")
                x = PrettyTable(["id","availability","ISSN","title","releaseDate","publisher","genre"])
                for row in rows:
                    x.add_row(row)
                print(x)
            else:
                print("Unfortunately we do not have the item")

        elif item is "3":
            if detailType != "None":
                details = input("What is the value of the detail, " + detailType + "? \n")
                detailDict = {"type": detailType, "value": details}
                findItemQuery = "SELECT * FROM Items NATURAL JOIN Scientific_Journals NATURAL JOIN SJ_Detail WHERE " + detailType + "=:value"
                cursor.execute(findItemQuery, detailDict)
            elif detailType == "" or detailType == "None":
                findItemQuery = "SELECT * FROM Items NATURAL JOIN Scientific_Journals NATURAL JOIN SJ_Detail"
                cursor.execute(findItemQuery)

            rows = cursor.fetchall()

            if rows:
                print("We do have the following item")
                x = PrettyTable(["id","availability","ISSN","title","releaseDate","field","researcher"])
                for row in rows:
                    x.add_row(row)
                print(x)
            else:
                print("Unfortunately we do not have the item")


        elif item is "4":
            if detailType != "None":
                details = input("What is the value of the detail, " + detailType + "? \n")
                detailDict = {"type": detailType, "value": details}
                findItemQuery = "SELECT * FROM Items NATURAL JOIN Books NATURAL JOIN Book_Detail WHERE " + detailType + "=:value"
                cursor.execute(findItemQuery, detailDict)
            elif detailType == "" or detailType == "None":
                findItemQuery = "SELECT * FROM Items NATURAL JOIN Books NATURAL JOIN Book_Detail"
                cursor.execute(findItemQuery)

            rows = cursor.fetchall()

            if rows:
                print("We do have the following item")
                x = PrettyTable(["id","availability","ISBN","name","releaseDate","author","publisher","genre","type"])
                for row in rows:
                    x.add_row(row)
                print(x)
            else:
                print("Unfortunately we do not have the item")


def borrow (cursor):

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

    print("User "+user_id+" has borrowed an item "+item_id)

    if conn:
        conn.commit()


def returnItem(cursor):
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

        cursor.execute("INSERT INTO Items(id) VALUES("+str(item_id)+")")
        if (item == str(1)):
            ISRC = input("Enter ISRC of the CD : ")
            cursor.execute("SELECT * FROM CD_Detail WHERE ISRC = '"+str(ISRC)+"'")

            if(cursor.fetchone() is None):
                title = makeSureNotNull("title")
                releaseDate = makeSureNotNull("release date(YYYY-MM-DD)")
                artist = makeSureNotNull("artist")
                studio = makeSureNotNull("studio")
                genre = ifEmptySetToNULL("genre")
                cursor.execute("INSERT INTO CD_Detail (ISRC, title, releaseDate, artist, studio, genre) VALUES('"+ISRC+"','"+title+"',DATE('"+releaseDate+"'),'"+artist+"','"+studio+"','"+genre+"')")

            cursor.execute("INSERT INTO CD (id, ISRC) VALUES ("+ str(item_id) +",'"+ISRC+"')")

        elif(item == str(2)):
            ISSN = input("Enter ISSN of the magazine : ")
            cursor.execute("SELECT * FROM Magazine_Detail WHERE ISSN = '"+str(ISSN)+"'")
            if(cursor.fetchone() is None):
                title = makeSureNotNull("title")
                releaseDate = makeSureNotNull("release date (YYYY-MM-DD)")
                publisher = makeSureNotNull("publisher")
                genre = ifEmptySetToNULL("genre")
                cursor.execute("INSERT INTO Magazine_Detail (ISSN, title, releaseDate, publisher, genre) VALUES('"+str(ISSN)+"','"+title+"',DATE('"+releaseDate+"'),'"+publisher+"','"+genre+"')")

            cursor.execute("INSERT INTO Magazines(id, ISSN) VALUES ("+ str(item_id) +",'"+ISSN+"')")

        elif(item == str(3)):
            ISSN = input("Enter ISSN of the Scientific Journal : ")
            cursor.execute("SELECT * FROM SJ_Detail WHERE ISSN = '"+str(ISSN)+"'")
            if(cursor.fetchone() is None):
                title = makeSureNotNull("title")
                releaseDate = makeSureNotNull("release date (YYYY-MM-DD)")
                field = makeSureNotNull("field")
                researcher = makeSureNotNull("genre")
                cursor.execute("INSERT INTO SJ_Detail (ISSN, title, releaseDate, field, researcher) VALUES('"+str(ISSN)+"','"+title+"',DATE('"+releaseDate+"'),'"+field+"','"+researcher+"')")

            cursor.execute("INSERT INTO Scientific_Journals (id, ISSN) VALUES ("+ str(item_id) +",'"+str(ISSN)+"')")

        elif(item == str(4)):
            ISBN = input("Enter ISBN of the Book : ")
            cursor.execute("SELECT * FROM Book_Detail WHERE ISBN = '"+str(ISBN)+"'")
            if(cursor.fetchone() is None):
                title = makeSureNotNull("title")
                author = makeSureNotNull("author")
                releaseDate = makeSureNotNull("release date (YYYY-MM-DD)")
                publisher = makeSureNotNull("publisher")
                genre = ifEmptySetToNULL("genre")
                book_type = "printed"
                cursor.execute("INSERT INTO Book_Detail (ISBN, title, releaseDate, author, publisher, genre, type) VALUES('"+str(ISBN)+"','"+title+"',DATE('"+releaseDate+"'),'"+author+"','"+publisher+"','"+genre+"','"+book_type+"')")

            cursor.execute("INSERT INTO Books (id, ISBN) VALUES ("+ str(item_id) +",'"+str(ISBN)+"')")

        print("Donation complete.")
        conn.commit()

def findEvent(cursor):
    attribute = input("Search by eid, name, type, description, room, audiences or eventDate? : ")
    if(attribute == "name" or attribute == "type" or attribute == "description" or attribute == "audiences" or attribute == "room"):
        search = input("Enter the "+ attribute +" you are searching for: ")
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
    event_id = input("Which event do you want to join? Specify by id. : ")
    cursor.execute("SELECT * FROM Events WHERE eid = " +event_id)
    result = cursor.fetchone()
    print(result)
    if result is None:
        print("Event ID "+event_id+" not found.")
        return

    user_id = input("Who wants to attend? Specify by user id : ")
    cursor.execute("SELECT pid FROM People WHERE pid = "+ user_id)
    result = cursor.fetchone()
    if result is None:
        print("User ID "+user_id+" not found.")
        return

    execution = "INSERT INTO Joining (eid, pid) VALUES ("+str(event_id)+","+str(user_id)+",0)"
    print("User "+user_id+" has joined an event "+event_id)

    conn.commit()

def volunteer(cursor):
    pidInput = input("Please enter your pid. (Enter \"None\" if you do not have a pid)\n")

    if pidInput != "None":
        checkPidQuery = "SELECT * FROM People WHERE pid=:pid"
        cursor.execute(checkPidQuery,{"pid":pidInput})

    rows = cursor.fetchone()

    # Person exists
    if rows:
        print(rows)
        print("Record exists already, adding to volunteer now")

        volunteerQuery = "INSERT INTO Personnels(pid, position, salary) VALUES (:pid, 'Volunteer', 0.00)"

        try:
            cursor.execute(volunteerQuery,{"pid":pidInput})
        except Error as e:
            print(e)

    else:
        firstName, lastName, email, phone, address = input("Please enter your first name, last name, email, phone, and address \n"
                                           "with a \"|\" entered between each field for separation \n").split("|")

        maxIDQuery = "SELECT MAX(pid) FROM People"
        cursor.execute(maxIDQuery)
        maxID = cursor.fetchone()

        if not all(maxID):
            print("maxID is empty")

        try:
            peopleQuery = "INSERT INTO People(pid,firstName,lastName,email,phone,address) VALUES (:pid,:fName,:lName,:email,:phone,:address)"
            cursor.execute(peopleQuery,{"pid":maxID[0]+1,"fName":firstName,"lName":lastName,"email":email,"phone":phone,"address":address})

            volunteerQuery = "INSERT INTO Personnels(pid, position, salary) VALUES (:pid, 'Volunteer', 0.00)"
            cursor.execute(volunteerQuery,{"pid":maxID[0]+1})

            print("Added new volunteer")

        except Error as e:
            print(e)

    if conn:
        conn.commit()


def askForHelp(cursor):
    uidInput = input("Please enter your uid?\n")
    descInput = input("What question do you want to ask our librarian?\n")

    maxRIDQuery = "SELECT MAX(rid) FROM Request"
    cursor.execute(maxRIDQuery)
    maxRID = cursor.fetchone()

    if not all(maxRID):
        print("maxRID is empty")

    try:
        requestByQuery = "INSERT INTO Request_by(pid, rid) VALUES (:pid, :rid)"
        cursor.execute(requestByQuery,{"pid":uidInput,"rid":maxRID[0]+1})

        requestQuery = "INSERT INTO Request(rid, description) VALUES (:rid, :description)"
        cursor.execute(requestQuery,{"rid":maxRID[0]+1,"description":descInput})

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
