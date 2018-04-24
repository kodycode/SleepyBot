from datetime import datetime, timedelta
from discord.ext import commands

bot = commands.Bot(command_prefix="~",
                   description="Sleepytime")


class SleepyTime:
    """Handle Sleepytime requests"""

    def __init__(self):
        """
        Runs bot
        """
        bot.run("Enter token here")

    @bot.event
    async def on_ready():
        print("SleepyBot online")

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
        await bot.say('Optimal times to sleep:\n'
                      '**{}** or **{}** or **{}** or **{}**'
                      ''.format(firstTime,
                                secondTime,
                                thirdTime,
                                fourthTime))


SleepyTime()
