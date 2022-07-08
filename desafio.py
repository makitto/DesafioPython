import sys
from colorama import init
from termcolor import colored
from random import randint
init()
import time
def slow():
    time.sleep(0.03)
def text():
    time.sleep(0.9)
House = [" ", " ", " ", " "," ",25,5,"House"]
Farm = [" ", " ", " ", " ","B",50,0,"Farm"]
Parking = [" ", " ", " ", " "," ",35,10,"Parkin"]
Building = [" ", " ", " ", " ","N",100,0,"Building"]
Shop = [" ", " ", " ", " "," ",100,25,"Shop"]
Ground = [" ", " ", " ", " "," ",50,15,"Ground"]
House2 = [" ", " ", " ", " ","L",100,0,"House2"]
Farm2 = [" ", " ", " ", " "," ",55,17,"Farm2"]
Parking2 = [" ", " ", " ", " "," ",60,20,"Parkin2"]
Ground2 = [" "," "," "," ","K",0,0,"Ground2"]
Shopping = [" ", " ", " ", " "," ",75,30,"Shopping"]
Hotel = [" ", " ", " ", " "," ",250,90,"Hotel"]
Storage = [" ", " ", " ", " "," ",80,32,"Storage"]
Hotel2 = [" ", " ", " ", " "," ",85,35,"Hotel2"]
Factory = [" ", " ", " ", " "," ",250,90,"Factory"]
Factory2 = [" ", " ", " ", " "," ",100,40,"Factory2"]
Hangar = [" ", " ", " ", " ","B",50,0,"Hangar"]
Hangar2 = [" ", " ", " ", " "," ",150,50,"Hangar2"]
Airport = [" ", " ", " ", " "," ",175,55,"Airport"]
House3 = [" ", " ", " ", " ","K",0,0,"House3"]

Begin=[colored("X", "red"), colored("X", "blue"),colored("X", "green"),colored("X", "yellow"),"K",0,0,"Begin"]
Positions=[Begin,House,Farm,Parking,Building,Shop,Ground,House2,Farm2,Parking2,Ground2,Shopping,Hotel,Storage,Hotel2,Factory,Factory2,Hangar,Hangar2,Airport,House3]

