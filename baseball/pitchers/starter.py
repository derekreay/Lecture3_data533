#!/usr/bin/env python
# coding: utf-8

# In[2]:


class personnel:
    def __init__(self, name, age, team, role, salary):
        self.name = name
        self.age = age
        self.team = team
        self.role = role
        self.__salary = salary
        
    def display(self):
        print("Name:", self.name, "Age:", self.age, "Team:", self.team, "Position:", self.role)
        
    def getSalary(self):
        print("Salary:", self.__salary)


# In[6]:


class starter(personnel):
    def __init__(self, name, age, team, role, salary,inningspitched, strikeouts, walks, earnedruns, hits, gamesstarted): 
        personnel.__init__(self, name, age, team, role, salary)
        self.gamesstarted = gamesstarted
        self.inningspitched = inningspitched
        self.strikeouts = strikeouts
        self.walks = walks
        self.earnedruns = earnedruns
        self.hits = hits
        self.gamesstarted = gamesstarted
    
    def display(self):
        personnel.display(self)
        print("IP:", self.inningspitched, "K:", self.strikeouts,
        "BB:", self.walks, "ER:", self.earnedruns, "Hits:", self.hits, "GS:", self.gamesstarted)
        
    def IPpG(self):
        if self.gamesstarted <= 0:
            print("Needs gamesstarted > 0 to calculate")
        else:
            return inningspitched/gamesstarted
        
    def ERA(self):
        if self.inningspitched <= 0:
            print("Needs inningspitched > 0 to calculate")
        else:
            return self.earnedruns*9/self.inningspitched            
    
    def WHIP(self):
        if self.inningspitched <= 0:
            print("Needs inningspitched > 0 to calculate")
        else:
            return (self.walks+self.hits)/self.inningspitched
    
    def Kp9(self):
        if self.inningspitched <= 0:
            print("Needs inningspitched > 0 to calculate")
        else:
            return self.strikeouts/self.inningspitched*9
    
    def BBp9(self):
        if self.inningspitched <= 0:
            print("Needs inningspitched > 0 to calculate")
        else:
            return self.walks/self.inningspitched*9

