class Employee:
    def __init__(self,fname,lname,grp,spec,phn):
        self.firstname = fname
        self.lastname = lname
        self.username = fname + " " + lname
        self.servicegroup = grp
        self.specification = spec
        self.phn = phn