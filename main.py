# bot.py
#https://uptimerobot.com/dashboard#mainDashboard
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from webserver import keep_alive
from discord.utils import get
import random


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')
checks = [
  'check check, roger that',
  "check 1 2, we're all good here",
  'checkirooskies!',
  'right away sir',
  'thanks for checking up on me',
  "actually I'm not feeling well... oh nevermind",
  'are you implying that I malfunction!!',
  'mate',
  "I'm just a robot, virtually standing in front of a human, asking them to love me",
  'checkin, get it, checkin... like chicken',
  'mate, checkmate'
]
quotes = [
  'History is lethal.',
  'If one seeks to become pregnant, one has no other choice but to live a lie and go to prison.'
  "Diving headfirst into other people's misery gives birth to shame.",
  'Blessed be the sun who strikes his problems, but more blessed be the son who strikes his apples.',
  'The only difference between self-realization and a non-sexual relationship, is that a non-sexual relationship means nothing.',
  'Tickling is bad for your brand.',
  'Decrease realism.',
  'Only old people give up popularity.',
  'Napalm likes you.'
]
@bot.command(name='check', help='responds')
async def check(ctx):
    response = random.choice(checks)
    await ctx.send(response)

@bot.command(name='quote', help='gives some wisdom')
async def quote(ctx):
    response = random.choice(quotes)
    await ctx.send(response)
  
@bot.command(name='verify', help='verifies that person is in server')
async def verify(ctx):
  if ctx.guild.name == "McGill CS (first-year)":
    if ctx.channel.name == "verification":
      guild = get(bot.guilds, name=GUILD)
      members = [member for member in guild.members]
      target = ctx.message.author
      
      await ctx.message.delete()
      checkrole = get(guild.roles, name="Certified Admitted")
      role = get(ctx.guild.roles, name="Verified")
      if role in target.roles:
        response = "You're already verified, thanks for checking!"
      elif target in members:
          checked = False
          member = members[members.index(target)]
          print(member.roles)
          for otherrole in member.roles:
              if otherrole == checkrole:
                  checked = True
          if checked:
              response = "You're verified, have a lovely day"
              await target.remove_roles(get(ctx.guild.roles, name="verifying"))
              await target.add_roles(role)
              welcome = "Welcome <@" + str(target.id) + ">!"
              general = get(ctx.guild.channels, name="general")
              await general.send(welcome)
          else:
              response = "You're on the McGill server but not verified, go go go!"
      else:
          response = 'You are not verified, to become verified, logon to the mcgill 2020 server'
      await ctx.send(response, delete_after=10)
    else:
      response = "This command is restricted to the verification channel"
      await ctx.send(response)

  else:
    for guild in bot.guilds:
        if guild.name == GUILD:
            break
    
    target = ctx.message.author
    members = [member for member in guild.members]
    
    checkrole = get(guild.roles, name="Certified Admitted")
    role = get(ctx.guild.roles, name="Verified")
    if role in target.roles:
      response = "You're already verified, thanks for checking!"
    elif target in members:
        checked = False
        member = members[members.index(target)]
        for otherrole in member.roles:
            if otherrole == checkrole:
                checked = True
        if checked:
            response = "You're verified, have a lovely day"
            await target.add_roles(role)
        else:
            response = "You're on the McGill server but not verified, go go go!"
    else:
        response = 'You are not verified, to become verified, logon to the mcgill 2020 server'
    await ctx.send(response)

keep_alive()
bot.run(TOKEN)
