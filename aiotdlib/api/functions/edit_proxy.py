# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import MISSING, dataclass, field

from ..types.all import (
    ProxyType,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class EditProxy(BaseObject):
    """
    Edits an existing proxy server for network requests. Can be called before authorization

    :param proxy_id: Proxy identifier
    :type proxy_id: :class:`Int32`
    :param server: Proxy server domain or IP address
    :type server: :class:`String`
    :param port: Proxy server port
    :type port: :class:`Int32`
    :param type_: Proxy type
    :type type_: :class:`ProxyType`
    :param enable: Pass true to immediately enable the proxy
    :type enable: :class:`Bool`
    """

    ID: typing.Literal["editProxy"] = field(default="editProxy", metadata={"alias": "@type"})
    proxy_id: Int32
    server: String
    port: Int32
    type_: ProxyType = field(default=MISSING, metadata={"alias": "type"})
    enable: Bool = field(default=False)
