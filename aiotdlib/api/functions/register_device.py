# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    DeviceToken,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class RegisterDevice(BaseObject):
    """
    Registers the currently used device for receiving push notifications. Returns a globally unique identifier of the push notification subscription

    :param device_token: Device token
    :type device_token: :class:`DeviceToken`
    :param other_user_ids: List of user identifiers of other users currently using the application
    :type other_user_ids: :class:`Vector[Int53]`
    """

    ID: typing.Literal["registerDevice"] = field(default="registerDevice", metadata={"alias": "@type"})
    device_token: DeviceToken
    other_user_ids: Vector[Int53]
