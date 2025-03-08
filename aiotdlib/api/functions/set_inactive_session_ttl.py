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
class SetInactiveSessionTtl(BaseObject):
    """
    Changes the period of inactivity after which sessions will automatically be terminated

    :param inactive_session_ttl_days: New number of days of inactivity before sessions will be automatically terminated; 1-366 days
    :type inactive_session_ttl_days: :class:`Int32`
    """

    ID: typing.Literal["setInactiveSessionTtl"] = field(default="setInactiveSessionTtl", metadata={"alias": "@type"})
    inactive_session_ttl_days: Int32
