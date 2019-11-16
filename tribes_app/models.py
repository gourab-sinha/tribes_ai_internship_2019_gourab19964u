#!/usr/bin/env python3
# -------------------------------------------------
# IMPORTS
# -------------------------------------------------
from neo4j import GraphDatabase
from datetime import datetime
import os
import uuid
import json
import codecs
from .views import graph

# Session 
session = graph.session()

# Find Function to find a node in Graph Database
def findnode(nodetype,nodeattr,nodeid):
    query = "MATCH (j:%s {%s: '%s'}) RETURN j.%s"%(nodetype,nodeattr,str(nodeid),nodeattr)
    obj = session.run(query)
    return obj.single()[0]


# -------------------------------------------------
# NODE CLASSES
# -------------------------------------------------
class Team:
    def __init__(self,teamObj):
        self.team_name = teamObj["name"]
        self.team_id = teamObj["id"]
        self.members = teamObj["members"]
        self.nodetype = "Team"
        self.nodeattr = "team_id"

    def createteam(self):
        team_id =  findnode(self.nodetype,self.nodeattr,self.nodeid)
        if team_id is None:
            query = "CREATE(n:Team{team_name:%s,%s:%s} RETURN n.team_id)"%(self.team_name,self.nodeattr,self.team_id)
            team_id = session.run(query).single()[0]
        for member in self.members:
            memberObj = Member(member)
            memeber_id = memberObj.createmember()
            query = '''MATCH (a:Member),(b:Team)
                       WHERE a.member_id = '%s' AND b.team_id = '%s'
                       CREATE (a)-[r:"plays for"]->(b)'''%(member_id,team_id)
            session.run(query)



class Member:
    def __init__(self,memberObj):
        self.member_name = memberObj["name"]
        self.member_id = memberObj["player_id"]
        self.member_age = memberObj["age"]
        self.nodetype = "Member"
        self.nodeattr = "memeber_id"

    def createmember(self):
        member =  findnode(self.nodetype,self.nodeattr,self.member_id)
        if member is None:
            query = "CREATE(n:Team{member_name:%s,%s:%s,age:%s} RETURN n.member_id)"%(self.member_name,self.nodeattr,self.member_id,self.member_age)
            member = session.run(query).single()[0]
            return member
        return member


class Ground:
    def __init__(self,groundObj):
        self.ground_name = groundObj["name"]
        self.ground_id = groundObj["ground_id"]
        self.ground_loc = groundObj["location"]
        self.groudn_host = groundObj["host_international"]
        self.nodetype = "Ground"
        self.nodeattr = "ground_id"
    def createground(self)
        ground_id =  findnode(self.nodetype,self.nodeattr,self.ground_id) 
        if ground_id is None:
            query = "CREATE(n:Ground{ground_name:%s,%s:%s,host_international:%s} RETURN n.ground_id)"%(self.ground_name,self.nodeattr,self.ground_id,self.groudn_host)
            ground_id = session.run(query).single()[0]

        city_id = City(ground_loc).createcity()
        state_id = State(ground_loc).createstate()
        country_id = Country(ground_loc).createcountry()
        query = '''MATCH (a:Ground),(b:City)
                       WHERE a.ground_id = '%s' AND b.city_id = '%s'
                       CREATE (a)-[r:"at"]->(b)'''%(ground_id,city_id)
        session.run(query)
        query = '''MATCH (a:City),(b:State)
                       WHERE a.city_id = '%s' AND b.state_id = '%s'
                       CREATE (a)-[r:in]->(b)'''%(city_id,state_id)
        session.run(query)
        query = '''MATCH (a:State),(b:Country)
                       WHERE a.state_id = '%s' AND b.country_id = '%s'
                       CREATE (a)-[r:in]->(b)'''%(state_id,country_id)
        session.run(query)



class City:
    def __init__(self,cityObj):
        self.city_name = cityObj["city"]
        self.city_id = cityObj["city"]
        self.nodetype = "City"
        self.nodeattr = "city_id"

    def createcity(self):
        city_id =  findnode(self.nodetype,self.nodeattr,self.city_id)
        if city_id is None:
            query = "CREATE(n:City{city_name:%s,%s:%s} RETURN n.city_id)"%(self.ground_name,self.nodeattr,self.city_id)
            city_id = session.run(query).single()[0]
            return city_id
        return city_id

class State:
    def __init__(self,stateObj):
        self.state_name = stateObj["state"]
        self.state_id = stateObj["state"]
        self.nodetype = "State"
        self.nodeattr = "state_id"

    def createstate(self):
        state_id =  findnode(self.nodetype,self.nodeattr,self.state_id)
        if state_id is None:
            query = "CREATE(n:State{state_name:%s,%s:%s} RETURN n.state_id)"%(self.state_name,self.nodeattr,self.state_id)
            state_id = session.run(query).single()[0]
            return state_id
        return state_id

class Country:
    def __init__(self,countryObj):
        self.country_name = countryObj["country"]
        self.country_id = countryObj["country"]
        self.nodetype = "Country"
        self.nodeattr = "country_id"

    def createcountry(self):
        country_id =  findnode(self.nodetype,self.nodeattr,self.country_id)
        if country_id is None:
            query = "CREATE(n:State{state_name:%s,%s:%s} RETURN n.country_id)"%(self.state_name,self.nodeattr,self.state_id)
            country_id = session.run(query).single()[0]
            return country_id
        return contry_id








