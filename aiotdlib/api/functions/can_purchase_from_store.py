# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    StorePaymentPurpose,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class CanPurchaseFromStore(BaseObject):
    """
    Checks whether an in-store purchase is possible. Must be called before any in-store purchase

    :param purpose: Transaction purpose
    :type purpose: :class:`StorePaymentPurpose`
    """

    ID: typing.Literal["canPurchaseFromStore"] = field(default="canPurchaseFromStore", metadata={"alias": "@type"})
    purpose: StorePaymentPurpose
