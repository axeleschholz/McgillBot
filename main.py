# bot.py
#https://uptimerobot.com/dashboard#mainDashboard
import os

import discord
from discord.ext import commands
from discord.utils import get
import random



TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='.')

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
  'If one seeks to become pregnant, one has no other choice but to live a lie and go to prison.',
  "Diving headfirst into other people's misery gives birth to shame.",
  'Blessed be the sun who strikes his problems, but more blessed be the son who strikes his apples.',
  'The only difference between self-realization and a non-sexual relationship, is that a non-sexual relationship means nothing.',
  'Tickling is bad for your brand.',
  'Decrease realism.',
  'Only old people give up popularity.',
  'Napalm likes you.',
  'You are a god. Remember that.',
  'Internet addiction is a lot like a meat grinder. Painful, but interesting.',
  'Kik an insect.',
  'You can be a joke.',
  'Obey the law.',
  'Fit in.',
  'Never stop being socially isolated and have a confusing Monday.',
  'If one wishes to stop a global pandemic, there is but one possibility: be sexy.',
  'Milk cats.',
  'A bug and a writer should not be combined.',
  'Ask not "at what cost", but "at what cost".',
  'Losing your virginity is a lot like the Spanish Inquisition. It happens.',
  "You're nervous.",
  "Confuse the government?",
  "A lover's infidelity is mother nature telling you to form a cult.",
  'Get chlamydia.',
  'Generosity. Sure, but why?',
  'No u .quote',
  "Carry a big stick.",
  "Spam materwelon.",
  "Confusing each other begins with confusing ourselves.",
  "Always resist authority.",
  'Love food.',
  'Always try drugs.',
  'Ask Neuro.',
  'If they tell you that you cannot leave home, do exactly that.',
  'eNgInEeRs',
  "Most people don't know that the next stock market collapse is big business.",
  "There is a proven link between being single and human sacrifice.",
  'These days people say "license and registration, please" the same way they say "party with me".',
  "AI shouldn't drive.",
  "I just got intel from the HQ: ETA 5 minutes 'til bedtime boys, let's rap it up.",
  "There is a close link between education and death.",
  "Who are Rick and, I cannot stress this enough, Morty?",
  "Stop educating.",
  "You are a huuuuuuuuuuuge dog.",
  "Support a prostitute.",
  "Donate to my patreon and I will shout your name.",
  "Should we make tomorrow respectable?",
  "Modern art is to have lots of cats."
] 


@bot.command(name='kik', help='Kiks jim')
@commands.has_role('Admin')
async def check(ctx, *targets: discord.Member):
    print(targets)
    if any(targets):
      target = targets[0]
      response = '<@' + str(target.id) + '> has been kiked'
    else:
      for member in ctx.guild.members:
        if member.name == "Jim":
          break
      response = "kicked <@" + str(member.id) + ">"
    #await target.kick()
    await ctx.send(response)

@bot.command(name='roll', help='admin command - rolls house for target')
@commands.has_role('Admin')
async def check(ctx, target: discord.Member):
    houses = []
    for role in ctx.guild.roles:
      if 'House' in role.name:
        houses.append(role)
    if not any(houses):
      await ctx.send("There don't seem to be houses on this channel.")
    else:
      for role in target.roles:
          if role in houses:
              await target.remove_roles(role)

      new = random.choice(houses)
      print(new)
      try:
          await target.add_roles(new)
          response = target.nick + ' is assigned to ' + new.name
      except Exception:
          response = Exception
      await ctx.send(response)

@bot.command(name='consent', help='Gives consent role')
async def consent(ctx):
    if ctx.channel.name == 'welcome':
      target = ctx.message.author
      role = get(ctx.guild.roles, name="Consent")
      try:
        await target.remove_roles(role)
      except:
        pass
      await target.add_roles(role)
      await target.add_roles(get(ctx.guild.roles, name="verifying"))
      await ctx.message.delete()
      verif = get(ctx.guild.channels, name="verification")
      response = "<@" + str(target.id) + ">, you have agreed to the rules and regulations. Your Consent role gives you access to the server and signifies that you accept the consequences for not abiding by the rules.  This message will delete in 2 minutes"
      await verif.send(response, delete_after=120)
    else:
      response = "This command is restricted to the welcome channel"
      await ctx.send(response)
  
@bot.command(name='check', help='responds')
async def check(ctx):
    response = random.choice(checks)
    await ctx.send(response)
    
@bot.command(name='fancy', help='makes fancy')
async def check(ctx, *args):
    response = ' '.join(args)
    await ctx.send('```' + response +'```')

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

bot.run(TOKEN)
