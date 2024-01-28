"""
Configuration file entities models
"""

import typing
import pydantic

import roothazardlib.configs

class TopSectionsConfigModel(
    roothazardlib.configs.ConstModel,
    pydantic.BaseModel
):
    """
    A Pydantic model representing the configuration for top sections.

    Attributes:
        port (pydantic.PositiveInt): The port number for the server.
        tls (TLSConfigModel): The TLS configuration for the server.
        bots (typing.Dict[str, BotConfigModel]): A dictionary of bot configurations.

    Methods:
        __setattr__(self, _: str, __: typing.Any) -> None:
            Overrides the default __setattr__ method to make the object readonly.
            Raises an AttributeError if any attempt is made to modify the object.

    Note:
        This class is a Pydantic BaseModel, providing data validation and parsing.
        The object is made readonly, preventing modifications after instantiation.
    """

    server: roothazardlib.configs.ServerConfigModel
    tls: roothazardlib.configs.TLSConfigModel


class VelesConfigModel(
    roothazardlib.configs.ConstModel,
    roothazardlib.configs.ConfigModel
):
    """
    A Pydantic model representing the configuration for the Njordr application.

    Attributes:
        bots (typing.Dict[str, BotConfigModel]):
            A dictionary mapping bot ids to their respective configurations.

    Methods:
        __setattr__(self, _: str, __: typing.Any) -> None:
            Overrides the default __setattr__ method to make the object readonly.
            Raises an AttributeError if any attempt is made to modify the object.

        Parameters:
            key (str): The name of the bot.

        Returns:
            BotConfigModel: The configuration for the specified bot.

    Note:
        This class is a Pydantic BaseModel, providing data validation and parsing.
        The object is made readonly, preventing modifications after instantiation.
    """

    cfg: TopSectionsConfigModel


class VelesConfig(roothazardlib.configs.YamlConfig): # pylint: disable=too-few-public-methods
    """
    Njordr specific config
    """

    _model: typing.Optional[VelesConfigModel]
