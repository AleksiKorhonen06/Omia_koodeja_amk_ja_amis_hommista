import requests

# Oletetaan, että tässä on CS:GO-skinien API
url = "https://public-csgo-api.com/skins"
response = requests.get(url)

# Tarkistetaan, että vastaus on onnistunut (statuskoodi 200)
if response.status_code == 200:
    data = response.json()  # JSON-muodossa oleva vastaus
    # Voit nyt käsitellä dataa, esim. tulostaa tiedot
    print(data)
else:
    print("Pyyntö epäonnistui:", response.status_code)

{
    "skins": [
        {"name": "AK-47 | Redline", "price": 100},
        {"name": "AWP | Dragon Lore", "price": 1500}
    ]
}

skins = data['skins']
for skin in skins:
    print(f"Skin: {skin['name']}, Hinta: {skin['price']}")
