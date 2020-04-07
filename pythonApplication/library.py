# import sqlite3
# conn = sqlite3.connect('library.db')
#
# task = input("How can I help you today? Here are the options: \n"
#              "1. Find an item in the library \n"
#              "2. Borrow an item from the library \n"
#              "3. Return a borrowed item \n"
#              "4. Donate an item to the library \n"
#              "5. Find an event in the library \n"
#              "6. Register for an event in the library \n"
#              "7. Volunteer for the library \n"
#              "8. Ask for help from a librarian \n"
#              "Please enter the number corresponding to the task you want to perform. \n")
#
# if task is "1":
#     print("Task 1")
#     itemDict = {"1": "CD", "2": "Magazines", "3": "Scientific_Journals", "4": "Books"}
#     item = 0
#     cursor = conn.cursor()
#
#     with conn:
#
#         while not int(item) in range(1,4):
#             item = input("How can I help you today? Here are the options: \n"
#                          "1. CD \n"
#                          "2. Magazines \n"
#                          "3. Scientific Journals \n"
#                          "4. Books \n"
#                          "Please enter the number corresponding to the item you want to query. \n")
#
#         detailType = input("What kind of detail do you know about this " + itemDict[item] + "? (author, studio, publisher, etc)\n"
#                            "Enter 'None' if you do not know any specific details \n")
#
#         print(type(detailType))
#
#         cur = conn.cursor()
#
#         if item is "1":
#             if detailType != "None":
#                 details = input("What is the value of the detail, " + detailType + "? \n")
#                 detailDict = {"type": detailType, "value": details}
#                 print(detailDict)
#                 findItemQuery = "SELECT * FROM Items NATURAL JOIN CD NATURAL JOIN CD_Detail WHERE " + detailType + "=:value"
#                 cur.execute(findItemQuery, detailDict)
#             else:
#                 findItemQuery = "SELECT * FROM Items NATURAL JOIN CD NATURAL JOIN CD_Detail"
#                 cur.execute(findItemQuery)
#
#         elif item is "2":
#             if detailType != "None":
#                 details = input("What is the value of the detail, " + detailType + "? \n")
#                 detailDict = {"type": detailType, "value": details}
#                 print(detailDict)
#                 findItemQuery = "SELECT * FROM Items NATURAL JOIN Magazines NATURAL JOIN Magazine_Detail WHERE " + detailType + "=:value"
#                 cur.execute(findItemQuery, detailDict)
#             else:
#                 findItemQuery = "SELECT * FROM Items NATURAL JOIN Magazines NATURAL JOIN Magazine_Detail"
#                 cur.execute(findItemQuery)
#
#         elif item is "3":
#             if detailType != "None":
#                 details = input("What is the value of the detail, " + detailType + "? \n")
#                 detailDict = {"type": detailType, "value": details}
#                 print(detailDict)
#                 findItemQuery = "SELECT * FROM Items NATURAL JOIN Scientific_Journals NATURAL JOIN SJ_Detail WHERE " + detailType + "=:value"
#                 cur.execute(findItemQuery, detailDict)
#             else:
#                 findItemQuery = "SELECT * FROM Items NATURAL JOIN Scientific_Journals NATURAL JOIN SJ_Detail"
#                 cur.execute(findItemQuery)
#
#         elif item is "4":
#             if detailType != "None":
#                 details = input("What is the value of the detail, " + detailType + "? \n")
#                 detailDict = {"type": detailType, "value": details}
#                 print(detailDict)
#                 findItemQuery = "SELECT * FROM Items NATURAL JOIN Scientific_Journals NATURAL JOIN SJ_Detail WHERE " + detailType + "=:value"
#                 cur.execute(findItemQuery, detailDict)
#             else:
#                 findItemQuery = "SELECT * FROM Items NATURAL JOIN Scientific_Journals NATURAL JOIN SJ_Detail"
#                 cur.execute(findItemQuery)
#
#         rows = cur.fetchall()
#
#         if rows:
#             print("We do have the following item")
#         else:
#             print("Unfortunate we do not have the item")
#
#         print(rows)
#
#     if conn:
#         conn.close()
#         print('Closed database successfully')
#
#
# elif task is "2":
#     print("Task  2")
# elif task is "3":
#     print("Task 3")
# elif task is "4":
#     print("Task 4")
# elif task is "5":
#     print("Task 5")
# elif task is "6":
#     print("Task 6")
# elif task is "7":
#     print("Task 7")
# elif task is "8":
#     print("Task 8")
# else:
#     print("Please enter one of the numbers, will exit now")
#
#     if conn:
#         conn.close()
#         print('Closed database successfully')

