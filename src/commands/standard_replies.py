import os
import json

STANDARD_REPLIES = json.loads(os.getenv('STANDARD_REPLIES', default=r"{}"))

async def reply_to_message(message):
    content = message.content.lower()

    if content == 'hello lallubot':
        await message.channel.send('Hello {0.author}'.format(message))
    else:
        for word in STANDARD_REPLIES:
            if word in content:
                await message.channel.send(str(STANDARD_REPLIES[word]))
