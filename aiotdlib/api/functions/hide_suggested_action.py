# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    SuggestedAction,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class HideSuggestedAction(BaseObject):
    """
    Hides a suggested action

    :param action: Suggested action to hide
    :type action: :class:`SuggestedAction`
    """

    ID: typing.Literal["hideSuggestedAction"] = field(default="hideSuggestedAction", metadata={"alias": "@type"})
    action: SuggestedAction
