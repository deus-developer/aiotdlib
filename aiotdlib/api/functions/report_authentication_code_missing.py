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
class ReportAuthenticationCodeMissing(BaseObject):
    """
    Reports that authentication code wasn't delivered via SMS; for official mobile applications only. Works only when the current authorization state is authorizationStateWaitCode

    :param mobile_network_code: Current mobile network code
    :type mobile_network_code: :class:`String`
    """

    ID: typing.Literal["reportAuthenticationCodeMissing"] = field(
        default="reportAuthenticationCodeMissing", metadata={"alias": "@type"}
    )
    mobile_network_code: String
