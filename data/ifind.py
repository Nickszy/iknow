from iFinDPy import *

class iFinD():
    
    def __init__(self,username,password):
        self.username = username
        self.password = password
    
    def login(self):
        THS_iFinDLogin(self.username,self.password)

    def logout(self):
        THS_iFinDLogout()
    


if __name__ == "__main__":
    ifind_data = iFinD()
    ifind_data.login()  
               
