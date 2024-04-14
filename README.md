# PandaAI - ChatGPT Discord Bot

PandaAI is a Discord bot that integrates the power of OpenAI's GPT models to bring intelligent conversational capabilities directly to your Discord server. Designed to enrich your community's interaction, PandaAI can engage in real-time conversations, answer questions, and provide helpful responses based on the context of the chat.

## Features

- **Intelligent Chat Handling:** Leverage the power of ChatGPT-3.5-Turbo to generate responses.
- **Customizable Interaction:** Configure command prefixes and responses to fit the culture and tone of your Discord server.
- **Secure and Scalable:** Designed with privacy and scalability in mind, PandaAI can handle multiple conversations simultaneously without compromising data security.

## Requirements

- Python 3.8+
- discord.py
- openai
- A valid Discord bot token
- An OpenAI API key

## Getting Started

To use PandaAI, you need to set up a Discord bot and obtain an OpenAI API token. Follow these step-by-step instructions to get everything up and running.

### Obtaining an OpenAI API Token

1. **Sign Up or Log In to OpenAI**
   - Visit [OpenAI's official website](https://www.openai.com/) and sign up for an account if you don't already have one. If you have an account, simply log in.

2. **API Access**
   - Navigate to the API section on your OpenAI dashboard. This is typically found in your account settings or under a dedicated API section.

3. **Create a New API Key**
   - Click on the button to generate a new API key. Label your key descriptively, so it’s easy to identify later (e.g., DiscordBot).

4. **Copy Your API Key**
   - Copy the API key generated and store it securely. You will need this key for your bot to interact with OpenAI’s services.

### Setting Up a Discord Bot

1. **Create a Discord Application**
   - Go to the Discord Developer Portal (https://discord.com/developers/applications) and log in with your Discord account.
   - Click on the “New Application” button. Name your application and save it.

2. **Add a Bot to Your Application**
   - Select the “Bot” tab in the settings menu on the left.
   - Click on “Add Bot” and confirm by clicking “Yes, do it!”

3. **Configure Your Bot**
   - Customize your bot’s name and avatar. Under the “TOKEN” section, click “Copy” to get your bot’s token. This token is sensitive and should be kept secure.

4. **Invite the Bot to Your Server**
   - Under the “OAuth2” tab, select “URL Generator” from the sidebar.
   - In the “SCOPES” section, check “bot”. In the “BOT PERMISSIONS” section, select the permissions your bot will need (at least “Send Messages” and “Read Message History”).
   - Copy the generated URL, paste it into your browser, select your server, and authorize the bot.

## Set Up Your Configuration
Create a .env file in the root directory and populate it with your Discord bot token and OpenAI API key:
```
DISCORD_TOKEN=your_discord_bot_token
OPENAI_API_KEY=your_openai_api_key
```
