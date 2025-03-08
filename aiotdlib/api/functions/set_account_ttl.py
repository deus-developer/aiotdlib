# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    AccountTtl,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetAccountTtl(BaseObject):
    """
    Changes the period of inactivity after which the account of the current user will automatically be deleted

    :param ttl: New account TTL
    :type ttl: :class:`AccountTtl`
    """

    ID: typing.Literal["setAccountTtl"] = field(default="setAccountTtl", metadata={"alias": "@type"})
    ttl: AccountTtl
