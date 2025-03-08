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
    UserPrivacySettingRules,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetUserPrivacySettingRules(BaseObject):
    """
    Changes user privacy settings

    :param setting: The privacy setting
    :type setting: :class:`UserPrivacySetting`
    :param rules: The new privacy rules
    :type rules: :class:`UserPrivacySettingRules`
    """

    ID: typing.Literal["setUserPrivacySettingRules"] = field(
        default="setUserPrivacySettingRules", metadata={"alias": "@type"}
    )
    setting: UserPrivacySetting
    rules: UserPrivacySettingRules
