import sqlite3

conn = sqlite3.connect('hito_login.db')
c=conn.cursor()



def data_entry():
    name=str(input("enter your name"))

    c.execute("SELECT email FROM User")
    data2 = c.fetchall()
    print(data2)
    while True:
        flag = True
        email = str(input("enter email"))

        for u_email in data2:
            existing_email = ''.join(u_email)
            if existing_email == email:
                flag = False
                print("The email is already register in the system. Please login or provide another email ")
                break

        if flag == True:
            break


    c.execute("SELECT username FROM User ")
    data1 = c.fetchall()
    print(data1)

    while True:
        flag = True
        username = str(input("enter username"))

        for u_name in data1:
            existing_username = ''.join(u_name)
            if existing_username == username:
                flag = False
                print("The username is already taken.please choose another ")
                break

        if flag == True:
            break

    while True:
        password = str(input("enter password"))
        if len(password)<8:
            print("Password shoul be combination of 8 character")
        else:
            break

    while True:
        phone = int(input("enter your phone number"))
        str_phone=str(phone)
        if len(str_phone)!=10:
            print("Please! Provide valid phone number")
        else:
            break

    address=str(input("enter address"))


    c.execute("INSERT INTO User  VALUES(?,?,?,?,?,? )",(name,email,phone,username,address,password))

    conn.commit()
    # c.close()
    # conn.close()


def login():
    c.execute("SELECT username,password FROM User")
    users = c.fetchall()
    print(users)
    while True:
        username=str(input("enter your username"))
        password=str(input("enter your password"))


        user_flag=False

        for user in users:
            if user[0]==username and user[1]==password:
                user_flag=True
                print("match found")
                break

        if user_flag==False:
            print("Either username or password is incorrect")
        else:
            break

    # c.execute("SELECT password FROM User")
    # pwd=c.fetchall()

    # user_flag=False
    # pwd_flag=False
    # for user in users:
    #     user_name=''.join(user)
    #     if user_name==username:
    #         user_flag=True
    #
    # if user_flag==False:
    #     print("Enter the valid username")
    #
    # for passes in pwd:
    #     entry_key=''.join(passes)
    #     if entry_key==password:
    #         pwd_flag==True
    #
    # if pwd_flag==False:
    #     print("your password is incorrect")
    #
    # if user_flag==True and pwd_flag==True:
    #     print(f'welcome {username} in hito ')




def data_read():
    c.execute("SELECT * FROM User")
    data=c.fetchall()
    for row in data:
        print(row)

# create_table()
login()
# data_read()
# login()