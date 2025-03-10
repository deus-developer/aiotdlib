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
class SendWebAppData(BaseObject):
    """
    Sends data received from a keyboardButtonTypeWebApp Web App to a bot

    :param bot_user_id: Identifier of the target bot
    :type bot_user_id: :class:`Int53`
    :param button_text: Text of the keyboardButtonTypeWebApp button, which opened the Web App
    :type button_text: :class:`String`
    :param data: The data
    :type data: :class:`String`
    """

    ID: typing.Literal["sendWebAppData"] = field(default="sendWebAppData", metadata={"alias": "@type"})
    bot_user_id: Int53
    button_text: String
    data: String
