
import sqlite3
import subprocess as sp

CONN_STRING = "moviedb.sqlite"

def get_connection(conn_string:str = CONN_STRING):
    try:
        conn = sqlite3.connect(conn_string)
        return conn
    except Exception as e:
        print("Unable to connect to Database")
        print(e)
        
def create_table():
    conn = get_connection()

    cursor = conn.cursor()

    query = '''
        CREATE TABLE IF NOT EXISTS movie(
            name VARCHAR(20) PRIMARY KEY, 
            actor VARCHAR(20), 
            actress VARCHAR(20),
            date DATE
        )
    '''
    try:
        cursor.execute(query)
        conn.commit()
    except Exception as e:
        print(e)
        print("Unable to create table")
    finally:
        conn.close()



def add_mov(name,actor,actress,date):
    conn = get_connection()

    cursor = conn.cursor()

    query = '''
        INSERT INTO movie( name, actor, actress, date )
                    VALUES ( ?,?,?,? )
    '''
    try:
        cursor.execute(query,(name,actor,actress,date))
        conn.commit()
    except Exception as e:
        print(e)
        print("Unable to add data ")
    finally:
        conn.close()



def get_movies():
    conn = get_connection()

    cursor = conn.cursor()

    query = '''
        SELECT *
        FROM movie
    '''
    try:
        cursor.execute(query)
        all_rows = cursor.fetchall()
        conn.commit()
    except Exception as e:
        print(e)
        print("Unable to get the data")
    finally:
        conn.close()

    return all_rows

def get_movie_by_act(name):
    conn = get_connection()

    cursor = conn.cursor()

    query = '''
        SELECT name, actor, actress, date
        FROM movie
        WHERE name = '{}'
    ''' .format(name)
    try:
        cursor.execute(query)
        all_rows = cursor.fetchall()
        return all_rows
        conn.commit()
    except Exception as e:
        print(e)
        print(f"Unable to get data for given name {name}")
    finally:
        conn.close()


def update_Mov(name,actor,actress,date):
    conn = get_connection()

    cursor = conn.cursor()

    query = '''
        UPDATE movie
        SET actor = ?, date = ?, actress = ?
        WHERE name = ?
    '''
    
    try:
        cursor.execute(query,(actor,date,actress,name))
        conn.commit()
    except Exception as e:
        print(e)
        print("Unable to update the data")
    finally:
        conn.close()


def delete_Mov(name):
    conn = get_connection()

    cursor = conn.cursor()

    query = '''
        DELETE
        FROM movie
        WHERE name = '{}'
    ''' .format(name)
    
    try:
        cursor.execute(query)
        conn.commit()
        cursor.execute("select * from movie")
        all_rows = cursor.fetchall()
        return all_rows
        conn.commit()
    except Exception as e:
        print(e)
        print("Unable to delete data")
    finally:
        conn.close()

    



create_table()



def add_data(name,actor,actress,date):
    add_mov(name,actor,actress,date)
def get_data():
    return get_movies()

def show_data():
    M1 = get_data()
    for M2 in M1:
        print(M2)

def show_data_by_name(name):
    M1 = get_movie_by_act(name)
    if not M1:
        print("No data found at roll",name)
    else:
        print (M1)

def select():
    sp.call('cls',shell=True)
    sel = input("1. Add data\n2.Show Data\n3.Search\n4.Update\n5.Delete\n6.Exit\n\n")

    
    if sel=='1':
        sp.call('cls',shell=True)
        name = input('movie name: ')
        actor = input('actor name: ')
        actress = input('actress name: ')
        date = input('date: ')
        add_data(name,actor,actress,date)
    elif sel=='2':
        sp.call('cls',shell=True)
        show_data()
        input("\n\npress enter to back:")
    elif sel=='3':
        sp.call('cls',shell=True)
        name=input('Enter movie name: ')
        show_data_by_name(name)
        input("\n\npress enter to back:")
    elif sel=='4':
        sp.call('cls',shell=True)
        name= input('Enter movie name: ')
        show_data_by_name(name)
        print()
        name = input('movie Name: ')
        actor = input('actor name: ')
        actress = input('actress name: ')
        date = input('date: ')
        update_Mov(name,actor,actress,date)
        input("\n\nYour data has been updated \npress enter to back:")
    elif sel=='5':
        sp.call('cls',shell=True)
        name = input('Enter Id: ')
        show_data_by_name(name)
        all_entries = delete_Mov(name)
        print(all_entries)
        input("\n\nYour data has been deleted \npress enter to back:")
    else:
        return 0;
    return 1;


while(select()):
    pass