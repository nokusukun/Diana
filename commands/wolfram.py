import pyowm
import tungsten
import json

def weather(self, args, token):
    if args != "":
    	owm = pyowm.OWM(token)
        obs = owm.weather_at_place(args)
        wjson = json.loads(obs.to_JSON())
        wobj = obs.get_weather()
        title = ":flag_{0}: **{1}, {2}**".format(wjson["Location"]["country"].lower(), wjson["Location"]["name"], wjson["Location"]["country"])
        em = discord.Embed(title=title, description="{6} | :thermometer: **{0}°C** (_{1}°F_) from **{2}** to **{3}°C**, wind at **{4}m/s**, humidity at **{5}%**".format(wobj.get_temperature("celsius")["temp"], 
                                                                                                                                                wobj.get_temperature("fahrenheit")["temp"],
                                                                                                                                                wobj.get_temperature("celsius")["temp_min"],
                                                                                                                                                wobj.get_temperature("celsius")["temp_max"],
                                                                                                                                                wjson["Weather"]["wind"]["speed"],
                                                                                                                                                wjson["Weather"]["humidity"],
                                                                                                                                                wobj.get_status()), colour=0x007AFF)
		return em


def wolf(self, args, token):
    if args != "":
    	waclient = tungsten.Tungsten(token)
        res = waclient.query(args)
        additional = ""
        em = discord.Embed(title='Wolfram Alpha', description="Query: "+args, colour=0x007AFF)
        em.set_author(name='{0}\'s Result'.format(message_object.author.name))
        em.set_footer(text="Wolfram Alpha Module", icon_url=self.pm.client.user.avatar_url)
        if res.success:
            for pod in res.pods:
                try:
                    em.add_field(name=pod.title, value=pod.format.get('plaintext')[0])
                except:
                    pass
            return em
        else:
            return discord.Embed(title='Wolfram Alpha', description="No results!", colour=0x007AFF)