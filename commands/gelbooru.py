import requests
import random
import discord
from bs4 import BeautifulSoup


def gelbooru_search(message, cache):

    if message in cache and len(cache) > 1:
        # checks if there's a cached search in the search cache and skips this one.
        url = "http://gelbooru.com/index.php?page=dapi&s=post&q=index&tags="
        r = requests.get(url + message)

    # If response is OK, continue.
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, "xml")
        count = int(soup.find("posts")['count'])

        # Skip empty searches.
        if count is 0:
            return None

        try:
            if len(cache) <= 1:
                # Skips the whole thing if there's still items in the cache, if not it searches again.
                # Calculate number of pages, and search one at random.
                maxpage = int(round(count/100))
                pid = list(range(0, maxpage))
                random.shuffle(pid)

                r = requests.get(url + message + "&pid=" + str(pid[0]))
                soup = BeautifulSoup(r.content, "xml")
                posts = soup.find_all("post")
                cache[message] = random.shuffle(posts) #shuffles and cache the posts.
        except:
            return None

        finally:
            # Create discord embed.
            posts = cache[message].pop()
            #pops one post from the cache. This ensures that the bot will go through all of the search results without sending any duplicates.
            #PSA: I overriden the 'posts' variable cause im a lazy ass fuck.

            post = "https:" + str(posts['file_url'])
            source_url = str(posts['source'])
            postid = str(posts['id'])
            orig_url = "http://gelbooru.com/index.php?page=post&s=view&id={id}".format(id=postid)
            print(postid)
            embed = discord.Embed(title="\n", url=post)
            embed.set_image(url=post)
            embed.add_field(name="Gelbooru", value="[[Gelbooru]]({o}) [[Source]]({s})".format(o=orig_url, s=source_url), inline=False)
            return embed
