# MHMUser
# Copyright (C) 2021-2022 MHMUser
#
# This file is a part of < https://github.com/DevMHM/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/DevMHM/pyMHMUser/blob/main/LICENSE>.

"""
Exceptions which can be raised by pyMHMUser Itself.
"""


class pyMHMUserError(Exception):
    ...


class TelethonMissingError(ImportError):
    ...


class DependencyMissingError(ImportError):
    ...


class RunningAsFunctionLibError(pyMHMUserError):
    ...
