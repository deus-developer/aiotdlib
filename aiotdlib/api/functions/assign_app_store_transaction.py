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
class AssignAppStoreTransaction(BaseObject):
    """
    Informs server about a purchase through App Store. For official applications only

    :param receipt: App Store receipt
    :type receipt: :class:`Bytes`
    :param purpose: Transaction purpose
    :type purpose: :class:`StorePaymentPurpose`
    """

    ID: typing.Literal["assignAppStoreTransaction"] = field(
        default="assignAppStoreTransaction", metadata={"alias": "@type"}
    )
    receipt: Bytes
    purpose: StorePaymentPurpose
