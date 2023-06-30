
from user import *
from stockcode import *

class drivercode:
    _game_no=0
    _entryfees=0
    list_of_players={}
    player_bullchips={}
    def __init__(self,userobj,l_o_s):
        print('''==========WELCOME TO BULLS BOARD===============
Games available:
1.SABSE BADA KHILADI (3 winners)
2.BADI MACHLI (2 winners)
3.RISK HAI TOH ISHQ HAI (1 winner)''' )
        self.user_ch=int(input('Whats your call?'))
        self.userobj=userobj
        self.l_o_s=l_o_s
        if self.user_ch==1:
            drivercode.gameone(self)
        elif self.user_ch==2:
            drivercode.gametwo(self)
        elif self.user_ch==3:
            drivercode.gamethree(self)
        elif self.user_ch==4:
            pass
    def gameone(self):
        print('''SABSE BADA KHILADI
        Intructions:
        1.Entry Fee Rs.5000
        2.Prize Money (1st.Rs.10000 2nd.Rs.7500 3rd. Rs.5000)
        3.Read all scheme related documents carefully
        To join, press 1, or any other key to go back''')
        self.user_ch=int(input('Choice='))
        if(self.user_ch==1):
            drivercode._game_no=1
            if(self.userobj.getbalance()<5000):
                print('Insufficient Funds! Add money now? 1.addMoney 2.Exit ')
                self.option=int(input('Enter Choice='))
                if(self.option==1):
                    self.addmoney=float(input('Amount='))
                    self.userobj.changebal(self.addmoney)
                    drivercode.gameone(self)
                else:
                    exit()
            else:
                drivercode._entryfees=5000
                self.userobj.changebal(-5000)
                self.bullchips=10000
                for stock in self.l_o_s:
                    print(stock.name,stock.iprice)
                print('BULLCHIPS OWNED:',self.bullchips)
                self.counter=True
                while(self.counter==True):
                    self.sname=input("Enter stock name you wish to buy=")
                    self.sqty=int(input('Enter No. of stocks='))
                    for i in self.l_o_s:
                        if(i.name==self.sname):
                            if(i.iprice*self.sqty<=self.bullchips):
                                print('stock purchased')
                                self.bullchips-=i.iprice*self.sqty
                                if self.userobj.username in drivercode.list_of_players:
                                    drivercode.list_of_players[self.userobj.username].append([self.sname,self.sqty])
                                else:
                                    drivercode.list_of_players[self.userobj.username]=[]
                                    drivercode.list_of_players[self.userobj.username].append([self.sname,self.sqty])
                                print('BULLCHIPS REMAINING:',self.bullchips)
                            else:
                                print('BULLCHIPS INsUFFIcient')
                    self.cont=int(input('1.Finish portfolio or 2.buy more'))
                    if(self.cont==1):
                        drivercode.player_bullchips[self.userobj.username]=self.bullchips

                        break
                for i in drivercode.list_of_players[self.userobj.username]:
                    print(i)
        else:
            drivercode.__init__(self,self.userobj,self.l_o_s)
    def gametwo(self):
        print('''BADI MACHLI
        Intructions:
        1.Entry Fee Rs.2000
        2.Prize Money (1st.Rs.5000 2nd.Rs.3000 )
        3.Read all scheme related documents carefully
        To join, press 1, or any other key to go back''')
        self.user_ch=int(input('Choice='))
        if(self.user_ch==1):
            drivercode._game_no=2
            if(self.userobj.getbalance()<2000):
                print('Insufficient Funds! Add money now? 1.addMoney 2.Exit ')
                self.option=int(input('Enter Choice='))
                if(self.option==1):
                    self.addmoney=float(input('Amount='))
                    self.userobj.changebal(self.addmoney)
                    drivercode.gameone(self)
                else:
                    exit()
            else:
                drivercode._entryfees=2000
                self.userobj.changebal(-2000)
                self.bullchips=10000
                for stock in self.l_o_s:
                    print(stock.name,stock.iprice)
                print('BULLCHIPS OWNED:',self.bullchips)
                self.counter=True
                while(self.counter==True):
                    self.sname=input("Enter stock name you wish to buy=")
                    self.sqty=int(input('Enter No. of stocks='))
                    for i in self.l_o_s:
                        if(i.name==self.sname):
                            if(i.iprice*self.sqty<=self.bullchips):
                                print('stock purchased')
                                self.bullchips-=i.iprice*self.sqty
                                if self.userobj.username in drivercode.list_of_players:
                                    drivercode.list_of_players[self.userobj.username].append([self.sname,self.sqty])
                                else:
                                    drivercode.list_of_players[self.userobj.username]=[]
                                    drivercode.list_of_players[self.userobj.username].append([self.sname,self.sqty])
                                print('BULLCHIPS REMAINING:',self.bullchips)
                            else:
                                print('BULLCHIPS INsUFFIcient')
                    self.cont=int(input('1.Finish portfolio or 2.buy more'))
                    if(self.cont==1):
                        drivercode.player_bullchips[self.userobj.username]=self.bullchips

                        break
                for i in drivercode.list_of_players[self.userobj.username]:
                    print(i)
        else:
            drivercode.__init__(self,self.userobj,self.l_o_s)
    def gamethree(self):
        print('''RISK HAI TOH ISHQ HAI
        Intructions:
        1.Entry Fee Rs.1000
        2.Prize Money (1st.Rs.3000)
        3.Read all scheme related documents carefully
        To join, press 1, or any other key to go back''')
        self.user_ch=int(input('Choice='))
        if(self.user_ch==1):
            drivercode._game_no=3
            if(self.userobj.getbalance()<1000):
                print('Insufficient Funds! Add money now? 1.addMoney 2.Exit ')
                self.option=int(input('Enter Choice='))
                if(self.option==1):
                    self.addmoney=float(input('Amount='))
                    self.userobj.changebal(self.addmoney)
                    drivercode.gameone(self)
                else:
                    exit()
            else:
                drivercode._entryfees=1000
                self.userobj.changebal(-1000)
                self.bullchips=10000
                for stock in self.l_o_s:
                    print(stock.name,stock.iprice)
                print('BULLCHIPS OWNED:',self.bullchips)
                self.counter=True
                while(self.counter==True):
                    self.sname=input("Enter stock name you wish to buy=")
                    self.sqty=int(input('Enter No. of stocks='))
                    for i in self.l_o_s:
                        if(i.name==self.sname):
                            if(i.iprice*self.sqty<=self.bullchips):
                                print('stock purchased')
                                self.bullchips-=i.iprice*self.sqty
                                if self.userobj.username in drivercode.list_of_players:
                                    drivercode.list_of_players[self.userobj.username].append([self.sname,self.sqty])
                                else:
                                    drivercode.list_of_players[self.userobj.username]=[]
                                    drivercode.list_of_players[self.userobj.username].append([self.sname,self.sqty])
                                print('BULLCHIPS REMAINING:',self.bullchips)
                            else:
                                print('BULLCHIPS INsUFFIcient')
                    self.cont=int(input('1.Finish portfolio or 2.buy more'))
                    if(self.cont==1):
                        drivercode.player_bullchips[self.userobj.username]=self.bullchips

                        break
                for i in drivercode.list_of_players[self.userobj.username]:
                    print(i)
                    
        else:
            drivercode.__init__(self,self.userobj,self.l_o_s)
         
    def simulator_run(self):
        self.countee=0
        while(self.countee<25200):
            for i in self.l_o_s:
                i.change()
            self.countee+=1
        for i in self.l_o_s:
                print(i.name,round(i.iprice,2))
    def updated_portfolio(self):
        for ite in drivercode.player_bullchips:
            for i in drivercode.list_of_players[ite]:
                for j in self.l_o_s:
                    if(j.name==i[0]):
                        drivercode.player_bullchips[ite]+=j.iprice*i[1]
        
    def leaderboard(self):
        print('=================================')
        self.rank=1
        drivercode.player_bullchips=dict(sorted(drivercode.player_bullchips.items(), key=lambda item: item[1],reverse=True))
        for it,jt in zip(drivercode.player_bullchips.keys(),drivercode.player_bullchips.values()):
            print(it,round(jt,2))
            if(drivercode._game_no==1):
                if(self.rank==1 and self.userobj.username==it):
                    self.userobj.changebal(drivercode._entryfees*2)
                    print('!!!WON 2x ON 1st RANK!!!')
                if(self.rank==2 and self.userobj.username==it):
                    self.userobj.changebal(drivercode._entryfees*1.5)
                    print('!!!WON 1.5x ON 2nd RANK!!!')
                if(self.rank==3 and self.userobj.username==it):
                    self.userobj.changebal(drivercode._entryfees*1)
                    print('!!!WON 1x ON 3rd RANK!!!')
            if(drivercode._game_no==2):
                if(self.rank==1 and self.userobj.username==it):
                    self.userobj.changebal(drivercode._entryfees*2.5)
                    print('!!!WON 2.5x ON 1st RANK!!!')
                if(self.rank==2 and self.userobj.username==it):
                    self.userobj.changebal(drivercode._entryfees*1.5)
                    print('!!!!!!WON 1.5x ON 2nd RANK!!!')
            if(drivercode._game_no==3):
                if(self.rank==1 and self.userobj.username==it):
                    self.userobj.changebal(drivercode._entryfees*3)
                    print('!!!!!!WON 3x ON 1st RANK!!!')
            self.rank+=1
    def bot_runner(self,botobj):
        self.botobj=botobj
        self.bot_bullchips=10000
        
        while(self.bot_bullchips>500):
            self.bot_stock=random.choice(self.l_o_s)
            self.bot_qty=random.randint(1,51)
            if(self.bot_stock.iprice*self.bot_qty<=self.bot_bullchips):
                self.bot_bullchips-=self.bot_stock.iprice*self.bot_qty
                if self.botobj.botname in drivercode.list_of_players:
                    drivercode.list_of_players[self.botobj.botname].append([self.bot_stock.name,self.bot_qty])
                else:
                    drivercode.list_of_players[self.botobj.botname]=[]
                    drivercode.list_of_players[self.botobj.botname].append([self.bot_stock.name,self.bot_qty])
        drivercode.player_bullchips[self.botobj.botname]=self.bot_bullchips

bot1=bot('rushil')
bot2=bot('nidhi')
bot3=bot('nisha')
bot4=bot('sahil')
bot5=bot('naman')
username=input('Username=')
password=input('Password=')
newuser=user(username,password)
maingame=drivercode(newuser,list_of_stocks)
maingame.bot_runner(bot1)
maingame.bot_runner(bot2)
maingame.bot_runner(bot3)
maingame.bot_runner(bot4)
maingame.bot_runner(bot5)
maingame.simulator_run()
maingame.updated_portfolio()
maingame.leaderboard()
