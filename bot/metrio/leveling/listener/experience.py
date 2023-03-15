import json
import nextcord
from nextcord.ext import commands
from src.loader import jsonLoader
from src.dictionaries import level


class Experience(commands.Cog):
    def __init__(self):
        self.bot = 1
        # TODO Muss das in die Bot listener oder wäre es nicht Außerhalb besser? (Schreib mir dann nochmal)
        # TODO Safe data in Dictionary and database

    @staticmethod
    async def add_new_exp(
        message: nextcord.Message
    ) -> None:

        """
        Attributes
        ----------
        :param message:
        :type message: nextcord.Message
        :return: None
        """

        if not level.get_leveling_server(message.guild.id):
            return print(level.get_leveling_server(message.guild.id))

        user_list = jsonLoader.Leveling().get_levels()

        if not any(user['discordUserID'] == message.author.id for user in user_list):
            new_user = {"discordUser": message.author.name, "discordUserID": message.author.id, "level": 1, "xp": 1}
            user_list.append(new_user)

            await message.channel.send(f"{message.author.mention}, You made your first XP!")
            with open("resources/information/leveling.json", "w") as file:
                json.dump(user_list, file, indent=4)
                return

        for user in user_list:
            if user['discordUserID'] == message.author.id:
                user['xp'] += level.get_leveling_server(message.guild.id)
                if user['xp'] > pow(2, user['level']):
                    user['level'] += 1
                    for role in jsonLoader.LevelRoles().get_Roles()[str(message.guild.id)]:
                        if int(user['level']) >= int(role['level']):
                            await message.author.add_roles(message.guild.get_role(role['roleID']))
                    await message.channel.send(
                              f"{message.author.mention} You just leveled up to Level {user['level']}")
                with open("resources/information/leveling.json", "w") as file:
                    json.dump(user_list, file, indent=4)
                    break


def setup(bot):
    bot.add_cog(Experience())
