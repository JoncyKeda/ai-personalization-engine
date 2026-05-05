from utils.user_model import user_profiles

# Available items
items = [
    "action_movie", "thriller_movie", "romance_movie",
    "comedy_movie", "horror_movie"
]

def recommend_items(user_id):
    if user_id not in user_profiles:
        return items[:3]

    history = user_profiles[user_id]

    # Simple behavior-based logic
    if "action_movie" in history:
        return ["action_movie", "thriller_movie"]
    elif "romance_movie" in history:
        return ["romance_movie", "comedy_movie"]
    elif "horror_movie" in history:
        return ["horror_movie", "thriller_movie"]
    else:
        return items[:3]
