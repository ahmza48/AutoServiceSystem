from flask import Flask,render_template,request,make_response,Response
from DBHandler import DBHandler
from Employee import Employee
from Appointment import Appointment
from base64 import b64encode
from werkzeug.utils import secure_filename #for uploading files
from flask_restful import Api,Resource
from resources import routes,resources
from flask_mail import Mail,Message


app = Flask(__name__)
app.config.from_pyfile("config.py")
app.secret_key=app.config['SECRET_KEY']
print(app.config['SECRET_KEY'])
resources.getApp(app)
api = Api(app)
routes.initialize_routes(api)

print(app.config['HOST'])

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = 'ameerza488@gmail.com'
app.config['MAIL_PASSWORD'] = 'ocwwprzhqmzestnc'


db = DBHandler(app.config["HOST"], app.config["USER"], app.config["PASSWORD"], app.config["DB"])
mail = Mail(app)

@app.route('/login')
def login_landing_page():
    return render_template('multiplelogin.html')

@app.route('/')
def home():
    db = DBHandler(app.config["HOST"], app.config["USER"], app.config["PASSWORD"], app.config["DB"])
    data = db.get_img()
    list = []
    print(data)
    j=0
    for single_tuple in data:
        temp = []
        i=0
        for record in single_tuple:
            if i==0:
                print(record,i)
                temp.append(b64encode(record).decode("utf-8"))
                i=i+1
                continue
            temp.append(record)
            i = i+1

        list.append(temp)
        j = j + 1
        if j == 4:
            break

    print(list)

    print(data)
    return render_template('home.html',data = list)

@app.route('/ourservices')
def our_services():
    db = DBHandler(app.config["HOST"], app.config["USER"], app.config["PASSWORD"], app.config["DB"])
    data = db.get_img()
    list = []
    print(data)
    for single_tuple in data:
        temp = []
        i = 0
        for record in single_tuple:
            if i == 0:
                print(record, i)
                temp.append(b64encode(record).decode("utf-8"))
                i = i + 1
                continue
            temp.append(record)
            i = i + 1

        list.append(temp)

    return render_template("services.html",data=list)

@app.route('/aboutus')
def about():
    return render_template('aboutus.html')

@app.route('/ourteam')
def ourteam():
    return render_template('ourteam.html')

@app.route('/appointment')
def appointment():
    return render_template('appointment.html')



@app.route('/appointmentsubmission', methods=["POST"])
def appointment_submision():
    print("IN SUBMISSION FORM")
    print(request.form["name"])
    print(request.form["name"],request.form["email"],request.form["time"],request.form["phoneNumber"],request.form["serviceCategory"],request.form["service"])
    appointment = Appointment(request.form["name"],request.form["email"],request.form["time"],request.form["phoneNumber"],request.form["serviceCategory"],request.form["service"],request.form["address"])
    dictionary = {
        "custName" : appointment.name,
        "email" : appointment.email,
        "start-time" : appointment.startTime,
        "end-time"   : appointment.endTime,
        "phn" :appointment.phn,
        "service-category" : appointment.serviceGroup,
        "service" : appointment.service,
        "address" : appointment.address
    }
    res = db.book_appointment(appointment)
    if res != False:
        email = request.form["email"]
        msg = Message('Thank you for your submission',
                      sender='ameerza488@gmail.com',
                      recipients=[email])

        msg.body = "Dear Customer Your Appointment Has Been Booked.\nYou Are due to pay the total amount of: "+str(res[1])+"\nThe Assignend Worker Name is: "+str(res[0][3])+"\nWorkers Contact Number: "+str(res[0][7])+"\nLooking Forward to service you."
        mail.send(msg)

        return render_template('success.html',dict=dictionary,employee=res[0],cost=res[1])
    return render_template('failed.html',dict=dictionary)


@app.route('/send_mail')
def send_email(email,apt,employee):

   msg = Message('Thank you for your submission',
                 sender='ameerza488@gmail.com',
                 recipients=[email])

   print(apt["service"])

   msg.body = "Your Appointment for "+ apt["service"] + " has been booked.\nThe Assigned Worker is: "+ employee[3]+"\nPhone Number: ",employee[7],".\nPlease do not hesitate to reach out to us if you have any questions or concerns. We are looking forward to serving you on [Date and Time of Appointment]."

   print(msg.body)

   mail.send(msg)
   return 'Email sent!'



@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/adminloginpage')
def admin_login_page():
    return render_template('adminloginpage.html')

@app.route('/adminlogin',methods=["POST"])
def admin_login():
    #if request.method == "GET":
    #   return render_template('adminloginpage.html')
    db = DBHandler(app.config["HOST"], app.config["USER"], app.config["PASSWORD"], app.config["DB"])
    res = db.admin_credentials()
    print(res)
    username = request.form["uname"]
    password = request.form["password"]
    if username == res[0][1] and password == res[0][2]:
        response = make_response(render_template('adminpanel.html',name=username))
        response.set_cookie("username",username)
        return response
    else:
        return render_template('adminloginpage.html',msg="Invalid Credentials")

@app.route('/adminpanel')
def adminpanel():  # put application's code here
    print(request.cookies.get("username"))
    if not request.cookies.get("username"):
        return render_template('adminloginpage.html')
    return render_template('adminpanel.html',name =request.cookies.get("username") )


