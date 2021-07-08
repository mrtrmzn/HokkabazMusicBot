from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""**Selam Ben {bn}**

`Grup sesli sohbetlerde müzik dinlemenize olanak sağlarım.`

          **📜 Kullanım Kılavuzu 📜**

💠 /play - __Şarkıyı oynatır.__
💠 /pause - __Şarkıyı durdurur.__
💠 /resume - __Şarkıyı devam ettirir.__
💠 /skip - __Sonraki şarkıya geçer.__
💠 /stop - __Botu kapatır.__
💠 /song - __Şarkı aratır.__

`Tamamiyle Türkçe altyapı ile kodlanmış müzik botunu kullanmak için @bizbizemusicbot kanalına göz atabilirsiniz.`

**📲 Developer By @mrtrmzn**

        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Destek Grubu", url="https://t.me/yediyirmidortbizbizee"
                    ),
                    InlineKeyboardButton(
                        "Botla Alakalı Sorular İçin", url="https://t.me/mrtrmzn"
                    )
                ]
            ]
        )
    )
