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
class PingProxy(BaseObject):
    """
    Computes time needed to receive a response from a Telegram server through a proxy. Can be called before authorization

    :param proxy_id: Proxy identifier. Use 0 to ping a Telegram server without a proxy
    :type proxy_id: :class:`Int32`
    """

    ID: typing.Literal["pingProxy"] = field(default="pingProxy", metadata={"alias": "@type"})
    proxy_id: Int32
