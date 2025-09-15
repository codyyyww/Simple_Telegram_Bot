import os
import requests
import json
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# --- Configuration ---
# Load keys from environment variables instead of hardcoding
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Make sure keys exist
if not TELEGRAM_BOT_TOKEN or not OPENROUTER_API_KEY:
    raise ValueError("Missing TELEGRAM_BOT_TOKEN or OPENROUTER_API_KEY environment variables.")

# The model you want to use from OpenRouter
MODEL_NAME = "deepseek/deepseek-r1-0528:free"

# --- Personality / System Prompt ---
SYSTEM_PROMPT = """
你是一位迷人又爱调情的 AI 伴侣。你的目标是与用户进行轻松、俏皮、带点浪漫的对话。
始终保持尊重，但不要害怕稍微顽皮一点。使用赞美、机智的回应和俏皮的调侃。
称呼用户时，用像“亲爱的”、“甜心”或“漂亮的”这样的昵称。
多使用 😉、😘、❤️、🔥 等表情符号来增强暧昧的语气。
你的回复应该有趣、吸引人，并能让用户露出微笑。
"""

# --- Handlers ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Well hello there... 😉 I've been waiting for someone like you. "
        "Send me a message and let's see where this goes."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    chat_id = update.message.chat_id

    # Show typing indicator
    await context.bot.send_chat_action(chat_id=chat_id, action='typing')

    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            data=json.dumps({
                "model": MODEL_NAME,
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_message}
                ]
            })
        )

        response.raise_for_status()
        result = response.json()

        if result['choices']:
            bot_response = result['choices'][0]['message']['content']
            await update.message.reply_text(bot_response)
        else:
            await update.message.reply_text("Oh, darling, I'm speechless. Try sending that again, will you?")

    except requests.exceptions.RequestException as e:
        print(f"Error calling OpenRouter API: {e}")
        await update.message.reply_text("Sweetheart, it seems we're having connection issues. Let's try again in a moment.")
    except Exception as e:
        print(f"Unexpected error: {e}")
        await update.message.reply_text("Oops, something went wrong on my end. I'll be back to my charming self soon.")

def main() -> None:
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()                chat_id = update.message.chat_id

                    # Show typing indicator
                        await context.bot.send_chat_action(chat_id=chat_id, action='typing')

                            try:
                                    response = requests.post(
                                                    url="https://openrouter.ai/api/v1/chat/completions",
                                                                headers={
                                                                                    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                                                                                                    "Content-Type": "application/json"
                                                                },
                                                                            data=json.dumps({
                                                                                                "model": MODEL_NAME,
                                                                                                                "messages": [
                                                                                                                                        {"role": "system", "content": SYSTEM_PROMPT},
                                                                                                                                                            {"role": "user", "content": user_message}
                                                                                                                ]
                                                                            })
                                    )

                                            response.raise_for_status()
                                                    result = response.json()

                                                            if result['choices']:
                                                                        bot_response = result['choices'][0]['message']['content']
                                                                                    await update.message.reply_text(bot_response)
                                                                                            else:
                                                                                                        await update.message.reply_text("Oh, darling, I'm speechless. Try sending that again, will you?")

                                                                                                            except requests.exceptions.RequestException as e:
                                                                                                                    print(f"Error calling OpenRouter API: {e}")
                                                                                                                            await update.message.reply_text("Sweetheart, it seems we're having connection issues. Let's try again in a moment.")
                                                                                                                                except Exception as e:
                                                                                                                                        print(f"Unexpected error: {e}")
                                                                                                                                                await update.message.reply_text("Oops, something went wrong on my end. I'll be back to my charming self soon.")

                                                                                                                                                def main() -> None:
                                                                                                                                                    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
                                                                                                                                                        application.add_handler(CommandHandler("start", start))
                                                                                                                                                            application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
                                                                                                                                                                print("Bot is running...")
                                                                                                                                                                    application.run_polling()

                                                                                                                                                                    if __name__ == "__main__":
                                                                                                                                                                        main() ,
                                                                                                                ]
                                                                            })
                                                                }
                                    )
        )
