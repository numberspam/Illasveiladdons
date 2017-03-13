import discord
from discord.ext import commands
import asyncio
from sys import argv

class Bogdabot:
    """
    Bog commands
    """
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))

    async def _meme(self, ctx, msg):
        author = ctx.message.author
        await self.bot.delete_message(ctx.message)
        await self.bot.say(msg)

    # list memes
    @commands.command(name="listbogs", pass_context=True)
    async def _listbogs(self, ctx):
        """List meme commands."""
        # this feels wrong...
        funcs = dir(self)
        msg = "```\n"
        msg += ", ".join(func for func in funcs if func != "bot" and func[0] != "_")
        msg += "```"
        await self._meme(ctx, msg)
        await self.bot.delete_message(ctx.message)

    # memes
    @commands.command(pass_context=True, hidden=True)
    async def bogpic(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/YHWhnNT.png")

    @commands.command(pass_context=True, hidden=True)
    async def bogbros(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/nD5z7VP.png")

    @commands.command(pass_context=True, hidden=True)
    async def oldschoolbog(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/liayIwn.png")

    @commands.command(pass_context=True, hidden=True)
    async def handsomebog(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/sK71cm4.png")

    @commands.command(pass_context=True, hidden=True)
    async def sciencebog(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/cEI2xBq.png")

    @commands.command(pass_context=True, hidden=True)
    async def happybog(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/KsuIDlC.png")

    @commands.command(pass_context=True, hidden=True)
    async def clonebog(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/8aZRYBq.png")

    @commands.command(pass_context=True, hidden=True)
    async def memebog(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/0OOnAGF.png")

    @commands.command(pass_context=True, hidden=True)
    async def thecall(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/UL7Ub4K.png")

    @commands.command(pass_context=True, hidden=True)
    async def thecall2(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/k6Hg2vN.png")

    @commands.command(pass_context=True, hidden=True)
    async def pepebog(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/p1ObJnw.png")

    @commands.command(pass_context=True, hidden=True)
    async def boghair(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/2R2F8BC.png")

    @commands.command(pass_context=True, hidden=True)
    async def ascension(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/MnfDZdu.png")

    @commands.command(pass_context=True, hidden=True)
    async def mosaic(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/BzczsWn.png")

    @commands.command(pass_context=True, hidden=True)
    async def nophone(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/DZKv3eN.png")

    @commands.command(pass_context=True, hidden=True)
    async def trippybog(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/9iZCkAB.png")

    @commands.command(pass_context=True, hidden=True)
    async def justrightbog(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/1xjOF3c.png")

    @commands.command(pass_context=True, hidden=True)
    async def laughingbog(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/Op9K40l.png")

    @commands.command(pass_context=True, hidden=True)
    async def trumpbog(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/IqI5Eo1.png")

    @commands.command(pass_context=True, hidden=True)
    async def incoming(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/NeqQfLf.png")

    @commands.command(pass_context=True, hidden=True)
    async def rundown(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/CUu0zjx.png")

# Load the extension
def setup(bot):
    bot.add_cog(Bogdabot(bot))