class Player():
    def __init__(self, name, playercolor, coloredname, money=300, locations=[Begin], position=0, dice1=0,dice2=0,loste=0,wone=0,j=0):
        self.property=[]
        self.name = name
        self.playercolor = playercolor
        self.coloredname = coloredname
        self.money = money
        self.figure = colored("X", playercolor)
        self.owner = colored("$",playercolor)
        self.locations = locations
        self.position=position
        self.dice1=dice1
        self.dice2=dice2
        self.loste=loste
        self.wone=wone
        self.j=j
    def append(self, x):
        self.property.append(x)
    def remove(self,x):
        self.property.remove(x)
    def removeall(self):
        self.property=[]
    def lost(self):
        self.money -= self.loste
    def won(self):
        self.money+= self.wone
    def current_money(self):
        text()
        print("You currently have ", self.money, " US on your account.")
    def current_properties(self):
        text()
        print("You currently own ", self.property, ".")
    def roll(self):
        self.dice1=randint(1,6)
        self.dice2=randint(1,6)
        text()
        print("First dice rolled at ",self.dice1, ".")
        text()
        print("Second dice rolled at ", self.dice2, ".")
    def work(self):
        if Positions[self.position][4] == "L":
            self.wone = Positions[self.position][5]
            self.won()
            text()
            print("You won a lottery, your award is ",  Positions[self.position][5], " US.")
            self.current_money()
        if Positions[self.position][4] == "B":
            self.wone = Positions[self.position][5]
            self.won()
            text()
            print("You won a Bingo, your award is ", Positions[self.position][5], " US.")
            self.current_money()
        if Positions[self.position][4] == "N":
            self.loste = Positions[self.position][5]
            self.lost()
            text()
            print("You paid a ", Positions[self.position][5], " US in taxes.")
            self.current_money()
        if Positions[self.position][4] != self.owner:
            for x in Igraci:
                if Positions[self.position][4] == x.owner:
                    self.loste = Positions[self.position][6]
                    self.lost()
                    x.wone = Positions[self.position][6]
                    x.won()
                    text()
                    print(Positions[self.position][7], " is owned by ", x.coloredname,".")
                    text()
                    print(self.coloredname, " paid ", x.wone, " US in rent to ", x.coloredname, ".")
                    self.current_money()
                    text()
                    print(x.coloredname, " currently has ", x.money, "US on his/her account.")
    def action(self):
        self.position=self.position+self.dice1+self.dice2
        if self.position<=39:
            text()
            print("You landed on", Positions[self.position][7], ".")
            self.work()
        if self.position>39:
            self.position=self.position-40
            text()
            print("You landed on", Positions[self.position][7], ".")
            text()
            print(self.coloredname ," made a full circle,"  ,self.coloredname," gets 100 US bonus.")
            self.money+=100
            self.current_money()
            self.work()
    def place(self):
        self.locations=[self.locations[-1],Positions[self.position]]
        if self.locations[-1][0]==" ":
            self.locations[-1][0]=self.figure
        elif self.locations[-1][1]==" ":
            self.locations[-1][1]=self.figure
        elif self.locations[-1][2]==" ":
            self.locations[-1][2]=self.figure
        elif self.locations[-1][3]==" ":
            self.locations[-1][3]=self.figure
    def clear(self):
        if self.locations[-2][0]==self.figure:
            self.locations[-2][0]=self.locations[-2][1]
            self.locations[-2][1]=self.locations[-2][2]
            self.locations[-2][2]=self.locations[-2][3]
            self.locations[-2][3]=" "
            f1()
        elif self.locations[-2][1]==self.figure:
            self.locations[-2][1]=self.locations[-2][2]
            self.locations[-2][2]=self.locations[-2][3]
            self.locations[-2][3]=" "
            f1()
        elif self.locations[-2][2]==self.figure:
            self.locations[-2][2]=self.locations[-2][3]
            self.locations[-2][3]=" "
            f1()
        elif self.locations[-2][3]==self.figure:
            self.locations[-2][3]=" "
            f1()
    def bonus(self):
        if self.locations[-1][4]=="J":
            self.j=1
            text()
            print("You are going to the jail.")
            self.position=10
            self.place()
            self.clear()
        elif self.locations[-1][4]==" ":
            text()
            print("The price of ", Positions[self.position][7], " is", Positions[self.position][5], "US.")
            self.current_money()
            text()
            print("Would you like to buy ", self.locations[-1][7], "? Please answer with Yes or No, if you choose No, the place will go for an auction.")
            tr=input()
            if tr=="Yes":
                self.loste=self.locations[-1][5]
                self.lost()
                self.locations[-1][4]=self.owner
                text()
                print(self.coloredname," bought ", self.locations[-1][7], "for ",self.locations[-1][5]," US.")
                self.current_money()
                self.append(self.locations[-1][7])
                self.current_properties()
                f1()
            if tr=="No":
                text()
                print("The auction starts...")
                tt=""
                m4=0
                won=""
                while tt!="No":
                    for x in Players:
                      if x.money >= 0:
                        text()
                        print("How much does ", x.coloredname, " offers this round for ", self.locations[-1][7], "? Please enter the number.")
                        k=int(input())
                        if k >m4:
                            won=x
                            m4=k
                    text()
                    print("Would you like to go for another round of an auction, if not the winner will be announced, please enter Yes or No.")
                    tt=input()
                text()
                print("The winner of this auction is ", won.coloredname, "he/she bought ", self.locations[-1][7], "for ", m4, "US .")
                won.append(self.locations[-1][7])
                won.money-=m4
                self.locations[-1][4]=won.owner
                text()
                print(won.coloredname, " currently has ", won.money, " US on his/her account.")
                text()
                print(won.coloredname, " currently owns ", won.property, ".")
                f1()
    def trade(self):
        text()
        print("Would you like to trade with someone? Please answer with Yes or No.")
        mm=input()
        if mm == "Yes":
            text()
            print("Please enter the name of the player you would like to trade with.")
            mn=input()
            for t in Players:
                if mn == t.name:
                    text()
                    print("What would you like to trade to ", t.coloredname, "? Please enter Money or Place.")
                    mm=input()
                    if mm=="Money":
                        self.current_money()
                        text()
                        print(t.coloredname, " currently has", t.money, " US on his/her balance.")
                        text()
                        print("How much money do you wish to give to ", t.coloredname, " ? Please enter a number.")
                        mm = int(input())
                        self.money -= mm
                        t.money += mm
                        text()
                        print("You gave", mm, " US to ", t.coloredname, ".")
                        self.current_money()
                        text()
                        print(t.coloredname, " currently has", t.money, " US on his/her account.")
                    if mm=="Place":
                        self.current_properties()
                        text()
                        print(t.coloredname, " currently owns ", t.property, ".")
                        text()
                        print("Please enter the name of the place you would like to give to ",t.coloredname, ".")
                        mm=input()
                        for x in Positions:
                            if x[7] == mm:
                                self.remove(x[7])
                                t.append(x[7])
                                x[4]=t.owner
                                text()
                                print(t.coloredname, " received ", x[7], "from ", self.coloredname)
                                self.current_properties()
                                text()
                                print(t.coloredname, " currently owns ", t.property, ".")
                                f1()
                    text()
                    print("Would you like to trade another thing to ", t.coloredname, " ? Please answer with Yes or No.")
                    u=input()
                    while u!="No":
                        text()
                        print("What would you like to trade to ", t.coloredname, " ,please enter Money or Place.")
                        mm = input()
                        if mm == "Money":
                            self.current_money()
                            text()
                            print(t.coloredname, " currently has", t.money, " US on his/her account.")
                            text()
                            print("How much money do you wish to give to ", t.coloredname, " ? Please enter a number.")
                            mm = int(input())
                            self.money -= mm
                            t.money += mm
                            text()
                            print("You gave", mm, " US to ", t.coloredname, ".")
                            self.current_money()
                            text()
                            print(t.coloredname, " currently has", t.money, " US on his/her account.")
                        if mm == "Place":
                            self.current_properties()
                            text()
                            print(t.coloredname, " currently owns ", t.property, ".")
                            text()
                            print("Please enter the name of the place you would like to give to ", t.coloredname, ".")
                            mm = input()
                            for x in Positions:
                                if x[7] == mm:
                                    self.remove(x[7])
                                    t.append(x[7])
                                    x[4] = t.owner
                                    text()
                                    print(t.coloredname, " received ", x[7], "from ", self.coloredname, ".")
                                    self.current_properties()
                                    text()
                                    print(t.coloredname, " currently owns ", t.property, ".")
                                    f1()
                    if u=="No":
                        text()
                        print("What would you like to receive from ", t.coloredname, " ? Please enter Money or Place.")
                        mm = input()
                        if mm == "Money":
                            self.current_money()
                            text()
                            print(t.coloredname, " currently has ", t.money, " on his account.")
                            text()
                            print("How much money do you wish to receive from ", t.coloredname, "? Please enter a number.")
                            mm = int(input())
                            self.money += mm
                            t.money -= mm
                            text()
                            print(self.coloredname, " received ", mm, " US from", t.coloredname, "." )
                            self.current_money()
                            text()
                            print(t.coloredname, " currently has", t.money, "US on his/her account.")
                        if mm == "Place":
                            self.current_properties()
                            text()
                            print(t.coloredname, " currently owns ", t.property, ".")
                            text()
                            print("Please enter the name of the place you would like to receive from ", t.coloredname)
                            mm = input()
                            for x in Positions:
                                if x[7] == mm:
                                    self.append(x[7])
                                    t.remove(x[7])
                                    x[4] = self.owner
                                    text()
                                    print(self.coloredname, " received ", x[7], "from ", t.coloredname)
                                    self.current_properties()
                                    text()
                                    print(t.coloredname, " currently owns ", t.property, ".")
                                    f1()
                        text()
                        print("Would you like to receive another thing from ", t.coloredname, "? Please answer with Yes or No.")
                        u = input()
                        while u != "No":
                            if mn == t.name:
                                text()
                                print("What would you like to receive from ", t.coloredname, " ? Please enter Money or Place.")
                                mm = input()
                                if mm == "Money":
                                    self.current_money()
                                    text()
                                    print(t.coloredname, " currently has ", t.money, " on his account.")
                                    text()
                                    print("How much money do you wish to receive from ", t.coloredname,"? Please enter a number.")
                                    mm = int(input())
                                    self.money += mm
                                    t.money -= mm
                                    text()
                                    print(self.coloredname, " received ", mm, " US from", t.coloredname, ".")
                                    self.current_money()
                                    text()
                                    print(t.coloredname, " currently has", t.money, " US on his/her account.")
                                if mm == "Place":
                                    self.current_properties()
                                    text()
                                    print(t.coloredname, " currently owns ", t.property, ".")
                                    text()
                                    print("Please enter the name of the place you would like to receive from ",t.coloredname)
                                    mm = input()
                                    for x in Positions:
                                        if x[7] == mm:
                                            self.append(x[7])
                                            t.remove(x[7])
                                            x[4] = self.owner
                                            text()
                                            print(self.coloredname, " received ", x[7], "from ", t.coloredname)
                                            self.current_properties()
                                            text()
                                            print(t.coloredname, " currently owns ", t.property, ".")
                                            f1()
                                text()
                                print("Would you like to receive another thing from ", t.coloredname,"? Please answer with Yes or No.")
                                u = input()
        else:
            text()
            print("You decided not to trade with anyone.")
    def invest(self):
        tray=0
        for k in Zone:
            if self.locations[-1] in k:
                for n in k:
                    if n[7] in self.property:
                        tray+=1
                if tray == len(k):
                    if self.locations[-1][4]==self.owner:
                        text()
                        print("Would you like to invest in ",self.locations[-1][7], ", if you invest,the rent of place that you invested in will raise for 10 percent of your investment, please answer with Yes or No.")
                        io=input()
                        if io=="Yes":
                            self.current_money()
                            text()
                            print("How much would you like to invest in ", self.locations[-1][7], ", please enter the number that ends with zero, for example 250.")
                            investment=int(input())
                            self.money-=investment
                            self.locations[-1][6]+=int(investment/10)
                            text()
                            print(self.coloredname, "invested in ", self.locations[-1][7], investment, " RSD,  the rent of ", self.locations[-1][7] ,"raised for ", int(investment/10), "RSD, the rent of ", self.locations[-1][7], "is now ", int(self.locations[-1][6]), "RSD.")
                        else:
                            text()
                            print(self.coloredname, " decided not to invest in ", self.locations[-1][7] )
        if self.dice1 != self.dice2:
            text()
            print(self.coloredname, " ends his/her turn.")
    def bankrupt(self):
        if self.money<0:
            for x in Positions:
                if x[4]==self.owner:
                    x[4]=" "
            for u in self.locations[-1]:
                if u==self.figure:
                    u=" "
            self.removeall()
            text()
            print(self.coloredname, " has bankrupted.")
            self.dice1=1
            self.dice2=2
            f1()
    def first_turn(self):
        if self.j == 1:
            text()
            print(self.coloredname, " is in jail this turn, he/she can't play.")
            self.j = 0
        else:
            if self.money > 0 and self.j != 1:
                text()
                print(self.coloredname, " is on the turn.")
                self.trade()
                text()
                input("Press ENTER to roll dices.")
                text()
                print(self.coloredname, " is now rolling dices.")
                self.roll()
                self.action()
                self.place()
                self.clear()
                self.bonus()
                self.invest()
                self.bankrupt()
    def second_turn(self):
        if self.dice1 == self.dice2:
            text()
            print(self.coloredname, " rolled doubles, he/she gets to play again.")
            if self.j == 1:
                text()
                print(print(self.coloredname, " is in jail this turn, he/she can't play."))
                self.j = 0
                self.dice1 = 1
                self.dice2 = 2
            else:
                if self.money > 0 and self.j != 1:
                    text()
                    print(self.coloredname, " is on the turn again.")
                    self.trade()
                    text()
                    input("Press ENTER to roll dices.")
                    text()
                    print(self.coloredname, " is now rolling dices.")
                    self.roll()
                    self.action()
                    self.place()
                    self.clear()
                    self.bonus()
                    time.sleep(1)
                    self.invest()
                    self.bankrupt()
                    time.sleep(3)
    def third_turn(self):
        if self.dice1 == self.dice2:
            text()
            print(self.coloredname, " rolled doubles for second time, he/she gets to play again.")
            if self.j == 1:
                text()
                print(print(self.coloredname, " is in jail this turn, he/she can't play."))
                self.j = 0
                self.dice1 = 1
                self.dice2 = 2
            else:
                if self.money > 0 and self.j != 1:
                    text()
                    print(self.coloredname, " is on the turn again.")
                    self.trade()
                    text()
                    input("Press ENTER to roll dices")
                    text()
                    print(self.coloredname, " is now rolling dices.")
                    self.roll()
                    if self.dice1 == self.dice2:
                        text()
                        print(self.coloredname, " rolled doubles for the third time, he/she is going to the jail.")
                        self.j = 1
                        self.position = 10
                        self.place()
                        self.clear()
                        self.dice1 = 1
                        self.dice2 = 2
                    else:
                        self.action()
                        self.place()
                        self.clear()
                        self.bonus()
                        self.invest()
                        self.bankrupt()
    def gameplay(self):
        self.first_turn()
        self.second_turn()
        self.third_turn()
