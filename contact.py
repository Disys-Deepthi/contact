class phone_Contacts:                                                                                   
    
    def __init__(self,Firstname,Lastname,Phone_number,Email_ID,Groups,DOB):                             
        self.firstname=Firstname
        self.lastname=Lastname
        self.phonenumber=Phone_number
        self.emailid=Email_ID
        self.groups=Groups
        self.dob=DOB
        
        
    def open_phcontacts(self):
        print("Phone Contacts")
    
        
    def firstname_verification(self):
        if type(self.firstname) == str:
            if len(self.firstname) <= 15:                                                                                
                print("Firstnameame verified")
            else:
                raise ValueError("Firstnameame should contain lesser than or equal to 15 letters")
        else:
            raise TypeError("Firstname should contain letters only")
        
    def lastname_verification(self):
        if type(self.lastname) == str:
            if len(self.lastname) <= 15:                                                                               
                print("Lastnameame verified")
            else:
                raise ValueError("Lastnameame should contain lesser than or equal to 15 letters")
        else:
            raise TypeError("Lastname should contain letters only")
        
    def phonenumber_verification(self):
        if (len(self.phonenumber)==10):
            if type(self.phonenumber) == str:                                                                            
                print("Phone number verified")
            else:
                raise TypeError("Phone number should contain only integers ")
        else:
            raise ValueError("phone number should not be grater than or lesser than 10")
        
    def emailid_verification(self):
        if type(self.emailid) == str:                                                                               
            if len(self.emailid) <= 25:                                                                              
                print("Emailid verified")
            else:
                raise ValueError("Emailid should not contain more than 25 values")
        else:
            raise TypeError("Invalid emailid")    
        

    def groups_verification(self):
        if type(self.groups) == str:
            if len(self.groups) <= 10:                                                                              
                print("Groups verified")
            else:
                raise ValueError("Groups should contain lesser than or equal to 10 letters")
        else:
            raise TypeError("Groups should contain letters only")

       
   


Deeps=phone_Contacts("Indhu","Mathi","9003085387","indhumathi22068@gmail.com","Family","06/04/2007")
Deeps.open_phcontacts()
Deeps.firstname_verification()
Deeps.lastname_verification()
Deeps.phonenumber_verification()
Deeps.emailid_verification()
Deeps.groups_verification()



        
phone=[{"Firstname":"nethra","Lastname":"Raj","Phno":9876543210,"Email_id":"nethra@gmail.com","Groups":"Freiends"},                                  
           {"Firstname":"Sudha","Lastname":"","Phno":9962851582,"Email_id":"sudha@gmail.com","Groups":"Family"}]


for i in phone:                                                                                                             
    for j,k in i.items():                                                                                                     
        print(f"{j}:{k}")

    
