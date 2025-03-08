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
class CreatePrivateChat(BaseObject):
    """
    Returns an existing chat corresponding to a given user

    :param user_id: User identifier
    :type user_id: :class:`Int53`
    :param force: Pass true to create the chat without a network request. In this case all information about the chat except its type, title and photo can be incorrect
    :type force: :class:`Bool`
    """

    ID: typing.Literal["createPrivateChat"] = field(default="createPrivateChat", metadata={"alias": "@type"})
    user_id: Int53
    force: Bool = field(default=False)
