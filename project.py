# PROLOG SECTION
# CIT144-Python Final Project
# This is a guest log entry form
# 12/7/2017
# Thomas Schueler
# Andrew Fraysure
# Jerry Alsbrooks
# Possible future enhancements:
# Unresolved bugs:
##############################

#import tkinter to make a gui
from tkinter import *
from tkinter.ttk import *

#import csv for output
import csv
 
 
class GuestBook:
          
    
        def __init__(self):
                window = Tk()
                window.title("Guest Book")
                label = Label(window, text = "Welcome to Python Vineyards", width = 26, justify = CENTER, font = "Helvetica 16 bold italic").grid(row = 0, column = 4, columnspan = 3, sticky = E+W)
                 
                #Row 1
                #dropdown box for inits
                self.title = StringVar()
                label = Label(window, text = "Title:", width = 6, justify = CENTER).grid(row = 1, column = 1, sticky = W+E ) 
                titles = [' ','Ms.','Mrs.','Mr.', 'Dr.']
                title = Combobox(window, width='4', height='5', textvariable=self.title, values=titles).grid(row = 1, column = 2, columnspan = 1, sticky = W+E)
        
 
                #Create the label for the guests first name
                label = Label(window, text = "First Name:", width = 11,justify = LEFT).grid(row = 1, column = 3)
                #Entry box for the guests name
                self.firstname = StringVar()
                firstname = Entry(window, textvariable = self.firstname, justify = LEFT).grid(row = 1, column =4, sticky = W)
 
                #Create the label for the guests Middle Initial
                label = Label(window, text = "Middle Initial:", width = 13,justify = CENTER).grid(row = 1, column = 5)
                #Entry box for the guests name
                self.middle = StringVar()
                middle = Entry(window, textvariable = self.middle, justify = LEFT).grid(row = 1, column =6, sticky = W)
                 
 
                #Create the label for the guests last name
                label = Label(window, text = "Last Name:", width = 10,justify = CENTER).grid(row = 1, column = 7)
                #Entry box for the guests name
                self.lastname = StringVar()
                lastname = Entry(window, textvariable = self.lastname, justify = LEFT).grid(row = 1, column = 8, sticky = W)
                ####################################################################################################################
                #row2
                #Create the label for the guests street
                label = Label(window, text = "Street:", width = 7, justify = RIGHT).grid(row = 2, column = 1)
                #entry box for the guests street
                self.street = StringVar()
                street = Entry(window, textvariable = self.street, justify = LEFT).grid(row = 2, column = 2, columnspan = 1, sticky = W+E)
                

                #Create the label for the guests city
                label = Label(window, text = "City:", width = 5, justify = RIGHT).grid(row = 2, column = 3)
                #entry box for the guests city
                self.city = StringVar()
                city = Entry(window, textvariable = self.city, justify = LEFT).grid(row = 2, column = 4, sticky = W)
                
                
                #Create the label for the guests state
                label = Label(window, text = "State:", width = 6, justify = RIGHT).grid(row = 2, column = 5)
                #entry box for guests state
                self.state = StringVar()
                states = [ 'Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa',
                           'Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire',
                           'New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee',
                           'Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming']
                state = Combobox(window, width='4', height='5', textvariable = self.state, values = states).grid(row = 2, column = 6, columnspan = 1, sticky = W+E)
                
                                
                #Create the label for the guests zipcode
                label = Label(window, text = "Zip Code:", width = 9, justify = RIGHT).grid(row = 2, column = 7, sticky = W)
                #entry box for guests zip code
                self.zipcode = StringVar()
                zipcode = Entry(window, textvariable = self.zipcode, width = 5, justify = LEFT).grid(row = 2, column = 8, sticky = W+E)
                ########################################################################################################################
                #Create a lable for the guests birthdate
                label = Label(window, text = "Birth Date:", width = 11, justify = RIGHT).grid(row = 3, column = 2)
                #entry box for the guests city
                self.birthMonth = StringVar()
                self.birthDay = StringVar()
                self.birthYear = StringVar()
                birthM = ['January','Febuary','March','April','May','June','July','August','September','October','November','December']
                birthMonth = Combobox(window, width='4', height='5', textvariable=self.birthMonth, values=birthM).grid(row = 3, column = 3, columnspan = 2, sticky = W+E)
                birthD = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'] 
                birthDay = Combobox(window, width='4', height='5', textvariable=self.birthDay, values=birthD).grid(row = 3, column = 5, columnspan = 1, sticky = W+E)
                birthY = ['1996','1995','1994','1993','1992','1991','1990','1988','1987','1986','1985','1984','1983','1982','1981','1980','1979','1978','1977','1976','1975','1974','1973','1972',
                          '1971','1970','1969','1968','1967','1966','1965','1964','1963','1962','1961','1960','1959','1958','1957','1956','1955','1954','1953','1952','1950','1949','1948','1947',
                          '1946','1945','1943','1942','1941','1940','1939','1938','1937','1936','1935','1934','1933','1932','1931','1930','1929','1928','1927','1926','1925','1924','1923','1922',
                          '1921','1920','1919','1918','1917','1916','1915','1914','1913','1912','1911','1910']
                birthYear = Combobox(window, width='4', height='5', textvariable=self.birthYear, values=birthY).grid(row = 3, column = 6, columnspan = 1, sticky = W+E)
   
                  
                #ask if they are interested in promotional emails
                label = Label(window, text = "Interested in Promotional Emails?", width = 32, justify = CENTER).grid(row = 4, column = 1, columnspan = 6)
                global emails
                emails = IntVar()
                Radiobutton(window, text='Yes', variable=emails, value=True).grid(row = 4, column = 5, sticky = W+E)
                Radiobutton(window, text='No', variable=emails, value=False).grid(row = 4, column = 6, sticky = W+E)

                #ask how they heard about us
                label = Label(window, text = "How Did You Hear About Us?", width = 26, justify = CENTER).grid(row = 9, column = 1, columnspan = 8)
                self.reply = StringVar()
                replies = [' ','Advertising','Friends','Groupon','Referral/Local','Repeat Visit','Visiting the City','Other (Specify in Comments)']
                reply = Combobox(window, width='17', height='8', textvariable=self.reply, values=replies).grid(row = 10, rowspan = 2, column = 1, columnspan = 8, sticky = W+E)
                  
  
                  
                ########################################################################################################################
  
                #Create the label for the comments
                label = Label(window, text = "Comments", width = 10, justify = CENTER).grid(row = 12, column = 1, columnspan = 8)
                #entry box for guests zip code
                self.comments = StringVar()
                comments = Entry(window, textvariable = self.comments, justify = LEFT).grid(row = 13, rowspan = 2, column = 1, columnspan = 8,  sticky = W+E)
                  
        
  
                #Button(window, text = "Save", command = self.Save) is what it should look like when commands are built
                button = Button(window, text = "Save", command = self.SaveButton).grid(row = 15, column = 1, columnspan = 8)
                  
  
                window.mainloop()
 
        def SaveButton(self):
                #This displays the inputs ont the screen so a running copy can be seen
                print(self.title.get(), self.firstname.get(), self.middle.get(), ".", self.lastname.get(), "\n",
                      self.street.get(), ",", self.city.get(), ",", self.state.get(), self.zipcode.get(), "\n", 
                      self.birthMonth.get(), self.birthDay.get(), ",", self.birthYear.get(), "\n", 
                      "Promotional Emails?:", "Yes" if emails.get() == True else "No", "\n",
                      "How Did You Find Us?:", self.reply.get(), "\n",
                      "Comments:", self.comments.get())
                #This creates a list of all the inputs
                data = [str(self.title.get()), str(self.firstname.get()),str(self.middle.get()), str(self.lastname.get()), str(self.street.get()), str(self.city.get()), str(self.state.get()),
                        str(self.zipcode.get()), str(self.birthMonth.get()), str(self.birthDay.get()), str(self.birthYear.get()),
                        str(self.reply.get()), str(self.comments.get())]
                #This exports that list to a .csv seperating values by commas, writing exactly the values entered
                with open('GuestLog.csv', 'a') as f:
                        writer = csv.writer(f, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
                        writer.writerow(data)
                #checks each box to make sure they are empty, if not it clears entries
                if self.title != "":
                        self.title.set('')
                if self.firstname !=  "":
                        self.firstname.set('')
                if self.middle != "":
                        self.middle.set('')
                if self.lastname != "":
                        self.lastname.set('')
                if self.street != "":
                        self.street.set('')
                if self.city != " ":
                       self.city.set('')                
                if self.state != "":
                        self.state.set('')
                if self.zipcode != "":
                        self.zipcode.set('')
                if self.birthMonth != '':
                        self.birthMonth.set('')
                if self.birthDay != '':
                        self.birthDay.set('')
                if self.birthYear != '':
                        self.birthYear.set('')
                if self.reply != '':
                        self.reply.set('')
                if self.comments != "":
                        self.comments.set('')
 
 
 
         
GuestBook()
