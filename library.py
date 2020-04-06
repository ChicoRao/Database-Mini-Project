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
    user_id = input("Who wants to borrow? Specify by user id : ")
    cursor.execute("SELECT pid FROM Users WHERE pid = '%s'" %user_id)
    if cursor.fetchone() == None:
        print("User ID %s not found." %user_id) 
        return
    
    item_id = input("Which item to borrow? Specify by item id : ")
    cursor.execute("SELECT id FROM Items WHERE id = '%s'" %item_id)
    if cursor.fetchone() == None:
        print("Item ID %s not found." %item_id)
        return
    
    

while 1:
    command = input('Enter command or type /help\n')
    if command == "/help":
        displayHelp()
    elif command == "/borrow":
        cursor = conn.cursor() 
        borrow (cursor)
    

        # item_id = input("Specify item id.")
        # if user id not exsist
        # if not available:
        #     print("Book is currently unavailable")
        # else 
    # else if command == "/return":

    # else if command == "/donate": 

    # else if command == "/findevent":

    # else if command == "/register":

    # else if command == "/volunteer":

    # else if command == "/request":