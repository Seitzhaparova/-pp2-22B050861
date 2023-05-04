import psycopg2
import csv

conn = psycopg2.connect(
    host ="localhost",
    database = "suppliers",
    user = "postgres",
    password = "postgre",
)

cursor = conn.cursor() 

init_action = input('''Please 
                \n\ttype 'create' to CREATE contact
                \n\ttype 'read' to GET contact from phonebooks
                \n\ttype 'update' to CHANGE something 
                \n\ttype 'delete' to DELETE contact
                \n\ttype 'insert' to INSERT data from file 
       ---> : ''')


def func(action):
    if action == 'create':
        name = input('type your NAME: ')
        email = input('type your EMAIL: ')
        number = input('type your PHONE NUMBER: ')
        company = input('type your COMPANY: ')
        cursor.execute(f"insert into phonebooks (name, email, number, company) values ('{name}', '{email}', '{number}', '{company}');")
        conn.commit()
        print(f'\nYou have succesfully created contact of {name}\n')
        

    if action == 'read':
        name = input('Who?, type NAME:  ')
        cursor.execute(f"select * from phonebooks where name = '{name}';")
        conn.commit() 
        contacts = cursor.fetchall()
        for contact in contacts:
            print(f"\n\tNAME: id: {contact[0]} | NAME: {contact[1]} | EMAIL: {contact[2]} | NUMBER: {contact[3]} | COMPANY: {contact[4]}\n")


    if action == 'update':
        name = input('Who?, type NAME:  ')
        cursor.execute(f"select count(*) from phonebooks where name = '{name}'")
        result = cursor.fetchone()
        for r in result:
            if r>1:
                id = int(input('What ID:  '))
                a = input(f"What do u wanna CHANGE in {name}'s of {id} contact? Type 'email', 'number', 'company'! :   ")
                if a == 'email':
                    email = input('type email: ')
                    cursor.execute(f"update phonebooks set email = '{email}' where name = '{name}' and id='{id}';")
                    conn.commit()
                if a == 'number':
                    number = input('type number: ')
                    cursor.execute(f"update phonebooks set number = '{number}' where name = '{name}' and id='{id}';")
                    conn.commit()
                if a == 'company':
                    company = input('type company: ')
                    cursor.execute(f"update phonebooks set company = '{company}' where name = '{name}' and id='{id}';")
                    conn.commit()
            else:
                a = input(f"What do u wanna CHANGE in {name}'s contact? Type 'email', 'number', 'company'! :   ")
                if a == 'email':
                    email = input('type email: ')
                    cursor.execute(f"update phonebooks set email = '{email}' where name = '{name}';")
                    conn.commit()
                if a == 'number':
                    number = input('type number: ')
                    cursor.execute(f"update phonebooks set number = '{number}' where name = '{name}';")
                    conn.commit()
                if a == 'company':
                    company = input('type company: ')
                    cursor.execute(f"update phonebooks set company = '{company}' where name = '{name}';")
                    conn.commit()
        print('\nSuccessfully updated!\n')

    if action == 'delete':
        name = input('Who?, type NAME:  ')
        cursor.execute(f"select count(*) from phonebooks where name = '{name}'")
        result = cursor.fetchone()
        for r in result:
            if r>1:
                id = int(input('What ID:  '))
                cursor.execute(f"delete from phonebooks where name = '{name}' AND id= '{id}'")
            else:
                cursor.execute(f"delete from phonebooks where name = '{name}'")
        print('\nSuccessfully deleted!\n')
    if action == 'insert':
        f = open(r"C:\Users\User\Desktop\pp2\new_contacts.csv", 'r')
        reader = csv.reader(f)
        next(reader) # Skip the header row.
        for row in reader:
            cursor.execute(f"insert into phonebooks values (%s, %s, %s, %s, %s)", row)
        conn.commit()
        print('\nSuccessfully inserted!\n')
        
    act = input('''What else do you want to do? 
                    If NOTHING, push ENTER button.
                    If YES, please type 'create', 'read', 'update', 'delete' , 'insert' :  ''')
    if len(act) <= 3:
        print('\nOk, thank you!\n')
        cursor.close()
        conn.close() 
        return 
    else:
        return func(act)


func(init_action)