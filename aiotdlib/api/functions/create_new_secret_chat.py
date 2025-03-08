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
class CreateNewSecretChat(BaseObject):
    """
    Creates a new secret chat. Returns the newly created chat

    :param user_id: Identifier of the target user
    :type user_id: :class:`Int53`
    """

    ID: typing.Literal["createNewSecretChat"] = field(default="createNewSecretChat", metadata={"alias": "@type"})
    user_id: Int53
