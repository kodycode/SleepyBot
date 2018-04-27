from datetime import datetime, timedelta
from discord.ext import commands
import json
import requests

DISCORD_BOT_URL = "https://discordbots.org/bot/438208284239855636/stats"
DBL = "cogs.dbl"
with open('config.json') as config:
    config_data = json.load(config)
bot = commands.Bot(command_prefix="~",
                   description="Sleepytime")


class SleepyTime:
    """Handle Sleepytime requests"""

    def __init__(self):
        """
        Runs bot
        """
        bot.run(config_data["bot_token"])

    @bot.event
    async def on_ready():
        try:
            if "dbl_token" in config_data:
                bot.load_extension(DBL)
            print("SleepyBot online")
        except Exception as e:
            error_msg = ('Failed to load cog manager\n{}: {}'
                         '').format(type(e).__name__, e)
            print(error_msg)

    @bot.command(name="sleep")
    async def sleepy_cmd(time, meridiem):
        """
        Calculates optimal times to sleep at
        An example of this command would be:
        "~sleep 8:30 AM"

        @param time - time to wake up at (i.e. 8:30)
        @param meridiem - AM or PM
        """
        timeInput = "{} {}".format(time, meridiem)
        timeToWake = ""
        try:
            timeToWake = datetime.strptime(timeInput, '%H:%M %p')
            if 'pm' in timeInput.lower():
                timeToWake = timeToWake + timedelta(hours=12)
        except:
            await bot.say('Error, please input a bedtime in the proper format '
                          '(ex: 10:00 AM)')
            return
        firstTime = timeToWake - timedelta(hours=9, minutes=0)
        secondTime = timeToWake - timedelta(hours=7.5, minutes=0)
        thirdTime = timeToWake - timedelta(hours=6, minutes=0)
        fourthTime = timeToWake - timedelta(hours=4.5, minutes=0)
        firstTime = datetime.strftime(firstTime, '%I:%M %p')
        secondTime = datetime.strftime(secondTime, '%I:%M %p')
        thirdTime = datetime.strftime(thirdTime, '%I:%M %p')
        fourthTime = datetime.strftime(fourthTime, '%I:%M %p')
        await bot.say('Optimal times to **fall asleep** to wake up at ({}):\n'
                      '**{}** or **{}** or **{}** or **{}**'
                      ''.format(timeInput,
                                firstTime,
                                secondTime,
                                thirdTime,
                                fourthTime))


def update_server_count(server_count):
    try:
        header = {'Authorization': '{}'.format(config_data["auth_token"])}
        payload = {'server_count': server_count}
        requests.post(DISCORD_BOT_URL,
                      headers=header,
                      data=payload)
    except:
        pass


SleepyTime()
