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
class SendWebAppCustomRequest(BaseObject):
    """
    Sends a custom request from a Web App

    :param bot_user_id: Identifier of the bot
    :type bot_user_id: :class:`Int53`
    :param method: The method name
    :type method: :class:`String`
    :param parameters: JSON-serialized method parameters
    :type parameters: :class:`String`
    """

    ID: typing.Literal["sendWebAppCustomRequest"] = field(
        default="sendWebAppCustomRequest", metadata={"alias": "@type"}
    )
    bot_user_id: Int53
    method: String
    parameters: String
