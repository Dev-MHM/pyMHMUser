# MHMUser
# Copyright (C) 2021-2022 MHMUser
#
# This file is a part of < https://github.com/DevMHM/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/DevMHM/pyMHMUser/blob/main/LICENSE>.

from . import *


def main():
    import os
    import sys
    import time

    from .functions.helper import time_formatter, updater
    from .startup.funcs import (
        WasItRestart,
        autopilot,
        customize,
        plug,
        ready,
        startup_stuff,
    )
    from .startup.loader import load_other_plugins

    # Option to Auto Update On Restarts..
    if (
        udB.get_key("UPDATE_ON_RESTART")
        and os.path.exists(".git")
        and mmo_bot.run_in_loop(updater())
    ):
        os.system(
            "git pull -f -q && pip3 install --no-cache-dir -U -q -r requirements.txt"
        )

        os.execl(sys.executable, "python3", "-m", "pyMHMUser")

    startup_stuff()

    mmo_bot.me.phone = None
    mmo_bot.first_name = mmo_bot.me.first_name

    if not mmo_bot.me.bot:
        udB.set_key("OWNER_ID", mmo_bot.uid)

    LOGS.info("Initialising...")

    mmo_bot.run_in_loop(autopilot())

    pmbot = udB.get_key("PMBOT")
    manager = udB.get_key("MANAGER")
    addons = udB.get_key("ADDONS") or Var.ADDONS
    vcbot = udB.get_key("VCBOT") or Var.VCBOT

    if HOSTED_ON == "termux" and udB.get_key("EXCLUDE_OFFICIAL") is None:
        _plugins = "autocorrect autopic compressor forcesubscribe gdrive glitch instagram nsfwfilter nightmode pdftools writer youtube"
        udB.set_key("EXCLUDE_OFFICIAL", _plugins)

    load_other_plugins(addons=addons, pmbot=pmbot, manager=manager, vcbot=vcbot)

    suc_msg = """
            ----------------------------------------------------------------------
                MHMuser has been deployed! Visit @MHMUser for updates!!
            ----------------------------------------------------------------------
    """

    # for channel plugins
    plugin_channels = udB.get_key("PLUGIN_CHANNEL")

    # Customize MHMuser Assistant...
    mmo_bot.run_in_loop(customize())

    # Load Addons from Plugin Channels.
    if plugin_channels:
        mmo_bot.run_in_loop(plug(plugin_channels))

    # Send/Ignore Deploy Message..
    if not udB.get_key("LOG_OFF"):
        mmo_bot.run_in_loop(ready())

    # Edit Restarting Message (if It's restarting)
    mmo_bot.run_in_loop(WasItRestart(udB))

    try:
        cleanup_cache()
    except BaseException:
        pass

    LOGS.info(
        f"Took {time_formatter((time.time() - start_time)*1000)} to start •MHMuser•"
    )
    LOGS.info(suc_msg)


if __name__ == "__main__":
    main()

    asst.run()
