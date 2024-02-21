#%%
#graph database

import os
from dotenv import load_dotenv
from datetime import datetime

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
     ArrayProperty ,UniqueIdProperty, RelationshipTo, FloatProperty, DateProperty, JSONProperty)
from neomodel.contrib import  SemiStructuredNode

#%%
#%%
# class Date(StructuredNode):
#     Date = DateProperty(unique_index=True)

# class Synonyms(StructuredNode):#1
#     Synonyms_array = ArrayProperty(StringProperty())

class Genre(StructuredNode):#2
    genre = StringProperty()
    mal_id = IntegerProperty(unique_index=True)

    @classmethod
    def get_or_create(cls, mal_id,name):
        class_node = cls.nodes.first_or_none(mal_id=mal_id)
        if class_node is None:
            class_node = cls(mal_id=mal_id,genre=name)
            class_node.save()
        return class_node
    
class Producer(StructuredNode):#3
    name = StringProperty()
    url = StringProperty()
    type = StringProperty()
    mal_id = IntegerProperty(unique_index=True)

    @classmethod
    def get_or_create(cls, mal_id,url,type,name):
        class_node = cls.nodes.first_or_none(mal_id=mal_id)
        if class_node is None:
            class_node = cls(mal_id=mal_id,url=url,type=type,name=name)
            class_node.save()
        return class_node
class Themes(StructuredNode):
    name = StringProperty()
    url = StringProperty()
    type = StringProperty()
    mal_id = IntegerProperty(unique_index=True)
    
    @classmethod
    def get_or_create(cls, mal_id,url,type,name):
        class_node = cls.nodes.first_or_none(mal_id=mal_id)
        if class_node is None:
            class_node = cls(mal_id=mal_id,url=url,type=type,name=name)
            class_node.save()
        return class_node
    
class Demographics(StructuredNode):
    name = StringProperty()
    url = StringProperty()
    type = StringProperty()
    mal_id = IntegerProperty(unique_index=True)

    @classmethod
    def get_or_create(cls, mal_id,url,type,name):
        class_node = cls.nodes.first_or_none(mal_id=mal_id)
        if class_node is None:
            class_node = cls(mal_id=mal_id,url=url,type=type,name=name)
            class_node.save()
        return class_node
class Manga(StructuredNode):
    name = StringProperty()
    url = StringProperty()
    type = StringProperty()
    mal_id = IntegerProperty(unique_index=True)
    
    @classmethod
    def get_or_create(cls, mal_id,url,type,name):
        class_node = cls.nodes.first_or_none(mal_id=mal_id)
        if class_node is None:
            class_node = cls(mal_id=mal_id,url=url,type=type,name=name)
            class_node.save()
        return class_node
class Studios(StructuredNode):
    name = StringProperty()
    url = StringProperty()
    type = StringProperty()
    mal_id = IntegerProperty(unique_index=True)
    
    @classmethod
    def get_or_create(cls, mal_id,url,type,name):
        class_node = cls.nodes.first_or_none(mal_id=mal_id)
        if class_node is None:
            class_node = cls(mal_id=mal_id,url=url,type=type,name=name)
            class_node.save()
        return class_node
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
    year = IntegerProperty()
    synonyms = JSONProperty()

    # Relationships
    # aired_from = RelationshipTo(Date, 'aired_from')
    # aired_till = RelationshipTo(Date, 'aired_till')
    # broadcasted = RelationshipTo(Date, 'Broadcasted_on')
    genres = RelationshipTo(Genre, 'is_of_genre')
    
    
    producers = RelationshipTo(Producer, 'produced')
    studios = RelationshipTo(Studios, 'made')
    themes = RelationshipTo(Themes, 'is_of_theme')
    demographics = RelationshipTo(Demographics, 'is_of_demographic')
    manga = RelationshipTo(Manga, 'is adapted from')
    # synonyms= RelationshipTo(Synonyms,'is aslo called')
    anime = RelationshipTo("Anime",relation_type="related to")
    
#%%

unique_relations_types= ['Side story', 'Parent story', 'Character', 'Sequel', 'Other', 'Adaptation', 'Spin-off', 'Prequel', 'Alternative setting', 'Alternative version', 'Full story', 'Summary']


#%%# ... 
def node_exists(node_class, mal_id_):
    obj = node_class.nodes.first_or_none(mal_id=mal_id_)
    if( obj == None):
        return False
    else:
        return True
        


#%%
anime_manga_relationships = []
anime_anime_relationships = []

