import requests
import time
import tqdm
import json
import re

base_url = "https://api.jikan.moe/v4/anime"

payload = {}
headers = {}


def replace_special_characters(input_string):

    result = re.sub(r"[^a-zA-Z0-9]", "_", input_string)
    return result


def main():
    for i in tqdm.tqdm(range(1, 26302)):

        response = requests.request(
            "GET", f"{base_url}/{i}/full", headers=headers, data=payload
        )
        if response.status_code == 200:
            res_json = response.json()

            mal_id = res_json["data"]["mal_id"]
            anime_name = replace_special_characters(
                res_json["data"]["titles"][0]["title"]
            )

            json.dump(res_json, open(f"data/json_data/{mal_id}_{anime_name}.json", "w"))
            json.dump(res_json, open(f"data/txt_data/{mal_id}_{anime_name}.txt", "w"))

            time.sleep(1)

if __name__=='__main__':
    main()