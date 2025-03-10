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
class GetProxyLink(BaseObject):
    """
    Returns an HTTPS link, which can be used to add a proxy. Available only for SOCKS5 and MTProto proxies. Can be called before authorization

    :param proxy_id: Proxy identifier
    :type proxy_id: :class:`Int32`
    """

    ID: typing.Literal["getProxyLink"] = field(default="getProxyLink", metadata={"alias": "@type"})
    proxy_id: Int32
