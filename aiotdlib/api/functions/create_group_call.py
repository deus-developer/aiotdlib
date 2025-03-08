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
class CreateGroupCall(BaseObject):
    """
    Creates a group call from a one-to-one call

    :param call_id: Call identifier
    :type call_id: :class:`Int32`
    """

    ID: typing.Literal["createGroupCall"] = field(default="createGroupCall", metadata={"alias": "@type"})
    call_id: Int32
