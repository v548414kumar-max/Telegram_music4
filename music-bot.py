from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎵 Music Bot is running successfully!")

app = ApplicationBuilder().token("8556266297:AAHGZmS1Y3L_i0snd5JTxMEB4Z3HmV8MyQM").build()
app.add_handler(CommandHandler("start", start))

print("Bot started successfully!")
app.run_polling()
