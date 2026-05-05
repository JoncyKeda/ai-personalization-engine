# Stores user interaction history

user_profiles = {}

def update_user_profile(user_id, item):
    if user_id not in user_profiles:
        user_profiles[user_id] = []

    user_profiles[user_id].append(item)
