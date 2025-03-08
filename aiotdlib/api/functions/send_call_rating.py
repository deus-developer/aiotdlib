# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    CallProblem,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SendCallRating(BaseObject):
    """
    Sends a call rating

    :param call_id: Call identifier
    :type call_id: :class:`Int32`
    :param rating: Call rating; 1-5
    :type rating: :class:`Int32`
    :param comment: An optional user comment if the rating is less than 5
    :type comment: :class:`String`
    :param problems: List of the exact types of problems with the call, specified by the user
    :type problems: :class:`Vector[CallProblem]`
    """

    ID: typing.Literal["sendCallRating"] = field(default="sendCallRating", metadata={"alias": "@type"})
    call_id: Int32
    rating: Int32
    comment: String
    problems: Vector[CallProblem]
