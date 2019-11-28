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
        print("Name:", self.name, "Age:", self.age, "Team:", self.team, "Role:", self.role)
        
    def getSalary(self):
        print("Salary:", self.__salary)
        
def batavg(atbats, hits):
    if atbats == 0:
        print("Cannot calculate batting average with no atbats")
    elif atbats < hits:
        print("Incorrect input cannot have an average higher than 1 or more hits than atbats")
    else:
        return hits/atbats
    
def singles(hits, doubles, triples, HR):
    if doubles+triples+HR > hits:
        print("Incorrect input cannot have more extra base hits than hits")
    else:
        return (hits-doubles-triples-HR)
    
def onbase(atbats, hits, walks):
    if atbats+walks == 0:
        print("Cannot calculate onbase with no plate appearances or walks")
    elif hits > atbats:
        print("Incorrect input cannot have an average higher than 1 or more hits than atbats")
    else:
        return (hits+walks)/(atbats+walks)

def totalbase(hits, doubles, triples, HR):
    try:
        return (singles(hits, doubles, triples, HR)+ 2*doubles + 3*triples + 4*HR)
    except:
        pass
    
def krate(atbats, K):
    if atbats == 0:
        print("cannot calculate a rate with no atbats")
    elif K > atbats:
        print("Incorrect input cannot have more K than atbats")
    else:
        return K/atbats


def slugging(atbats, hits, doubles, triples, hr):
    try:
        if atbats == 0:
            print("Cannot calculated slugging percentage with no atbats")
        elif hits > atbats:
            print("Cannot have more hits than atbats")
        else:
            return (totalbase(hits, doubles, triples, hr))/(atbats)
    except:
        pass
 
def obps(atbats, hits, doubles, triples, hr, walks):
    try:
        return slugging(atbats, hits, doubles, triples, hr)+onbase(atbats, hits, walks)
    except:
        pass
    
def walkrate(atbats, walks):
    if atbats+walks == 0:
        print("Cannot calculate walkrate with no plate appearances or walks")
    else:
        return walks/(walks+atbats)


# In[ ]:




