import json
import requests
import discord


def urbandict(word):
    ud_url = 'http://api.urbandictionary.com/v0/define?term=' + word
    try:
        # Returns first entry for requested word.
        response = json.loads(requests.get(ud_url).text)['list'][0]

    except:
        # logger.exception('urbandict failed.')
        print("no")
        return None

    definition = response['definition']
    permalink = response['permalink']
    title = response['word']
    example = "_" + response['example'] + "_"

    embed = discord.Embed(title="\n", url=permalink)
    embed.set_author(name="urbandictionary", icon_url="https://www.urbandictionary.com/favicon.ico")
    embed.add_field(name=title, value=definition + "\n\n" + example, inline=False)

    return embed
