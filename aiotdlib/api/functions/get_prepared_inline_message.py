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
class GetPreparedInlineMessage(BaseObject):
    """
    Saves an inline message to be sent by the given user

    :param bot_user_id: Identifier of the bot that created the message
    :type bot_user_id: :class:`Int53`
    :param prepared_message_id: Identifier of the prepared message
    :type prepared_message_id: :class:`String`
    """

    ID: typing.Literal["getPreparedInlineMessage"] = field(
        default="getPreparedInlineMessage", metadata={"alias": "@type"}
    )
    bot_user_id: Int53
    prepared_message_id: String
