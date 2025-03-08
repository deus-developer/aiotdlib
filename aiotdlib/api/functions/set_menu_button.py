# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    BotMenuButton,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetMenuButton(BaseObject):
    """
    Sets menu button for the given user or for all users; for bots only

    :param user_id: Identifier of the user or 0 to set menu button for all users
    :type user_id: :class:`Int53`
    :param menu_button: New menu button
    :type menu_button: :class:`BotMenuButton`
    """

    ID: typing.Literal["setMenuButton"] = field(default="setMenuButton", metadata={"alias": "@type"})
    user_id: Int53
    menu_button: BotMenuButton
