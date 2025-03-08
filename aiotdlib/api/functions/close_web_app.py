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
class CloseWebApp(BaseObject):
    """
    Informs TDLib that a previously opened Web App was closed

    :param web_app_launch_id: Identifier of Web App launch, received from openWebApp
    :type web_app_launch_id: :class:`Int64`
    """

    ID: typing.Literal["closeWebApp"] = field(default="closeWebApp", metadata={"alias": "@type"})
    web_app_launch_id: Int64
