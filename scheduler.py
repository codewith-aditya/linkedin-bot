# ============== SMART SCHEDULER ==============
import schedule
import time
import json
import os
from datetime import datetime
from config import POSTING_TIMES, USE_AI_IMAGES
from post_generator import generate_post
from image_generator import get_image_for_post
from linkedin_api import post_with_image, post_text_only

LOG_FILE = "posts_log.json"


def load_log():
    """Post history load karo"""
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_log(log_entry):
    """Post log save karo"""
    logs = load_log()
    logs.append(log_entry)
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=2, ensure_ascii=False)


def execute_post(post_type="scheduled"):
    """Ek complete post execute karo"""
    
    print(f"\n{'='*60}")
    print(f"🚀 Starting {post_type} post at {datetime.now()}")
    print(f"{'='*60}")
    
    # Step 1: Post generate karo
    post_data = generate_post()
    content = post_data["content"]
    
    print(f"\n📝 Topic: {post_data['topic']}")
    print(f"🏷️ Theme: {post_data['theme']}")
    print(f"\n{content}\n")
    
    # Step 2: Image generate karo
    image_path = None
    if USE_AI_IMAGES:
        image_path = get_image_for_post(content)
    
    # Step 3: LinkedIn pe post karo
    success = False
    if image_path:
        success = post_with_image(content, image_path)
    else:
        success = post_text_only(content)
    
    # Step 4: Log save karo
    log_entry = {
        "timestamp": str(datetime.now()),
        "type": post_type,
        "topic": post_data["topic"],
        "theme": post_data["theme"],
        "content": content,
        "image": image_path,
        "success": success
    }
    save_log(log_entry)
    
    if success:
        print(f"\n✅ Post published successfully! 🎉")
    else:
        print(f"\n❌ Post failed!")
    
    return success


def setup_schedule():
    """Weekly schedule set karo"""
    
    day_map = {
        "Monday": schedule.every().monday,
        "Tuesday": schedule.every().tuesday,
        "Wednesday": schedule.every().wednesday,
        "Thursday": schedule.every().thursday,
        "Friday": schedule.every().friday,
        "Saturday": schedule.every().saturday,
        "Sunday": schedule.every().sunday,
    }
    
    print("\n📅 WEEKLY SCHEDULE:")
    print("-" * 40)
    
    for day, times in POSTING_TIMES.items():
        for post_time in times:
            day_map[day].at(post_time).do(execute_post, post_type=f"{day}_{post_time}")
            print(f"  ✅ {day} at {post_time}")
    
    print("-" * 40)
    print(f"  📊 Total posts/week: {sum(len(t) for t in POSTING_TIMES.values())}")
    print()


def run_scheduler():
    """Scheduler start karo — runs forever"""
    
    setup_schedule()
    
    print("🤖 Bot is running! Press Ctrl+C to stop.\n")
    
    while True:
        schedule.run_pending()
        time.sleep(30)


def get_post_stats():
    """Post statistics dekho"""
    
    logs = load_log()
    
    if not logs:
        print("📊 No posts yet!")
        return
    
    total = len(logs)
    successful = sum(1 for l in logs if l.get("success"))
    failed = total - successful
    
    print(f"\n📊 POST STATISTICS")
    print(f"{'='*40}")
    print(f"  Total Posts:      {total}")
    print(f"  ✅ Successful:    {successful}")
    print(f"  ❌ Failed:        {failed}")
    print(f"  📈 Success Rate:  {(successful/total*100):.1f}%")
    print(f"  📅 First Post:    {logs[0]['timestamp'][:10]}")
    print(f"  📅 Last Post:     {logs[-1]['timestamp'][:10]}")
    print(f"{'='*40}\n")