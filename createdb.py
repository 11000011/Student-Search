#!/usr/bin/env python3
"""
A python3 script to generate sqlite database from iitk database
"""
import os
import sqlite3
import time

import search

def create_table(filename):
    """
    Creates table for a new db
    """
    print("Creating Tables")
    conn = sqlite3.connect(filename)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE PEOPLE
                         (ROLLNUM INT,
                         NAME VARCHAR(255),
                         PHONENUM VARCHAR(25),
                         MOBILENUM VARCHAR(25),
                         DEPT VARCHAR(255),
                         EMAIL VARCHAR(255),
                         HALL VARCHAR(255),
                         ROOM VARCHAR(255),
                         HOMETOWN VARCHAR(1023),
                         BLOODGROUP VARCHAR(25),
                         CATEGORY VARCHAR(15),
                         GENDER VARCHAR(15),
                         PROGRAM VARCHAR(25)
                         )''')
    conn.commit()
    conn.close()

def generate(start, end, filename):
    """
    Generates a db from the given set of parameters
    """
    if not os.path.isfile(filename):
        create_table(filename)
    conn = sqlite3.connect(filename)
    cursor = conn.cursor()
    students = []
    for student in range(start, end + 1):
        try:
            page = search.get_page(student)
            (perm, hometown, phone, mobile) = search.parse_home_address(page)
            (hall, room) = search.parse_address(page)
            data = (student, search.parse_name(page), phone, mobile, search.parse_department(page),
                    search.parse_mail(page), hall, room, hometown, search.parse_blood_group(page),
                    search.parse_category(page), search.parse_gender(page), search.parse_program(page)
                    )
            students.append(data)
        except:
            print("Failed at " + str(student))
        finally:
            print("Done with " + str(student))
            time.sleep(.3)
    cursor.executemany('INSERT INTO PEOPLE VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', students)
    conn.commit()
    conn.close()

def main():
    """
    The main function to call the rest of the code
    """
    start = int(input("Enter Start roll : "))
    end = int(input("Enter End roll: "))
    filename = input("Enter DB Name: ")
    generate(start, end, filename)

if __name__ == '__main__':
    main()