import sqlite3
from sqlite3 import Error
conn = sqlite3.connect('library.db')


def displayHelp ():
    print("/finditem     : find item from the library")
    print("/borrow       : Borrow item from the library")
    print("/return       : Return item to the library")
    print("/donate       : Add item to the library")
    print("/findevent    : Find an event happening in library")
    print("/register     : Register an event in library")
    print("/volunteer    : Add volunteer personel to the library")
    print("/request      : Request for librarian\'s help")
    print("/quit         : Quit the program")

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
    itemDict = {"1": "CD", "2": "Magazines", "3": "Scientific_Journals", "4": "Books"}
    item = 0

    with conn:
        while not int(item) in range(1, 5):
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

        if item is "1":
            if detailType != "None":
                details = input("What is the value of the detail, " + detailType + "? \n")
                detailDict = {"type": detailType, "value": details}
                print(detailDict)
                findItemQuery = "SELECT * FROM Items NATURAL JOIN CD NATURAL JOIN CD_Detail WHERE " + detailType + "=:value"
                cursor.execute(findItemQuery, detailDict)
            else:
                findItemQuery = "SELECT * FROM Items NATURAL JOIN CD NATURAL JOIN CD_Detail"
                cursor.execute(findItemQuery)

        elif item is "2":
            if detailType != "None":
                details = input("What is the value of the detail, " + detailType + "? \n")
                detailDict = {"type": detailType, "value": details}
                print(detailDict)
                findItemQuery = "SELECT * FROM Items NATURAL JOIN Magazines NATURAL JOIN Magazine_Detail WHERE " + detailType + "=:value"
                cursor.execute(findItemQuery, detailDict)
            else:
                findItemQuery = "SELECT * FROM Items NATURAL JOIN Magazines NATURAL JOIN Magazine_Detail"
                cursor.execute(findItemQuery)

        elif item is "3":
            if detailType != "None":
                details = input("What is the value of the detail, " + detailType + "? \n")
                detailDict = {"type": detailType, "value": details}
                print(detailDict)
                findItemQuery = "SELECT * FROM Items NATURAL JOIN Scientific_Journals NATURAL JOIN SJ_Detail WHERE " + detailType + "=:value"
                cursor.execute(findItemQuery, detailDict)
            else:
                findItemQuery = "SELECT * FROM Items NATURAL JOIN Scientific_Journals NATURAL JOIN SJ_Detail"
                cursor.execute(findItemQuery)

        elif item is "4":
            if detailType != "None":
                details = input("What is the value of the detail, " + detailType + "? \n")
                detailDict = {"type": detailType, "value": details}
                print(detailDict)
                findItemQuery = "SELECT * FROM Items NATURAL JOIN Scientific_Journals NATURAL JOIN SJ_Detail WHERE " + detailType + "=:value"
                cursor.execute(findItemQuery, detailDict)
            else:
                findItemQuery = "SELECT * FROM Items NATURAL JOIN Scientific_Journals NATURAL JOIN SJ_Detail"
                cursor.execute(findItemQuery)

        rows = cursor.fetchall()

        if rows:
            print("We do have the following item")
        else:
            print("Unfortunate we do not have the item")

        print(rows)


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

def register(cursor):
    event = input("What is the event are you registering for? \n")

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
        borrow (cursor)
    elif command == "/finditem":
        finditem(cursor)
    elif command == "/return":
        returnItem(cursor)
    # elif command == "/donate":

    # elif command == "/findevent":

    elif command == "/register":
        register(cursor)
    elif command == "/volunteer":
        volunteer(cursor)
    elif command == "/request":
        askForHelp(cursor)
    elif command == "/quit":
        if conn:
            conn.close();
            print("Database closed successfully")
        break
