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
class CheckChatInviteLink(BaseObject):
    """
    Checks the validity of an invite link for a chat and returns information about the corresponding chat

    :param invite_link: Invite link to be checked
    :type invite_link: :class:`String`
    """

    ID: typing.Literal["checkChatInviteLink"] = field(default="checkChatInviteLink", metadata={"alias": "@type"})
    invite_link: String
