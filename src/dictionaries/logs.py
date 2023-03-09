from database.query import Query


query = Query(
    pool_name="log_channels",
    pool_size=3
)
__logs_settings = {}


async def set_log_channel(server_id: int, channel_id: int) -> None:
    channel = query.execute(
        query="SELECT channelId FROM logs WHERE serverId=%s",
        data=[int(server_id)]
    )
    if not channel:
        query.execute(
            "INSERT INTO logs (serverId, channelId) VALUE (%s,%s)",
            data=[int(server_id), int(channel_id)]
        )
        __logs_settings[server_id] = channel_id
        return

    query.execute(
        query=f"UPDATE logs SET channelId={channel_id} WHERE serverId=%s",
        data=[int(server_id)]
    )
    __logs_settings[server_id] = channel_id


def get_log_channel(server_id: int):
    if server_id not in __logs_settings:
        return
    return __logs_settings[server_id]


async def load_log_channels() -> print:
    data = query.execute(
        query="SELECT * FROM logs",
        data=[]
    )

    if not data:
        return print("No logs to load")

    for guilds in data:
        __logs_settings[guilds[0]] = guilds[1]

    return print("Logs loaded")
