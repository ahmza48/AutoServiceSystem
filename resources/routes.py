from .resources import *

def initialize_routes(api):
    api.add_resource(EmployeeApi, '/api/employees')
    api.add_resource(ServiceApi, '/api/services')
    api.add_resource(ServiceGrp, '/api/services/<string:servicegrp>')
    api.add_resource(AppointmentDelete,'/api/appointments/delete/<int:id>')