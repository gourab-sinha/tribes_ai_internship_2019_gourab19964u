#!/usr/bin/env python3
# -------------------------------------------------
# IMPORTS
# -------------------------------------------------
from neo4j import GraphDatabase
from datetime import datetime
from .views import graph
import datetime

# Session
session = graph.session()


# Function to find a node in Graph Database to avoid redundency
def find_node(node_type, node_attr, node_id):
    query = "MATCH (j:%s {%s:'%s'}) RETURN j.%s" % (node_type, node_attr, str(node_id), node_attr)
    obj = session.run(query).single()
    return obj


# -------------------------------------------------
# NODE CLASSES
# -------------------------------------------------
class Team:

    def __init__(self, team_obj):
        self.team_name = team_obj["name"]
        self.team_id = team_obj["id"]
        self.members = team_obj["members"]
        self.node_type = "Team"
        self.node_attr = "team_id"
        self.time_created = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def create_team(self):
        team_id = find_node(self.node_type, self.node_attr, self.team_id)
        if team_id is None:
            query = '''CREATE(n:Team{team_name:"%s",%s:"%s",time_created:"%s"}) 
                       RETURN n.team_id''' % (self.team_name, self.node_attr, self.team_id, self.time_created)
            team_id = session.run(query).single()[0]
            for member in self.members:
                member_obj = Member(member)
                player_id = member_obj.create_member()
                query = '''MATCH (a:Player),(b:Team)
                           WHERE a.player_id = '%s' AND b.team_id = '%s'
                           CREATE (a)-[:PlAY_FOR]->(b)''' % (player_id, team_id)
                session.run(query)


class Member:
    def __init__(self, member_obj):
        self.member_name = member_obj["name"]
        self.member_id = member_obj["player_id"]
        self.member_age = member_obj["age"]
        self.node_type = "Player"
        self.node_attr = "player_id"
        self.time_created = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def create_member(self):
        member = find_node(self.node_type, self.node_attr, self.member_id)
        if member is None:
            query = '''CREATE(n:Player{player_name:"%s",%s:"%s",age:"%s",time_created:"%s"}) 
                       RETURN n.player_id''' % (
                       self.member_name, self.node_attr, self.member_id, self.member_age, self.time_created)
            member = session.run(query).single()[0]
            return member

        for m_id in member:
            return m_id


class Ground:
    def __init__(self, ground_obj):
        self.ground_name = ground_obj["ground_id"]
        self.ground_id = ground_obj["ground_id"]
        self.ground_loc = ground_obj["location"]
        self.ground_host = ground_obj["host_international"]
        self.node_type = "Ground"
        self.node_attr = "ground_id"
        self.time_created = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def create_ground(self):
        ground_id = find_node(self.node_type, self.node_attr, self.ground_id)
        if ground_id is None:
            query = '''CREATE(n:Ground{ground_name:"%s",%s:"%s",
                       host_international:"%s",time_created:"%s"}) RETURN n.ground_id''' % (
                       self.ground_name, self.node_attr, self.ground_id, self.ground_host, 
                       self.time_created)

            if self.ground_host is True:
                international = {"name": "International", "id": "International"}
                int_obj = International(international)
                int_id = int_obj.create_international()
            else:
                international = {"name": "Domestic", "id": "Domestic"}
                int_obj = International(international)
                int_id = int_obj.create_international()

            ground_id = session.run(query).single()[0]
            city_id = City(self.ground_loc).createcity()
            state_id = State(self.ground_loc).create_state()
            country_id = Country(self.ground_loc).create_country()
            query = '''MATCH (a:Ground),(b:City)
                           WHERE a.ground_id = '%s' AND b.city_id = '%s'
                           CREATE (a)-[r:PRESENT_AT]->(b)''' % (ground_id, city_id)
            session.run(query)
            query = '''MATCH (a:City),(b:State)
                           WHERE a.city_id = '%s' AND b.state_id = '%s'
                           CREATE (a)-[r:PRESENT_IN]->(b)''' % (city_id, state_id)
            session.run(query)
            query = '''MATCH (a:State),(b:Country)
                           WHERE a.state_id = '%s' AND b.country_id = '%s'
                           CREATE (a)-[r:PRESENT_IN]->(b)''' % (state_id, country_id)
            session.run(query)
            query = '''MATCH (a:Ground),(b:International)
                           WHERE a.ground_id = '%s' AND b.int_id = '%s'
                           CREATE (a)-[r:HOSTS]->(b)''' % (ground_id, int_id)
            session.run(query)
            return ground_id

        for g_id in ground_id:
            return g_id


