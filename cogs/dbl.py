import dbl
import asyncio
import json


class DiscordBotsOrgAPI:
    """Handles interactions with the discordbots.org API"""

    def __init__(self, bot, dbl_token):
        self.bot = bot
        self.dblpy = dbl.Client(self.bot, dbl_token)
        self.bot.loop.create_task(self.update_stats())

    async def update_stats(self):
        """
        This function runs every 30 minutes to automatically
        update your server count
        """
        while True:
            try:
                await self.dblpy.post_server_count()
            except Exception as e:
                print('Failed to post server count\n{}: {}'
                      ''.format(type(e).__name__, e))
            await asyncio.sleep(1800)


def setup(bot):
    with open('config.json') as config:
        config_data = json.load(config)
    if "dbl_token" in config_data:
        bot.add_cog(DiscordBotsOrgAPI(bot), config_data["dbl_token"])
