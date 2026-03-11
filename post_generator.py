# ============== AI POST GENERATOR ==============
import openai
from config import OPENAI_API_KEY, POST_LANGUAGE, ADD_EMOJIS, POST_LENGTH
from topics import get_today_topic, get_trending_topic

openai.api_key = OPENAI_API_KEY

LENGTH_MAP = {
    "short": "80-120 words",
    "medium": "150-250 words",
    "long": "250-400 words"
}

LANGUAGE_MAP = {
    "english": "Write in professional English",
    "hindi": "Write in Hindi (Devanagari script)",
    "hinglish": "Write in Hinglish (Hindi + English mix, Roman script)"
}


def generate_post(custom_topic=None, include_trending=False):
    """AI se killer LinkedIn post generate karo"""
    
    if custom_topic:
        topic_data = {"topic": custom_topic, "theme": "Custom", "day": ""}
    elif include_trending:
        topic_data = {"topic": get_trending_topic(), "theme": "Trending 🔥", "day": ""}
    else:
        topic_data = get_today_topic()
    
    emoji_instruction = "Use relevant emojis naturally" if ADD_EMOJIS else "Don't use emojis"
    
    prompt = f"""
    Write a VIRAL LinkedIn post about: {topic_data['topic']}
    Theme: {topic_data['theme']}
    
    STRICT RULES:
    1. START with a powerful HOOK (bold statement, controversial opinion, or question)
    2. Use very short paragraphs (1-2 lines MAX)
    3. {emoji_instruction}
    4. Include a personal story, insight, or data point
    5. Use "I" statements to make it personal
    6. End with a thought-provoking QUESTION to boost comments
    7. Add 4-5 relevant hashtags at the very end
    8. {LANGUAGE_MAP[POST_LANGUAGE]}
    9. Length: {LENGTH_MAP[POST_LENGTH]}
    10. Add line breaks between paragraphs for readability
    11. NO clickbait, keep it authentic
    12. Include ONE actionable takeaway
    
    FORMAT EXAMPLE:
    [Hook Line]
    
    [Story/Insight - 2-3 short paragraphs]
    
    [Key Takeaway]
    
    [Engagement Question]
    
    #hashtag1 #hashtag2 #hashtag3
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system", 
                "content": """You are a top LinkedIn content creator with 500K+ followers. 
                You write posts that get 10,000+ impressions. Your style is authentic, 
                insightful, and engaging. You never sound robotic or generic."""
            },
            {"role": "user", "content": prompt}
        ],
        temperature=0.85,
        max_tokens=600
    )
    
    post = response.choices[0].message.content.strip()
    
    return {
        "content": post,
        "topic": topic_data["topic"],
        "theme": topic_data["theme"],
        "day": topic_data.get("day", "")
    }


def generate_image_prompt(post_content):
    """Post ke liye image prompt generate karo"""
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "Generate a DALL-E image prompt for a LinkedIn post thumbnail."
            },
            {
                "role": "user",
                "content": f"""Based on this LinkedIn post, create a professional image prompt:
                
                Post: {post_content[:500]}
                
                Rules:
                - Professional, clean, modern design
                - Suitable for LinkedIn (business social media)
                - Include relevant visual metaphors
                - Bright, engaging colors
                - NO text in the image
                - Style: Corporate illustration or professional photography
                
                Return ONLY the image prompt, nothing else."""
            }
        ],
        temperature=0.7,
        max_tokens=200
    )
    
    return response.choices[0].message.content.strip()