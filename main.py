# bot.py
import os

import discord
from discord.ext import commands
from discord.utils import get
import random

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#TOKEN = os.getenv('DISCORD_TOKEN')
#GUILD = os.getenv('DISCORD_GUILD')
GUILD = 'McGill Entering Class of 2020'
TOKEN = 'NzE4MjY3MDIxNTMxNTQ1NjMw.XtmYSg.EnHPtlDshRRJ3XgsC25fLh_4Ykg'
bot = commands.Bot(command_prefix='.')

codes = {}
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

consents = ["you're all set!",
            "you're good to go!",
            "have a good time!",
            "nicely done!"]

@bot.event
async def on_member_join(member):
    print(f"{member} has joined {member.guild.name}")
    if member.guild.name == GUILD:
      guild = get(bot.guilds, name=member.guild.name)
      info = get(guild.channels, name='information')
      log = get(guild.channels, name='verification-log')
      entry = "<@" + str(member.id) + "> has joined the server, welcome message has been sent."
      message = "Welcome <@" + str(member.id) + ">!\nYou should give our rules a read at <#" + str(info.id) + ">.\nBy verifying yourself, you agree to our rules set out in <#" + str(info.id) + "> and failure to abide by the rules may result in a warning or ban.\nFeel free to peruse the rest of the announcements and information or message an Administrator/Moderator if you need any help!"
      
      await member.send(message)
      nextmessage = "Please enter your mcgill email address in the following format to verify yourself: ```.email firstname.lastname@mail.mcgill.ca```"
      await member.send(nextmessage)
      await log.send(entry)


      
  
@bot.command(name='kik', help='Kiks jim')
async def check(ctx, *targets: discord.Member):
    print(targets)
    if any(targets):
      target = targets[0]
      response = '<@' + str(target.id) + '> has been kiked'
      #await target.kick()
    else:
      for member in ctx.guild.members:
        if member.name == "Jim":
          break
      response = "kicked <@" + str(member.id) + ">"
    
    await ctx.send(response)

@bot.command(name='roll', help='admin command - rolls house for target')
@commands.has_role('Moderator')
async def check(ctx, target: discord.Member):
    houses = []
    for role in ctx.guild.roles:
      if 'House ' in role.name:
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

@bot.command()
@commands.has_role('Moderator')
async def dm(ctx, user: discord.User, *, message=None):
  await user.send(message)

@bot.command()
async def newverify(ctx, *targets: discord.Member):
    if not any(targets):
      members = [ctx.message.author]
    else:
      members = []
      for target in targets:
        members.append(target)
    for member in members:
      guild = get(bot.guilds, name=member.guild.name)
      info = get(guild.channels, name='information')
      message = "Welcome <@" + str(member.id) + ">!\nYou should give our rules a read at <#" + str(info.id) + ">.\nBy verifying yourself, you agree to our rules set out in <#" + str(info.id) + "> and failure to abide by the rules may result in a warning or ban.\nFeel free to peruse the rest of the announcements and information or message an Administrator/Moderator if you need any help!"
      await member.send(message)
      nextmessage = "Please enter your mcgill email address in the following format to verify yourself: ```.email firstname.lastname@mail.mcgill.ca```"
      await member.send(nextmessage)
    
@bot.command(name='email', help='sends email verification code')
async def email(ctx, arg):
    user = ctx.message.author
    guild = get(bot.guilds, name=GUILD)
    log = get(guild.channels, name='verification-log')
    entries = []
    entries.append("<@" + str(user.id) + "> has submitted their email")
    if '@mail.mcgill.ca' in arg or arg == "axel.eschholz@gmail.com":
        def generate_code():
            global codes
            code = ''
            for i in range(4):
                num = random.randint(0,9)
                code += str(num)
            if code not in list(codes.keys()):
              codes[code] = [user, arg]
              return code
            else:
              return generate_code()
        
        def send_msg(sender, to, subject, body):
            msg = MIMEMultipart()
            msg['From'] = sender
            msg['To'] = to
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))
            s.send_message(msg)
            
        if __name__ == "__main__":
            s = smtplib.SMTP(host='smtp.gmail.com', port=587)
            s.starttls()
            s.login('martythemcgillbot@gmail.com', 'emailtime')
            code = generate_code()
            body = 'Your verification code is ' + code + '\nThis code is valid for 10 minutes. \n\nDO NOT REPLY TO THIS EMAIL'
            send_msg('martythemcgillbot@gmail.com', arg, 'Verification', body)

            s.quit()
        
        response = "An email has been sent to that address with a verification code. Please respond to this message with: ```.code (insert code here)``` to be verified, thanks!"
        entries.append("<@" + str(user.id) + "> has been sent a verification code of " + code + ".")
        
    else:
        response = "That is not a valid mcgill email address."
        entries.append("<@" + str(user.id) + ">'s email was not valid")

    await ctx.send(response)
    for each in entries:
      await log.send(each)
      
@bot.command()
async def code(ctx, arg):
    code = arg
    user = ctx.message.author
    guild = get(bot.guilds, name=GUILD)
    log = get(guild.channels, name='verification-log')
    entries = []
    entries.append("<@" + str(user.id) + "> has submitted the code: " + code + ".")
    if code in list(codes.keys()):
      if user == codes[code][0]:
        #get objects
        guild = get(bot.guilds, name=GUILD)
        target = get(guild.members, id=user.id)
        role = get(guild.roles, name="Certified Admitted")
        
        #name breakdown
        email = codes[code][1]
        name = email.split('@')[0].split('.')
        for part in name:
          new = ''
          for x,letter in enumerate(part):
            if x == 0:
              letter = letter.upper()
            new += letter
          part = new
        nickname = name[0] + ' ' + name[1]
        
        #finish
        await target.add_roles(role)
        message = "You're all set, thanks for verifying and please proceed to the main server. Enjoy!"
        entries.append("<@" + str(target.id) + "> has been verified.")
        codes.pop(code)
        place = get(guild.channels, name='general')
        await target.edit(nick=nickname)
        entries.append("<@" + str(target.id) + ">'s nickname has been changed to " + nickname + ".")
        welcome = "Welcome! <@" + str(target.id) + ">"
        await user.send(message)
        await place.send(welcome)
      else:
        message = "That's someone else's code, don't try to fool me!"
        entries.append("<@" + str(target.id) + "> tried to use someone else's code! Arrest them!")
        await user.send(message)
    else:
        message = "Invalid code, please try again or contact a moderator for help.\nIf you did not request the email in the last 10 minutes, please do so again."
        entries.append("<@" + str(target.id) + ">'s code was invalid.")
        await user.send(message)
    
    for each in entries:
      await log.send(each)
      
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
          
      await ctx.send("<@" + str(ctx.author.id) + "> " + response, delete_after=10)
     
    else:
      response = "This command is restricted to the verification channel"
      await ctx.send(response)

  else:
    if ctx.channel.name == 'verification':
      for guild in bot.guilds:
          if guild.name == GUILD:
              break

      target = ctx.message.author
      members = [member for member in guild.members]
      try:
          await ctx.message.delete()
      except:
          pass
      checkrole = get(guild.roles, name="Certified Admitted")
      role = get(ctx.guild.roles, name="Verified")
      if not role:
          role = get(ctx.guild.roles, id=725648846675247134)
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
      await ctx.send("<@" + str(ctx.author.id) + "> " + response, delete_after=10)
    else:
      response = "This command is restricted to the verification channel"
      await ctx.send(response)

bot.run(TOKEN)
