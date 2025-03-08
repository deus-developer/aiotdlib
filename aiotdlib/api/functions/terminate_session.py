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
class TerminateSession(BaseObject):
    """
    Terminates a session of the current user

    :param session_id: Session identifier
    :type session_id: :class:`Int64`
    """

    ID: typing.Literal["terminateSession"] = field(default="terminateSession", metadata={"alias": "@type"})
    session_id: Int64
