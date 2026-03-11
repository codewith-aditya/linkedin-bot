# ============== LINKEDIN API ==============
import requests
import json
from config import LINKEDIN_ACCESS_TOKEN, LINKEDIN_PERSON_ID

BASE_URL = "https://api.linkedin.com/v2"

HEADERS = {
    "Authorization": f"Bearer {LINKEDIN_ACCESS_TOKEN}",
    "Content-Type": "application/json",
    "X-Restli-Protocol-Version": "2.0.0"
}


def post_text_only(content):
    """Sirf text post karo (bina image)"""
    
    url = f"{BASE_URL}/ugcPosts"
    
    payload = {
        "author": f"urn:li:person:{LINKEDIN_PERSON_ID}",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": content},
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }
    
    response = requests.post(url, headers=HEADERS, json=payload)
    
    if response.status_code == 201:
        print("🎉 Text post published successfully!")
        return True
    else:
        print(f"❌ Text post failed: {response.status_code} - {response.text}")
        return False


def upload_image(image_path):
    """LinkedIn pe image upload karo"""
    
    # Step 1: Register upload
    register_url = f"{BASE_URL}/assets?action=registerUpload"
    
    register_payload = {
        "registerUploadRequest": {
            "recipes": ["urn:li:digitalmediaRecipe:feedshare-image"],
            "owner": f"urn:li:person:{LINKEDIN_PERSON_ID}",
            "serviceRelationships": [
                {
                    "relationshipType": "OWNER",
                    "identifier": "urn:li:userGeneratedContent"
                }
            ]
        }
    }
    
    reg_response = requests.post(register_url, headers=HEADERS, json=register_payload)
    
    if reg_response.status_code != 200:
        print(f"❌ Image registration failed: {reg_response.text}")
        return None
    
    reg_data = reg_response.json()
    upload_url = reg_data["value"]["uploadMechanism"][
        "com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest"
    ]["uploadUrl"]
    asset = reg_data["value"]["asset"]
    
    # Step 2: Upload image
    with open(image_path, "rb") as image_file:
        upload_headers = {
            "Authorization": f"Bearer {LINKEDIN_ACCESS_TOKEN}",
            "Content-Type": "application/octet-stream"
        }
        upload_response = requests.put(upload_url, headers=upload_headers, data=image_file)
    
    if upload_response.status_code in [200, 201]:
        print(f"✅ Image uploaded: {asset}")
        return asset
    else:
        print(f"❌ Image upload failed: {upload_response.status_code}")
        return None


def post_with_image(content, image_path):
    """Image ke saath post karo 🖼️"""
    
    # Image upload karo
    asset = upload_image(image_path)
    
    if not asset:
        print("⚠️ Image upload fail, posting text only...")
        return post_text_only(content)
    
    url = f"{BASE_URL}/ugcPosts"
    
    payload = {
        "author": f"urn:li:person:{LINKEDIN_PERSON_ID}",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": content},
                "shareMediaCategory": "IMAGE",
                "media": [
                    {
                        "status": "READY",
                        "description": {"text": "Post image"},
                        "media": asset,
                        "title": {"text": "LinkedIn Post"}
                    }
                ]
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }
    
    response = requests.post(url, headers=HEADERS, json=payload)
    
    if response.status_code == 201:
        print("🎉 Image post published successfully!")
        return True
    else:
        print(f"❌ Image post failed: {response.status_code} - {response.text}")
        return False


def check_token():
    """LinkedIn token valid hai ya nahi check karo"""
    
    url = f"{BASE_URL}/me"
    response = requests.get(url, headers=HEADERS)
    
    if response.status_code == 200:
        data = response.json()
        name = f"{data.get('localizedFirstName', '')} {data.get('localizedLastName', '')}"
        print(f"✅ Token valid! Logged in as: {name}")
        return True
    else:
        print(f"❌ Token invalid or expired: {response.status_code}")
        return False