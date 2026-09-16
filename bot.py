from telegram import Update
from telegram.ext import ApplicationBuilder, ChatMemberHandler, ContextTypes

TOKEN = "8893183833:AAGVed5OIxY6Rvase-l_aOwj-1dGKioMTjg"

async def track_left_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = update.chat_member
    old_status = result.old_chat_member.status
    new_status = result.new_chat_member.status
    user = result.new_chat_member.user

    # Member ထွက်သွားခြင်း (Left သို့မဟုတ် Kicked) ကို စစ်ဆေးခြင်း
    if old_status in ["member", "administrator", "restricted"] and new_status in ["left", "kicked"]:
        user_name = user.full_name
        username = f"(@{user.username})" if user.username else ""
        channel_name = result.chat.title

        alert_msg = (
            f"🚨 Member ထွက်သွားပါပြီ\n"
            f"👤 Name: {user_name} {username}\n"
            f"🆔 User ID: {user.id}\n"
            f"📢 Channel: {channel_name}"
        )

        try:
            await context.bot.send_message(
                chat_id=result.chat.id,
                text=alert_msg
            )
        except Exception as e:
            print(f"Error: {e}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(ChatMemberHandler(track_left_member, ChatMemberHandler.CHAT_MEMBER))
    print("Bot is running...")
    app.run_polling(allowed_updates=["chat_member"])

if __name__ == "__main__":
    main()
