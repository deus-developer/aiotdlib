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
class ConfirmSession(BaseObject):
    """
    Confirms an unconfirmed session of the current user from another device

    :param session_id: Session identifier
    :type session_id: :class:`Int64`
    """

    ID: typing.Literal["confirmSession"] = field(default="confirmSession", metadata={"alias": "@type"})
    session_id: Int64
