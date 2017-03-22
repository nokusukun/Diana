import requests
import random
import discord
from bs4 import BeautifulSoup


def gelbooru_search(message):

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
            # Calculate number of pages, and search one at random.
            maxpage = int(round(count/100))
            pid = list(range(0, maxpage))
            random.shuffle(pid)

            r = requests.get(url + message + "&pid=" + str(pid[0]))
            soup = BeautifulSoup(r.content, "xml")
            posts = soup.find_all("post")

            # Choose random post id from actual post count on page.
            if count < 100:
                postid = list(range(1, count % 100))
                random.shuffle(postid)

            else:
                postid = list(range(1, 100))
                random.shuffle(postid)

        except:
            return None

        finally:
            # Create discord embed.
            post = "https:" + str(posts[int(postid[0])]['file_url'])
            source_url = str(posts[int(postid[0])]['source'])
            postid = str(posts[int(postid[0])]['id'])
            orig_url = "http://gelbooru.com/index.php?page=post&s=view&id={id}".format(id=postid)
            print(postid)
            embed = discord.Embed(title="\n", url=post)
            embed.set_image(url=post)
            embed.add_field(name="Gelbooru", value="[[Gelbooru]]({o}) [[Source]]({s})".format(o=orig_url, s=source_url), inline=False)
            return embed
