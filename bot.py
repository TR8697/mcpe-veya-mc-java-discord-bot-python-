import discord
from discord.ext import commands
from discord.ui import Button, View

# Discord botu örneği oluştur
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Olay: Bot hazır ve Discord'a bağlandığında
@bot.event
async def on_ready():
    print(f'Bot {bot.user} olarak giriş yaptı')

# Olay: Bir mesaj alındığında
@bot.event
async def on_message(message):
    # Bot tarafından gönderilen mesajları yoksay
    if message.author == bot.user:
        return

    # Mesajın 'embed' ile başlayıp başlamadığını kontrol et
    if message.content.startswith('embed'):
        await send_embed(message.channel)

# Gömülü mesajı ve düğmeleri göndermek için bir fonksiyon
async def send_embed(channel):
    # Boş bir gömülü mesaj oluştur
    embed = discord.Embed(title="", description="", color=discord.Color.blue())
    embed.set_author(name="muhammet", icon_url="")

    # İki düğme oluştur ve her birine etiket ve URL atayın
    button = Button(label="Oy Sitesi", url="https://example.com/oy-sitesi")
    button1 = Button(label="Oyna", url="https://example.com/oyna")

    # Bir görünüm oluştur ve düğmeleri ekleyin
    view = View()
    view.add_item(button)
    view.add_item(button1)

    # Gömülü mesajı ve düğmeleri belirtilen kanala gönderin
    await channel.send(embed=embed, view=view)

# Botu kendi bot tokeninizle çalıştırın
bot.run('BOT_TOKENINIZ')
