#!/usr/bin/env python3
"""
A python3 script to search student info from iitk database
"""
import urllib.request
import time

def parse_name(page):
    """
    Extracts name from the page
    """
    name = page.split("<b>Name: </b>\\r\\n\\t\\t\\t\\t\\t\\t"
                      + "\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t")[1]
    name = name.split("\\r\\n")[0]
    return name

def parse_program(page):
    """
    Parses the program - B.Tech, M.Tech...
    """
    program = page.split("<b>Program: </b>\\r\\n\\t\\t\\t\\t\\t\\t\\t"
                         + "\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t")[1]
    program = program.split("\\r\\n")[0]
    return program

def parse_department(page):
    """
    Parses the department
    """
    dep = page.split("<b>Department: </b>\\r\\n\\t\\t\\t\\t\\t\\t\\t"
                     + "\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t")[1]
    dep = dep.split("\\r\\n")[0]
    return dep

def parse_address(page):
    """
    Gets the hostel info
    """
    hostelinf = page.split("<b>Hostel Info: </b>\\r\\n\\t\\t\\t\\t\\t\\t\\t\\t"
                           + "\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t")[1]
    hostelinf = hostelinf.split("\\r\\n")[0]
    hall = hostelinf.split(",")[0]
    room = hostelinf.split(",")[1]
    return hall, room

def parse_mail(page):
    """
    Gets mailing information
    """
    mail = page.split("mailto:")[1].split("\"")[0]
    return mail

def parse_blood_group(page):
    """
    Gets the blood group
    """
    bldgrp = page.split("<b> Blood Group:</b>\\r\\n\\t\\t\\t\\t\\t\\t\\t\\t\\t"
                        + "\\t\\t\\t\\t\\t\\t\\t\\t\\t")[1]
    bldgrp = bldgrp.split("\\r\\n")[0]
    return bldgrp

def parse_category(page):
    """
    Gets the category
    """
    cat = page.split("Category:</b>")[1].split("<")[0]
    return cat

def parse_gender(page):
    """
    Gets the gender
    """
    gend = page.split("<b> Gender:</b>\\r\\n\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t"
                      + "\\t\\t\\t\\t\\t\\t\\t")[1].split("\\r\\n")[0]
    return gend

def parse_father_name(page):
    """
    Extracts father's name
    """
    father_name = page.split("<b>Permanent Address :</b>")[1].split("<br>")[0]
    return father_name

def parse_home_address(page):
    """
    Extracts home address and number
    """
    perm = page.split("<b>Permanent Address :</b>")[1].split("<br>")[1]
    perm = perm.split("<br>")[0]
    arr = perm.split(",")
    index = len(arr)
    hometown = arr[index-3] + "," + arr[index-2]
    phone = page.split("Phone no:")[2].split("<")[0]
    mobile = page.split("Mobile no:")[2].split("<")[0]
    return (perm, hometown, phone, mobile)

def get_page(roll):
    """
    Gets the entire page from iitk servers
    """
    document = urllib.request.urlopen("http://oa.cc.iitk.ac.in/Oa/Jsp/"
                                      + "OAServices/IITk_SrchRes1.jsp?"
                                      + "typ=stud&numtxt="
                                      + str(roll) + "&sbm=Y")
    page = str(document.read())
    return page

def parse_data(page):
    """
    Parses data from the page
    """
    print("Name : " + parse_name(page))
    print("Gender : " + parse_gender(page))
    print("Email : " + parse_mail(page))
    print("Program : " + parse_program(page))
    print("Dep : " + parse_department(page))
    (hall, room) = parse_address(page)
    print("Hall : " + hall)
    print("Room : " + room)
    print("Blood Group : " + parse_blood_group(page))
    print("Category : " + parse_category(page))
    print("\n Father's Name : \n\t" + parse_father_name(page))
    (perm, hometown, phone, mobile) = parse_home_address(page)
    print("\n Address : \n\t" + perm)
    print("\n Hometown : \n\t" + hometown)
    print("\nPhone : " + phone)
    print("Mobile : " + mobile)

def main():
    """
    The main function to handle it
    """
    roll = input("Roll no : ")
    page = get_page(roll)
    print("Connection Successful")

    time.sleep(.3)
    print("Roll : " + roll)
    parse_data(page)


if __name__ == '__main__':
    main()
