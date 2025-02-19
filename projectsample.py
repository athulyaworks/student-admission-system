import mysql.connector
from tabulate import tabulate
mydb=mysql.connector.connect(host="localhost",user="root",password="",database="admission_table")
mycursor=mydb.cursor()
option=0
while True:
    try:
        print(' +-----------+ ')
        print(' |1.Admission|')
        print(' |2.Courses  |')
        print(' |3.Exit     |')
        print(' +-----------+')

        while True:
            try:
                option = int(input('Enter option: '))
                while option <= 0 or option > 3:
                    print('Please enter a valid option (1, 2, or 3).')
                    option = int(input('Enter option: '))
                break  
            except ValueError:
                print("Invalid input! Please enter a number.")

        
        if option == 1:
            while True:
                print('+------------------+')
                print('|1.New Admission   |')
                print('|2.Edit Admission  |')
                print('|3.Delete          |')
                print('|4.View            |')
                print('|5.Back            |')
                print('+------------------+')

                while True:
                    try:
                        opt = int(input('Select option: '))
                        if 0 < opt <= 5:
                            break  
                        else:
                            print("Please enter a valid option!")  
                    except ValueError:
                        print("Invalid input! Please enter a number.")  


                # New Admission 
                if opt == 1:
                    while True:
                        print('ENTER')
                        print('-----------')

                        
                        while True:
                            name = input('Enter name: ')
                            if not name:
                                print('You must enter a value')
                            else:
                                break

                        
                        while True:
                            phone = input('Enter phone: ')
                            if not phone:
                                print('You must enter a value')
                            else:
                                break

                        
                        while True:
                            gmail = input('Enter Gmail: ')
                            if not gmail:
                                print('You must enter a value')
                            else:
                                break

                        
                        while True:
                            district = input('Enter district: ')
                            if not district:
                                print('You must enter a value')
                            else:
                                break

                        mycursor.execute("SELECT * FROM course")
                        myresult = mycursor.fetchall()
                        print(tabulate(myresult, headers=['id', 'name', 'fees', 'duration'], tablefmt='psql'))

                        while True:
                            try:
                                c_id = int(input('Enter course id: '))
                                for x in myresult:
                                    if c_id == x[0]:
                                        sql = "INSERT INTO admission(name, phone, gmail, district, course) VALUES (%s, %s, %s, %s, %s)"
                                        val = (name, phone, gmail, district, x[1])
                                        mycursor.execute(sql, val)
                                        mydb.commit()
                                        print('Added successfully')
                                        break
                                else:
                                    print('ID not found!!')
                                    continue
                                break  
                            except ValueError:
                                print('Invalid input! Please enter a valid course ID.')
                        break  
                    break  

                if int(opt) == 2:
                    # EDIT ADMISSION
                    op=1
                    while op<=5:
                        print('Edit')
                        print('+---------------------+')
                        print('|0.Viewop(id,name)    |')
                        print('|1.name               |')
                        print('|2.phone              |')
                        print('|3.gmail              |')
                        print('|4.district           |')            
                        print('|5.course             |')
                        print('+---------------------+')
                        while True:
                            try:
                                op=int(input("Enter your option:"))
                                if op>=0 and op<=5:
                                    break
                                else:
                                    print("Invalid option")
                            except:
                                print("invalid")
                        if op == 0:
                            # View name and ID
                            print("ID  NAME")
                            mycursor.execute("SELECT id,name FROM admission")
                            myresult = mycursor.fetchall()
                            print(tabulate(myresult, headers=['ID', 'NAME'], tablefmt='psql'))
                            break  

                        elif op == 1: 
                            # Edit Name
                            print("Edit name")
                            mycursor.execute("SELECT id FROM admission")
                            adm = mycursor.fetchall()
                            while True:
                                try:
                                    id1 = int(input("Enter the ID of the student to be edited: "))
                                    for x in adm:
                                        if id1 == x[0]:
                                            new_name = input("Enter the new name: ")
                                            while not new_name:
                                                print("You must enter a value")
                                                new_name = input("Enter the new name: ")                                          
                                            sql = "UPDATE admission SET name = %s WHERE id = %s"
                                            val = (new_name, id1)
                                            mycursor.execute(sql, val)
                                            mydb.commit()
                                            print("Name successfully updated!!")
                                            break
                                    else:
                                        print("ID not found")
                                except ValueError:
                                    print("Invalid ID! Please enter a valid numeric ID.") 
                                try:
                                    if id1 == x[0]:
                                        break
                                except:
                                    pass  

                        elif op == 2: 
                            # Edit Phone Number
                            print("Edit phone number")
                            mycursor.execute("SELECT id FROM admission")
                            adm = mycursor.fetchall()
                            while True:
                                try:
                                    id1 = int(input("Enter the ID of the student to be edited: "))
                                    for x in adm:
                                        if id1 == x[0]:
                                            new_ph = input("Enter the new number: ")
                                            while not new_ph:
                                                print("You must enter a value")
                                                new_ph = input("Enter the new number: ")                                          
                                            sql = "UPDATE admission SET phone = %s WHERE id = %s"
                                            val = (new_ph, id1)
                                            mycursor.execute(sql, val)
                                            mydb.commit()
                                            print("Number successfully updated!!")
                                            break
                                    else:
                                        print("ID not found")
                                except ValueError:
                                    print("Invalid ID! Please enter a valid numeric ID.")
                                try:   
                                    if id1 == x[0]:
                                        break
                                except:
                                    pass
                            break
                        elif op == 3:
                            # Edit Gmail
                            print("Edit Gmail")
                            mycursor.execute("SELECT id FROM admission")
                            adm = mycursor.fetchall()
                            while True:
                                try:                             
                                    id1 = int(input("Enter the ID of the student to be edited: "))
                                    for x in adm:
                                        if id1 == x[0]:
                                            new_id = input("Enter the new Gmail ID: ")
                                            while not new_id:
                                                print("You must enter a value")
                                                new_id = input("Enter the new Gmail ID: ")
                                            sql = "UPDATE admission SET gmail=%s WHERE id=%s"
                                            val = (new_id, id1)
                                            mycursor.execute(sql, val)
                                            mydb.commit()
                                            print("Successfully edited!!")
                                            break
                                    else:
                                        print("ID not found")
                                except ValueError:
                                    print("Invalid ID! Please enter a valid numeric ID.")
                                try:
                                    if id1 == x[0]:
                                        break
                                except:
                                    pass
                        
                        elif op == 4:
                            # Edit District
                            print("Edit District")
                            mycursor.execute("SELECT id FROM admission")
                            adm = mycursor.fetchall()
                            while True:
                                try:                             
                                    id1 = int(input("Enter the ID of the student to be edited: "))
                                    for x in adm:
                                        if id1 == x[0]:
                                            new_disct = input("Enter the new district: ")                                   
                                            while not new_disct:
                                                print("You must enter a value")
                                                new_disct = input("Enter District: ")
                                            sql = "UPDATE admission SET district=%s WHERE id=%s"
                                            val = (new_disct, id1)
                                            mycursor.execute(sql, val)
                                            mydb.commit()
                                            print("Successfully edited!!")
                                            break
                                    else:
                                        print("ID not found")
                                except ValueError:
                                    print("Invalid ID! Please enter a valid numeric ID.")
                                try:
                                    if id1 == x[0]:
                                        break
                                except:
                                    pass
                        
                        elif op == 5:
                            # Edit Enrolled Course
                            print("Edit enrolled course")
                            mycursor.execute("SELECT id FROM admission")
                            adm = mycursor.fetchall()
                            while True:
                                try:
                                    id1 = int(input("Enter the ID of the student to be edited: "))
                                    for x in adm:
                                        if id1 == x[0]:
                                            print("SELECT A COURSE TO BE ENROLLED")
                                            mycursor.execute("SELECT * FROM course")
                                            myresult = mycursor.fetchall()
                                            print(tabulate(myresult, headers=['ID', 'NAME', 'FEES', 'Duration'], tablefmt='psql'))
                                            while True:
                                                try:
                                                    new_course = int(input("Enter the new course ID: "))
                                                    for course in myresult:
                                                        if new_course == course[0]:
                                                            sql = "UPDATE admission SET course=%s WHERE id=%s"
                                                            val = (course[1], id1)
                                                            mycursor.execute(sql, val)
                                                            mydb.commit()
                                                            print("Course added successfully!!")
                                                            break
                                                    else:
                                                        print("Course ID not found! Try again.")
                                                        continue
                                                    break
                                                except ValueError:
                                                    print("Invalid input! Please enter a valid course ID.")
                                            break
                                    else:
                                        print("Student ID not found! Please try again.")
                                        continue
                                    break
                                except ValueError:
                                    print("Invalid input! Please enter a valid student ID.")
                            break  

                    break 

                elif opt==3:
                    #DELETE STUDENT ID FROM ADMISSION
                        mycursor.execute("SELECT id FROM admission")
                        myresult = mycursor.fetchall()
                        while True:
                            try:
                                id1=int(input('id of the student you want to delete: '))
                                for x in myresult:
                                    if id1==x[0]:
                                        sql="DELETE FROM admission WHERE id=%s"
                                        val=(id1,)
                                        mycursor.execute(sql,val)
                                        mydb.commit()
                                        print('Deleted successfully')
                                        break
                                else:
                                    print('ID not found!')
                            except ValueError:
                                print('id not found!!')
                            try:
                                if id1==x[0]:
                                    break
                            except:
                                pass  
                elif opt==4:
                    # VIEW STUDENT TABLE
                    print("VIEW")
                    mycursor.execute("SELECT * FROM admission")
                    myresult = mycursor.fetchall()
                    print(tabulate(myresult, headers=['ID','NAME', 'PHONE','EMAIL','DISTRICT','ENROLLED COURSE'], tablefmt='psql'))                   
                else:
                    if opt==5:
                        pass
        
        elif option == 2:
            while True:  
                print('+----------------------+')
                print('|1.Add course          |')
                print('|2.Edit course         |')
                print('|3.Available course    |')
                print('|4.Delete course       |')
                print('|5.Back!               |')
                print('+----------------------+')

                try:
                    ch = int(input('Select option: '))
                except ValueError:
                    print("Invalid input! Please enter a number between 1 and 5.")
                    continue  

                if ch == 1:
                    #------ADD COURSE---------
                    print('ENTER')
                    print('<--------->')        
                    while True:
                        c_name = input('New course: ')
                        if not c_name:
                            print('You must enter a course name.')
                        else:
                            break

                    
                    while True:
                        try:
                            fees = int(input('Enter fees: '))
                            break
                        except ValueError:
                            print('Invalid input! Please enter a valid number for fees.')

                    
                    while True:
                        dur = input('Duration of this course: ')
                        if not dur:
                            print('You must enter a duration.')
                        else:
                            break

                    sql = "INSERT INTO course(name, fees, duration) VALUES (%s, %s, %s)"
                    val = (c_name, fees, dur)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print('Course added successfully!')

                elif ch == 2:
                    #------EDIT COURSE--------
                    print('Edit course')
                    print('<---------->')
                    print('1.Name')
                    print('2.Fees')
                    print('3.Duration')

                    while True:
                        try:
                            choice = int(input('Select option: '))
                            break  
                        except ValueError:
                            print('Invalid input! Please enter a number between 1 and 3.')



                    if choice in [1, 2, 3]:
                        mycursor.execute("SELECT c_id FROM course")
                        adm = mycursor.fetchall()

                        
                        while True:
                            try:
                                id1 = int(input('Enter the ID of the course to be edited: '))
                                if any(id1 == x[0] for x in adm):
                                    break
                                else:
                                    print('Course ID not found! Please enter a valid ID.')
                            except ValueError:
                                print('Invalid input! Please enter a valid numeric ID.')

                        
                        if choice == 1:
                            # EDIT COURSE NAME
                            while True:
                                new_name = input('Enter new course name: ')
                                if not new_name:
                                    print('You must enter a course name.')
                                else:
                                    sql = "UPDATE course SET name = %s WHERE c_id = %s"
                                    val = (new_name, id1)
                                    mycursor.execute(sql, val)
                                    mydb.commit()
                                    print('Course name updated successfully!')
                                    break
                
                        elif choice == 2:
                            # EDIT COURSE FEES
                            while True:
                                try:
                                    new_fee = int(input('Enter new course fees: '))
                                    sql = "UPDATE course SET fees = %s WHERE c_id = %s"
                                    val = (new_fee, id1)
                                    mycursor.execute(sql, val)
                                    mydb.commit()
                                    print('Course fees updated successfully!')
                                    break
                                except ValueError:
                                    print('Invalid input! Please enter a valid number for fees.')
                
                        elif choice == 3:
                            # EDIT COURSE DURATION
                            while True:
                                new_dur = input('Enter new course duration: ')
                                if not new_dur:
                                    print('You must enter a duration.')
                                else:
                                    sql = "UPDATE course SET duration = %s WHERE c_id = %s"
                                    val = (new_dur, id1)
                                    mycursor.execute(sql, val)
                                    mydb.commit()
                                    print('Course duration updated successfully!')
                                    break
                    else:
                        print("Invalid option. Please select from the given options.")

                elif ch == 3:
                    # View Available Courses
                    mycursor.execute("SELECT * FROM course")
                    courses = mycursor.fetchall()
                    print(tabulate(courses, headers=['ID', 'Name', 'Fees', 'Duration'], tablefmt='psql'))

                elif ch == 4:
                    # Delete Course
                    print('Delete Course')
                    mycursor.execute("SELECT * FROM course")
                    courses = mycursor.fetchall()
                    #print(tabulate(courses, headers=['ID', 'Name', 'Fees', 'Duration'], tablefmt='psql'))

                    while True:
                        try:
                            del_id = int(input('Enter the ID of the course to delete: '))
                            if any(del_id == x[0] for x in courses):
                                sql = "DELETE FROM course WHERE c_id = %s"
                                mycursor.execute(sql, (del_id,))
                                mydb.commit()
                                print('Course deleted successfully!')
                                break
                            else:
                                print('Course ID not found! Please enter a valid ID.')
                        except ValueError:
                            print('Invalid input! Please enter a valid numeric ID.')

                elif ch == 5:
                    break  

                else:
                    print('Invalid option. Please select a valid option.')

        elif option == 3:
            print('Exiting the program.')
            break

        else:
            print('Invalid option. Please select a valid option.')
    except:
        print('Its invalid,try again!!')