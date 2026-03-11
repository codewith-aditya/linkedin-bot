# 🤖 LinkedIn Bot

An AI-powered LinkedIn automation bot that auto-generates and schedules posts using the Claude API.

> Built by [@codewith-aditya](https://github.com/codewit-aditya)

---

## 📁 Project Structure

```
linkedin-bot/
├── config.py           # API keys, scheduling config, and settings
├── post_generator.py   # Claude API-powered post content generator
├── image_generator.py  # AI image generation for post attachments
├── linkedin_api.py     # LinkedIn API wrapper (auth + posting)
├── scheduler.py        # Cron-based post scheduling logic
├── topics.py           # Topic bank, tones, and content formats
├── main.py             # Entry point — runs the bot
├── posts_log.json      # Log of all published posts
└── images/             # Saved AI-generated images
```

---

## ⚙️ Setup

### 1. Clone the repo

```bash
git clone https://github.com/codewith-aditya/linkedin-bot.git
cd linkedin-bot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the root:

```env
LINKEDIN_CLIENT_ID=your_client_id
LINKEDIN_CLIENT_SECRET=your_client_secret
LINKEDIN_ACCESS_TOKEN=your_access_token
LINKEDIN_USER_URN=urn:li:person:XXXXXXX

ANTHROPIC_API_KEY=your_claude_api_key
OPENAI_API_KEY=your_openai_key        # Optional (for image gen)
```

### 4. Run the bot

```bash
python main.py
```

---

## 🚀 Features

- **AI Post Generation** — Uses Claude to write engaging LinkedIn posts
- **Topic Rotation** — Cycles through a curated topic bank automatically
- **Tone Variety** — Alternates between storytelling, analytical, motivational, and contrarian styles
- **Auto Scheduler** — Posts at a configured time daily (default: 9 AM IST)
- **Image Support** — Optional AI-generated images via DALL-E
- **Post Logging** — Every published post is saved to `posts_log.json`

---

## 🛠️ Tech Stack

- **Python** — Core bot logic
- **Claude API (Anthropic)** — Post content generation
- **LinkedIn API** — Publishing posts
- **OpenAI DALL-E** *(optional)* — Image generation
- **APScheduler / cron** — Scheduling

---

## 📌 Configuration

All settings live in `config.py`:

| Setting | Default | Description |
|---|---|---|
| `POST_FREQUENCY_DAYS` | `1` | How often to post |
| `POST_TIME` | `09:00` | Daily post time |
| `TIMEZONE` | `Asia/Kolkata` | Your timezone |
| `INCLUDE_HASHTAGS` | `True` | Add hashtags to posts |
| `HASHTAG_COUNT` | `5` | Number of hashtags |
| `INCLUDE_IMAGE` | `False` | Attach AI image to post |

---

## 📄 License

MIT License © [Aditya](https://github.com/codewith-aditya)
