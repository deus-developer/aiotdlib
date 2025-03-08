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
class GetLocalizationTargetInfo(BaseObject):
    """
    Returns information about the current localization target. This is an offline request if only_local is true. Can be called before authorization

    :param only_local: Pass true to get only locally available information without sending network requests
    :type only_local: :class:`Bool`
    """

    ID: typing.Literal["getLocalizationTargetInfo"] = field(
        default="getLocalizationTargetInfo", metadata={"alias": "@type"}
    )
    only_local: Bool = field(default=False)
