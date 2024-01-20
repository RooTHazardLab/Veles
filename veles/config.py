"""
Configuration file entities models
"""

import typing
import pydantic

import yaml

class TLSConfigModel(pydantic.BaseModel):
    """
    A Pydantic model representing the TLS configuration for a server.

    Attributes:
        cert (pydantic.FilePath): Path to the TLS certificate file.
        key (pydantic.FilePath): Path to the TLS private key file.
        ca (pydantic.FilePath): Path to the TLS certificate authority file.

    Methods:
        __setattr__(self, _: str, __: typing.Any) -> None:
            Overrides the default __setattr__ method to make the object readonly.
            Raises an AttributeError if any attempt is made to modify the object.

    Note:
        This class is a Pydantic BaseModel, providing data validation and parsing.
        The object is made readonly, preventing modifications after instantiation.
    """

    client_cert: pydantic.FilePath
    client_key: pydantic.FilePath
    ca: pydantic.FilePath

    def __setattr__(self, _: str, __: typing.Any) -> None:
        """
        Override the default __setattr__ method to make the object readonly.

        Args:
            _: Ignored parameter.
            __: Ignored parameter.

        Raises:
            AttributeError: If any attempt is made to modify the object.
        """

        raise AttributeError("Object is readonly")


class TopSectionsConfigModel(pydantic.BaseModel):
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

    port: pydantic.PositiveInt
    tls: TLSConfigModel

    def __setattr__(self, _: str, __: typing.Any) -> None:
        """
        Override the default __setattr__ method to make the object readonly.

        Args:
            _: Ignored parameter.
            __: Ignored parameter.

        Raises:
            AttributeError: If any attempt is made to modify the object.
        """

        raise AttributeError("Object is readonly")


class VelesConfigModel(pydantic.BaseModel):
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

    def __setattr__(self, _: str, __: typing.Any) -> None:
        """
        Override the default __setattr__ method to make the object readonly.

        Args:
            _: Ignored parameter.
            __: Ignored parameter.

        Raises:
            AttributeError: If any attempt is made to modify the object.
        """

        raise AttributeError("Object is readonly")


class Singletone(type):
    """
    Singletone metaclass for making singletones
    """

    __instances: dict[type, typing.Any] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)

        return cls.__instances[cls]


class VelesConfig(metaclass=Singletone):
    """
    VelesConfig singletone
    """

    __model: typing.Optional[VelesConfigModel] = None

    def __init__(self, config_dir: typing.Optional[str]) -> None:
        if self.__model is None:
            with open(f"{config_dir}/config.yaml", mode="r", encoding="utf-8") as config_file:
                config_obj = yaml.safe_load(config_file)

            for key, value in config_obj["tls"].items():
                config_obj["tls"][key] = f"{config_dir}/{value}"

            self.__model = VelesConfigModel(cfg=config_obj)

    def __setattr__(self, name: str, value: typing.Any) -> None:
        if "__" in name:
            super().__setattr__(name, value)
        else:
            raise AttributeError("Object is readonly")

    def __getattribute__(self, name: str) -> typing.Any:
        if "__" in name:
            return super().__getattribute__(name)

        return getattr(self.__model, name)
