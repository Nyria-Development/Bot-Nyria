import json
import nextcord
from nextcord.ext import commands
from src.loader import jsonLoader
from src.dictionaries import level


class experience(commands.Cog):
    def __init__(self):
        self.bot = 1

    async def add_new_exp(self, message):
        if level.get_leveling_server(message.guild.id):
            print("yes xp")
            user_list = jsonLoader.Leveling().get_levels()
            if any(user['discordUserID'] == message.author.id for user in user_list):
                for user in user_list:
                    if user['discordUserID'] == message.author.id:
                        user['xp'] += level.get_leveling_server(message.guild.id)
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
        else:
            print(level.get_leveling_server(message.guild.id))





def setup(bot):
    bot.add_cog(experience())
