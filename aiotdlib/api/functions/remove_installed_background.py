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
class RemoveInstalledBackground(BaseObject):
    """
    Removes background from the list of installed backgrounds

    :param background_id: The background identifier
    :type background_id: :class:`Int64`
    """

    ID: typing.Literal["removeInstalledBackground"] = field(
        default="removeInstalledBackground", metadata={"alias": "@type"}
    )
    background_id: Int64
