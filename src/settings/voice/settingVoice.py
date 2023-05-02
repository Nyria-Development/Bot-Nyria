import nextcord

__category = {}


async def set_category(
        guild_id: int,
        category_name: str
) -> None:

    """
    Attributes
    ----------
    :param guild_id:
    :param category_name:
    :return: None
    ----------
    """

    __category[guild_id] = category_name


async def get_category(
        guild_id: int
) -> str | None:

    """
    Attributes
    ----------
    :param guild_id:
    :return: None
    ----------
    """
    try:
        category_name = __category[guild_id]
    except KeyError:
        return

    return category_name
