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
class ToggleChatIsTranslatable(BaseObject):
    """
    Changes the translatable state of a chat

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param is_translatable: New value of is_translatable
    :type is_translatable: :class:`Bool`
    """

    ID: typing.Literal["toggleChatIsTranslatable"] = field(
        default="toggleChatIsTranslatable", metadata={"alias": "@type"}
    )
    chat_id: Int53
    is_translatable: Bool
