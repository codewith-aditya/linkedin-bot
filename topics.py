# ============== TOPIC MANAGEMENT ==============
import random
from datetime import datetime

# Day-wise topics (multiple topics per day!)
TOPIC_SCHEDULE = {
    "Monday": {
        "theme": "Motivation Monday 🔥",
        "topics": [
            "career growth mindset",
            "Monday motivation for professionals",
            "overcoming challenges at work",
            "success habits of top leaders",
        ]
    },
    "Tuesday": {
        "theme": "Tech Tuesday 💻",
        "topics": [
            "AI trends in 2025",
            "no-code tools for business",
            "future of remote work tech",
            "cybersecurity tips for startups",
            "cloud computing simplified",
        ]
    },
    "Wednesday": {
        "theme": "Wisdom Wednesday 🧠",
        "topics": [
            "leadership lessons from great CEOs",
            "books every professional must read",
            "life lessons from failures",
            "emotional intelligence at work",
        ]
    },
    "Thursday": {
        "theme": "Throwback / Tips Thursday 💡",
        "topics": [
            "productivity hacks that actually work",
            "networking tips for introverts",
            "resume tips that get interviews",
            "personal branding strategies",
        ]
    },
    "Friday": {
        "theme": "Feature Friday 🚀",
        "topics": [
            "startup ideas for 2025",
            "freelancing vs full-time debate",
            "side hustle ideas for developers",
            "investment tips for young professionals",
        ]
    },
    "Saturday": {
        "theme": "Story Saturday 📖",
        "topics": [
            "my journey in tech",
            "lessons from my first job",
            "biggest career mistake I made",
            "how I built my personal brand",
        ]
    },
    "Sunday": {
        "theme": "Self-care Sunday 🌿",
        "topics": [
            "work-life balance tips",
            "mental health for professionals",
            "hobbies that make you a better leader",
            "digital detox strategies",
        ]
    }
}

# Extra trending topics pool
TRENDING_TOPICS = [
    "ChatGPT and future of jobs",
    "LinkedIn algorithm secrets",
    "how to get promoted faster",
    "skills that will matter in 2026",
    "why soft skills beat hard skills",
    "Gen Z vs Millennials at work",
    "Web3 and career opportunities",
    "how to negotiate salary like a pro",
]

def get_today_topic():
    """Aaj ke din ka random topic do"""
    day = datetime.now().strftime("%A")
    day_data = TOPIC_SCHEDULE.get(day, TOPIC_SCHEDULE["Monday"])
    
    topic = random.choice(day_data["topics"])
    theme = day_data["theme"]
    
    return {
        "day": day,
        "theme": theme,
        "topic": topic
    }

def get_trending_topic():
    """Trending pool se random topic"""
    return random.choice(TRENDING_TOPICS)

def get_custom_topics_list():
    """Saare topics return karo"""
    all_topics = []
    for day, data in TOPIC_SCHEDULE.items():
        for topic in data["topics"]:
            all_topics.append({"day": day, "theme": data["theme"], "topic": topic})
    return all_topics