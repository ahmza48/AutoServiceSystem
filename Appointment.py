class Appointment:
    def __init__(self,name,email,time,phn,serviceGroup,service,address):
        self.name = name
        self.email = email
        indx = time.split('-')
        self.startTime = indx[0]
        self.endTime = indx[1]
        self.phn = phn
        self.serviceGroup = serviceGroup
        self.service = service
        self.address = address

        print(self.name,self.email,self.startTime,self.endTime,self.phn,self.serviceGroup,self.service)
