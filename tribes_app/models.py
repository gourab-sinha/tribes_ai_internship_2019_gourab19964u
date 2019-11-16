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
    query = "MATCH (j:%s {%s:'%s'}) RETURN j.%s"%(nodetype,nodeattr,str(nodeid),nodeattr)
    obj = session.run(query).single()
    return obj


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
        team_id =  findnode(self.nodetype,self.nodeattr,self.team_id)
        if team_id is None:
            query = '''CREATE(n:Team{team_name:"%s",%s:"%s"}) RETURN n.team_id'''%(self.team_name,self.nodeattr,self.team_id)
            team_id = session.run(query).single()[0]
            for member in self.members:
                memberObj = Member(member)
                player_id = memberObj.createmember()
                query = '''MATCH (a:Player),(b:Team)
                           WHERE a.player_id = '%s' AND b.team_id = '%s'
                           CREATE (a)-[:Play_for]->(b)'''%(player_id,team_id)
                session.run(query)



class Member:
    def __init__(self,memberObj):
        self.member_name = memberObj["name"]
        self.member_id = memberObj["player_id"]
        self.member_age = memberObj["age"]
        self.nodetype = "Player"
        self.nodeattr = "player_id"

    def createmember(self):
        member =  findnode(self.nodetype,self.nodeattr,self.member_id)
        if member is None:
            query = '''CREATE(n:Player{player_name:"%s",%s:"%s",age:"%s"}) RETURN n.player_id'''%(self.member_name,self.nodeattr,self.member_id,self.member_age)
            member = session.run(query).single()[0]
            return member

        for m_id in member:
            return m_id


class Ground:
    def __init__(self,groundObj):
        self.ground_name = groundObj["ground_id"]
        self.ground_id = groundObj["ground_id"]
        self.ground_loc = groundObj["location"]
        self.ground_host = groundObj["host_international"]
        self.nodetype = "Ground"
        self.nodeattr = "ground_id"

    def createground(self):
        ground_id =  findnode(self.nodetype,self.nodeattr,self.ground_id) 
        if ground_id is None:
            query = '''CREATE(n:Ground{ground_name:"%s",%s:"%s",
                       host_international:"%s"}) RETURN n.ground_id'''%(
                       self.ground_name,self.nodeattr,self.ground_id,self.ground_host)

            if self.ground_host is True:
                international = {"name":"International","id":"International"}
                intObj = International(international)
                int_id = intObj.createinternational()
            else:
                international = {"name":"Domestic","id":"Domestic"}
                intObj = International(international)
                int_id = intObj.createinternational()

            ground_id = session.run(query).single()[0]
            city_id = City(self.ground_loc).createcity()
            state_id = State(self.ground_loc).createstate()
            country_id = Country(self.ground_loc).createcountry()
            query = '''MATCH (a:Ground),(b:City)
                           WHERE a.ground_id = '%s' AND b.city_id = '%s'
                           CREATE (a)-[r:at]->(b)'''%(ground_id,city_id)
            session.run(query)
            query = '''MATCH (a:City),(b:State)
                           WHERE a.city_id = '%s' AND b.state_id = '%s'
                           CREATE (a)-[r:in]->(b)'''%(city_id,state_id)
            session.run(query)
            query = '''MATCH (a:State),(b:Country)
                           WHERE a.state_id = '%s' AND b.country_id = '%s'
                           CREATE (a)-[r:in]->(b)'''%(state_id,country_id)
            session.run(query)
            query = '''MATCH (a:Ground),(b:International)
                           WHERE a.ground_id = '%s' AND b.int_id = '%s'
                           CREATE (a)-[r:hosts]->(b)'''%(ground_id,int_id)
            session.run(query)
            return ground_id

        # return ground_id[0][self.nodeattr]
        for g_id in ground_id:
            return g_id



class City:
    def __init__(self,cityObj):
        self.city_name = cityObj["city"]
        self.city_id = cityObj["city"]
        self.nodetype = "City"
        self.nodeattr = "city_id"

    def createcity(self):
        city_id =  findnode(self.nodetype,self.nodeattr,self.city_id)
        if city_id is None:
            query = '''CREATE(n:City{city_name:"%s",%s:"%s"}) RETURN n.city_id'''%(self.city_name,self.nodeattr,self.city_id)
            city_id = session.run(query).single()[0]
            return city_id

        for c_id in city_id:
            return c_id

