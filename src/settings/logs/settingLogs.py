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

from typing import Union

import nextcord

__logs = dict()
config_log_list = [
    "on_message",
    "on_message_edit",
    "on_message_delete",
    "on_reaction_add",
    "on_reaction_remove",
    "on_role_add",
    "on_role_remove",
    "on_role_update",
    "on_role_create",
    "on_role_delete",
    "on_member_update_nick",
    "on_member_update_avatar",
    "on_member_join",
    "on_member_leave",
    "on_member_ban",
    "on_member_unban",
]


async def set_logs(
        bot,
        server_id: int,
        log_channel_id: int,
        log_config_int: int
) -> None:
    """
    Attributes
    ----------
    :param bot:
    :param log_config_int:
    :param server_id:
    :param log_channel_id:
    :return: None
    ----------
    """

    __logs[server_id] = {
        "log_channel_id": log_channel_id,
        "log_channel": bot.get_channel(log_channel_id),
        "log_config_int": log_config_int
    }


async def create_log(
        bot,
        server_id: int,
        log_channel_id: int,
        log_config_list: list
) -> None:
    """
    Attributes
    ----------
    :param bot:
    :param log_config_list:
    :param log_channel_id:
    :param server_id:
    :return:
    ----------
    """

    log_config_int = 0
    for i, item in enumerate(log_config_list):
        if item == "on":
            log_config_int |= (1 << i)
        elif item == "off":
            log_config_int &= ~(1 << i)
    __logs[server_id] = {
        "log_channel_id": log_channel_id,
        "log_channel": bot.get_channel(log_channel_id),
        "log_config_int": log_config_int
    }


def get_logs(
        guild_id: int
) -> bool | dict:
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


def get_logs_on_off(
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

    logs_list = {"log_channel": logs['log_channel'], "log_channel_id": logs['log_channel_id']}
    reversed_binary_str = f"{bin(logs['log_config_int'])[2:]}"[::-1]
    if len(reversed_binary_str) < len(config_log_list):
        num_zeros_to_add = len(config_log_list) - len(reversed_binary_str)
        reversed_binary_str += '0' * num_zeros_to_add
    for i, char in enumerate(reversed_binary_str):
        logs_list.update({config_log_list[i]: "on" if char == "1" else "off"})

    return logs_list