class City:
    def __init__(self, city_obj):
        self.city_name = city_obj["city"]
        self.city_id = city_obj["city"]
        self.node_type = "City"
        self.node_attr = "city_id"
        self.time_created = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def createcity(self):
        city_id = find_node(self.node_type, self.node_attr, self.city_id)
        if city_id is None:
            query = '''CREATE(n:City{city_name:"%s",%s:"%s",time_created:"%s"}) 
                       RETURN n.city_id''' % (self.city_name, self.node_attr, 
                       self.city_id, self.time_created)
            city_id = session.run(query).single()[0]
            return city_id

        for c_id in city_id:
            return c_id


class State:
    def __init__(self, state_obj):
        self.state_name = state_obj["state"]
        self.state_id = state_obj["state"]
        self.node_type = "State"
        self.node_attr = "state_id"
        self.time_created = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def create_state(self):
        state_id = find_node(self.node_type, self.node_attr, self.state_id)
        if state_id is None:
            query = '''CREATE(n:State{state_name:"%s",%s:"%s",time_created:"%s"}) 
                       RETURN n.state_id''' % (self.state_name, self.node_attr, 
                       self.state_id, self.time_created)
            state_id = session.run(query).single()[0]
            return state_id

        for s_id in state_id:
            return s_id


class Country:
    def __init__(self, country_obj):
        self.country_name = country_obj["country"]
        self.country_id = country_obj["country"]
        self.node_type = "Country"
        self.node_attr = "country_id"
        self.time_created = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def create_country(self):
        country_id = find_node(self.node_type, self.node_attr, self.country_id)
        if country_id is None:
            query = '''CREATE(n:Country{country_name:"%s",
                       %s:"%s",time_created:"%s"}) 
                       RETURN n.country_id''' % (self.country_name, 
                       self.node_attr, self.country_id, self.time_created)
            country_id = session.run(query).single()[0]
            return country_id

        for c_id in country_id:
            return c_id


class International:
    def __init__(self, international_obj):
        self.name = international_obj["name"]
        self.int_id = international_obj["id"]
        self.node_type = "International"
        self.node_attr = "int_id"
        self.time_created = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def create_international(self):
        int_id = find_node(self.node_type, self.node_attr, self.int_id)
        if int_id is None:
            query = '''CREATE(n:International{name:"%s",int_id:"%s",time_created:"%s"}) 
                       RETURN n.int_id''' % (self.name, self.int_id, self.time_created)
            int_id = session.run(query).single()[0]
            return int_id

        for i_id in int_id:
            return i_id


class Match:
    def __init__(self, sport_obj):
        self.match_name = sport_obj["name"]
        self.match_id = sport_obj["match_id"]
        self.team_sport = sport_obj["team_sport"]
        self.members_count = sport_obj["members_count"]
        self.match_date = sport_obj["match_date"]
        self.match_winner = sport_obj["winner_team_id"]
        self.match_player = sport_obj["player_of_the_match"]
        self.match_ground = sport_obj["ground_id"]
        self.node_type = "Match"
        self.node_attr = "match_id"
        self.time_created = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def create_match(self, team_obj):
        match_id = find_node(self.node_type, self.node_attr, self.match_id)
        if match_id is None:
            query = '''CREATE(n:Match{match_name:"%s", match_id:"%s",
                       team_sport:"%s", members_count:"%s",
                       match_date:"%s", time_created:"%s"
                       }) RETURN n.match_id''' % (self.match_name,
                       self.match_id, self.team_sport,
                       self.members_count, self.match_date,
                       self.time_created)
            match_id = session.run(query).single()[0]
            query = '''MATCH (a:Match),(b:Player)
                           WHERE a.match_id = "%s" AND b.player_id = "%s"
                           CREATE (a)-[r:PLAYER_OF_THE_MATCH]->(b)''' % (match_id, self.match_player)
            session.run(query)
            query = '''MATCH (a:Match),(b:Ground)
                       WHERE a.match_id = "%s" AND b.ground_id = "%s"
                       CREATE (a)-[r:PLAYED_AT]->(b)''' % (match_id, self.match_ground)
            session.run(query)

            query = '''MATCH (a:Match),(b:Team)
                       WHERE a.match_id = "%s" AND b.team_id="%s"
                       CREATE (a)-[r:WINNER]->(b)''' % (match_id, self.match_winner)
            session.run(query)
            for team in team_obj:
                team_id = team["id"]
                query = '''MATCH (a:Team),(b:Match)
                           WHERE a.team_id = "%s" AND b.match_id ="%s"
                           CREATE (a)-[r:PLAYED]->(b)''' % (team_id, match_id)
                session.run(query)
                if team_id != self.match_winner:
                    query = '''MATCH(a:Team),(b:Team)
                               WHERE a.team_id = "%s" AND b.team_id = "%s"
                               CREATE (a)-[r:PLAYED_WITH]->(b)''' % (team_id, self.match_winner)
                    session.run(query)
