#%%
#graph database

import os
from dotenv import load_dotenv

load_dotenv(".env")
PASSWORD = os.getenv("NEO4J_PASSWORD")
URI = os.getenv("NEO4J_URI")
USERNAME= os.getenv("NEO4J_USER")
AUTH = (USERNAME, PASSWORD)

# %%
# making a csv
import json
import pandas as pd
import numpy as np


# %%
sample_json_path = "data/json_data/19_Monster.json"
sample_json = json.load(open(sample_json_path,"r"))["data"]
# %%
from neo4j import GraphDatabase
import os
from neomodel import config
my_driver = GraphDatabase().driver(URI, auth=AUTH)
config.DRIVER = my_driver

# %%
from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
     ArrayProperty ,UniqueIdProperty, RelationshipTo, FloatProperty, DateProperty)
from neomodel.contrib import  SemiStructuredNode

#%%
#%%
class Date(StructuredNode):
    Date = DateProperty()

class Synonyms(StructuredNode):#1
    Synonyms_array = ArrayProperty(StringProperty())

class Genre(StructuredNode):#2
    genre = StringProperty()
    mal_id = IntegerProperty(unique_index=True)

class Producer(StructuredNode):#3
    name = StringProperty()
    url = StringProperty()
    type = StringProperty()
    mal_id = IntegerProperty(unique_index=True)

class Themes(StructuredNode):
    name = StringProperty()
    url = StringProperty()
    type = StringProperty()
    mal_id = IntegerProperty(unique_index=True)
    
    
class Demographics(StructuredNode):
    name = StringProperty()
    url = StringProperty()
    type = StringProperty()
    mal_id = IntegerProperty(unique_index=True)

class Manga(StructuredNode):
    name = StringProperty()
    url = StringProperty()
    type = StringProperty()
    mal_id = IntegerProperty(unique_index=True)
    
class Studios(StructuredNode):
    name = StringProperty()
    url = StringProperty()
    type = StringProperty()
    mal_id = IntegerProperty(unique_index=True)
#%%
class Anime(SemiStructuredNode):
    mal_id = IntegerProperty(unique_index=True)#
    url = StringProperty()#
    title = StringProperty()#
    type = StringProperty()#
    source = StringProperty()#
    episodes = IntegerProperty()#
    status = StringProperty()#
    airing = StringProperty()#
    duration = StringProperty()#
    rating = StringProperty()#
    score = FloatProperty()#
    scored_by = IntegerProperty()#
    rank = IntegerProperty()#
    popularity = IntegerProperty()#
    members = IntegerProperty()#
    favorites = IntegerProperty()#
    synopsis = StringProperty()#
    background = StringProperty()#
    season = StringProperty()#
    year = DateProperty()


    # Relationships
    aired_from = RelationshipTo(Date, 'aired_from')
    aired_till = RelationshipTo(Date, 'aired_till')
    broadcasted = RelationshipTo(Date, 'Broadcasted_on')
    genres = RelationshipTo(Genre, 'is_of_genre')
    
    
    producers = RelationshipTo(Producer, 'produced')
    studios = RelationshipTo(Studios, 'made')
    themes = RelationshipTo(Themes, 'is_of_theme')
    demographics = RelationshipTo(Demographics, 'is_of_demographic')
    manga = RelationshipTo(Manga, 'is adapted from')
    synonyms= RelationshipTo(Synonyms,'is aslo called')
    
    
#%%

# Function to process one node
def process_anime_node(anime_data):
    pass #to do