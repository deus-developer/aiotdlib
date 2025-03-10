# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    CallProtocol,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class CreateCall(BaseObject):
    """
    Creates a new call

    :param user_id: Identifier of the user to be called
    :type user_id: :class:`Int53`
    :param protocol: The call protocols supported by the application
    :type protocol: :class:`CallProtocol`
    :param is_video: Pass true to create a video call
    :type is_video: :class:`Bool`
    :param group_call_id: Identifier of the group call to which the user will be added after exchanging private key via the call; pass 0 if none; currently, ignored
    :type group_call_id: :class:`Int32`
    """

    ID: typing.Literal["createCall"] = field(default="createCall", metadata={"alias": "@type"})
    user_id: Int53
    protocol: CallProtocol
    is_video: Bool = field(default=False)
    group_call_id: Int32 = field(default=0)
