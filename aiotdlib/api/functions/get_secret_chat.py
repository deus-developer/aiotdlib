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
class GetSecretChat(BaseObject):
    """
    Returns information about a secret chat by its identifier. This is an offline request

    :param secret_chat_id: Secret chat identifier
    :type secret_chat_id: :class:`Int32`
    """

    ID: typing.Literal["getSecretChat"] = field(default="getSecretChat", metadata={"alias": "@type"})
    secret_chat_id: Int32
