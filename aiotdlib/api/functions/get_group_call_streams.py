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
class GetGroupCallStreams(BaseObject):
    """
    Returns information about available group call streams

    :param group_call_id: Group call identifier
    :type group_call_id: :class:`Int32`
    """

    ID: typing.Literal["getGroupCallStreams"] = field(default="getGroupCallStreams", metadata={"alias": "@type"})
    group_call_id: Int32
