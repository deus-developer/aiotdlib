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
class DisconnectWebsite(BaseObject):
    """
    Disconnects website from the current user's Telegram account

    :param website_id: Website identifier
    :type website_id: :class:`Int64`
    """

    ID: typing.Literal["disconnectWebsite"] = field(default="disconnectWebsite", metadata={"alias": "@type"})
    website_id: Int64
