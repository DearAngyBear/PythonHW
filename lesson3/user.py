class User:
    def __init__ (self, first_name, last_name):
        # print ('Угу') # временная строка для отображения создания класса
        self.fname = first_name
        self.lname = last_name

    def sayFirstName (self):
        print ("Моё имя", self.fname)

    def sayLastName (self):
        print ("Моя фамилия", self.lname)
        
    def sayFullName (self):
        print ("Моё полное имя", self.fname, self.lname)
