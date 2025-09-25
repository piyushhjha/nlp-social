import json
from collections import Counter

# Load dataset
with open("seed_data.json", "r", encoding="utf-8") as f:
    posts = json.load(f)

print("✅ Total posts:", len(posts))

# Disaster / Non-disaster counts
disaster_count = sum(1 for p in posts if p["labels"].get("disaster"))
non_disaster_count = len(posts) - disaster_count
print("🌪️ Disaster posts:", disaster_count)
print("🙂 Non-disaster posts:", non_disaster_count)

# Breakdown by disaster type
types = [p["labels"].get("type") for p in posts if p["labels"].get("disaster")]
counts = Counter(types)

print("\n📊 Disaster Type Breakdown:")
for t, c in counts.items():
    print(f" - {t}: {c}")
