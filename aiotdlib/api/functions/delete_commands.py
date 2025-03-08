# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    BotCommandScope,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class DeleteCommands(BaseObject):
    """
    Deletes commands supported by the bot for the given user scope and language; for bots only

    :param language_code: A two-letter ISO 639-1 language code or an empty string
    :type language_code: :class:`String`
    :param scope: The scope to which the commands are relevant; pass null to delete commands in the default bot command scope, defaults to None
    :type scope: :class:`BotCommandScope`, optional
    """

    ID: typing.Literal["deleteCommands"] = field(default="deleteCommands", metadata={"alias": "@type"})
    language_code: String
    scope: typing.Optional[BotCommandScope] = field(default=None)
