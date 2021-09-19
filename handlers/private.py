from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CWXwtVQADumEbXh17uzZt9_VFbx5YMS9X7LmBAAKgCwAC_eJgUYTe7_DjL_XOHgQ")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎀
ɪ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜsɪᴄ ɪɴ ʏᴏᴜʀ  ɢʀᴏᴜᴩ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ. 
ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ ᴀɴᴅ ᴘʟᴀʏ ᴍᴜsɪᴄ ғʀᴇᴇʟʏ 🤗 Developed By [king](https://t.me/abhinasroy) !**

        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔨 Owner🔨", url="https://t.me/abhinasroy")
                  ],[
                    InlineKeyboardButton(
                        "sᴜᴘᴘᴏʀᴛ👿", url="https://t.me/DOSTI_GROUP_1234"
                    ),
                    InlineKeyboardButton(
                        "ᴄʜᴀɴɴᴇʟ", url="https://t.me/ABOUT_ABHINAS"
                    )    
                ],[ 
                    InlineKeyboardButton(
                        "➕ᴀᴅᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ➕", url="https://t.me/Group_25king_bot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Yes iᴍ online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊Uᴩᴅᴀᴛᴇs", url="https://t.me/ABOUT_ABHINAS")
                ]
            ]
        )
   )
