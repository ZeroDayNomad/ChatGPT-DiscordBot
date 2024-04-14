import discord
from discord.ext import commands
import openai

# Initialize OpenAI GPT with your API key
openai.api_key = 'Your_OpenAI_Token'

# Create an Intents object with necessary permissions
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

# Initialize the bot with these intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def chat(ctx, *, query):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": query}]
        )
        if 'choices' in response and response['choices']:
            message_content = response['choices'][0]['message']['content']
            await ctx.send(message_content)
        else:
            await ctx.send("Failed to get a response.")
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")


# Run the bot with your token
bot.run('Your_Discord_Bot_Token')
