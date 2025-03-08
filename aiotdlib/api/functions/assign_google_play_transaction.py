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
class AssignGooglePlayTransaction(BaseObject):
    """
    Informs server about a purchase through Google Play. For official applications only

    :param package_name: Application package name
    :type package_name: :class:`String`
    :param store_product_id: Identifier of the purchased store product
    :type store_product_id: :class:`String`
    :param purchase_token: Google Play purchase token
    :type purchase_token: :class:`String`
    :param purpose: Transaction purpose
    :type purpose: :class:`StorePaymentPurpose`
    """

    ID: typing.Literal["assignGooglePlayTransaction"] = field(
        default="assignGooglePlayTransaction", metadata={"alias": "@type"}
    )
    package_name: String
    store_product_id: String
    purchase_token: String
    purpose: StorePaymentPurpose
