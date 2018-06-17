from dbutils import DbUtils as dbu
import tkinter as tk
class Login(object):
	def __init__(self):
		self._username = ""
		self._password = ""
		self._windows = tk.Tk()
	@property
	def username(self):
		return self._username
	@username.setter
	def username(self,v):
		self._username = v
	@property
	def password(self):
		return self._password
	@password.setter
	def password(self,v):
		self._password = v
	@property
	def windows(self):
		return self._windows
	@windows.setter
	def windows(self,v):
		self._windows = v
	def showLoginForm(self):
		rootA = self.windows
		rootA.title('Login')
		instruction = Label(rootA, text='Please Login\n')
		instruction.grid(sticky=E)
		u = Label(rootA, text='Username: ')
		p = Label(rootA, text='Password: ')
		u.grid(row=1, sticky=W)
		p.grid(row=2, sticky=W)
		self.username = Entry(rootA)
		self.password = Entry(rootA, show='*')
		self.username.grid(row=1, column=1)
		self.password.grid(row=2, column=1)
		loginB = Button(rootA, text='Login', command=self.doubleCheck)
		loginB.grid(columnspan=2, sticky=W)
		rootA.mainloop()
	def doubleCheck(self):
		db = dbu("sqlite pathfile, req sur table user name == _name and pwd == _pwd")
		
		