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
class GetBusinessConnection(BaseObject):
    """
    Returns information about a business connection by its identifier; for bots only

    :param connection_id: Identifier of the business connection to return
    :type connection_id: :class:`String`
    """

    ID: typing.Literal["getBusinessConnection"] = field(default="getBusinessConnection", metadata={"alias": "@type"})
    connection_id: String
