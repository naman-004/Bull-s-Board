
import csv
import pandas as pd
class user:
    stocks=[]
    def __init__(self,username,passw):
        self.username=username
        self.passw=passw
        self.uf=open('new.csv','r')
        self.cr=csv.DictReader(self.uf)
      

        check=0
        for i in self.cr:
            
            if(i['Username']==self.username):
                check+=1
                if(i['Password']==self.passw):
                    check+=1
                    print("LOGINNED SUCCESFUULY")
            
        if(check==0):
            print('Username not found')
            self.temp=0
            print('Do you want to 1.create new user or 2.try again? or 3.Exit')
            self.temp=int(input('Choice='))
            if(self.temp==1):
                user.createuser(self)
                
            elif(self.temp==2):
                temp_user=input('username=')
                temp_pass=input('password=')
                user.__init__(self,temp_user,temp_pass)
            else:
                print("THEEK HAI BHAI")
                exit()
        if(check==1):
            print('Password invalid Try again?')
            self.temp=(input('Choice(yes/no)='))
            if(self.temp=='yes'):
                temp_user=input('username=')
                temp_pass=input('password=')
                user.__init__(self,temp_user,temp_pass)
                
            else:
                print("THEEK HAI BHAI")
                exit()
        self.uf.close()
    def createuser(self):
        self.newuser=input('Username=')
        self.uf=open('new.csv','r')
        self.cr=csv.DictReader(self.uf)
        self.check=0
        for i in self.cr:
            
            if(i['Username']==self.newuser):
                self.check+=1
        if(self.check==1):
            print('This username already exists')
            user.createuser(self)
        else:
            self.newpass=input('Password=')
            self.newbal=float(input("Initial balance="))
            uf=open('new.csv','a',newline='')
            cw=csv.writer(uf)
            cw.writerow([self.newuser,self.newpass,self.newbal])
            uf.close()
        self.uf.close()
    def getbalance(self):
        self.filvar=open('new.csv','r')
        self.csvar=csv.DictReader(self.filvar)
        for j in self.csvar:
            if(j['Username']==self.username):
                return float(j['Balance'])
                self.filvar.close()
        
    def changepass(self):
        csvread=pd.read_csv('new.csv')
        rowindex=csvread.loc[csvread['Username']==self.username].index[0]
        csvread.loc[rowindex,'Password']=input('New Password=')
        csvread.to_csv('new.csv',index=False)
    def changebal(self,tran_money):
        self.tran_money=tran_money
        csvread=pd.read_csv('new.csv')
        rowindex=csvread.loc[csvread['Username']==self.username].index[0]
        csvread.loc[rowindex,'Balance']=user.getbalance(self)+self.tran_money
        csvread.to_csv('new.csv',index=False)
class bot:
    def __init__(self,botname):
        self.botname=botname
    def getbalance(self):
        self.filvar=open('new.csv','r')
        self.csvar=csv.DictReader(self.filvar)
        for j in self.csvar:
            if(j['Username']==self.botname):
                return float(j['Balance'])
                self.filvar.close()
    def changebal(self,tran_money):
        self.tran_money=tran_money
        csvread=pd.read_csv('new.csv')
        rowindex=csvread.loc[csvread['Username']==self.botname].index[0]
        csvread.loc[rowindex,'Balance']=bot.getbalance(self)+self.tran_money
        csvread.to_csv('new.csv',index=False)
        
#user_name=input('username=')
#pass_word=input('password=')
#u1=user(user_name,pass_word)
#u1.changepass()
#u1.createuser()