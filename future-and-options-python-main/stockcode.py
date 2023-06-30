import random
class stocks:
    stock_dic={('TCS','HDFC Bank','Hindustan Uniliever','M&M'):'big',('Infinity inc.','Wipro','ITC','SBI','NTPC','Tata steel'):'medium',('JPpower','Suzlon energy','Yes Bank','IRFC','Reliance Power'):'penny'}
    def __init__(self,name,iprice):
        self.name=name
        self.iprice=iprice
    def change(self):
        for i in stocks.stock_dic:
            if self.name in i:
                if(stocks.stock_dic[i]=='big'):
                    self.iprice+=random.uniform(self.iprice*-0.0003,self.iprice*0.0003)
                elif(stocks.stock_dic[i]=='medium'):
                    self.iprice+=random.uniform(self.iprice*-0.0005,self.iprice*0.0005)
                else:
                    self.iprice+=random.uniform(self.iprice*-0.0007,self.iprice*0.0007)


list_of_stocks=[stocks('Infinity inc.',570.0),stocks('TCS',3501.0),stocks('HDFC Bank',1655.0),stocks('Wipro',406.0),stocks('ITC',383.0),stocks('Hindustan Uniliever',2515.0),stocks('SBI',531.0),stocks('M&M',1341.0),stocks('NTPC',168.0),stocks('Tata steel',112.0),stocks('JPpower',6.8),stocks('Suzlon energy',8.9),stocks('Yes Bank',16.1),stocks('IRFC',28.75),stocks('Reliance Power',11.05)]
