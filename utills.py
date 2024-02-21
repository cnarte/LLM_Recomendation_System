#%%
# making a list of unique relation types 
import os
import json
from tqdm import tqdm
# Folder path containing your JSON files
folder_path = "data/json_data"

# Set to store unique relationship types
unique_relation_types = set()

# Iterate through all files in the folder
for filename in tqdm(os.listdir(folder_path)):
    if filename.endswith(".json"):
        file_path = os.path.join(folder_path, filename)

        # Read and process the JSON file
        with open(file_path, "r") as file:
            anime_data = json.load(file)

            # Extract relations from the current anime data
            relations_data = anime_data["data"].get("relations", [])

            # Iterate through relations and extract relationship types
            for relation_data in relations_data:
                relation_type = relation_data.get("relation", "")
                
                unique_relation_types.add(relation_type)

        # Release memory by clearing the anime_data
        del anime_data

# Print the unique relationship types
print(unique_relation_types)
