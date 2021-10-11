from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CWXwtVQADumEbXh17uzZt9_VFbx5YMS9X7LmBAAKgCwAC_eJgUYTe7_DjL_XOHgQ")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎀
I̸ c̸a̸n̸ P̸L̸A̸Y̸ M̸U̸S̸I̸C̸ I̸N̸ Y̸O̸U̸R̸ G̸R̸O̸U̸P̸ V̸O̸I̸C̸E̸ C̸H̸A̸T̸. 
A̸D̸D̸ M̸E̸ T̸O̸ Y̸O̸U̸R̸ G̸R̸O̸U̸P̸ A̸N̸D̸ P̸L̸A̸Y̸ M̸U̸S̸I̸C̸ 🤗 D̸E̸V̸E̸L̸O̸P̸E̸D̸ B̸Y̸ [A̸B̸H̸I̸N̸A̸S̸](https://t.me/abhinasroy) !**

        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔨O͜͡W͜͡N͜͡E͜͡R͜͡🔨", url="https://t.me/abhinasroy")
                  ],[
                    InlineKeyboardButton(
                        "G͜͡R͜͡O͜͡U͜͡P͜͡👿", url="https://t.me/DOSTI_GROUP_1234"
                    ),
                    InlineKeyboardButton(
                        "C͜͡H͜͡A͜͡N͜͡N͜͡E͜͡L͜͡", url="https://t.me/ABOUT_ABHINAS"
                    )    
                ],[ 
                    InlineKeyboardButton(
                        "➕A͜͡D͜͡D͜͡ T͜͡O͜͡ Y͜͡O͜͡U͜͡R͜͡ G͜͡R͜͡O͜͡U͜͡P͜͡➕", url="https://t.me/Group_25king_bot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Y͜͡E͜͡S͜͡ I͜͡M͜͡ O͜͡N͜͡L͜͡I͜͡N͜͡E͜͡ ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊U͜͡P͜͡D͜͡A͜͡T͜͡E͜͡S͜͡", url="https://t.me/ABOUT_ABHINAS")
                ]
            ]
        )
   )