#EMPLOYEES START
@app.route('/employees')
def view_employees():
    if not request.cookies.get("username"):
        return render_template('adminloginpage.html')
    # db = DBHandler('localhost', 'root', '1513118majeed', 'carservice')
    # emps = db.view_employees()
    return render_template("employeedata.html")

@app.route('/addemployeepage')
def add_employee_page():
    if not request.cookies.get("username"):
        return render_template('adminloginpage.html')
    return render_template("addemployeepage.html")

@app.route('/addemployee',methods=["POST"])
def add_employee():
    if not request.cookies.get("username"):
        return render_template('adminloginpage.html')
    emp = Employee(request.form["fname"],request.form["lname"],request.form["servicegroup"],request.form["spec"],request.form["phn"])
    db = DBHandler(app.config["HOST"], app.config["USER"], app.config["PASSWORD"], app.config["DB"])
    flag = db.add_employee(emp)
    if flag:
        return view_employees()

@app.route('/delete/employee/<int:id>')
def delete_employee(id):
    if not request.cookies.get("username"):
        return render_template('adminloginpage.html')
    print("In Delete")
    db = DBHandler(app.config["HOST"], app.config["USER"], app.config["PASSWORD"], app.config["DB"])
    flag = db.delete_employee(id)
    if flag:
        return view_employees()
    else:
        return render_template('employeedata.html',msg="Cannot Delete Current User")

#EMPLOYEE END

@app.route('/services')
def services():
    if not request.cookies.get("username"):
        return render_template('adminloginpage.html')
    return render_template('servicedata.html')

@app.route('/delete/service/<int:id>')
def delete_service(id):
    if not request.cookies.get("username"):
        return render_template('adminloginpage.html')
    print("In Delete")
    db = DBHandler(app.config["HOST"], app.config["USER"], app.config["PASSWORD"], app.config["DB"])
    flag = db.delete_service(id)
    if flag:
        return services()

@app.route('/addservice')
def add_service():
    return render_template('addservice.html')


@app.route('/uploadservice',methods=["POST"])
def upload_service():
    print("hello")
    print(request.form["servicename"],request.form["servicegroup"],request.form["servicecost"],request.form["description"])

    pic = request.files['pic']
    if not pic:
        return 'No pic uploaded!', 400

    filename = secure_filename(pic.filename)
    mimetype = pic.mimetype
    if not filename or not mimetype:
        return 'Bad upload!', 400
    print(request.form["servicename"],request.form["servicegroup"],request.form["servicecost"],request.form["description"])
    db = DBHandler(app.config["HOST"], app.config["USER"], app.config["PASSWORD"], app.config["DB"])
    flag = db.upload_service(request.form["servicename"],request.form["servicegroup"],request.form["servicecost"],request.form["description"],pic.read(), filename, mimetype)
    print(flag)
    if flag:
        return render_template("servicedata.html")

@app.route('/viewappointments')
def viewappointments():
    if not request.cookies.get("username"):
        return render_template('adminloginpage.html')
    result = db.get_appointments()
    return render_template('appointmentdata.html',result=result)

@app.route('/viewfeedback')
def viewfeedback():
    if not request.cookies.get("username"):
        return render_template('adminloginpage.html')
    db = DBHandler(app.config["HOST"], app.config["USER"], app.config["PASSWORD"], app.config["DB"])
    feedback = db.view_feedbacks()
    return render_template("customerfeedback.html",feedback = feedback)

@app.route('/adminlogout')
def admin_logout():
    res = make_response(render_template("adminloginpage.html"))
    res.set_cookie("username", "", expires=0)
    return res

@app.route('/upload',methods=["POST"])
def upload_img():
    pic = request.files["pic"]

    if not pic:
        return 'No pic uploaded!', 400

    filename = secure_filename(pic.filename)
    mimetype = pic.mimetype

    if not filename or not mimetype:
        return 'Bad upload!', 400
    db = DBHandler(app.config["HOST"], app.config["USER"], app.config["PASSWORD"], app.config["DB"])
    db.upload_img(pic.read(),filename,mimetype)
    #img = Img(img=pic.read(), name=filename, mimetype=mimetype)
    #db.session.add(img)
    #db.session.commit()

    return 'Img Uploaded!', 200


@app.route('/employeeloginpage')
def employee_login_page():
    return render_template('employeelogin.html')

@app.route('/employeelogin',methods=["POST","GET"])
def employee_login():
    if request.method == "GET":
        return render_template('employeelogin.html')
    username = request.form["uname"]
    password = request.form["password"]
    records = db.get_employee_credentials()
    print(records)
    print(len(records))
    for record in records:
        print(record)
        if(record[1]==username and record[2] ==password):
            appointment = db.get_specific_appointment(record[0])
            response = make_response(render_template('employeeappointments.html', name=username,apt=appointment))
            response.set_cookie("employeename", username)
            return response
    return render_template('employeelogin.html', msg="Invalid Credentials")


@app.route('/contactus')
def contact_us():
    return render_template('contactus.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/failed')
def failed():
    return render_template('failed.html')


if __name__ == '__main__':
    app.run(debug=True)