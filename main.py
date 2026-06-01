import discord
from discord.ext import commands
from discord import app_commands

TOKEN = "TWÓJ_TOKEN_BOTA_TUTAJ"

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# ===== SELECT MENU =====
class CennikSelect(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(
                label="× SERVER BOOST",
                description="Kliknij, aby zobaczyć ofertę SERVER BOOST",
                emoji="💎",
                value="server_boost"
            ),
            discord.SelectOption(
                label="× NITRO",
                description="Kliknij, aby zobaczyć ofertę NITRO",
                emoji="🎮",
                value="nitro"
            ),
            discord.SelectOption(
                label="× MEMBERSY",
                description="Kliknij, aby zobaczyć ofertę MEMBERSY",
                emoji="👤",
                value="membersy"
            ),
        ]
        super().__init__(
            placeholder="❌ × Nie wybrano żadnej opcji",
            options=options,
            custom_id="cennik_select"
        )

    async def callback(self, interaction: discord.Interaction):
        wybor = self.values[0]

        if wybor == "server_boost":
            embed = discord.Embed(
                title="💎 × SERVER BOOST",
                description=(
                    "─────────────────────────\n\n"
                    "**× SERVER BOOST 14x**\n"
                    "× 💸 **Cena: 14 PLN**\n"
                    "× 📅 **Czas Trwania: 1 Miesiąc**\n\n"
                    "**× SERVER BOOST 28x**\n"
                    "× 💸 **Cena: 28 PLN**\n"
                    "× 📅 **Czas Trwania: 1 Miesiąc**\n\n"
                    "**💎 × SERVER BOOST 14x**\n"
                    "× 💸 **Cena: 40 PLN**\n"
                    "× 📅 **Czas Trwania: 3 Miesiące**\n\n"
                    "─────────────────────────\n"
                    "📩 Napisz do nas po zakupie!\n"
                    "⏰ Czas realizacji: **do 24h**"
                ),
                color=discord.Color.from_rgb(255, 105, 180)
            )
            embed.set_footer(text="Protiskiro Shop • Server Boost")

        elif wybor == "nitro":
            embed = discord.Embed(
                title="🎮 × NITRO BOOST",
                description=(
                    "─────────────────────────\n\n"
                    "**× NITRO BOOST**\n"
                    "× 💸 **Cena: 20 PLN**\n"
                    "× 📅 **Czas Trwania: 1 Miesiąc**\n\n"
                    "─────────────────────────\n"
                    "📩 Napisz do nas po zakupie!\n"
                    "⏰ Czas realizacji: **do 24h**"
                ),
                color=discord.Color.from_rgb(128, 0, 255)
            )
            embed.set_footer(text="Protiskiro Shop • Nitro")

        elif wybor == "membersy":
            embed = discord.Embed(
                title="👤 × MEMBERSY",
                description=(
                    "─────────────────────────\n\n"
                    "**👤 × ONLINE M3MBERS**\n"
                    "➤ Ilość: 500\n"
                    "💸 Cena: **14 PLN**\n"
                    "➤ Ilość: 1.000\n"
                    "💸 Cena: **20 PLN**\n\n"
                    "**👤 × OFFLINE M3MBERS**\n"
                    "➤ Ilość: 500\n"
                    "💸 Cena: **12 PLN**\n"
                    "➤ Ilość: 1.000\n"
                    "💸 Cena: **15 PLN**\n\n"
                    "**👤 × R3AKCJE**\n"
                    "➤ Ilość: 500\n"
                    "💸 Cena: **14 PLN**\n"
                    "➤ Ilość: 1.000\n"
                    "💸 Cena: **19 PLN**\n\n"
                    "─────────────────────────\n"
                    "📩 Napisz do nas po zakupie!\n"
                    "⏰ Czas realizacji: **do 24h**"
                ),
                color=discord.Color.from_rgb(0, 180, 255)
            )
            embed.set_footer(text="Protiskiro Shop • Membersy")

        await interaction.response.send_message(embed=embed, ephemeral=True)


class CennikView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(CennikSelect())


@bot.event
async def on_ready():
    print(f"✅ Bot zalogowany jako {bot.user}")
    bot.add_view(CennikView())
    try:
        await bot.tree.sync()
        print("✅ Komendy zsynchronizowane")
    except Exception as e:
        print(f"Błąd: {e}")


@bot.tree.command(name="cennik", description="Wyślij cennik na kanał")
@app_commands.checks.has_permissions(administrator=True)
async def cennik(interaction: discord.Interaction):
    embed = discord.Embed(
        title="📋 Wybierz kategorię...",
        description="Witamy w **Protiskiro Shop**!\nWybierz kategorię z listy poniżej 👇",
        color=discord.Color.blurple()
    )
    embed.set_footer(text="Protiskiro Shop")
    await interaction.channel.send(embed=embed, view=CennikView())
    await interaction.response.send_message("✅ Cennik wysłany!", ephemeral=True)


bot.run(TOKEN)
