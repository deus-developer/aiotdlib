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
class InviteGroupCallParticipants(BaseObject):
    """
    Invites users to an active group call. Sends a service message of type messageInviteVideoChatParticipants for video chats

    :param group_call_id: Group call identifier
    :type group_call_id: :class:`Int32`
    :param user_ids: User identifiers. At most 10 users can be invited simultaneously
    :type user_ids: :class:`Vector[Int53]`
    """

    ID: typing.Literal["inviteGroupCallParticipants"] = field(
        default="inviteGroupCallParticipants", metadata={"alias": "@type"}
    )
    group_call_id: Int32
    user_ids: Vector[Int53]
