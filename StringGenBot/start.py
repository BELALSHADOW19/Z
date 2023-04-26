from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""مرحبا  {msg.from_user.mention},

انا اسمي {me2},
اقوم بصنع جلسات فقط اخطر من اسفل الجلسة التي تريدها 
تم التطوير بواسطة  : [ َ𝙎ُِ𝙊ِّ𝙐ٓ𝙍ٍّ𝘾ٍَٖ𝙀َِ◌َٰ͜͡ ٍ𝙇َٰ𝘼ُ𝙑َٰ𝘼⚡️ ](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="اضغط لاستخراج الجلسه", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("قناة السورس", url="https://t.me/SOURCELAVA"),
                ],
                [
                    InlineKeyboardButton("جروب الدعم", url="https://t.me/GROUP_LAVA"),
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
