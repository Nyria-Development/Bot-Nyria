from database.query import Query

query = Query(
    pool_name="level_setting",
    pool_size=3
)
__level_settings = {}


async def set_leveling(server_id: int, leveling_setting, leveling_speed) -> None:
    leveling = query.execute(
        query="SELECT * FROM leveling WHERE serverId=%s",
        data=[int(server_id)]
    )
    if leveling_setting == "True":
        if not leveling:
            query.execute(
                "INSERT INTO leveling (serverId, levelSpeed) VALUE (%s,%s)",
                data=[int(server_id), int(leveling_speed)]
            )
            __level_settings[server_id] = leveling_speed
        else:
            query.execute(
                query=f"UPDATE leveling SET levelSpeed={leveling_speed} WHERE serverId=%s",
                data=[int(server_id)]
            )
            __level_settings[server_id] = leveling_speed
            return
    else:
        if leveling:
            query.execute(
                "Delete From leveling WHERE serverId=%s",
                data=[int(server_id)]
            )
            __level_settings[server_id] = 0
            return


def get_leveling_server(server_id: int):
    if server_id not in __level_settings:
        return False
    return __level_settings[server_id]


async def load_leveling_servers() -> print:
    data = query.execute(
        query="SELECT * FROM leveling",
        data=[]
    )

    if not data:
        return print("No leveling Server to load")

    for guilds in data:
        __level_settings[guilds[0]] = guilds[1]

    return print("leveling Server loaded")
