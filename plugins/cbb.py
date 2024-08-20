from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>┏━━━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━━━┓\n┃ 𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋 : <a href='https://t.me/Aakash1230'>Aakash</a>\n┃ 𝖢𝗋𝖾𝖺𝗍𝗈𝗋 : <a href='tg://user?id={OWNER_ID}'> 𝖶𝖺𝗂𝖿𝗎 </a>\n┃ 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾 : <code>𝖯𝗒𝗍𝗁𝗈𝗇3</code>\n┃ 𝖫𝗂𝖻𝗋𝖺𝗋𝗒 : <a href='https://docs.pyrogram.org/'>𝖯𝗒𝗋𝗈𝗀𝗋𝖺𝗆 𝖺𝗌𝗒𝗇𝖼𝗂𝗈 {__version__}</a>\n┃ 𝖲𝗈𝗎𝗋𝖼𝖾 𝖢𝗈𝖽𝖾 : <a href=https://t.me/Aakash1230>𝖳𝖺𝗅𝗄 𝖳𝗈 𝖧𝗂𝗆</a>\n┃ Check Out : @Romance_Library\n┃ Harem Animes : @Harem_Library\n┗━━━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━━━┛</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
