# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    UserPrivacySetting,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class GetUserPrivacySettingRules(BaseObject):
    """
    Returns the current privacy settings

    :param setting: The privacy setting
    :type setting: :class:`UserPrivacySetting`
    """

    ID: typing.Literal["getUserPrivacySettingRules"] = field(
        default="getUserPrivacySettingRules", metadata={"alias": "@type"}
    )
    setting: UserPrivacySetting
