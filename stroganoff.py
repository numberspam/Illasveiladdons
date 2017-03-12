# Some code borrowed from Kurisu by 916253 & ihaveamac
# license: Apache License 2.0
# https://github.com/916253/Kurisu

import discord
from discord.ext import commands
import asyncio
from sys import argv

class Strog:
    """
    FIGHT THE BOG
    """
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))

    async def _strog(self, ctx, msg):
        author = ctx.message.author
        await self.bot.delete_message(ctx.message)
        await self.bot.say(msg)

    # list memes
    @commands.command(name="liststrog", pass_context=True)
    async def _liststrog(self, ctx):
        """List recipes."""
        # this feels wrong...
        funcs = dir(self)
        msg = "```\n"
        msg += ", ".join(func for func in funcs if func != "bot" and func[0] != "_")
        msg += "```"
        await self._strog(ctx, msg)

    # start list
    @commands.command(pass_context=True, hidden=True)
    async def strog1(self, ctx):
        """recipes."""
        await self._strog(ctx, "http://www.foodnetwork.com/recipes/paula-deen/beef-stroganoff-recipe")


    @commands.command(pass_context=True, hidden=True)
    async def strog2(self, ctx):
        """recipes."""
        await self._strog(ctx, "http://www.bettycrocker.com/recipes/classic-beef-stroganoff/c17a904f-a8f6-48ae-bedb-5b301a8ea317")
        
    @commands.command(pass_context=True, hidden=True)
    async def strog3(self, ctx):
        """recipes."""
        await self._strog(ctx, "http://allrecipes.com/recipe/25202/beef-stroganoff-iii/")
        
    @commands.command(pass_context=True, hidden=True)
    async def strog4(self, ctx):
        """recipes."""
        await self._strog(ctx, "http://www.simplyrecipes.com/recipes/beef_stroganoff/")
        
    @commands.command(pass_context=True, hidden=True)
    async def strog5(self, ctx):
        """recipes."""
        await self._strog(ctx, "http://www.food.com/recipe/best-beef-stroganoff-73922")


# Load the extension
def setup(bot):
    bot.add_cog(Strog(bot))
