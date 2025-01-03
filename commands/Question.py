import discord
from discord.ext import commands
import openai
from gpt_api_key import GPT_API_KEY
class Question(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.api_key = GPT_API_KEY
        openai.api_key = self.api_key

    @commands.command(name="질문", aliases=['물어보기'], description="질문")
    async def question(self, ctx, *, question=None):
        if question is None:
            embed = discord.Embed(
                title="❗ 오류",
                description="!질문 [질문할 내용] <-- 이렇게 써",
                color=discord.Color.red()
            )
            await ctx.reply(embed=embed)
            return

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "다음 질문에 대해 간단히 답변해주세요."},
                    {"role": "user", "content": question}
                ]
            )
            
            answer = response.choices[0].message.content

            embed = discord.Embed(
                title="답변",
                description=answer,
                color=discord.Color.green()
            )
            embed.set_footer(text=f"질문: {question}")
            
        except Exception as e:
            embed = discord.Embed(
                title="❗ 오류",
                description="GPT API",
                color=discord.Color.red()
            )
            
        await ctx.reply(embed=embed)