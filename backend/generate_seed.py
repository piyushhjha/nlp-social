import json
import random
from datetime import datetime, timedelta

random.seed(42)

cities = [
    "Patna","Bengaluru","Kolkata","Delhi","Mumbai","Jaipur","Siliguri",
    "Guwahati","Lucknow","Varanasi","Shimla","Leh","Manali","Kullu",
    "Aizawl","Imphal","Thiruvananthapuram","Chennai","Pune","Nagpur",
    "Bhopal","Hyderabad","Visakhapatnam","Vijayawada","Surat","Ahmedabad",
    "Indore","Jamshedpur","Kochi","Cuttack","Srinagar","Patiala"
]

disaster_templates = {
    "flood": [
        "Massive flooding in {area}, {city}. Houses submerged, people trapped on roofs. Need boats and food supplies urgently.",
        "Water level rising fast near {area}, {city}. Roads are blocked and several neighborhoods underwater. Request immediate evacuation.",
        "Severe rains caused flood in {city} around {area}. People stranded, need rescue and medical aid."
    ],
    "earthquake": [
        "Strong earthquake of magnitude {mag} struck near {city}. Several buildings collapsed and people injured. Need ambulances and rescue teams.",
        "Tremors felt in {city}, aftershocks continuing. Multiple reports of damage and trapped people. Please send help.",
    ],
    "wildfire": [
        "Wildfire spreading near {area} close to {city}. Smoke everywhere and villages evacuated. Need firefighting support.",
        "Large forest fire at {area}, {city} outskirts — houses at risk and smoke making breathing difficult. Volunteers needed to help evacuate."
    ],
    "cyclone": [
        "Cyclone warning near {city} coast. Heavy winds and rains expected; coastal areas being evacuated. Secure loose objects and move to safe shelters.",
        "Storm surge expected in {city} due to cyclone. Authorities issuing evacuation orders for low-lying areas.",
    ],
    "landslide": [
        "Landslide on the road near {area} between {city} and nearby areas after heavy rains. Vehicles trapped, rescue required.",
        "A hillside collapse at {area}, {city} blocking the highway. Multiple people reported missing."
    ],
    "heatwave": [
        "Heatwave alert in {city}: temperatures above {temp}C. Several cases of heat exhaustion reported. Need water stations and cooling centers.",
    ],
    "building_collapse": [
        "A building collapsed in {area}, {city}. People are trapped under debris. Immediate rescue required.",
    ],
    "gas_leak": [
        "Gas leak reported at {area}, {city}. Evacuations underway, several people have breathing issues. Hazmat team needed.",
    ],
}

non_disaster_templates = [
    "Enjoying a beautiful day at {area}, {city}. Perfect weather for a walk!",
    "Local market in {area}, {city} has lovely handicrafts. Support small businesses!",
    "Caught a fantastic sunset at {area}, {city}. #photography",
    "Trying out a popular cafe in {city}. Great coffee and vibes!",
    "Attended a cultural festival in {city} today. Amazing performances and food."
]

users = [
    "local_reporter","traveler","citizen_john","rescue_team","volunteer_group",
    "newsbot","firstresponder","samaritan","travel_diary","observer"
]

posts = []
base_date = datetime(2025, 8, 1, 8, 0)

for i in range(1, 201):
    is_disaster = random.random() < 0.7  # ~70% disaster posts
    city = random.choice(cities)
    area = random.choice([
        "Gandhi Nagar","Near the river","Industrial Area","Market Road","Hill Top",
        "Coastal Road","Old Town","Station Road","Airport Road","Lake Side"
    ])
    user = random.choice(users) + (str(random.randint(1,200)) if random.random() < 0.5 else "")
    created = base_date + timedelta(days=random.randint(0, 39), hours=random.randint(0,23), minutes=random.randint(0,59))
    created_at = created.isoformat() + "+05:30"
    likes = random.randint(0, 500)
    retweets = random.randint(0, 200)

    if is_disaster:
        dtype = random.choice(list(disaster_templates.keys()))
        template = random.choice(disaster_templates[dtype])
        mag = round(random.uniform(4.0,7.5),1)
        temp = random.randint(40,50)
        text = template.format(area=area, city=city, mag=mag, temp=temp)
        location_text = f"{area}, {city}"
        labels = {"disaster": True, "type": dtype}
    else:
        text = random.choice(non_disaster_templates).format(area=area, city=city)
        location_text = None if random.random() < 0.3 else f"{area}, {city}"
        labels = {"disaster": False}

    post = {
        "id": f"p{i}",
        "source": random.choice(["twitter","instagram","facebook"]),
        "user": user,
        "text": text,
        "created_at": created_at,
        "likes": likes,
        "retweets": retweets,
        "location_text": location_text,
        "labels": labels
    }
    posts.append(post)

with open('seed_data.json', 'w', encoding='utf-8') as f:
    json.dump(posts, f, ensure_ascii=False, indent=2)

print('✅ Generated seed_data.json with', len(posts), 'posts')
