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
class GetPhoneNumberInfo(BaseObject):
    """
    Returns information about a phone number by its prefix. Can be called before authorization

    :param phone_number_prefix: The phone number prefix
    :type phone_number_prefix: :class:`String`
    """

    ID: typing.Literal["getPhoneNumberInfo"] = field(default="getPhoneNumberInfo", metadata={"alias": "@type"})
    phone_number_prefix: String
