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
class CheckWebAppFileDownload(BaseObject):
    """
    Checks whether a file can be downloaded and saved locally by Web App request

    :param bot_user_id: Identifier of the bot, providing the Web App
    :type bot_user_id: :class:`Int53`
    :param file_name: Name of the file
    :type file_name: :class:`String`
    :param url: URL of the file
    :type url: :class:`String`
    """

    ID: typing.Literal["checkWebAppFileDownload"] = field(
        default="checkWebAppFileDownload", metadata={"alias": "@type"}
    )
    bot_user_id: Int53
    file_name: String
    url: String
