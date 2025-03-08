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
class RemoveProxy(BaseObject):
    """
    Removes a proxy server. Can be called before authorization

    :param proxy_id: Proxy identifier
    :type proxy_id: :class:`Int32`
    """

    ID: typing.Literal["removeProxy"] = field(default="removeProxy", metadata={"alias": "@type"})
    proxy_id: Int32
