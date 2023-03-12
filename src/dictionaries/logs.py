from database.query import Query

query = Query(
    pool_name="log_channels",
    pool_size=3
)
__logs_settings = {}  # for guild: [channel_id(0), log_active(1), message_log(2), reaction_log(3), member_log(4)]


async def config_log_settings(server_id: int, log_channel_id, log, message_log, reaction_log, on_member_log):
    data = query.execute(
        query="SELECT * FROM logs WHERE serverId=%s",
        data=[int(server_id)]
    )
    log = 1 if log == "on" else 0
    message_log = 1 if message_log == "on" else 0
    reaction_log = 1 if reaction_log == "on" else 0
    on_member_log = 1 if on_member_log == "on" else 0
    if not data:
        query.execute(
            query="INSERT INTO logs (serverId, channelId, log_active, on_message, on_reaction, on_member_event) VALUE (%s,%s,%s,%s,%s,%s)",
            data=[int(server_id), int(log_channel_id), log, message_log, reaction_log, on_member_log]
        )
        __logs_settings[server_id] = [log_channel_id, log, message_log, reaction_log, on_member_log]
        return
    query.execute(
        query=f"UPDATE logs SET channelId={log_channel_id}, log_active={log}, on_message={message_log}, on_reaction={reaction_log}, on_member_event={on_member_log} WHERE serverId=%s",
        data=[int(server_id)]
    )
    __logs_settings[server_id] = [log_channel_id, log, message_log, reaction_log, on_member_log]


def get_log_channel(server_id: int):
    if server_id not in __logs_settings:
        return 0
    return __logs_settings[server_id][0]


def get_log_on_state(server_id: int, on_event: int):
    if server_id not in __logs_settings:
        return
    return __logs_settings[server_id][on_event]


async def load_log_channels() -> print:
    data = query.execute(
        query="SELECT * FROM logs",
        data=[]
    )

    if not data:
        return print("No logs to load")

    for guilds in data:
        __logs_settings[guilds[0]] = [guilds[1], guilds[2], guilds[3], guilds[4], guilds[5]]

    return print("Logs loaded")