def check_bankrupt():
    for x in Players:
        if x.money < 0:
            text()
            print(x.coloredname, " has bankrupted he/she can't play anymore")
def winner():
    tre=0
    tru=""
    for x in Players:
        if x.money > tre:
            tru=x.coloredname
    text()
    print("The winner of the game is", tru, "CONGRATULATIONS !!!")
text()
print("WELCOME TO THE GAME OF MONOPOLY")
print()
text()
print("Please enter the name of the first player.")
a1= input()
Player1 = Player(a1, "red", colored(a1,"red"))
text()
print("Please enter the name of the second player.")
a2=input()
Player2 = Player(a2, "blue", colored(a2,"blue"))
text()
print("Please enter the name of the third player.")
a3 = input()
Player3 = Player(a3, "green", colored(a3,"green"))
text()
print("Please enter the name of the fourth player.")
a4 = input()
Player4 = Player(a4, "yellow", colored(a4,"yellow"))
text()
print("Name of the first player is ", Player1.coloredname, " his/her figure will be of red color.")
text()
print("Name of the second player is ", Player2.coloredname, " his/her figure will be of blue color.")
text()
print("Name of the third player is ", Player3.coloredname, " his/her figure will be of green color.")
text()
print("Name of the fourth player is ", Player4.coloredname, " his/her figure will be of yellow color.")