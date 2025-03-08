# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    ChatAdministratorRights,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetDefaultChannelAdministratorRights(BaseObject):
    """
    Sets default administrator rights for adding the bot to channel chats; for bots only

    :param default_channel_administrator_rights: Default administrator rights for adding the bot to channels; pass null to remove default rights, defaults to None
    :type default_channel_administrator_rights: :class:`ChatAdministratorRights`, optional
    """

    ID: typing.Literal["setDefaultChannelAdministratorRights"] = field(
        default="setDefaultChannelAdministratorRights", metadata={"alias": "@type"}
    )
    default_channel_administrator_rights: typing.Optional[ChatAdministratorRights] = field(default=None)
