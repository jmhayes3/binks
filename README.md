# Binks

## Quickstart

Create Discord Bot:

1. [Go to Discord developer portal](https://discord.com/developers/applications)
    - Under Application » Bot
        * Enable Message Content Intent
        * Enable Server Members Intent (for replacing user mentions with the username)
2. Invite the bot to a server
    - Go to Application » OAuth2 » URL Generator
    - Enable `bot`
    - Enable Send Messages, Read Messages/View Channels, and Read Message History
    - Under Generated URL, click Copy and paste the URL in your browser
3. Rename `.env.example` to `.env` and edit the file
    - You can get the token from Application » Bot » Token, **never share this with anyone**
    - Set the channels to the channel ID, comma separated
        1. In Discord, go to User Settings » Advanced, and enable Developer Mode
        2. Right click on a channel you want to use, and click Copy Channel ID

Start LLM backend:

```sh
ollama pull llama2
ollama serve
```

Run:

```sh
python binks.py
```

