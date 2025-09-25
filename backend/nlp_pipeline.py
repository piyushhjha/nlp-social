import re
from typing import Dict

# Simple keyword-based NLP classifier
DISASTER_KEYWORDS = {
    "flood": ["flood", "submerged", "water level", "underwater"],
    "earthquake": ["earthquake", "tremor", "aftershock", "richter"],
    "wildfire": ["wildfire", "forest fire", "smoke", "burning"],
    "cyclone": ["cyclone", "storm surge", "hurricane", "typhoon"],
    "landslide": ["landslide", "collapse", "mudslide"],
    "heatwave": ["heatwave", "temperature", "heat exhaustion"],
    "building_collapse": ["building collapsed", "debris", "trapped"],
    "gas_leak": ["gas leak", "hazmat", "toxic", "breathing issues"]
}

def analyze_post(text: str) -> Dict:
    """
    Simulate NLP pipeline:
    - Detect if text mentions disaster
    - Identify disaster type (keyword-based)
    - Extract key entities (locations, numbers)
    """
    text_lower = text.lower()
    labels = {"disaster": False, "type": None}

    for dtype, keywords in DISASTER_KEYWORDS.items():
        if any(kw in text_lower for kw in keywords):
            labels["disaster"] = True
            labels["type"] = dtype
            break

    # Simple regex to pull numbers (like magnitudes, temperatures)
    numbers = re.findall(r"\d+\.?\d*", text)

    # Extract location words (dummy: after "in" or "at")
    locations = re.findall(r"(?:in|at)\s+([A-Z][a-zA-Z]+)", text)

    return {
        "labels": labels,
        "numbers": numbers,
        "locations": locations
    }


if __name__ == "__main__":
    sample_text = "Strong earthquake of magnitude 6.5 struck near Delhi. Buildings collapsed."
    result = analyze_post(sample_text)
    print("Sample:", sample_text)
    print("Analysis:", result)
