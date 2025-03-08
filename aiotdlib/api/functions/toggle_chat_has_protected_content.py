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
class ToggleChatHasProtectedContent(BaseObject):
    """
    Changes the ability of users to save, forward, or copy chat content. Supported only for basic groups, supergroups and channels. Requires owner privileges

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param has_protected_content: New value of has_protected_content
    :type has_protected_content: :class:`Bool`
    """

    ID: typing.Literal["toggleChatHasProtectedContent"] = field(
        default="toggleChatHasProtectedContent", metadata={"alias": "@type"}
    )
    chat_id: Int53
    has_protected_content: Bool
