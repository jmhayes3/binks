# Binks

## Quickstart

Create Discord Bot:

1. [Create a Discord bot](https://discord.com/developers/applications)
    - Under Application » Bot
        - Enable Message Content Intent
        - Enable Server Members Intent (for replacing user mentions with the username)
2. Invite the bot to a server
    1. Go to Application » OAuth2 » URL Generator
    2. Enable `bot`
    3. Enable Send Messages, Read Messages/View Channels, and Read Message History
    4. Under Generated URL, click Copy and paste the URL in your browser
3. Rename `.env.example` to `.env` and edit the file
    - You can get the token from Application » Bot » Token, **never share this with anyone**
    - Make sure to change the model if you aren't using `orca`
    - Ollama IP can be kept the same unless you have changed the port
    - Set the channels to the channel ID, comma separated
        1. In Discord, go to User Settings » Advanced, and enable Developer Mode
        2. Right click on a channel you want to use, and click Copy Channel ID
    - You can edit the system message the bot uses, or disable it entirely

Start LLM backend:

```sh
ollama pull llama2
ollama serve
```

Run:

```sh
python binks.py
```

