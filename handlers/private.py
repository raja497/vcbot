from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CWXwtVQADumEbXh17uzZt9_VFbx5YMS9X7LmBAAKgCwAC_eJgUYTe7_DjL_XOHgQ")
    await message.reply_text(
        f"""**Hey, I'm {bn} 馃巰
I谈 c谈a谈n谈 P谈L谈A谈Y谈 M谈U谈S谈I谈C谈 I谈N谈 Y谈O谈U谈R谈 G谈R谈O谈U谈P谈 V谈O谈I谈C谈E谈 C谈H谈A谈T谈. 
A谈D谈D谈 M谈E谈 T谈O谈 Y谈O谈U谈R谈 G谈R谈O谈U谈P谈 A谈N谈D谈 P谈L谈A谈Y谈 M谈U谈S谈I谈C谈 馃 D谈E谈V谈E谈L谈O谈P谈E谈D谈 B谈Y谈 [A谈B谈H谈I谈N谈A谈S谈](https://t.me/abhinasroy) !**

        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "馃敤O汀蜏W汀蜏N汀蜏E汀蜏R汀蜏馃敤", url="https://t.me/abhinasroy")
                  ],[
                    InlineKeyboardButton(
                        "G汀蜏R汀蜏O汀蜏U汀蜏P汀蜏馃懣", url="https://t.me/DOSTI_GROUP_1234"
                    ),
                    InlineKeyboardButton(
                        "C汀蜏H汀蜏A汀蜏N汀蜏N汀蜏E汀蜏L汀蜏", url="https://t.me/ABOUT_ABHINAS"
                    )    
                ],[ 
                    InlineKeyboardButton(
                        "鉃旳汀蜏D汀蜏D汀蜏 T汀蜏O汀蜏 Y汀蜏O汀蜏U汀蜏R汀蜏 G汀蜏R汀蜏O汀蜏U汀蜏P汀蜏鉃?", url="https://t.me/Group_25king_bot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Y汀蜏E汀蜏S汀蜏 I汀蜏M汀蜏 O汀蜏N汀蜏L汀蜏I汀蜏N汀蜏E汀蜏 鉁?**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "馃攰U汀蜏P汀蜏D汀蜏A汀蜏T汀蜏E汀蜏S汀蜏", url="https://t.me/ABOUT_ABHINAS")
                ]
            ]
        )
   )
