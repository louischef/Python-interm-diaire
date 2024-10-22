import requests
import json
import pycountry 
import time

# afficher le total, si le total est supérieur à 160 alors
# segmenter par age
payload = {}
headers = {
  'cookie': '_ga=GA1.1.1918504426.1728396486; _ga_T6YTNDVC1F=GS1.1.1728405026.2.0.1728405026.0.0.0',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-encoding': 'gzip, deflate, br, zstd',
  'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
  'cache-control': 'max-age=0',
  'priority': 'u=0, i',
  'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8"," "Chromium";v="129":',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'none',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36:'
}

def getData(payload: dict, headers: dict, country: pycountry, ageMin: int, ageMax: int) -> dict:
    url = f"https://ws-public.interpol.int/notices/v1/red?nationality={country.alpha_2}&ageMax={ageMax}&ageMin={ageMin}"
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code != 200:
        print(f"Erreur lors de la requête: {response.status_code}")
        return {"total": 0, "notices": []}
    json_object = json.loads(response.text)
    total = json_object["total"]
    if total > 160:
        new_age = (ageMin+ ageMax) // 2 #diviser l'age à chaque fois par deux pour affiner
        getData(payload, headers, pycountry.countries.get(alpha_2='RU'), ageMin, new_age) # donc à chaque fois qu'il y a trop de requete, il affinera avec le nouvel age
        getData(payload, headers, pycountry.countries.get(alpha_2='RU'), new_age, ageMax) 
        print(new_age)
    return json_object


def loadJsonData(data):
    with open(f'data.json', 'w', encoding='utf-8') as f:
      json.dump(data, f, ensure_ascii=False, indent=4)

