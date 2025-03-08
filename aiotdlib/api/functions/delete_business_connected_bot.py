# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.base import *


@dataclass(slots=True, kw_only=True)
class DeleteBusinessConnectedBot(BaseObject):
    """
    Deletes the business bot that is connected to the current user account

    :param bot_user_id: Unique user identifier for the bot
    :type bot_user_id: :class:`Int53`
    """

    ID: typing.Literal["deleteBusinessConnectedBot"] = field(
        default="deleteBusinessConnectedBot", metadata={"alias": "@type"}
    )
    bot_user_id: Int53
