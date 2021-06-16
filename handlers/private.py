from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""**Selam Ben {bn}**

`Sesli sohbetlerde müzik dinlemenize olanak sağlarım.`

          📜Kullanma Kılavuzu📜

💠 /play - Şarkıyı oynatır.
💠 /pause - Şarkıyı durdurur.
💠 /resume - Şarkıyı devam ettirir.
💠 /skip - Diğer şarkıya geçer.
💠 /stop - Botu kapatır.
💠 /song - Şarkı aratır.

`Tamamiyle Türkçe altyapı ile kodlanmış müzik botunu kullanabilmek için @TurkishMusi

__Küçük bir ücret karşılığında grubunuza özel müzik botu yaptırabilirsiniz detaylı bilgi için iletişim @Zep_Unb.__

**🤖 Developer By @Zep_Unb**

        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Sohbet ", url="https://t.me/DepressionalistChat"
                    ),
                    InlineKeyboardButton(
                        "Kanalımız 📣", url="https://t.me/Depressionalist"
                    )
                ]
            ]
        )
    )
