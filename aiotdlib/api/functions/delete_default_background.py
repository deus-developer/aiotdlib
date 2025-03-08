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
class DeleteDefaultBackground(BaseObject):
    """
    Deletes default background for chats

    :param for_dark_theme: Pass true if the background is deleted for a dark theme
    :type for_dark_theme: :class:`Bool`
    """

    ID: typing.Literal["deleteDefaultBackground"] = field(
        default="deleteDefaultBackground", metadata={"alias": "@type"}
    )
    for_dark_theme: Bool = field(default=False)
