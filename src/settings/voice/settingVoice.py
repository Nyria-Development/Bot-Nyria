# All Rights Reserved
# Copyright (c) 2023 Nyria
#
# This code, including all accompanying software, documentation, and related materials, is the exclusive property
# of Nyria. All rights are reserved.
#
# Any use, reproduction, distribution, or modification of the code without the express written
# permission of Nyria is strictly prohibited.
#
# No warranty is provided for the code, and Nyria shall not be liable for any claims, damages,
# or other liability arising from the use or inability to use the code.

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
