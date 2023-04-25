import discord
from discord.ext import commands
import os
import subprocess
import shutil

TOKEN = "TOKEN"
channel_id = 0000000000000

intents = discord.Intents.all()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

def obfuscation(path, author):
    copy = f"{os.getcwd()}/obfuscated/{author}.lua"

    # Removing duplicates
    if os.path.exists(copy):
        os.remove(copy)

    # Copying the uploaded file to perform operations on it
    shutil.copyfile(path, copy)

    # Copying the obfuscate file to the copied file
    text_file = open(f"{os.getcwd()}/obfuscate.lua", "r")
    data = text_file.read()
    text_file.close()
    f = open(copy, "a")
    f.truncate(0)
    f.write(data)
    f.close()

   # Saving the uploaded file to the obfuscation script
    originalupload = open(path, "r")
    originalupload_data = originalupload.read()
    originalupload.close()

    with open(copy, "r") as in_file:
        buf = in_file.readlines()

    with open(copy, "w") as out_file:
        for line in buf:
            if line == "--SCRIPT\n":
                line = originalupload_data + '\n'
            out_file.write(line)


    # Running the script and creating a new file with the obfuscated result.
    output = subprocess.getoutput(f'lua {copy}')

    if os.path.exists(f"{os.getcwd()}/obfuscated/{author}-obfuscated.lua"):
        os.remove(f"{os.getcwd()}/obfuscated/{author}-obfuscated.lua")

    f = open(f"{os.getcwd()}/obfuscated/{author}-obfuscated.lua", "a")
    f.write(output)
    f.close()

    os.remove(copy)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if message.channel.id == channel_id and message.attachments:
        for attachment in message.attachments:
            if attachment.filename.endswith('.lua'):
                uploads_dir = f"{os.getcwd()}/uploads"
                obfuscated_dir = f"{os.getcwd()}/obfuscated"

                if not os.path.exists(uploads_dir):
                    os.makedirs(uploads_dir)
                if not os.path.exists(obfuscated_dir):
                    os.makedirs(obfuscated_dir)

                print(f'\nNew lua script received from {message.author}.')
                print(f'Attachment Link: {message.attachments[0].url}\n')
                response = await message.attachments[0].read()
                path = f"{os.getcwd()}/uploads/{message.author}.lua"

                if os.path.exists(path):
                    os.remove(path)

                open(path, "wb").write(response)
                obfuscation(path, message.author)
                embed=discord.Embed(title="File has been obfuscated", color=0x3357FF)
                await message.channel.send(embed=embed, file=discord.File(f"{os.getcwd()}/obfuscated/{message.author}-obfuscated.lua"))
            else:
                await message.channel.send("The file doesn't have a .lua extension. Please check the file.")
    await bot.process_commands(message)

bot.run(TOKEN)
