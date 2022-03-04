# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 12:23:58 2022

@author: Admin
"""
import networkx as nx

class Simulation():
    
    """Creating and drawing network, creating variables for value holding""" 
    def __init__(self, nodesnr):
        self.nodesnr = nodesnr
        self.G = nx.erdos_renyi_graph(nodesnr, 0.3) 
        #self.G = nx.barabasi_albert_graph(nodesnr, 2)
        #self.G = nx.watts_strogatz_graph(nodesnr, 2, 1)

        nx.draw_networkx(self.G);
        
        self.friends = []
        self.friendfriendcount = 0
        self.personfriendcount = []
        self.paradoxtrue = 0
        self.paradoxfalse = 0

    """Method calling other methods responsible for simulations"""
    def simulate(self):
        self.getfriendsofallpeople()
        self.getallfriends()
        self.avgpersonfriends()
        self.results(self.G)
        self.paradoxtest()

    """Creates sorted list of all neighbors (friends) of each node (person)"""
    def getallfriends(self):
        for person in self.G:
            fl = list(self.G.neighbors(person))
            for x in fl:
                self.friends.append(x)
        self.friends.sort()
    
    """Gets numbers of friends of each person"""        
    def getfriendsofallpeople(self):
        for node in self.G:
            #print(node, list(G.neighbors(node)))
            self.personfriendcount.append(len(list(self.G.neighbors(node))))
    
    """Says, how many friends does an average PERSON (random person) have"""
    def avgpersonfriends(self):
        print(f"Average person has {sum(self.personfriendcount)/len(self.personfriendcount)} friends.")
        
    """Determines, how many friends does an average FRIEND 
        (random persons friend) have"""
    def avgfriendfriend(self, kappa):      
        if kappa == []:
            return 0
        else:
            kap = sum(kappa)/len(kappa)
            return kap
        
    """Tests, if the friendship paradox works in current network"""
    def paradoxtest(self):
        if self.paradoxtrue > self.paradoxfalse:
            print("Friendship paradox in the current network works!")
            print("This means, that if we pick random persons friend,")
            print(f"he will have more friends than the first person in {self.paradoxtrue/self.nodesnr*100} % of cases.")
        else:
            print("Friendship paradox in the current network doesnt work!")
            print("This means, that if we pick random persons friend,")
            print(f"he will have more friends than the first person only in {self.paradoxtrue/self.nodesnr*100} % of cases.")
    
    """Calculates number of friends of friends
        and prints the results to the console"""
    def results(self, x):
        for node in x:
            friendsoffriends = [nx.degree(x, v) for v in x.neighbors(node)]
            self.friendfriendcount = (self.friendfriendcount + 
                                      (self.avgfriendfriend(friendsoffriends)))
            if self.avgfriendfriend(friendsoffriends) > x.degree(node):
                self.paradoxtrue = self.paradoxtrue + 1
            else:
                self.paradoxfalse = self.paradoxfalse + 1    
                
            print("_____________________")
            print(f"Stats for Node index: {node}")
            print(f"Number of friends: {x.degree(node)}")
            print(f"Average friend of this person has this many friends: {self.avgfriendfriend(friendsoffriends)}")
       
        print("__________________")
        print(" ")
        print("In this network:")
        print(f"Average person has {sum(self.personfriendcount)/len(self.personfriendcount)} friends")    
        print(f"Average friend of a person has {self.friendfriendcount/x.number_of_nodes()} friends")

s = Simulation(100)
s.simulate()