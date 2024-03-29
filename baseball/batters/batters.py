#!/usr/bin/env python
# coding: utf-8

# In[7]:


class personnel:
    def __init__(self, name, age, team, role, salary):
        self.name = name
        self.age = age
        self.team = team
        self.role = role
        self.__salary = salary
        
    def display(self):
        print("Name:", self.name, "Age:", self.age, "Team:", self.team, "Role:", self.role)
        
    def getSalary(self):
        print("Salary:", self.__salary)
        
class batter(personnel):
    def __init__(self, name, age, team, role, salary, atbats, hits, doubles, triples, HR, walks):
        personnel.__init__(self, name, age, team, role, salary)
        self.atbats = atbats
        self.hits = hits
        self.doubles = doubles
        self.triples = triples
        self.hr = HR
        self.walks = walks
        
    
    def batavg(self):
        if self.atbats == 0:
            print("Cannot calculate batting average with no atbats")
        elif self.atbats < self.hits:
            print("Incorrect input cannot have an average higher than 1 or more hits than atbats")
        else:
            return self.hits/self.atbats
    
    def slugging(self):
        try:
            if self.atbats == 0:
                print("Cannot calculated slugging percentage with no atbats")
            elif self.hits > self.atbats:
                print("Cannot have more hits than atbats")
            else:
                return (self.totalbase())/(self.atbats)
        except:
            pass

    def onbase(self):
        if self.atbats+self.walks == 0:
            print("Cannot calculate onbase with no plate appearances or walks")
        elif self.hits > self.atbats:
            print("Incorrect input cannot have an average higher than 1 or more hits than atbats")
        else:
            return (self.hits+self.walks)/(self.atbats+self.walks)
    
    def obps(self):
        return self.slugging()+self.onbase()
    
    def obps(self):
        try:
            return self.slugging()+self.onbase()
        except:
            pass
    
    def walkrate(self):
        if self.atbats+self.walks == 0:
            print("Cannot calculate walkrate with no plate appearances or walks")
        else:
            return self.walks/(self.walks+self.atbats)
    
    def singles(self):
        if self.doubles+self.triples+self.hr > self.hits:
            print("Incorrect input cannot have more extra base hits than hits")
        else:
            return (self.hits-self.doubles-self.triples-self.hr)
    
    def display(self):
        personnel.display(self)
        print("At bats:", self.atbats, "Hits:", self.hits, "Doubles:", self.doubles, "Triples:", self.triples, "Home Runs:", self.hr, "Walks:", self.walks)
    
    def simplateappearances(self, plateappearances):
        import numpy as np
        outcome = []
        j=np.random.rand(10)

        for i in range(0,len(j)):
            if j[i] < self.batavg():
                outcome.append(1)
            else:
                outcome.append(0)
        
        for i in range(0, len(outcome)):
            if outcome[i] == 1:
                test = np.random.rand(1)
                if test < self.singles()/self.hits:
                    outcome[i] = 1
                elif test < (self.singles()+self.doubles)/self.hits:
                    outcome[i] = 2
                elif test < (self.singles()+self.doubles+self.triples)/self.hits:
                    outcome[i] = 3
                else:
                    outcome[i] = 4
        
        return outcome
    
    def count(self, x):
        singles = 0
        doubles = 0
        triples = 0
        homeruns = 0
        hits = 0
        for i in x:
            if i == 1:
                singles += 1
                hits += 1
            elif i == 2:
                doubles += 1
                hits += 1
            elif i == 3:
                triples += 1
                hits += 1
            elif i == 4:
                homeruns +=1
                hits += 1
        print("In", len(x), "at bats:", singles, "singles,", doubles, "doubles,", triples, "triples,", homeruns, "homeruns, for", hits, "total hits")
        y=[len(x), hits, doubles ,triples, homeruns]
        return y


# In[8]:





# In[ ]:




