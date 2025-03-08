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
class EndGroupCallRecording(BaseObject):
    """
    Ends recording of an active group call. Requires groupCall.can_be_managed group call flag

    :param group_call_id: Group call identifier
    :type group_call_id: :class:`Int32`
    """

    ID: typing.Literal["endGroupCallRecording"] = field(default="endGroupCallRecording", metadata={"alias": "@type"})
    group_call_id: Int32
