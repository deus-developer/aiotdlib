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
class RemoveAllFilesFromDownloads(BaseObject):
    """
    Removes all files from the file download list

    :param only_active: Pass true to remove only active downloads, including paused
    :type only_active: :class:`Bool`
    :param only_completed: Pass true to remove only completed downloads
    :type only_completed: :class:`Bool`
    :param delete_from_cache: Pass true to delete the file from the TDLib file cache
    :type delete_from_cache: :class:`Bool`
    """

    ID: typing.Literal["removeAllFilesFromDownloads"] = field(
        default="removeAllFilesFromDownloads", metadata={"alias": "@type"}
    )
    only_active: Bool = field(default=False)
    only_completed: Bool = field(default=False)
    delete_from_cache: Bool = field(default=False)
