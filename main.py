# ============== LINKEDIN BOT - MAIN ==============
"""
🤖 LinkedIn Auto-Post Bot by AstraGPT
Features:
  ✅ AI-generated posts (GPT-4)
  ✅ AI-generated images (DALL-E 3)
  ✅ Multiple topics per day
  ✅ Weekly schedule
  ✅ Post logging & stats
  ✅ Manual & auto modes
"""

from linkedin_api import check_token
from post_generator import generate_post
from image_generator import get_image_for_post
from scheduler import execute_post, run_scheduler, get_post_stats
from config import USE_AI_IMAGES


def show_menu():
    """Interactive menu"""
    
    print("""
╔══════════════════════════════════════════╗
║     🤖 LINKEDIN AUTO-POST BOT          ║
║        by Tantra AI Labs ✨              ║
╠══════════════════════════════════════════╣
║                                          ║
║  1️⃣  Auto Mode (Schedule chalao)        ║
║  2️⃣  Post Now (Abhi post karo)          ║
║  3️⃣  Preview Post (Dekho bina post)     ║
║  4️⃣  Custom Topic Post                  ║
║  5️⃣  Post Stats                         ║
║  6️⃣  Check LinkedIn Token               ║
║  7️⃣  Exit                               ║
║                                          ║
╚══════════════════════════════════════════╝
    """)


def preview_post():
    """Post preview — bina publish kare dekho"""
    
    post_data = generate_post()
    
    print(f"\n{'='*50}")
    print(f"📋 PREVIEW - {post_data['theme']}")
    print(f"📌 Topic: {post_data['topic']}")
    print(f"{'='*50}")
    print(f"\n{post_data['content']}\n")
    print(f"{'='*50}")
    
    choice = input("\n🤔 Publish karna hai? (y/n): ").lower()
    if choice == 'y':
        execute_post(post_type="manual_preview")


def custom_topic_post():
    """Apna topic deke post karo"""
    
    topic = input("\n📝 Topic enter karo: ")
    
    from post_generator import generate_post as gen
    post_data = gen(custom_topic=topic)
    
    print(f"\n{'='*50}")
    print(f"\n{post_data['content']}\n")
    print(f"{'='*50}")
    
    choice = input("\n🤔 Publish? (y/n/edit): ").lower()
    
    if choice == 'y':
        content = post_data['content']
        image_path = None
        
        if USE_AI_IMAGES:
            img_choice = input("🖼️ Image bhi generate karein? (y/n): ").lower()
            if img_choice == 'y':
                image_path = get_image_for_post(content)
        
        if image_path:
            from linkedin_api import post_with_image
            post_with_image(content, image_path)
        else:
            from linkedin_api import post_text_only
            post_text_only(content)
            
    elif choice == 'edit':
        print("\nEdited post paste karo (Enter 2 baar press karo end mein):")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        edited = "\n".join(lines)
        
        from linkedin_api import post_text_only
        post_text_only(edited)


def main():
    """Main function"""
    
    print("\n🚀 LinkedIn Bot Starting...\n")
    
    while True:
        show_menu()
        choice = input("👉 Option choose karo (1-7): ").strip()
        
        if choice == "1":
            print("\n🤖 Auto mode starting...")
            run_scheduler()
            
        elif choice == "2":
            execute_post(post_type="manual_instant")
            
        elif choice == "3":
            preview_post()
            
        elif choice == "4":
            custom_topic_post()
            
        elif choice == "5":
            get_post_stats()
            
        elif choice == "6":
            check_token()
            
        elif choice == "7":
            print("\n👋 Bye bhai! Bot band ho raha hai.\n")
            break
            
        else:
            print("❌ Invalid option! 1-7 mein choose kar.\n")
        
        input("\n⏎ Press Enter to continue...")


if __name__ == "__main__":
    main()