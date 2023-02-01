import nextcord

__perms = {}


async def add_perms(channel_id: int, member: nextcord.Member):
    __perms[channel_id] = {"voice_owner": f"{member}"}


async def change_perms(user: str, voice: nextcord.VoiceChannel):
    __perms[voice.id]["voice_owner"] = user


async def get_host(channel_id: int):
    return __perms[channel_id]


async def remove_perms(channel_id: int):
    del __perms[channel_id]


async def check_permissions(ctx: nextcord.Interaction, voice: nextcord.VoiceChannel):
    try:
        if str(__perms[voice.id]["voice_owner"]) == str(ctx.user):
            return True
    except KeyError:
        return False