# Function to process one node
def process_anime_node(anime_json):
    # pass #to do
    anime_data = anime_json["data"]
    mal_id = anime_data.get("mal_id")
    
    if not node_exists(Anime,mal_id):
        
        url = anime_data.get("url")
        title = anime_data.get("title")
        anime_type = anime_data.get("type")
        source = anime_data.get("source")
        episodes = anime_data.get("episodes")   
        status = anime_data.get("status")
        airing = anime_data.get("airing")
        duration = anime_data.get("duration")
        rating = anime_data.get("rating")
        score = anime_data.get("score")
        scored_by = anime_data.get("scored_by")
        rank = anime_data.get("rank")
        popularity = anime_data.get("popularity")
        members = anime_data.get("members")
        favorites = anime_data.get("favorites")
        synopsis = anime_data["synopsis"]
        background = anime_data.get("background")
        season = anime_data.get("season")
        year = anime_data.get("year")
        synonyms_ = anime_data.get("titles")

        # Creating Anime node
        
            
        anime_node = Anime(mal_id=mal_id, url=url, title=title, type=anime_type, source=source, episodes=episodes,
                        status=status, airing=airing, duration=duration, rating=rating, score=score,
                        scored_by=scored_by, rank=rank, popularity=popularity, members=members,
                        favorites=favorites, synopsis=synopsis, background=background, season=season, year=year,synonyms=synonyms_)
        anime_node.save()  # Save the anime_node

        
        # Creating Genre nodes and relationships
        genres_data = anime_data.get("genres", [])
        for genre_data in genres_data:
            genre_node = Genre.get_or_create(genre_data.get("mal_id"),genre_data.get("name"))
            anime_node.genres.connect(genre_node)

        # Creating Producers nodes and relationships
        producers_data = anime_data.get("producers", [])
        for producer_data in producers_data:
            producer_node = Producer.get_or_create(name=producer_data.get("name"), url=producer_data.get("url"),
                                type=producer_data.get("type"), mal_id=producer_data.get("mal_id"))

            anime_node.producers.connect(producer_node)

        # Creating Studios nodes and relationships
        studios_data = anime_data.get("studios", [])
        for studio_data in studios_data:
            studio_node = Studios.get_or_create(name=studio_data.get("name"), url=studio_data.get("url"),
                                type=studio_data.get("type"), mal_id=studio_data.get("mal_id"))

            anime_node.studios.connect(studio_node)

        # Creating Themes nodes and relationships
        themes_data = anime_data.get("themes", [])
        for theme_data in themes_data:
            theme_node = Themes.get_or_create(name=theme_data.get("name"), url=theme_data.get("url"),
                                type=theme_data.get("type"), mal_id=theme_data.get("mal_id"))
            anime_node.themes.connect(theme_node)

        # Creating Demographics nodes and relationships
        demographics_data = anime_data.get("demographics", [])
        for demographic_data in demographics_data:
            demographic_node = Demographics.get_or_create(name=demographic_data.get("name"), url=demographic_data.get("url"),
                                            type=demographic_data.get("type"), mal_id=demographic_data.get("mal_id"))
            anime_node.demographics.connect(demographic_node)
            
        # Save the anime_node again after all relationships are connected
        anime_node.save()

        relations = anime_data.get("relations", [])
        for rel in relations:
            relation_type = rel.get("relation")
            for ent  in rel.get("entry"):
                if ent.get("type") == "manga":
                    anime_manga_relationships.append(
                        {
                            "manga_mal_id": ent.get("mal_id"),
                            "anime_man_id": mal_id,
                            "relation_type": relation_type
                        }
                    )
                elif ent.get("type") == "anime":
                    anime_anime_relationships.append(
                        {
                            "anime_from": mal_id,
                            "anime_to": ent.get("mal_id"),
                            "relation_type": relation_type
                        }
                    )

    
    #Handling relations
    



# %%
# process a node
from tqdm import tqdm

folder_path = "data/json_data"

for filename in tqdm(os.listdir(folder_path)):
    if filename.endswith(".json"):
        file_path = os.path.join(folder_path, filename)

        # Read and process the JSON file
        with open(file_path, "r") as file:
            anime_json = json.load(file)
            process_anime_node(anime_json=anime_json)
        
# %%
relationships = {
    "anime_relations" : anime_anime_relationships,
    "manga_relations" : anime_manga_relationships
}
json.dump(relationships,open('data/relaionships.json','w'))

# %%
