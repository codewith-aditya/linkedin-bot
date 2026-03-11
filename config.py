# ============== ALL API KEYS & CONFIG ==============

# OpenAI
OPENAI_API_KEY = "sk-your-openai-api-key"

# LinkedIn
LINKEDIN_ACCESS_TOKEN = "your-linkedin-access-token"
LINKEDIN_PERSON_ID = "your-linkedin-person-id"

# Image Settings
IMAGE_FOLDER = "images"
USE_AI_IMAGES = True  # True = AI generate karega, False = local folder se uthayega

# Post Settings
POST_LANGUAGE = "english"  # "english", "hindi", "hinglish"
ADD_EMOJIS = True
POST_LENGTH = "medium"  # "short", "medium", "long"

# Schedule Settings (24hr format)
POSTING_TIMES = {
    "Monday":    ["09:00", "18:00"],
    "Tuesday":   ["09:00"],
    "Wednesday": ["09:00", "17:30"],
    "Thursday":  ["09:00"],
    "Friday":    ["09:00", "18:00"],
    "Saturday":  ["10:00"],
    "Sunday":    ["11:00"],
}