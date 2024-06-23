import discord 

client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_message(msg discord.Message):
    if msg.author == client.user:
        return
    if msg.content.lower() == 'Привет':
        await msg.channel.send('Здраствуйте.')
        
    if msg.content.lower() == 'Как дела?':
        await msg.channel.send('Отлично!')
