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
class ToggleSessionCanAcceptSecretChats(BaseObject):
    """
    Toggles whether a session can accept incoming secret chats

    :param session_id: Session identifier
    :type session_id: :class:`Int64`
    :param can_accept_secret_chats: Pass true to allow accepting secret chats by the session; pass false otherwise
    :type can_accept_secret_chats: :class:`Bool`
    """

    ID: typing.Literal["toggleSessionCanAcceptSecretChats"] = field(
        default="toggleSessionCanAcceptSecretChats", metadata={"alias": "@type"}
    )
    session_id: Int64
    can_accept_secret_chats: Bool = field(default=False)
