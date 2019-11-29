#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


class reliever(personnel):
    def __init__(self, name, age, team, role, salary,inningspitched, strikeouts, walks, earnedruns, hits,saves, holds, chances):
        personnel.__init__(self, name, age, team, role, salary)
        self.saves = saves
        self.holds = holds
        self.chances = chances
        self.inningspitched = inningspitched
        self.strikeouts = strikeouts
        self.hits = hits
        self.walks = walks
        self.earnedruns = earnedruns
    
    def display(self):
        personnel.display(self)
        print("IP:", self.inningspitched, "K:", self.strikeouts,
        "BB:", self.walks, "ER:", self.earnedruns, "Hits:", self.hits,
               "SV:", self.saves, "HD:", self.holds, "CH:", self.chances)
        
    def SVper(self):
        if self.chances <= 0:
            print("Needs chances > 0 to calculate")
        else:
            return self.saves/self.chances
    
    def HDper(self):
        if self.chances <= 0:
            print("Needs chances > 0 to calculate")
        else:
            return self.saves/self.chances
        
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

