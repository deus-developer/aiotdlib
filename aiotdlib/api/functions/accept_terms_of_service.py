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
class AcceptTermsOfService(BaseObject):
    """
    Accepts Telegram terms of services

    :param terms_of_service_id: Terms of service identifier
    :type terms_of_service_id: :class:`String`
    """

    ID: typing.Literal["acceptTermsOfService"] = field(default="acceptTermsOfService", metadata={"alias": "@type"})
    terms_of_service_id: String
