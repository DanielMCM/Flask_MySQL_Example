import regex
import xmltodict

class contact():
    def __init__(self,FirstName=None, LastName=None, address=None, email=None,phone=None, pth = None):
        if pth != None:
            f = open(pth, "r")
            f = xmltodict.parse(f.read())
            self.FirstName = f["contact"]["firstname"]
            self.LastName = f["contact"]["lastname"]
            self.address = f["contact"]["address"]
            self.email = f["contact"]["email"]
            self.phone = f["contact"]["phone"]
        else:
            self.FirstName = FirstName
            self.LastName = LastName
            self.address = address
            self.email = email
            self.phone = phone

    def insert(self,mysql):
        # validate the received values
        if self.FirstName  and self.LastName  and self.email:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.callproc('sp_createContact',(self.FirstName,self.LastName,self.address,self.email,self.phone))

            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return json.dumps({'message':'User created successfully !'})
            else:
                return json.dumps({'error':str(data[0])})
        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})

    def validate(self):
        if validate_email(self.email) and validate_compulsory(self.email,self.FirstName,self.LastName):
            return True
    
def validate_email(email):
	if email == "":
		return false;
	regexp = "[^@]+@[^@]+\.[^@]+"
	return re.match(regexp, email);

def validate_compulsory(email,FirstName,LastName):
    if email == "" or FirstName == "" or LastName == "":
        return False
    else:
        return True