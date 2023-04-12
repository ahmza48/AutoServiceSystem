from flask import request, Response, jsonify
from flask_restful import Resource
from DBHandler import DBHandler
import json

app = None
db = None

def getApp(newApp):
    global app
    app = newApp
    app.config.from_pyfile("config.py")
    print(1)
    print(app.config['USER'])
    global db
    db = DBHandler(app.config["HOST"], app.config["USER"], app.config["PASSWORD"], app.config["DB"])


EMPLOYEES = ["id","firstname","lastname","username","password","servicegroup","specification","phn","isAvailable"]
SERVICES = ['id', 'servicename', 'servicegroup','servicecost', 'description']

#db = DBHandler(app.config["HOST"], app.config["USER"], app.config["PASSWORD"], app.config["DB"])

class EmployeeApi(Resource):
    def get(self):
        dict = []
        employees = db.view_employees()
        print(employees)
        for record in employees:
            i = 0
            temp = {}
            for entry in record:
                temp[EMPLOYEES[i]]=entry
                i=i+1
            dict.append(temp)
        print(dict)
        res = json.dumps(dict)
        print(res)
        return res
        #employees = employees.to_json()

class ServiceApi(Resource):
    def get(self):
        dicts = []
        services = db.view_services()
        print(services)
        for service in services:
            i = 0
            temp = {}
            for i in range(0, len(SERVICES)):
                temp[SERVICES[i]] = service[i]
                i = i + 1
            dicts.append(temp)
        print(dicts)
        res = json.dumps(dicts)
        print(res)
        return res

class ServiceGrp(Resource):
    def get(self,servicegrp):
        dicts = []
        services = db.view_service(servicegrp)
        print(services)
        for service in services:
            dicts.append(service[0])
        return dicts


class AppointmentDelete(Resource):
    def delete(self,id):
        res = db.delete_appointment(id)
        print(res)
        return res