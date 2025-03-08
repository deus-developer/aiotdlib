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
class ToggleSessionCanAcceptCalls(BaseObject):
    """
    Toggles whether a session can accept incoming calls

    :param session_id: Session identifier
    :type session_id: :class:`Int64`
    :param can_accept_calls: Pass true to allow accepting incoming calls by the session; pass false otherwise
    :type can_accept_calls: :class:`Bool`
    """

    ID: typing.Literal["toggleSessionCanAcceptCalls"] = field(
        default="toggleSessionCanAcceptCalls", metadata={"alias": "@type"}
    )
    session_id: Int64
    can_accept_calls: Bool = field(default=False)
