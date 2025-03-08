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
class SetDefaultGroupAdministratorRights(BaseObject):
    """
    Sets default administrator rights for adding the bot to basic group and supergroup chats; for bots only

    :param default_group_administrator_rights: Default administrator rights for adding the bot to basic group and supergroup chats; pass null to remove default rights, defaults to None
    :type default_group_administrator_rights: :class:`ChatAdministratorRights`, optional
    """

    ID: typing.Literal["setDefaultGroupAdministratorRights"] = field(
        default="setDefaultGroupAdministratorRights", metadata={"alias": "@type"}
    )
    default_group_administrator_rights: typing.Optional[ChatAdministratorRights] = field(default=None)
