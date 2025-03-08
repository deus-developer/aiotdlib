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
class ToggleGeneralForumTopicIsHidden(BaseObject):
    """
    Toggles whether a General topic is hidden in a forum supergroup chat; requires can_manage_topics right in the supergroup

    :param chat_id: Identifier of the chat
    :type chat_id: :class:`Int53`
    :param is_hidden: Pass true to hide and close the General topic; pass false to unhide it
    :type is_hidden: :class:`Bool`
    """

    ID: typing.Literal["toggleGeneralForumTopicIsHidden"] = field(
        default="toggleGeneralForumTopicIsHidden", metadata={"alias": "@type"}
    )
    chat_id: Int53
    is_hidden: Bool = field(default=False)
