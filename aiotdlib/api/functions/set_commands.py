# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    BotCommand,
    BotCommandScope,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetCommands(BaseObject):
    """
    Sets the list of commands supported by the bot for the given user scope and language; for bots only

    :param commands: List of the bot's commands
    :type commands: :class:`Vector[BotCommand]`
    :param language_code: A two-letter ISO 639-1 language code. If empty, the commands will be applied to all users from the given scope, for which language there are no dedicated commands
    :type language_code: :class:`String`
    :param scope: The scope to which the commands are relevant; pass null to change commands in the default bot command scope, defaults to None
    :type scope: :class:`BotCommandScope`, optional
    """

    ID: typing.Literal["setCommands"] = field(default="setCommands", metadata={"alias": "@type"})
    commands: Vector[BotCommand]
    language_code: String = field(default="")
    scope: typing.Optional[BotCommandScope] = field(default=None)
