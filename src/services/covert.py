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

class Convert:
    @staticmethod
    async def convert_to_byte(value: str) -> str:

        """
        Attributes
        ----------
        :param value:
        :return: None
        ----------
        """

        converted_value = str(bytes(str(value), "utf-8")).replace("\\", "")[2:-1]
        return converted_value

    @staticmethod
    async def convert_to_unicode(value: str) -> bytes:
        value_as_unicode = value.encode("utf-8")

        return value_as_unicode
