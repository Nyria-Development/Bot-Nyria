import json
import nextcord
from nextcord.ext import commands
from src.loader import jsonLoader


class experience(commands.Cog):
    def __init__(self):
        self.bot = 1
        self.xp_speed = 1 #can be changed by every Guild

    async def add_new_exp(self, message):
        user_list = jsonLoader.Leveling().get_levels()
        if any(user['discordUserID'] == message.author.id for user in user_list):
            for user in user_list:
                if user['discordUserID'] == message.author.id:
                    user['xp'] += self.xp_speed
                    if user['xp'] > pow(2, user['level']):
                        user['level'] += 1
                        await message.channel.send(f"{message.author.mention} You just leveld up to Level {user['level']}")
                    with open("resources/information/leveling.json", "w") as file:
                        json.dump(user_list, file, indent=4)
                    break
        else:
            new_user = {"discordUser": message.author.name, "discordUserID": message.author.id, "level": 1, "xp": 1}
            user_list.append(new_user)
            await message.channel.send(f"{message.author.mention}, You made your first XP!")
            with open("resources/information/leveling.json", "w") as file:
                json.dump(user_list, file, indent=4)





def setup(bot):
    bot.add_cog(experience())
