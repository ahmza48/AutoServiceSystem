import pymysql
from Employee import Employee
from Appointment import Appointment


class DBHandler:
    def __init__(self,host,user,password,database):
        self.host=host
        self.user = user
        self.password=password
        self.database=database

    def admin_credentials(self):
        mydb = None
        mydbCursor = None
        try:
            # Get DB Connection
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            # Get cursor object
            mydbCursor = mydb.cursor()
            sql = "Select * from admin"
            mydbCursor.execute(sql)
            res = mydbCursor.fetchall()
            print(res)
            return res
        except Exception as e:
            print(str(e))

    def add_employee(self, employee):
        mydb = None
        mydbCursor = None
        try:
            # Get DB Connection
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            # Get cursor object
            mydbCursor = mydb.cursor()
            sql = "Insert Into Employees(firstname,lastname,username,servicegroup,specification,phn) VALUES (%s,%s,%s,%s,%s,%s)"
            args = (employee.firstname,employee.lastname,employee.username,employee.servicegroup,employee.specification,employee.phn)
            mydbCursor.execute(sql,args)
            mydb.commit()
            return True
        except Exception as e:
            print(str(e))

    def view_employees(self):
        mydb = None
        mydbCursor = None
        try:
            # Get DB Connection
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            # Get cursor object
            mydbCursor = mydb.cursor()
            sql = "SELECT * FROM EMPLOYEES"
            mydbCursor.execute(sql)
            res = mydbCursor.fetchall()
            return res
        except Exception as e:
            print(str(e))

    def view_services(self):
        mydb = None
        mydbCursor = None
        try:
            # Get DB Connection
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            # Get cursor object
            mydbCursor = mydb.cursor()
            sql = "SELECT * FROM SERVICES"
            mydbCursor.execute(sql)
            res = mydbCursor.fetchall()
            return res
        except Exception as e:
            print(str(e))

    def view_service(self,grp):
        mydb = None
        mydbCursor = None
        try:
            # Get DB Connection
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            # Get cursor object
            mydbCursor = mydb.cursor()
            sql = "SELECT servicename FROM SERVICES where servicegroup=%s"
            args = (grp)
            mydbCursor.execute(sql,grp)
            res = mydbCursor.fetchall()
            return res
        except Exception as e:
            print(str(e))

    def delete_service(self,id):
        mydb = None
        mydbCursor = None
        try:
            # Get DB Connection
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            # Get cursor object
            mydbCursor = mydb.cursor()
            sql = "DELETE FROM services WHERE id=%s;"
            args = (id)
            mydbCursor.execute(sql, args)
            mydb.commit()
            return True
        except Exception as e:
            print(str(e))


    def view_feedbacks(self):
        mydb = None
        mydbCursor = None
        try:
            # Get DB Connection
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            # Get cursor object
            mydbCursor = mydb.cursor()
            sql = "SELECT * FROM CONTACT_US"
            mydbCursor.execute(sql)
            res = mydbCursor.fetchall()
            return res
        except Exception as e:
            print(str(e))


    def delete_employee(self,id):
        mydb = None
        mydbCursor = None
        try:
            # Get DB Connection
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            # Get cursor object
            mydbCursor = mydb.cursor()
            sql = "DELETE FROM employees WHERE id=%s;"
            args = (id)
            mydbCursor.execute(sql, args)
            mydb.commit()
            return True
        except Exception as e:
            print(str(e))
            return False


    def upload_img(self,img,name,mimetype):
        mydb = None
        mydbCursor = None
        try:
            # Get DB Connection
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            # Get cursor object
            mydbCursor = mydb.cursor()
            sql = "Insert Into img(img,name,mimetype) VALUES (%s,%s,%s)"
            args = (img, name, mimetype)
            mydbCursor.execute(sql, args)
            mydb.commit()
            return True
        except Exception as e:
            print(str(e))

    def upload_service(self,name,group,cost,description,img,imgname,mimetype):
        mydb = None
        mydbCursor = None
        try:
            # Get DB Connection
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            # Get cursor object
            mydbCursor = mydb.cursor()
            sql = "Insert Into services(servicename,servicegroup,servicecost,description,img,imgname,mimetype) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            args = (name,group, cost,description,img, imgname, mimetype)
            mydbCursor.execute(sql, args)
            mydb.commit()
            return True
        except Exception as e:
            print("In Exception!")
            print(str(e))

    def get_img(self):
        mydb = None
        mydbCursor = None
        try:
            # Get DB Connection
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            # Get cursor object
            mydbCursor = mydb.cursor()
            sql = "SELECT img,mimetype,servicename,servicecost,description FROM services"
            mydbCursor.execute(sql)
            res = mydbCursor.fetchall()
            return res
        except Exception as e:
            print(str(e))

    def get_employee_credentials(self):
        mydb = None
        mydbCursor = None
        try:
            # Get DB Connection
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            # Get cursor object
            mydbCursor = mydb.cursor()
            sql = "SELECT id,username,password FROM employees"
            mydbCursor.execute(sql)
            res = mydbCursor.fetchall()
            return res
        except Exception as e:
            print(str(e))

    def get_appointments(self):
        mydb = None
        mydbCursor = None
        try:
            # Get DB Connection
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            # Get cursor object
            mydbCursor = mydb.cursor()
            sql = "SELECT * FROM appointment"
            mydbCursor.execute(sql)
            res = mydbCursor.fetchall()
            return res
        except Exception as e:
            print(str(e))

    def get_specific_appointment(self,id):
        mydb = None
        mydbCursor = None
        try:
            # Get DB Connection
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            # Get cursor object
            mydbCursor = mydb.cursor()
            sql = "SELECT * FROM appointment WHERE employeeid = %s"
            args = (id)
            mydbCursor.execute(sql,id)
            res = mydbCursor.fetchall()
            return res
        except Exception as e:
            print(str(e))

    def delete_appointment(self,id):
        mydb = None
        mydbCursor = None
        try:
            # Get DB Connection
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            # Get cursor object
            mydbCursor = mydb.cursor()

            sql = "SELECT employeeid from appointment where id=%s"
            args = (id)
            mydbCursor.execute(sql,args)
            employee = mydbCursor.fetchone()
            employeeId = employee[0]

            sql ="UPDATE employees SET isAvailable = %s where id = %s"
            args=(1,employeeId)
            mydbCursor.execute(sql,args)
            mydb.commit()

            sql = "DELETE FROM appointment WHERE id = %s"
            args = (id)
            mydbCursor.execute(sql,args)
            mydb.commit()
            return True
        except Exception as e:
            print(str(e))

    def book_appointment(self,appointment):
        mydb = None
        mydbCursor = None
        category = appointment.serviceGroup
        if category == "car":
            service = appointment.service
            print(service)
            if (service.lower()) == "car wash":
                try:
                    mydb = pymysql.connect(host=self.host, user=self.user, password=self.password,
                                           database=self.database)
                    mydbCursor = mydb.cursor()
                    sql = "Select * from employees where specification=%s AND isAvailable=%s"
                    args = ("car wash",True)
                    mydbCursor.execute(sql,args)
                    res = mydbCursor.fetchone()
                    print(res)
                    if res != None:
                        sql = "SELECT servicecost from services where servicename=%s"
                        args = (appointment.service)
                        mydbCursor.execute(sql, args)
                        result = mydbCursor.fetchone()
                        cost = result[0]

                        sql = "Insert Into appointment(username,email,starttime,endtime,phn,servicegroup,service,employeeid,address,total) Values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                        args = (appointment.name,appointment.email,appointment.startTime,appointment.endTime,appointment.phn,appointment.serviceGroup,appointment.service,res[0],appointment.address,cost)
                        mydbCursor.execute(sql, args)
                        mydb.commit()
                        sql = "UPDATE employees SET isAvailable=%s WHERE id = %s;"
                        args = (False, res[0])
                        mydbCursor.execute(sql, args)
                        mydb.commit()
                        return [res, cost]
                    else:
                        return False
                except Exception as e:
                    print("IN EXCEPTION")
                    print(str(e))
            else:
                try:
                    mydb = pymysql.connect(host=self.host, user=self.user, password=self.password,
                                           database=self.database)
                    mydbCursor = mydb.cursor()
                    sql = "Select * from employees where servicegroup=%s AND isAvailable=%s"
                    args = (category, True)
                    mydbCursor.execute(sql, args)
                    res = mydbCursor.fetchone()
                    print(res)
                    if res != None:
                        sql = "SELECT servicecost from services where servicename=%s"
                        args = (appointment.service)
                        mydbCursor.execute(sql,args)
                        result=mydbCursor.fetchone()
                        cost = result[0]

                        sql = "Insert Into appointment(username,email,starttime,endtime,phn,servicegroup,service,employeeid,address,total) Values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                        args = (
                        appointment.name, appointment.email, appointment.startTime, appointment.endTime, appointment.phn,
                        appointment.serviceGroup, appointment.service, res[0],appointment.address,cost)
                        mydbCursor.execute(sql, args)
                        mydb.commit()
                        sql = "UPDATE employees SET isAvailable=%s WHERE id = %s;"
                        args = (False, res[0])
                        mydbCursor.execute(sql, args)
                        mydb.commit()
                        return [res,cost]
                    else:
                        return False
                except Exception as e:
                    print("IN EXCEPTION")
                    print(str(e))
        else:
            service = appointment.service
            print(service)
            if (service.lower()) == "bike wash":
                try:
                    mydb = pymysql.connect(host=self.host, user=self.user, password=self.password,
                                           database=self.database)
                    mydbCursor = mydb.cursor()
                    sql = "Select * from employees where specification=%s AND isAvailable=%s"
                    args = ("bike wash", True)
                    mydbCursor.execute(sql, args)
                    res = mydbCursor.fetchone()
                    print(res)
                    if res != None:
                        sql = "SELECT servicecost from services where servicename=%s"
                        args = (appointment.service)
                        mydbCursor.execute(sql, args)
                        result = mydbCursor.fetchone()
                        cost = result[0]


                        sql = "Insert Into appointment(username,email,starttime,endtime,phn,servicegroup,service,employeeid,address,total) Values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                        args = (appointment.name, appointment.email, appointment.startTime, appointment.endTime,
                                appointment.phn, appointment.serviceGroup, appointment.service, res[0],appointment.address,cost)
                        mydbCursor.execute(sql, args)
                        mydb.commit()
                        sql = "UPDATE employees SET isAvailable=%s WHERE id = %s;"
                        args = (False, res[0])
                        mydbCursor.execute(sql, args)
                        mydb.commit()
                        return [res,cost]
                    else:
                        return False
                except Exception as e:
                    print("IN EXCEPTION")
                    print(str(e))
            else:
                try:
                    mydb = pymysql.connect(host=self.host, user=self.user, password=self.password,
                                           database=self.database)
                    mydbCursor = mydb.cursor()
                    sql = "Select * from employees where servicegroup=%s AND isAvailable=%s"
                    args = (category, True)
                    mydbCursor.execute(sql, args)
                    res = mydbCursor.fetchone()
                    print(res)
                    if res != None:
                        sql = "SELECT servicecost from services where servicename=%s"
                        args = (appointment.service)
                        mydbCursor.execute(sql, args)
                        result = mydbCursor.fetchone()
                        cost = result[0]

                        sql = "Insert Into appointment(username,email,starttime,endtime,phn,servicegroup,service,employeeid,address,total) Values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                        args = (
                            appointment.name, appointment.email, appointment.startTime, appointment.endTime,
                            appointment.phn,
                            appointment.serviceGroup, appointment.service, res[0], appointment.address,cost)
                        mydbCursor.execute(sql, args)
                        mydb.commit()
                        sql = "UPDATE employees SET isAvailable=%s WHERE id = %s;"
                        args = (False, res[0])
                        mydbCursor.execute(sql, args)
                        mydb.commit()
                        return [res,cost]
                    else:
                        return False
                except Exception as e:
                    print("IN EXCEPTION")
                    print(str(e))