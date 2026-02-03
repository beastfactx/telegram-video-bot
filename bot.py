import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

import os

BOT_TOKEN = os.getenv("5850270544:AAGPPuZ8wHSfbewXw4vnR0JNPpD3yYtZSCQ")


VIDEO_ID = "BAACAgUAAxkBAAMyaYJEtL-97XDB9iMJPlBzczmiZQkAAkwcAAJrfhlUcSJQJJiqAR44BA"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "എന്തൂട്ര ഗെടിയെ🐘🎆🪅"
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text and update.message.text.lower() == "pappy":
        await update.message.reply_video(
            video=VIDEO_ID,
            supports_streaming=True
        )


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("പെടന്നെ പെട🌈")
    app.run_polling()


if __name__ == "__main__":
    main()

