# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    BusinessFeature,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class GetBusinessFeatures(BaseObject):
    """
    Returns information about features, available to Business users

    :param source: Source of the request; pass null if the method is called from settings or some non-standard source, defaults to None
    :type source: :class:`BusinessFeature`, optional
    """

    ID: typing.Literal["getBusinessFeatures"] = field(default="getBusinessFeatures", metadata={"alias": "@type"})
    source: typing.Optional[BusinessFeature] = field(default=None)
