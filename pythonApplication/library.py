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