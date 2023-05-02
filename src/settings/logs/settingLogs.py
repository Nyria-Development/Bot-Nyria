__logs = dict()


async def set_logs(
        server_id: int,
        log_channel_id: int,
        on_message: str,
        on_message_edit: str,
        on_message_delete: str,
        on_reaction_add: str,
        on_member_ban: str,
        on_member_unban: str
) -> None:

    """
    Attributes
    ----------
    :param server_id:
    :param log_channel_id:
    :param on_message:
    :param on_message_edit:
    :param on_message_delete:
    :param on_reaction_add:
    :param on_member_ban:
    :param on_member_unban:
    :return: None
    ----------
    """

    __logs[server_id] = {
        "log_channel_id": log_channel_id,
        "on_message": on_message,
        "on_message_edit": on_message_edit,
        "on_message_delete": on_message_delete,
        "on_reaction_add": on_reaction_add,
        "on_member_ban": on_member_ban,
        "on_member_unban": on_member_unban
    }


async def get_logs(
        guild_id: int
) -> dict | bool:

    """
    Attributes
    ----------
    :param guild_id:
    :return: None
    ----------
    """

    try:
        logs = __logs[guild_id]
    except KeyError:
        return False

    return logs
