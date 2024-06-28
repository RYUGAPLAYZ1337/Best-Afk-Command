import discord
from discord.ext import commands
import json
import datetime
ghosty= Bot.commands(command_prefix="$",intents = discord.Intents.all()

ravanxGhostyxsanemixvoidxAdityaXasyncdevxcosmicdevtoken="your token here"
def loadafksghosty():
    try:
        with open('afk.json', 'r') as f:
            data = json.load(f)
            if "global" not in data:
                data["global"] = []
            return data
    except FileNotFoundError:
        return {"global": []}

def saveafksghosty():
    with open('afk.json', 'w') as f:
        json.dump(afksghosty, f, indent=4)

afksghosty = loadafksghosty()

class afkbuttonRavanxVoidxGhostyxSanemixCosmicdevelopers(discord.ui.Button):
    def __init__(self, ctx: commands.Context, label, reason, style=discord.ButtonStyle.primary, customid="serverafkghosty"):
        super().__init__(style=style, label=label, custom_id=customid)
        self.ctx = ctx
        self.reason = reason

    async def callback(self, interaction: discord.Interaction):
        userid = str(interaction.user.id)

        if interaction.user.id != self.ctx.author.id:
            await interaction.response.send_message(embed=discord.Embed(description=f"Only **{self.ctx.author}** can use this command. Use `{self.ctx.prefix}{self.ctx.command}` to run this command", color=colorok), ephemeral=True)
            return False

        timestamp = datetime.datetime.utcnow().isoformat()

        if self.custom_id == "serverafkghosty":
            serverid = str(interaction.guild.id)
            if serverid not in afksghosty:
                afksghosty[serverid] = []
            afksghosty[serverid].append({"id": userid, "reason": self.reason, "timestamp": timestamp, "mentions": []})
            saveafksghosty()
            successmessage = f"{interaction.user.name}, successfully sets your server AFK"
        elif self.custom_id == "globalafkghosty":
            afksghosty["global"].append({"id": userid, "reason": self.reason, "timestamp": timestamp, "mentions": []})
            saveafksghosty()
            successmessage = f"{interaction.user.name}, successfully sets your global AFK"

        successembed = discord.Embed(
            description=f"<:XcapeArrowRight:1219236733946957904> Reason: {self.reason}",
            color=colorok
        )
        successembed.set_author(name=f"{successmessage}", icon_url=f"{interaction.user.avatar.url}")

        await interaction.message.edit(embed=successembed, view=None)

@ghosty.command()
async def afkk(ctx, *, reason="I'm Afk :D"):
    view = discord.ui.View()
    view.add_item(afkbuttonRavanxVoidxGhostyxSanemixCosmicdevelopers(ctx, "Global AFK", reason, customid="globalafkghosty", style=discord.ButtonStyle.green))
    view.add_item(afkbuttonRavanxVoidxGhostyxSanemixCosmicdevelopers(ctx, "Server AFK", reason, customid="serverafkghosty", style=discord.ButtonStyle.green))
    ghostyembedafk = discord.Embed(
        description="",
        color=colorok
    )
    ghostyembedafk.set_author(name=f"{ctx.author.display_name}, Choose your AFK style from the buttons below.", icon_url=f"{ctx.author.avatar.url}")

    await ctx.send(embed=ghostyembedafk, view=view)

@ghosty.event
async def on_message(message):
    if message.author.bot:
        return

    userid = str(message.author.id)
    serverid = str(message.guild.id)

    afkremovedghosty = False
    removedreasonghosty = ""
    removedtimestampghosty = None
    removedmentionsghosty = []

    if serverid in afksghosty:
        originallengthghosty = len(afksghosty[serverid])
        for entry in afksghosty[serverid]:
            if entry["id"] == userid:
                removedreasonghosty = entry["reason"]
                removedtimestampghosty = entry["timestamp"]
                removedmentionsghosty = entry["mentions"]
                afksghosty[serverid].remove(entry)
                afkremovedghosty = True
                break
        if afkremovedghosty:
            saveafksghosty()

    if not afkremovedghosty and "global" in afksghosty:
        originallengthghosty = len(afksghosty["global"])
        for entry in afksghosty["global"]:
            if entry["id"] == userid:
                removedreasonghosty = entry["reason"]
                removedtimestampghosty = entry["timestamp"]
                removedmentionsghosty = entry["mentions"]
                afksghosty["global"].remove(entry)
                afkremovedghosty = True
                break
        if afkremovedghosty:
            saveafksghosty()

    if afkremovedghosty:
        removedtimeghosty = datetime.datetime.fromisoformat(removedtimestampghosty)
        afkdurationghosty = datetime.datetime.utcnow() - removedtimeghosty
        afksecondsghosty = int(afkdurationghosty.total_seconds())
        afkminutesghosty = afksecondsghosty // 60
        afkhoursghosty = afkminutesghosty // 60
        afkminutesghosty = afkminutesghosty % 60
        afksecondsghosty = afksecondsghosty % 60

        if afkhoursghosty > 0:
            durationmessageghosty = f"{afkhoursghosty} hours {afkminutesghosty} minutes"
        elif afkminutesghosty > 0:
            durationmessageghosty = f"{afkminutesghosty} minutes"
        else:
            durationmessageghosty = f"{afksecondsghosty} seconds"

        mentionmessagesghosty = "\n".join([f"`{idx + 1}.` **{mention['user']}** `-` [Message Link]({mention['link']})" for idx, mention in enumerate(removedmentionsghosty)])
        mentiontextghosty = f"\n<:MekoPing:1256193984867598368> Following user(s) mentioned you while you were AFK:\n{mentionmessagesghosty}" if removedmentionsghosty else ""

        embed = discord.Embed(
            description=f"<:XcapeArrowRight:1219236733946957904> Reason was: {removedreasonghosty}",
            color=colorok
        )
        embed.add_field(name=f"<:MekoPing:1256193984867598368> Following user(s) mentioned you while you were AFK:", value=f"{mentionmessagesghosty}" if removedmentionsghosty else "")
        embed.set_author(name=f"Your global AFK has been removed after {durationmessageghosty}", icon_url=f"{message.author.avatar.url}")

        await message.channel.send(f"{message.author.mention}", embed=embed)

   
    for user in message.mentions:
        userid = str(user.id)
        afkreasonghosty = None
        afktimestampghosty = None
        afktypeghosty = None

      
        if serverid in afksghosty:
            for entry in afksghosty[serverid]:
                if entry["id"] == userid:
                    afkreasonghosty = entry["reason"]
                    afktimestampghosty = entry["timestamp"]
                    afktypeghosty = "server"
                    break

      
        if not afkreasonghosty and "global" in afksghosty:
            for entry in afksghosty["global"]:
                if entry["id"] == userid:
                    afkreasonghosty = entry["reason"]
                    afktimestampghosty = entry["timestamp"]
                    afktypeghosty = "global"
                    break

        if afkreasonghosty:
            afktimeghosty = datetime.datetime.fromisoformat(afktimestampghosty)
            afkdurationghosty = datetime.datetime.utcnow() - afktimeghosty
            afksecondsghosty = int(afkdurationghosty.total_seconds())
            afkminutesghosty = afksecondsghosty // 60
            afkhoursghosty = afkminutesghosty // 60
            afkminutesghosty = afkminutesghosty % 60
            afksecondsghosty = afksecondsghosty % 60

            if afkhoursghosty > 0:
                durationmessageghosty = f"{afkhoursghosty} hours {afkminutesghosty} minutes"
            elif afkminutesghosty > 0:
                durationmessageghosty = f"{afkminutesghosty} minutes"
            else:
                durationmessageghosty = f"{afksecondsghosty} seconds"

            afktypemessageghosty = "globally " if afktypeghosty == "global" else ""
            
            afknowghosty = discord.Embed(
                description="",
                color=colorok
            )
            afknowghosty.set_author(name=f"{user.display_name}, went AFK {afktypemessageghosty}{durationmessageghosty} ago", icon_url=user.avatar.url)
            await message.channel.send(embed=afknowghosty)

           
            if afktypeghosty == "server":
                for entry in afksghosty[serverid]:
                    if entry["id"] == userid:
                        entry["mentions"].append({"user": message.author.display_name, "link": message.jump_url})
                        break
            elif afktypeghosty == "global":
                for entry in afksghosty["global"]:
                    if entry["id"] == userid:
                        entry["mentions"].append({"user": message.author.display_name, "link": message.jump_url})
                        break
            saveafksghosty()

    await ghosty.process_commands(message)
ghosty.run(ravanxGhostyxsanemixvoidxAdityaXasyncdevxcosmicdevtoken)
