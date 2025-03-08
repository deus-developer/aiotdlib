# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    BusinessConnectedBot,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetBusinessConnectedBot(BaseObject):
    """
    Adds or changes business bot that is connected to the current user account

    :param bot: Connection settings for the bot
    :type bot: :class:`BusinessConnectedBot`
    """

    ID: typing.Literal["setBusinessConnectedBot"] = field(
        default="setBusinessConnectedBot", metadata={"alias": "@type"}
    )
    bot: BusinessConnectedBot
