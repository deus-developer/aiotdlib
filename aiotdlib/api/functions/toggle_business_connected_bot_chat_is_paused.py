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
class ToggleBusinessConnectedBotChatIsPaused(BaseObject):
    """
    Pauses or resumes the connected business bot in a specific chat

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param is_paused: Pass true to pause the connected bot in the chat; pass false to resume the bot
    :type is_paused: :class:`Bool`
    """

    ID: typing.Literal["toggleBusinessConnectedBotChatIsPaused"] = field(
        default="toggleBusinessConnectedBotChatIsPaused", metadata={"alias": "@type"}
    )
    chat_id: Int53
    is_paused: Bool = field(default=False)
