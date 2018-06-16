import discord
from discord.ext import commands

TOKEN = 'NDU2OTQ0MDI0MzEwMzgyNTky.DgSGqg.JaYrwxRSuVRbD_4_DZr4v_Ec5rk'

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.event
async def on_member_join(member):
    guild = member.guild
    role = discord.utils.get(guild.roles, name="Piker")
    channel = guild.text_channels[1]
    await channel.send(member.name + ' has joined the server and has been given the role ' + role.name)
    await member.add_roles(role)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if 'fuck' in message.content:
        msg = 'hey this is a christian server'
        await message.channel.send(msg)
    await bot.process_commands(message)

#@bot.command()
#async def add(ctx, a: int, b: int):
#    await ctx.send(a + b)


#@bot.command()
#async def multiply(ctx, a: int, b: int):
#    await ctx.send(a * b)


@bot.command(aliases=['sah'])
async def greet(ctx):
    await ctx.send(f":smiley: :wave: Sah\' {ctx.author.mention}!")


@bot.command()
async def pikesup(ctx):
    guild = ctx.guild
    role = discord.utils.get(guild.roles, name='@everyone')
    await ctx.send(f"PIKES UP! :raised_back_of_hand: {role}")



@bot.command()
async def poll(ctx, question: str, *options: str):
    if len(options) <= 1:
        await ctx.send("You need more than one option to make a poll!")
        return
    if len(options) > 10:
        await ctx.send("Cannot make a poll with more than 10 options!")
        return
    if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
        reactions = ['✅', '❌']
    else:
        reactions = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']

    description = []
    for x, option in enumerate(options):
        description += '\n {} {}'.format(reactions[x], option)
    embed = discord.Embed(title=question, description=''.join(description))
    react_message = await ctx.send(embed=embed)
    for reaction in reactions[:len(options)]:
        await react_message.add_reaction(reaction)
    embed.set_footer(text='Poll ID: {}'.format(react_message.id))
    await react_message.edit(embed=embed)


#@bot.command()
#async def cat(ctx):
#    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")


@bot.command()
async def info(ctx):
    embed = discord.Embed(title="PikerBot", description="A bot for the Pikers.", color=0xeee657)

    # give info about you here
    embed.add_field(name="Author", value="BMendez0415")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="https://discordapp.com/api/oauth2/authorize?client_id=456944024310382592&permissions=268503040&scope=bot")

    await ctx.send(embed=embed)


bot.remove_command('help')


@bot.command()
async def help(ctx):
    embed = discord.Embed(title="PikerBot", description="A bot made for the Pikers. List of commands are:", color=0xeee657)

    #embed.add_field(name="!add X Y", value="Gives the addition of **X** and **Y**", inline=False)
    #embed.add_field(name="!multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
    embed.add_field(name="!greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name="!poll question option1 option2...", value="Creates a poll with react emojis", inline=False)
    #embed.add_field(name="!cat", value="Gives a cute cat gif to lighten up the mood.", inline=False)
    embed.add_field(name="!info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="!help", value="Gives this message", inline=False)

    await ctx.author.send(embed=embed)
bot.run(TOKEN)