class State:
    def __init__(self,stateObj):
        self.state_name = stateObj["state"]
        self.state_id = stateObj["state"]
        self.nodetype = "State"
        self.nodeattr = "state_id"

    def createstate(self):
        state_id =  findnode(self.nodetype,self.nodeattr,self.state_id)
        if state_id is None:
            query = '''CREATE(n:State{state_name:"%s",%s:"%s"}) RETURN n.state_id'''%(self.state_name,self.nodeattr,self.state_id)
            state_id = session.run(query).single()[0]
            return state_id

        for s_id in state_id:
            return s_id

class Country:
    def __init__(self,countryObj):
        self.country_name = countryObj["country"]
        self.country_id = countryObj["country"]
        self.nodetype = "Country"
        self.nodeattr = "country_id"

    def createcountry(self):
        country_id =  findnode(self.nodetype,self.nodeattr,self.country_id)
        if country_id is None:
            query = '''CREATE(n:Country{country_name:"%s",
                       %s:"%s"}) RETURN n.country_id'''%(self.country_name,
                       self.nodeattr,self.country_id)
            country_id = session.run(query).single()[0]
            return country_id

        for c_id in country_id:
            return c_id

class International:
    def __init__(self,internationalObj):
        self.name = internationalObj["name"]
        self.int_id = internationalObj["id"]
        self.nodetype = "International"
        self.nodeattr = "int_id"

    def createinternational(self):
        int_id = findnode(self.nodetype,self.nodeattr,self.int_id)
        if int_id is None:
            query = '''CREATE(n:International{name:"%s",int_id:"%s"}) RETURN n.int_id'''%(self.name,self.int_id)
            int_id = session.run(query).single()[0]
            return int_id

        for i_id in int_id:
            return i_id

class Match:
    def __init__(self,sportObj):
        self.match_name = sportObj["name"]
        self.match_id = sportObj["match_id"]
        self.team_sport = sportObj["team_sport"]
        self.members_count = sportObj["members_count"]
        self.match_date = sportObj["match_date"]
        self.match_winner = sportObj["winner_team_id"]
        self.match_player = sportObj["player_of_the_match"]
        self.match_ground = sportObj["ground_id"]
        self.nodetype = "Match"
        self.nodeattr = "match_id"

    def creatematch(self,teamObj):
        match_id =  findnode(self.nodetype,self.nodeattr,self.match_id)
        if match_id is None:
            query = '''CREATE(n:Match{
                       match_name:"%s",
                       match_id:"%s",
                       team_sport:"%s",
                       members_count:"%s",
                       match_date:"%s"
                       }) RETURN n.match_id'''%(self.match_name,
                       self.match_id,
                       self.team_sport,
                       self.members_count,
                       self.match_date)
            match_id = session.run(query).single()[0]
            query = '''MATCH (a:Match),(b:Player)
                           WHERE a.match_id = "%s" AND b.player_id = "%s"
                           CREATE (a)-[r:PLAYER_OF_THE_MATCH]->(b)'''%(match_id,self.match_player)
            session.run(query)
            query = '''MATCH (a:Match),(b:Ground)
                           WHERE a.match_id = "%s" AND b.ground_id = "%s"
                           CREATE (a)-[r:PLAYER_AT]->(b)'''%(match_id,self.match_ground)
            session.run(query)
            print(teamObj)
            for team in teamObj:
                team_id = team["id"]
                print(team_id)
                print("List of teams")
                query = '''MATCH (a:Team),(b:Match)
                           WHERE a.player_id = "%s" AND b.macth_id = "%s"
                           CREATE (a)-[r:PLAYED]->(b)'''%(team_id,match_id)
                session.run(query)
                query = '''MATCH (a:Team),(b:Team)
                           WHERE a.player_id = "%s" AND b.macth_id = "%s"
                           CREATE (a)-[r:PLAYED_WITH]->(b)'''%(team_id,self.match_winner)
                session.run(query)












