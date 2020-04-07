import sqlite3
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
    print("Search by title or ID")
    search_type = input("Enter ID or title : ")
    if(search_type == "ID"):
        id = input("Enter ID of an item : ")
        cursor.execute("SELECT * FROM Items WHERE id = "+ id)
    
    elif(search_type == "title"):
        title = input("Enter title of an item : ")
        cursor.execute("SELECT * FROM Items WHERE title LIKE '%"+ title+"%'")
    
    else:
        print("Invalid search type.")
        finditem(cursor)

    result = cursor.fetchall()
    if(len(result) == 0):
        print("Item not found.")
    iteration = 1
    for column in result:
        print("Item #"+str(iteration))
        print("id :" + str(column[0]))
        print("title :" + column[1])
        print("release_date :" + str(column[2]))
        print("avilability :" + str(column[3]) + "\n")
        iteration = iteration + 1

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

    #else if command == "/donate": 
        
    # else if command == "/findevent":

    # else if command == "/register":

    # else if command == "/volunteer":

    # else if command == "/request":