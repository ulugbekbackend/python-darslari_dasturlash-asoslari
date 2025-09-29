import json
x=10
x_json=json.dumps(x)
ism="Ulug'bek"
ism_json=json.dumps(ism)
sonlar = [12, 45, 23, 67]
sonlar_json=json.dumps(sonlar)

bemor = {
  "ism": "Alijon Valiyev",
  "yosh": 30,
  "oila": True,
  "farzandlar": ("Ahmad","Bonu"),
  "allergiya": None,
  "dorilar": [
    {"nomi": "Analgin", "miqdori": 0.5},
    {"nomi": "Panadol", "miqdori": 1.2}
  ]
}

bemor_json = json.dumps(bemor,indent=4)
# print(bemor_json)

with open('bemor.json','w') as f:
    json.dump(bemor,f)

bemor =json.loads(bemor_json)
# print(bemor)

with open('bemor.json', 'r') as fayl:
    bemor=json.load(fayl)
# print(bemor)


data = {
    "address_components": [
        {
            "long_name": "Almazar District",
            "short_name": "Almazar District",
            "types": [
                "political",
                "sublocality",
                "sublocality_level_1"
            ]
        },
        {
            "long_name": "Tashkent",
            "short_name": "Tashkent",
            "types": [
                "locality",
                "political"
            ]
        },
        {
            "long_name": "Tashkent Region",
            "short_name": "Tashkent Region",
            "types": [
                "administrative_area_level_1",
                "political"
            ]
        },
        {
            "long_name": "Uzbekistan",
            "short_name": "UZ",
            "types": [
                "country",
                "political"
            ]
        }
    ],
    "formatted_address": "Almazar District, Tashkent, Uzbekistan",
    "geometry": {
        "bounds": {
            "northeast": {
                "lat": 41.3954567,
                "lng": 69.269883
            },
            "southwest": {
                "lat": 41.3249733,
                "lng": 69.16497629999999
            }
        },
        "location": {
            "lat": 41.3645355,
            "lng": 69.2281531
        },
        "location_type": "APPROXIMATE",
        "viewport": {
            "northeast": {
                "lat": 41.3954567,
                "lng": 69.269883
            },
            "southwest": {
                "lat": 41.3249733,
                "lng": 69.16497629999999
            }
        }
    },
    "place_id": "ChIJ195FnkeMrjgR3nkapKKdk7A",
    "types": [
        "political",
        "sublocality",
        "sublocality_level_1"
    ]
}

kenglik = data['geometry']['location']['lat']
uzunlik = data['geometry']['location']['lng']
print(f"{kenglik},{uzunlik}")