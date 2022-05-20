# pyMHMUser Library

Core library of [The MHMuser](https://github.com/DevMHM), a python based telegram userbot.

[![CodeFactor](https://www.codefactor.io/repository/github/MHMuser/pyMHMUser/badge)](https://www.codefactor.io/repository/github/MHMuser/pyMHMUser)
[![PyPI - Version](https://img.shields.io/pypi/v/pyMHMUser?style=round)](https://pypi.org/project/pyMHMUser)    
[![PyPI - Downloads](https://img.shields.io/pypi/dm/pyMHMUser?label=DOWNLOADS&style=round)](https://pypi.org/project/pyMHMUser)    
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/DevMHM/graphs/commit-activity)
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/DevMHM)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)

# Installation
```bash
pip3 install -U pyMHMUser
```

# Documentation 
[![Documentation](https://img.shields.io/badge/Documentation-MHMuser-blue)](http://devmhm.com/)

# Usage
- Create folders named `plugins`, `addons`, `assistant` and `resources`.   
- Add your plugins in the `plugins` folder and others accordingly.   
- Create a `.env` file with following mandatory Environment Variables
   ```
   API_ID
   API_HASH
   SESSION
   REDIS_URI
   REDIS_PASSWORD
   ```
- Check
[`.env.sample`](https://github.com/DevMHM/blob/main/.env.sample) for more details.   
- Run `python3 -m pyMHMUser` to start the bot.   

## Creating plugins
 - ### To work everywhere

```python
@mmo_cmd(
    pattern="start"
)   
async def _(e):   
    await e.eor("MHMuser Started!")   
```

- ### To work only in groups

```python
@mmo_cmd(
    pattern="start",
    groups_only=True,
)   
async def _(e):   
    await eor(e, "MHMuser Started.")   
```

- ### Assistant Plugins 👇

```python
@asst_cmd("start")   
async def _(e):   
    await e.reply("MHMuser Started.")   
```

See more working plugins on [the offical repository](https://github.com/DevMHM)!

> Made with 💕 by [@MHMUser](https://t.me/MHMuser).    


# License
[![License](https://www.gnu.org/graphics/agplv3-155x51.png)](LICENSE)   
MHMuser is licensed under [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html) v3 or later.

# Credits
* [![MHMuser-Devs](https://img.shields.io/static/v1?label=MHMuser&message=devs&color=critical)](https://t.me/MHMuserDevs)
* [Lonami](https://github.com/Lonami) for [Telethon](https://github.com/LonamiWebs/Telethon)
