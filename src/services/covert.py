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
