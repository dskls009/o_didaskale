# bot.py
import os
import json
import discord
import asyncio
from discord.ext import commands
from dotenv import load_dotenv
from models import Word, db, NominalNumber
from sqlalchemy import or_

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
  db.create_all()
  print("Ready!")

async def oops(ctx):
    await ctx.send(
        "Oops, I think I rushed things a bit. Would you mind starting over? Sorry!")

@bot.command(name='add_data')
async def add_data(ctx):
  await ctx.send("Hello! I'll help you adding words to the bot database.")
  await ctx.send("Input the meaning of the word you want to add.")
  try:
      meaning = await bot.wait_for("message", check=lambda x: x.author.id == ctx.author.id, timeout=90)
      if meaning.author.bot:
          return oops(ctx)
      palavra = Word(meaning=meaning.content)
      print(meaning.content)
      await asyncio.sleep(1)

      await ctx.send("Now input the declension paradigm. (If you're not certain, put only the number or a dot)")
      paradigm = await bot.wait_for("message", check=lambda x: x.author.id == ctx.author.id, timeout=90)
      if paradigm.author.bot:
          return oops(ctx)
      palavra.paradigm = paradigm.content
      print(paradigm.content)
      await asyncio.sleep(1)

      await ctx.send("Now let's decline the word, starting with nominative singular:")
      nom_s = await bot.wait_for("message", check=lambda x: x.author.id == ctx.author.id, timeout=90)
      if nom_s.author.bot:
          return oops(ctx)
      palavra.singular = NominalNumber(nominative=nom_s.content)
      print(nom_s.content)
      await asyncio.sleep(1)

      await ctx.send("Accusative singular:")
      acc_s = await bot.wait_for("message", check=lambda x: x.author.id == ctx.author.id, timeout=90)
      if acc_s.author.bot:
          return oops(ctx)
      palavra.singular.accusative = acc_s.content
      print(acc_s.content)
      await asyncio.sleep(1)

      await ctx.send("Genitive singular:")
      gen_s = await bot.wait_for("message", check=lambda x: x.author.id == ctx.author.id, timeout=90)
      if gen_s.author.bot:
          return oops(ctx)
      palavra.singular.genitive = gen_s.content
      print(gen_s.content)
      await asyncio.sleep(1)

      await ctx.send("Dative singular:")
      dat_s = await bot.wait_for("message", check=lambda x: x.author.id == ctx.author.id, timeout=90)
      if dat_s.author.bot:
          return oops(ctx)
      palavra.singular.dative = dat_s.content
      print(dat_s.content)
      await asyncio.sleep(1)

      await ctx.send("Finally, vocative singular:")
      voc_s = await bot.wait_for("message", check=lambda x: x.author.id == ctx.author.id, timeout=90)
      if voc_s.author.bot:
          return oops(ctx)
      palavra.singular.vocative = voc_s.content
      print(voc_s.content)
      await asyncio.sleep(1)

      await ctx.send("Great! Now, do you know the dual form of this word? Answer with Y or N.")
      y_n = await bot.wait_for("message", check=lambda x: x.author.id == ctx.author.id, timeout=90)
      if y_n.content.lower() == 'y':
          await ctx.send("Incredible! Then, give me the nominative dual:")
          nom_d = await bot.wait_for("message", check=lambda x: x.author.id == ctx.author.id, timeout=90)
          if nom_d.author.bot:
              return oops(ctx)
          palavra.dual = NominalNumber(nominative=nom_d.content)
          print(nom_d.content)
          await asyncio.sleep(1)

          await ctx.send("Accusative dual:")
          acc_d = await bot.wait_for("message", check=lambda x: x.author.id == ctx.author.id, timeout=90)
          if acc_d.author.bot:
              return oops(ctx)
          palavra.dual.accusative = acc_d.content
          print(acc_d.content)
          await asyncio.sleep(1)

          await ctx.send("Genitive dual:")
          gen_d = await bot.wait_for("message", check=lambda x: x.author.id == ctx.author.id, timeout=90)
          if gen_d.author.bot:
              return oops(ctx)
          palavra.dual.genitive = gen_d.content
          print(gen_d.content)
          await asyncio.sleep(1)

          await ctx.send("Dative dual:")
          dat_d = await bot.wait_for("message", check=lambda x: x.author.id == ctx.author.id, timeout=90)
          if dat_d.author.bot:
              return oops(ctx)
          palavra.dual.dative = dat_d.content
          print(dat_d.content)
          await asyncio.sleep(1)

          await ctx.send("Finally, vocative dual:")
          voc_d = await bot.wait_for("message", check=lambda x: x.author.id == ctx.author.id, timeout=90)
          if voc_d.author.bot:
              return oops(ctx)
          palavra.dual.vocative = voc_d.content
          print(voc_d.content)
          await asyncio.sleep(1)

          await ctx.send("Wonderful! Now let's do the plural form, starting with nominative:")
      elif y_n.content.lower() == 'n':
          await ctx.send("Don't worry, I don't know many dual forms too.")
          await ctx.send("Does this word have a plural form? Answer with Y or N.")
          y_n = await bot.wait_for("message", check=lambda x: x.author.id == ctx.author.id, timeout=90)
          if y_n.content.lower() == 'n':
              await ctx.send("Okay! We're done here, then.")
              await ctx.send("To look up this word's paradigm try the command '.search <meaning>' or '.search <nominative singular>' or '.search <paradigm>' and I should tell how to decline it.")
              db.session.add(palavra)
              db.session.commit()
              return
          elif y_n.content.lower():
              await ctx.send("Let's do the nominative plural:")
      else:
          await ctx.send("What? Unfortunately you'll have to start over again. I don't understand.")
          return
      nom_p = await bot.wait_for("message", check=lambda x: x.author.id == ctx.author.id, timeout=90)
      if nom_p.author.bot:
          return oops(ctx)
      palavra.plural = NominalNumber(nominative=nom_p.content)
      print(nom_p.content)
      await asyncio.sleep(1)

      await ctx.send("Accusative plural:")
      acc_p = await bot.wait_for("message", check=lambda x: x.author.id == ctx.author.id, timeout=90)
      if acc_p.author.bot:
          return oops(ctx)
      palavra.plural.accusative = acc_p.content
      print(acc_p.content)
      await asyncio.sleep(1)

      await ctx.send("Genitive plural:")
      gen_p = await bot.wait_for("message", check=lambda x: x.author.id == ctx.author.id, timeout=90)
      if gen_p.author.bot:
          return oops(ctx)
      palavra.plural.genitive = gen_p.content
      print(gen_p.content)
      await asyncio.sleep(1)

      await ctx.send("Dative plural:")
      dat_p = await bot.wait_for("message", check=lambda x: x.author.id == ctx.author.id, timeout=90)
      if dat_p.author.bot:
          return oops(ctx)
      palavra.plural.dative = dat_p.content
      print(dat_p.content)
      await asyncio.sleep(1)

      await ctx.send("Finally, vocative plural:")
      voc_p = await bot.wait_for("message", check=lambda x: x.author.id == ctx.author.id, timeout=90)
      if voc_p.author.bot:
          return oops(ctx)
      palavra.plural.vocative = voc_p.content
      print(voc_p.content)
      await asyncio.sleep(1)

      await ctx.send("Good! Now I know one more word. Thanks for that!")
      await ctx.send("To look up this word's paradigm try the command '.search <meaning>' or '.search <nominative singular>' or '.search <paradigm>' and I should tell how to decline it.")
      db.session.add(palavra)
      db.session.commit()
      return
  except asyncio.TimeoutError:
      await ctx.send("Sorry, you didn't reply in time!")
      return

def declinator(word_json, description):

  singular = word_json["singular"]
  plural = word_json["plural"]

  singular_nominative = singular["nominative"]
  singular_genitive = singular["genitive"]
  singular_dative = singular["dative"]
  singular_accusative = singular["accusative"]
  singular_vocative = singular["vocative"]

  plural_nominative = plural["nominative"]
  plural_genitive = plural["genitive"]
  plural_dative = plural["dative"]
  plural_accusative = plural["accusative"]
  plural_vocative = plural["vocative"]

  em = discord.Embed(title = description, color = discord.Color.blue())
  em.add_field(name = "Singular", value = f"Nominative: {singular_nominative} \n Genitive: {singular_genitive} \n Dative: {singular_dative} \n Accusative: {singular_accusative} \n Vocative: {singular_vocative}")
  em.add_field(name = "Plural", value = f"Nominative: {plural_nominative} \n Genitive: {plural_genitive} \n Dative: {plural_dative} \n Accusative: {plural_accusative} \n Vocative: {plural_vocative}")
  return em

def conjugator_present(verb_json, description):
  if (verb_json):
    tense = verb_json["present"]

    indicative = tense["indicative"]
    imperative = tense["imperative"]
    optative = tense["optative"]
    subjunctive = tense["subjunctive"]

    indicative_active = indicative["active"]
    indicative_middle = indicative["middle"]
    indicative_passive = indicative["passive"]

    imperative_active = imperative["active"]
    imperative_middle = imperative["middle"]
    imperative_passive = imperative["passive"]

    optative_active = optative["active"]
    optative_middle = optative["middle"]
    optative_passive = optative["passive"]

    subjunctive_active = subjunctive["active"]
    subjunctive_middle = subjunctive["middle"]
    subjunctive_passive = subjunctive["passive"]

    indicative_active_singular = indicative_active["singular"]
    indicative_active_plural = indicative_active["plural"]
    indicative_middle_singular = indicative_middle["singular"]
    indicative_middle_plural = indicative_middle["plural"]
    indicative_passive_singular = indicative_passive["singular"]
    indicative_passive_plural = indicative_passive["plural"]

    indicative_active_singular_first = indicative_active_singular["first"]
    indicative_active_singular_second = indicative_active_singular["second"]
    indicative_active_singular_third = indicative_active_singular["third"]
    indicative_active_plural_first = indicative_active_plural["first"]
    indicative_active_plural_second = indicative_active_plural["second"]
    indicative_active_plural_third = indicative_active_plural["third"]

    indicative_middle_singular_first = indicative_middle_singular["first"]
    indicative_middle_singular_second = indicative_middle_singular["second"]
    indicative_middle_singular_third = indicative_middle_singular["third"]
    indicative_middle_plural_first = indicative_middle_plural["first"]
    indicative_middle_plural_second = indicative_middle_plural["second"]
    indicative_middle_plural_third = indicative_middle_plural["third"]

    indicative_passive_singular_first = indicative_passive_singular["first"]
    indicative_passive_singular_second = indicative_passive_singular["second"]
    indicative_passive_singular_third = indicative_passive_singular["third"]
    indicative_passive_plural_first = indicative_passive_plural["first"]
    indicative_passive_plural_second = indicative_passive_plural["second"]
    indicative_passive_plural_third = indicative_passive_plural["third"]

    imperative_active_singular = imperative_active["singular"]
    imperative_active_plural = imperative_active["plural"]
    imperative_middle_singular = imperative_middle["singular"]
    imperative_middle_plural = imperative_middle["plural"]
    imperative_passive_singular = imperative_passive["singular"]
    imperative_passive_plural = imperative_passive["plural"]

    imperative_active_singular_first = imperative_active_singular["first"]
    imperative_active_singular_second = imperative_active_singular["second"]
    imperative_active_singular_third = imperative_active_singular["third"]
    imperative_active_plural_first = imperative_active_plural["first"]
    imperative_active_plural_second = imperative_active_plural["second"]
    imperative_active_plural_third = imperative_active_plural["third"]

    imperative_middle_singular_first = imperative_middle_singular["first"]
    imperative_middle_singular_second = imperative_middle_singular["second"]
    imperative_middle_singular_third = imperative_middle_singular["third"]
    imperative_middle_plural_first = imperative_middle_plural["first"]
    imperative_middle_plural_second = imperative_middle_plural["second"]
    imperative_middle_plural_third = imperative_middle_plural["third"]

    imperative_passive_singular_first = imperative_passive_singular["first"]
    imperative_passive_singular_second = imperative_passive_singular["second"]
    imperative_passive_singular_third = imperative_passive_singular["third"]
    imperative_passive_plural_first = imperative_passive_plural["first"]
    imperative_passive_plural_second = imperative_passive_plural["second"]
    imperative_passive_plural_third = imperative_passive_plural["third"]

    optative_active_singular = optative_active["singular"]
    optative_active_plural = optative_active["plural"]
    optative_middle_singular = optative_middle["singular"]
    optative_middle_plural = optative_middle["plural"]
    optative_passive_singular = optative_passive["singular"]
    optative_passive_plural = optative_passive["plural"]

    optative_active_singular_first = optative_active_singular["first"]
    optative_active_singular_second = optative_active_singular["second"]
    optative_active_singular_third = optative_active_singular["third"]
    optative_active_plural_first = optative_active_plural["first"]
    optative_active_plural_second = optative_active_plural["second"]
    optative_active_plural_third = optative_active_plural["third"]

    optative_middle_singular_first = optative_middle_singular["first"]
    optative_middle_singular_second = optative_middle_singular["second"]
    optative_middle_singular_third = optative_middle_singular["third"]
    optative_middle_plural_first = optative_middle_plural["first"]
    optative_middle_plural_second = optative_middle_plural["second"]
    optative_middle_plural_third = optative_middle_plural["third"]

    optative_passive_singular_first = optative_passive_singular["first"]
    optative_passive_singular_second = optative_passive_singular["second"]
    optative_passive_singular_third = optative_passive_singular["third"]
    optative_passive_plural_first = optative_passive_plural["first"]
    optative_passive_plural_second = optative_passive_plural["second"]
    optative_passive_plural_third = optative_passive_plural["third"]

    subjunctive_active_singular = subjunctive_active["singular"]
    subjunctive_active_plural = subjunctive_active["plural"]
    subjunctive_middle_singular = subjunctive_middle["singular"]
    subjunctive_middle_plural = subjunctive_middle["plural"]
    subjunctive_passive_singular = subjunctive_passive["singular"]
    subjunctive_passive_plural = subjunctive_passive["plural"]

    subjunctive_active_singular_first = subjunctive_active_singular["first"]
    subjunctive_active_singular_second = subjunctive_active_singular["second"]
    subjunctive_active_singular_third = subjunctive_active_singular["third"]
    subjunctive_active_plural_first = subjunctive_active_plural["first"]
    subjunctive_active_plural_second = subjunctive_active_plural["second"]
    subjunctive_active_plural_third = subjunctive_active_plural["third"]

    subjunctive_middle_singular_first = subjunctive_middle_singular["first"]
    subjunctive_middle_singular_second = subjunctive_middle_singular["second"]
    subjunctive_middle_singular_third = subjunctive_middle_singular["third"]
    subjunctive_middle_plural_first = subjunctive_middle_plural["first"]
    subjunctive_middle_plural_second = subjunctive_middle_plural["second"]
    subjunctive_middle_plural_third = subjunctive_middle_plural["third"]

    subjunctive_passive_singular_first = subjunctive_passive_singular["first"]
    subjunctive_passive_singular_second = subjunctive_passive_singular["second"]
    subjunctive_passive_singular_third = subjunctive_passive_singular["third"]
    subjunctive_passive_plural_first = subjunctive_passive_plural["first"]
    subjunctive_passive_plural_second = subjunctive_passive_plural["second"]
    subjunctive_passive_plural_third = subjunctive_passive_plural["third"]

    inf_active = tense["infinitive"]["active"]
    inf_middle = tense["infinitive"]["middle"]
    inf_passive = tense["infinitive"]["passive"]

    em = discord.Embed(title=description, color = discord.Color.blue())
    if (inf_active or inf_middle or inf_passive):
      em.add_field(name = "Present Infinitives", value =f"Active: {inf_active}\nMiddle: {inf_middle}\nPassive: {inf_passive}")
    if (indicative_active_singular_first or indicative_active_singular_second or indicative_active_singular_third or indicative_active_plural_first or indicative_active_plural_second or indicative_active_plural_third):
      em.add_field(name = "Present Indicative Active", value =f"1.s.: {indicative_active_singular_first}\n2.s.: {indicative_active_singular_second}\n3.s.: {indicative_active_singular_third}\n1.p.: {indicative_active_plural_first}\n2.p.: {indicative_active_plural_second}\n3.p.: {indicative_active_plural_third}")
    if (indicative_middle_singular_first or indicative_middle_singular_second or indicative_middle_singular_third or indicative_middle_plural_first or indicative_middle_plural_second or indicative_middle_plural_third):
      em.add_field(name = "Present Indicative Middle", value =f"1.s.: {indicative_middle_singular_first}\n2.s.: {indicative_middle_singular_second}\n3.s.: {indicative_middle_singular_third}\n1.p.: {indicative_middle_plural_first}\n2.p.: {indicative_middle_plural_second}\n3.p.: {indicative_middle_plural_third}")
    if (indicative_passive_singular_first or indicative_passive_singular_second or indicative_passive_singular_third or indicative_passive_plural_first or indicative_passive_plural_second or indicative_passive_plural_third):
      em.add_field(name = "Present Indicative Passive", value =f"1.s.: {indicative_passive_singular_first}\n2.s.: {indicative_passive_singular_second}\n3.s.: {indicative_passive_singular_third}\n1.p.: {indicative_passive_plural_first}\n2.p.: {indicative_passive_plural_second}\n3.p.: {indicative_passive_plural_third}")

    if (imperative_active_singular_first or imperative_active_singular_second or imperative_active_singular_third or imperative_active_plural_first or imperative_active_plural_second or imperative_active_plural_third):
      em.add_field(name = "Present Imperative Active", value =f"1.s.: {imperative_active_singular_first}\n2.s.: {imperative_active_singular_second}\n3.s.: {imperative_active_singular_third}\n1.p.: {imperative_active_plural_first}\n2.p.: {imperative_active_plural_second}\n3.p.: {imperative_active_plural_third}")
    if (imperative_middle_singular_first or imperative_middle_singular_second or imperative_middle_singular_third or imperative_middle_plural_first or imperative_middle_plural_second or imperative_middle_plural_third):
      em.add_field(name = "Present Imperative Middle", value =f"1.s.: {imperative_middle_singular_first}\n2.s.: {imperative_middle_singular_second}\n3.s.: {imperative_middle_singular_third}\n1.p.: {imperative_middle_plural_first}\n2.p.: {imperative_middle_plural_second}\n3.p.: {imperative_middle_plural_third}")
    if (imperative_passive_singular_first or imperative_passive_singular_second or imperative_passive_singular_third or imperative_passive_plural_first or imperative_passive_plural_second or imperative_passive_plural_third):
      em.add_field(name = "Present Imperative Passive", value =f"1.s.: {imperative_passive_singular_first}\n2.s.: {imperative_passive_singular_second}\n3.s.: {imperative_passive_singular_third}\n1.p.: {imperative_passive_plural_first}\n2.p.: {imperative_passive_plural_second}\n3.p.: {imperative_passive_plural_third}")

    if (optative_active_singular_first or optative_active_singular_second or optative_active_singular_third or optative_active_plural_first or optative_active_plural_second or optative_active_plural_third):
      em.add_field(name = "Present Optative Active", value =f"1.s.: {optative_active_singular_first}\n2.s.: {optative_active_singular_second}\n3.s.: {optative_active_singular_third}\n1.p.: {optative_active_plural_first}\n2.p.: {optative_active_plural_second}\n3.p.: {optative_active_plural_third}")
    if (optative_middle_singular_first or optative_middle_singular_second or optative_middle_singular_third or optative_middle_plural_first or optative_middle_plural_second or optative_middle_plural_third):
      em.add_field(name = "Present Optative Middle", value =f"1.s.: {optative_middle_singular_first}\n2.s.: {optative_middle_singular_second}\n3.s.: {optative_middle_singular_third}\n1.p.: {optative_middle_plural_first}\n2.p.: {optative_middle_plural_second}\n3.p.: {optative_middle_plural_third}")
    if (optative_passive_singular_first or optative_passive_singular_second or optative_passive_singular_third or optative_passive_plural_first or optative_passive_plural_second or optative_passive_plural_third):
      em.add_field(name = "Present Optative Passive", value =f"1.s.: {optative_passive_singular_first}\n2.s.: {optative_passive_singular_second}\n3.s.: {optative_passive_singular_third}\n1.p.: {optative_passive_plural_first}\n2.p.: {optative_passive_plural_second}\n3.p.: {optative_passive_plural_third}")

    if (subjunctive_active_singular_first or subjunctive_active_singular_second or subjunctive_active_singular_third or subjunctive_active_plural_first or subjunctive_active_plural_second or subjunctive_active_plural_third):
      em.add_field(name = "Present subjunctive Active", value =f"1.s.: {subjunctive_active_singular_first}\n2.s.: {subjunctive_active_singular_second}\n3.s.: {subjunctive_active_singular_third}\n1.p.: {subjunctive_active_plural_first}\n2.p.: {subjunctive_active_plural_second}\n3.p.: {subjunctive_active_plural_third}")
    if (subjunctive_middle_singular_first or subjunctive_middle_singular_second or subjunctive_middle_singular_third or subjunctive_middle_plural_first or subjunctive_middle_plural_second or subjunctive_middle_plural_third):
      em.add_field(name = "Present subjunctive Middle", value =f"1.s.: {subjunctive_middle_singular_first}\n2.s.: {subjunctive_middle_singular_second}\n3.s.: {subjunctive_middle_singular_third}\n1.p.: {subjunctive_middle_plural_first}\n2.p.: {subjunctive_middle_plural_second}\n3.p.: {subjunctive_middle_plural_third}")
    if (subjunctive_passive_singular_first or subjunctive_passive_singular_second or subjunctive_passive_singular_third or subjunctive_passive_plural_first or subjunctive_passive_plural_second or subjunctive_passive_plural_third):
      em.add_field(name = "Present subjunctive Passive", value =f"1.s.: {subjunctive_passive_singular_first}\n2.s.: {subjunctive_passive_singular_second}\n3.s.: {subjunctive_passive_singular_third}\n1.p.: {subjunctive_passive_plural_first}\n2.p.: {subjunctive_passive_plural_second}\n3.p.: {subjunctive_passive_plural_third}")

    return em
  return None

def conjugator_imperfect(verb_json, description):
  if (verb_json):
    tense = verb_json["imperfect"]

    indicative = tense["indicative"]
    imperative = tense["imperative"]
    optative = tense["optative"]
    subjunctive = tense["subjunctive"]

    indicative_active = indicative["active"]
    indicative_middle = indicative["middle"]
    indicative_passive = indicative["passive"]

    imperative_active = imperative["active"]
    imperative_middle = imperative["middle"]
    imperative_passive = imperative["passive"]

    optative_active = optative["active"]
    optative_middle = optative["middle"]
    optative_passive = optative["passive"]

    subjunctive_active = subjunctive["active"]
    subjunctive_middle = subjunctive["middle"]
    subjunctive_passive = subjunctive["passive"]

    indicative_active_singular = indicative_active["singular"]
    indicative_active_plural = indicative_active["plural"]
    indicative_middle_singular = indicative_middle["singular"]
    indicative_middle_plural = indicative_middle["plural"]
    indicative_passive_singular = indicative_passive["singular"]
    indicative_passive_plural = indicative_passive["plural"]

    indicative_active_singular_first = indicative_active_singular["first"]
    indicative_active_singular_second = indicative_active_singular["second"]
    indicative_active_singular_third = indicative_active_singular["third"]
    indicative_active_plural_first = indicative_active_plural["first"]
    indicative_active_plural_second = indicative_active_plural["second"]
    indicative_active_plural_third = indicative_active_plural["third"]

    indicative_middle_singular_first = indicative_middle_singular["first"]
    indicative_middle_singular_second = indicative_middle_singular["second"]
    indicative_middle_singular_third = indicative_middle_singular["third"]
    indicative_middle_plural_first = indicative_middle_plural["first"]
    indicative_middle_plural_second = indicative_middle_plural["second"]
    indicative_middle_plural_third = indicative_middle_plural["third"]

    indicative_passive_singular_first = indicative_passive_singular["first"]
    indicative_passive_singular_second = indicative_passive_singular["second"]
    indicative_passive_singular_third = indicative_passive_singular["third"]
    indicative_passive_plural_first = indicative_passive_plural["first"]
    indicative_passive_plural_second = indicative_passive_plural["second"]
    indicative_passive_plural_third = indicative_passive_plural["third"]

    imperative_active_singular = imperative_active["singular"]
    imperative_active_plural = imperative_active["plural"]
    imperative_middle_singular = imperative_middle["singular"]
    imperative_middle_plural = imperative_middle["plural"]
    imperative_passive_singular = imperative_passive["singular"]
    imperative_passive_plural = imperative_passive["plural"]

    imperative_active_singular_first = imperative_active_singular["first"]
    imperative_active_singular_second = imperative_active_singular["second"]
    imperative_active_singular_third = imperative_active_singular["third"]
    imperative_active_plural_first = imperative_active_plural["first"]
    imperative_active_plural_second = imperative_active_plural["second"]
    imperative_active_plural_third = imperative_active_plural["third"]

    imperative_middle_singular_first = imperative_middle_singular["first"]
    imperative_middle_singular_second = imperative_middle_singular["second"]
    imperative_middle_singular_third = imperative_middle_singular["third"]
    imperative_middle_plural_first = imperative_middle_plural["first"]
    imperative_middle_plural_second = imperative_middle_plural["second"]
    imperative_middle_plural_third = imperative_middle_plural["third"]

    imperative_passive_singular_first = imperative_passive_singular["first"]
    imperative_passive_singular_second = imperative_passive_singular["second"]
    imperative_passive_singular_third = imperative_passive_singular["third"]
    imperative_passive_plural_first = imperative_passive_plural["first"]
    imperative_passive_plural_second = imperative_passive_plural["second"]
    imperative_passive_plural_third = imperative_passive_plural["third"]

    optative_active_singular = optative_active["singular"]
    optative_active_plural = optative_active["plural"]
    optative_middle_singular = optative_middle["singular"]
    optative_middle_plural = optative_middle["plural"]
    optative_passive_singular = optative_passive["singular"]
    optative_passive_plural = optative_passive["plural"]

    optative_active_singular_first = optative_active_singular["first"]
    optative_active_singular_second = optative_active_singular["second"]
    optative_active_singular_third = optative_active_singular["third"]
    optative_active_plural_first = optative_active_plural["first"]
    optative_active_plural_second = optative_active_plural["second"]
    optative_active_plural_third = optative_active_plural["third"]

    optative_middle_singular_first = optative_middle_singular["first"]
    optative_middle_singular_second = optative_middle_singular["second"]
    optative_middle_singular_third = optative_middle_singular["third"]
    optative_middle_plural_first = optative_middle_plural["first"]
    optative_middle_plural_second = optative_middle_plural["second"]
    optative_middle_plural_third = optative_middle_plural["third"]

    optative_passive_singular_first = optative_passive_singular["first"]
    optative_passive_singular_second = optative_passive_singular["second"]
    optative_passive_singular_third = optative_passive_singular["third"]
    optative_passive_plural_first = optative_passive_plural["first"]
    optative_passive_plural_second = optative_passive_plural["second"]
    optative_passive_plural_third = optative_passive_plural["third"]

    subjunctive_active_singular = subjunctive_active["singular"]
    subjunctive_active_plural = subjunctive_active["plural"]
    subjunctive_middle_singular = subjunctive_middle["singular"]
    subjunctive_middle_plural = subjunctive_middle["plural"]
    subjunctive_passive_singular = subjunctive_passive["singular"]
    subjunctive_passive_plural = subjunctive_passive["plural"]

    subjunctive_active_singular_first = subjunctive_active_singular["first"]
    subjunctive_active_singular_second = subjunctive_active_singular["second"]
    subjunctive_active_singular_third = subjunctive_active_singular["third"]
    subjunctive_active_plural_first = subjunctive_active_plural["first"]
    subjunctive_active_plural_second = subjunctive_active_plural["second"]
    subjunctive_active_plural_third = subjunctive_active_plural["third"]

    subjunctive_middle_singular_first = subjunctive_middle_singular["first"]
    subjunctive_middle_singular_second = subjunctive_middle_singular["second"]
    subjunctive_middle_singular_third = subjunctive_middle_singular["third"]
    subjunctive_middle_plural_first = subjunctive_middle_plural["first"]
    subjunctive_middle_plural_second = subjunctive_middle_plural["second"]
    subjunctive_middle_plural_third = subjunctive_middle_plural["third"]

    subjunctive_passive_singular_first = subjunctive_passive_singular["first"]
    subjunctive_passive_singular_second = subjunctive_passive_singular["second"]
    subjunctive_passive_singular_third = subjunctive_passive_singular["third"]
    subjunctive_passive_plural_first = subjunctive_passive_plural["first"]
    subjunctive_passive_plural_second = subjunctive_passive_plural["second"]
    subjunctive_passive_plural_third = subjunctive_passive_plural["third"]

    inf_active = tense["infinitive"]["active"]
    inf_middle = tense["infinitive"]["middle"]
    inf_passive = tense["infinitive"]["passive"]

    em = discord.Embed(title=description, color = discord.Color.blue())
    if (inf_active or inf_middle or inf_passive):
      em.add_field(name = "Imperfect Infinitives", value =f"Active: {inf_active}\nMiddle: {inf_middle}\nPassive: {inf_passive}")
    if (indicative_active_singular_first or indicative_active_singular_second or indicative_active_singular_third or indicative_active_plural_first or indicative_active_plural_second or indicative_active_plural_third):
      em.add_field(name = "Imperfect Indicative Active", value =f"1.s.: {indicative_active_singular_first}\n2.s.: {indicative_active_singular_second}\n3.s.: {indicative_active_singular_third}\n1.p.: {indicative_active_plural_first}\n2.p.: {indicative_active_plural_second}\n3.p.: {indicative_active_plural_third}")
    if (indicative_middle_singular_first or indicative_middle_singular_second or indicative_middle_singular_third or indicative_middle_plural_first or indicative_middle_plural_second or indicative_middle_plural_third):
      em.add_field(name = "Imperfect Indicative Middle", value =f"1.s.: {indicative_middle_singular_first}\n2.s.: {indicative_middle_singular_second}\n3.s.: {indicative_middle_singular_third}\n1.p.: {indicative_middle_plural_first}\n2.p.: {indicative_middle_plural_second}\n3.p.: {indicative_middle_plural_third}")
    if (indicative_passive_singular_first or indicative_passive_singular_second or indicative_passive_singular_third or indicative_passive_plural_first or indicative_passive_plural_second or indicative_passive_plural_third):
      em.add_field(name = "Imperfect Indicative Passive", value =f"1.s.: {indicative_passive_singular_first}\n2.s.: {indicative_passive_singular_second}\n3.s.: {indicative_passive_singular_third}\n1.p.: {indicative_passive_plural_first}\n2.p.: {indicative_passive_plural_second}\n3.p.: {indicative_passive_plural_third}")

    if (imperative_active_singular_first or imperative_active_singular_second or imperative_active_singular_third or imperative_active_plural_first or imperative_active_plural_second or imperative_active_plural_third):
      em.add_field(name = "Imperfect Imperative Active", value =f"1.s.: {imperative_active_singular_first}\n2.s.: {imperative_active_singular_second}\n3.s.: {imperative_active_singular_third}\n1.p.: {imperative_active_plural_first}\n2.p.: {imperative_active_plural_second}\n3.p.: {imperative_active_plural_third}")
    if (imperative_middle_singular_first or imperative_middle_singular_second or imperative_middle_singular_third or imperative_middle_plural_first or imperative_middle_plural_second or imperative_middle_plural_third):
      em.add_field(name = "Imperfect Imperative Middle", value =f"1.s.: {imperative_middle_singular_first}\n2.s.: {imperative_middle_singular_second}\n3.s.: {imperative_middle_singular_third}\n1.p.: {imperative_middle_plural_first}\n2.p.: {imperative_middle_plural_second}\n3.p.: {imperative_middle_plural_third}")
    if (imperative_passive_singular_first or imperative_passive_singular_second or imperative_passive_singular_third or imperative_passive_plural_first or imperative_passive_plural_second or imperative_passive_plural_third):
      em.add_field(name = "Imperfect Imperative Passive", value =f"1.s.: {imperative_passive_singular_first}\n2.s.: {imperative_passive_singular_second}\n3.s.: {imperative_passive_singular_third}\n1.p.: {imperative_passive_plural_first}\n2.p.: {imperative_passive_plural_second}\n3.p.: {imperative_passive_plural_third}")

    if (optative_active_singular_first or optative_active_singular_second or optative_active_singular_third or optative_active_plural_first or optative_active_plural_second or optative_active_plural_third):
      em.add_field(name = "Imperfect Optative Active", value =f"1.s.: {optative_active_singular_first}\n2.s.: {optative_active_singular_second}\n3.s.: {optative_active_singular_third}\n1.p.: {optative_active_plural_first}\n2.p.: {optative_active_plural_second}\n3.p.: {optative_active_plural_third}")
    if (optative_middle_singular_first or optative_middle_singular_second or optative_middle_singular_third or optative_middle_plural_first or optative_middle_plural_second or optative_middle_plural_third):
      em.add_field(name = "Imperfect Optative Middle", value =f"1.s.: {optative_middle_singular_first}\n2.s.: {optative_middle_singular_second}\n3.s.: {optative_middle_singular_third}\n1.p.: {optative_middle_plural_first}\n2.p.: {optative_middle_plural_second}\n3.p.: {optative_middle_plural_third}")
    if (optative_passive_singular_first or optative_passive_singular_second or optative_passive_singular_third or optative_passive_plural_first or optative_passive_plural_second or optative_passive_plural_third):
      em.add_field(name = "Imperfect Optative Passive", value =f"1.s.: {optative_passive_singular_first}\n2.s.: {optative_passive_singular_second}\n3.s.: {optative_passive_singular_third}\n1.p.: {optative_passive_plural_first}\n2.p.: {optative_passive_plural_second}\n3.p.: {optative_passive_plural_third}")

    if (subjunctive_active_singular_first or subjunctive_active_singular_second or subjunctive_active_singular_third or subjunctive_active_plural_first or subjunctive_active_plural_second or subjunctive_active_plural_third):
      em.add_field(name = "Imperfect subjunctive Active", value =f"1.s.: {subjunctive_active_singular_first}\n2.s.: {subjunctive_active_singular_second}\n3.s.: {subjunctive_active_singular_third}\n1.p.: {subjunctive_active_plural_first}\n2.p.: {subjunctive_active_plural_second}\n3.p.: {subjunctive_active_plural_third}")
    if (subjunctive_middle_singular_first or subjunctive_middle_singular_second or subjunctive_middle_singular_third or subjunctive_middle_plural_first or subjunctive_middle_plural_second or subjunctive_middle_plural_third):
      em.add_field(name = "Imperfect subjunctive Middle", value =f"1.s.: {subjunctive_middle_singular_first}\n2.s.: {subjunctive_middle_singular_second}\n3.s.: {subjunctive_middle_singular_third}\n1.p.: {subjunctive_middle_plural_first}\n2.p.: {subjunctive_middle_plural_second}\n3.p.: {subjunctive_middle_plural_third}")
    if (subjunctive_passive_singular_first or subjunctive_passive_singular_second or subjunctive_passive_singular_third or subjunctive_passive_plural_first or subjunctive_passive_plural_second or subjunctive_passive_plural_third):
      em.add_field(name = "Imperfect subjunctive Passive", value =f"1.s.: {subjunctive_passive_singular_first}\n2.s.: {subjunctive_passive_singular_second}\n3.s.: {subjunctive_passive_singular_third}\n1.p.: {subjunctive_passive_plural_first}\n2.p.: {subjunctive_passive_plural_second}\n3.p.: {subjunctive_passive_plural_third}")

    return em
  return None

def conjugator_future(verb_json, description):
  if (verb_json):
    tense = verb_json["future"]

    indicative = tense["indicative"]
    imperative = tense["imperative"]
    optative = tense["optative"]
    subjunctive = tense["subjunctive"]

    indicative_active = indicative["active"]
    indicative_middle = indicative["middle"]
    indicative_passive = indicative["passive"]

    imperative_active = imperative["active"]
    imperative_middle = imperative["middle"]
    imperative_passive = imperative["passive"]

    optative_active = optative["active"]
    optative_middle = optative["middle"]
    optative_passive = optative["passive"]

    subjunctive_active = subjunctive["active"]
    subjunctive_middle = subjunctive["middle"]
    subjunctive_passive = subjunctive["passive"]

    indicative_active_singular = indicative_active["singular"]
    indicative_active_plural = indicative_active["plural"]
    indicative_middle_singular = indicative_middle["singular"]
    indicative_middle_plural = indicative_middle["plural"]
    indicative_passive_singular = indicative_passive["singular"]
    indicative_passive_plural = indicative_passive["plural"]

    indicative_active_singular_first = indicative_active_singular["first"]
    indicative_active_singular_second = indicative_active_singular["second"]
    indicative_active_singular_third = indicative_active_singular["third"]
    indicative_active_plural_first = indicative_active_plural["first"]
    indicative_active_plural_second = indicative_active_plural["second"]
    indicative_active_plural_third = indicative_active_plural["third"]

    indicative_middle_singular_first = indicative_middle_singular["first"]
    indicative_middle_singular_second = indicative_middle_singular["second"]
    indicative_middle_singular_third = indicative_middle_singular["third"]
    indicative_middle_plural_first = indicative_middle_plural["first"]
    indicative_middle_plural_second = indicative_middle_plural["second"]
    indicative_middle_plural_third = indicative_middle_plural["third"]

    indicative_passive_singular_first = indicative_passive_singular["first"]
    indicative_passive_singular_second = indicative_passive_singular["second"]
    indicative_passive_singular_third = indicative_passive_singular["third"]
    indicative_passive_plural_first = indicative_passive_plural["first"]
    indicative_passive_plural_second = indicative_passive_plural["second"]
    indicative_passive_plural_third = indicative_passive_plural["third"]

    imperative_active_singular = imperative_active["singular"]
    imperative_active_plural = imperative_active["plural"]
    imperative_middle_singular = imperative_middle["singular"]
    imperative_middle_plural = imperative_middle["plural"]
    imperative_passive_singular = imperative_passive["singular"]
    imperative_passive_plural = imperative_passive["plural"]

    imperative_active_singular_first = imperative_active_singular["first"]
    imperative_active_singular_second = imperative_active_singular["second"]
    imperative_active_singular_third = imperative_active_singular["third"]
    imperative_active_plural_first = imperative_active_plural["first"]
    imperative_active_plural_second = imperative_active_plural["second"]
    imperative_active_plural_third = imperative_active_plural["third"]

    imperative_middle_singular_first = imperative_middle_singular["first"]
    imperative_middle_singular_second = imperative_middle_singular["second"]
    imperative_middle_singular_third = imperative_middle_singular["third"]
    imperative_middle_plural_first = imperative_middle_plural["first"]
    imperative_middle_plural_second = imperative_middle_plural["second"]
    imperative_middle_plural_third = imperative_middle_plural["third"]

    imperative_passive_singular_first = imperative_passive_singular["first"]
    imperative_passive_singular_second = imperative_passive_singular["second"]
    imperative_passive_singular_third = imperative_passive_singular["third"]
    imperative_passive_plural_first = imperative_passive_plural["first"]
    imperative_passive_plural_second = imperative_passive_plural["second"]
    imperative_passive_plural_third = imperative_passive_plural["third"]

    optative_active_singular = optative_active["singular"]
    optative_active_plural = optative_active["plural"]
    optative_middle_singular = optative_middle["singular"]
    optative_middle_plural = optative_middle["plural"]
    optative_passive_singular = optative_passive["singular"]
    optative_passive_plural = optative_passive["plural"]

    optative_active_singular_first = optative_active_singular["first"]
    optative_active_singular_second = optative_active_singular["second"]
    optative_active_singular_third = optative_active_singular["third"]
    optative_active_plural_first = optative_active_plural["first"]
    optative_active_plural_second = optative_active_plural["second"]
    optative_active_plural_third = optative_active_plural["third"]

    optative_middle_singular_first = optative_middle_singular["first"]
    optative_middle_singular_second = optative_middle_singular["second"]
    optative_middle_singular_third = optative_middle_singular["third"]
    optative_middle_plural_first = optative_middle_plural["first"]
    optative_middle_plural_second = optative_middle_plural["second"]
    optative_middle_plural_third = optative_middle_plural["third"]

    optative_passive_singular_first = optative_passive_singular["first"]
    optative_passive_singular_second = optative_passive_singular["second"]
    optative_passive_singular_third = optative_passive_singular["third"]
    optative_passive_plural_first = optative_passive_plural["first"]
    optative_passive_plural_second = optative_passive_plural["second"]
    optative_passive_plural_third = optative_passive_plural["third"]

    subjunctive_active_singular = subjunctive_active["singular"]
    subjunctive_active_plural = subjunctive_active["plural"]
    subjunctive_middle_singular = subjunctive_middle["singular"]
    subjunctive_middle_plural = subjunctive_middle["plural"]
    subjunctive_passive_singular = subjunctive_passive["singular"]
    subjunctive_passive_plural = subjunctive_passive["plural"]

    subjunctive_active_singular_first = subjunctive_active_singular["first"]
    subjunctive_active_singular_second = subjunctive_active_singular["second"]
    subjunctive_active_singular_third = subjunctive_active_singular["third"]
    subjunctive_active_plural_first = subjunctive_active_plural["first"]
    subjunctive_active_plural_second = subjunctive_active_plural["second"]
    subjunctive_active_plural_third = subjunctive_active_plural["third"]

    subjunctive_middle_singular_first = subjunctive_middle_singular["first"]
    subjunctive_middle_singular_second = subjunctive_middle_singular["second"]
    subjunctive_middle_singular_third = subjunctive_middle_singular["third"]
    subjunctive_middle_plural_first = subjunctive_middle_plural["first"]
    subjunctive_middle_plural_second = subjunctive_middle_plural["second"]
    subjunctive_middle_plural_third = subjunctive_middle_plural["third"]

    subjunctive_passive_singular_first = subjunctive_passive_singular["first"]
    subjunctive_passive_singular_second = subjunctive_passive_singular["second"]
    subjunctive_passive_singular_third = subjunctive_passive_singular["third"]
    subjunctive_passive_plural_first = subjunctive_passive_plural["first"]
    subjunctive_passive_plural_second = subjunctive_passive_plural["second"]
    subjunctive_passive_plural_third = subjunctive_passive_plural["third"]

    inf_active = tense["infinitive"]["active"]
    inf_middle = tense["infinitive"]["middle"]
    inf_passive = tense["infinitive"]["passive"]

    em = discord.Embed(title=description, color = discord.Color.blue())
    if (inf_active or inf_middle or inf_passive):
      em.add_field(name = "Future Infinitives", value =f"Active: {inf_active}\nMiddle: {inf_middle}\nPassive: {inf_passive}")
    if (indicative_active_singular_first or indicative_active_singular_second or indicative_active_singular_third or indicative_active_plural_first or indicative_active_plural_second or indicative_active_plural_third):
      em.add_field(name = "Future Indicative Active", value =f"1.s.: {indicative_active_singular_first}\n2.s.: {indicative_active_singular_second}\n3.s.: {indicative_active_singular_third}\n1.p.: {indicative_active_plural_first}\n2.p.: {indicative_active_plural_second}\n3.p.: {indicative_active_plural_third}")
    if (indicative_middle_singular_first or indicative_middle_singular_second or indicative_middle_singular_third or indicative_middle_plural_first or indicative_middle_plural_second or indicative_middle_plural_third):
      em.add_field(name = "Future Indicative Middle", value =f"1.s.: {indicative_middle_singular_first}\n2.s.: {indicative_middle_singular_second}\n3.s.: {indicative_middle_singular_third}\n1.p.: {indicative_middle_plural_first}\n2.p.: {indicative_middle_plural_second}\n3.p.: {indicative_middle_plural_third}")
    if (indicative_passive_singular_first or indicative_passive_singular_second or indicative_passive_singular_third or indicative_passive_plural_first or indicative_passive_plural_second or indicative_passive_plural_third):
      em.add_field(name = "Future Indicative Passive", value =f"1.s.: {indicative_passive_singular_first}\n2.s.: {indicative_passive_singular_second}\n3.s.: {indicative_passive_singular_third}\n1.p.: {indicative_passive_plural_first}\n2.p.: {indicative_passive_plural_second}\n3.p.: {indicative_passive_plural_third}")

    if (imperative_active_singular_first or imperative_active_singular_second or imperative_active_singular_third or imperative_active_plural_first or imperative_active_plural_second or imperative_active_plural_third):
      em.add_field(name = "Future Imperative Active", value =f"1.s.: {imperative_active_singular_first}\n2.s.: {imperative_active_singular_second}\n3.s.: {imperative_active_singular_third}\n1.p.: {imperative_active_plural_first}\n2.p.: {imperative_active_plural_second}\n3.p.: {imperative_active_plural_third}")
    if (imperative_middle_singular_first or imperative_middle_singular_second or imperative_middle_singular_third or imperative_middle_plural_first or imperative_middle_plural_second or imperative_middle_plural_third):
      em.add_field(name = "Future Imperative Middle", value =f"1.s.: {imperative_middle_singular_first}\n2.s.: {imperative_middle_singular_second}\n3.s.: {imperative_middle_singular_third}\n1.p.: {imperative_middle_plural_first}\n2.p.: {imperative_middle_plural_second}\n3.p.: {imperative_middle_plural_third}")
    if (imperative_passive_singular_first or imperative_passive_singular_second or imperative_passive_singular_third or imperative_passive_plural_first or imperative_passive_plural_second or imperative_passive_plural_third):
      em.add_field(name = "Future Imperative Passive", value =f"1.s.: {imperative_passive_singular_first}\n2.s.: {imperative_passive_singular_second}\n3.s.: {imperative_passive_singular_third}\n1.p.: {imperative_passive_plural_first}\n2.p.: {imperative_passive_plural_second}\n3.p.: {imperative_passive_plural_third}")

    if (optative_active_singular_first or optative_active_singular_second or optative_active_singular_third or optative_active_plural_first or optative_active_plural_second or optative_active_plural_third):
      em.add_field(name = "Future Optative Active", value =f"1.s.: {optative_active_singular_first}\n2.s.: {optative_active_singular_second}\n3.s.: {optative_active_singular_third}\n1.p.: {optative_active_plural_first}\n2.p.: {optative_active_plural_second}\n3.p.: {optative_active_plural_third}")
    if (optative_middle_singular_first or optative_middle_singular_second or optative_middle_singular_third or optative_middle_plural_first or optative_middle_plural_second or optative_middle_plural_third):
      em.add_field(name = "Future Optative Middle", value =f"1.s.: {optative_middle_singular_first}\n2.s.: {optative_middle_singular_second}\n3.s.: {optative_middle_singular_third}\n1.p.: {optative_middle_plural_first}\n2.p.: {optative_middle_plural_second}\n3.p.: {optative_middle_plural_third}")
    if (optative_passive_singular_first or optative_passive_singular_second or optative_passive_singular_third or optative_passive_plural_first or optative_passive_plural_second or optative_passive_plural_third):
      em.add_field(name = "Future Optative Passive", value =f"1.s.: {optative_passive_singular_first}\n2.s.: {optative_passive_singular_second}\n3.s.: {optative_passive_singular_third}\n1.p.: {optative_passive_plural_first}\n2.p.: {optative_passive_plural_second}\n3.p.: {optative_passive_plural_third}")

    if (subjunctive_active_singular_first or subjunctive_active_singular_second or subjunctive_active_singular_third or subjunctive_active_plural_first or subjunctive_active_plural_second or subjunctive_active_plural_third):
      em.add_field(name = "Future subjunctive Active", value =f"1.s.: {subjunctive_active_singular_first}\n2.s.: {subjunctive_active_singular_second}\n3.s.: {subjunctive_active_singular_third}\n1.p.: {subjunctive_active_plural_first}\n2.p.: {subjunctive_active_plural_second}\n3.p.: {subjunctive_active_plural_third}")
    if (subjunctive_middle_singular_first or subjunctive_middle_singular_second or subjunctive_middle_singular_third or subjunctive_middle_plural_first or subjunctive_middle_plural_second or subjunctive_middle_plural_third):
      em.add_field(name = "Future subjunctive Middle", value =f"1.s.: {subjunctive_middle_singular_first}\n2.s.: {subjunctive_middle_singular_second}\n3.s.: {subjunctive_middle_singular_third}\n1.p.: {subjunctive_middle_plural_first}\n2.p.: {subjunctive_middle_plural_second}\n3.p.: {subjunctive_middle_plural_third}")
    if (subjunctive_passive_singular_first or subjunctive_passive_singular_second or subjunctive_passive_singular_third or subjunctive_passive_plural_first or subjunctive_passive_plural_second or subjunctive_passive_plural_third):
      em.add_field(name = "Future subjunctive Passive", value =f"1.s.: {subjunctive_passive_singular_first}\n2.s.: {subjunctive_passive_singular_second}\n3.s.: {subjunctive_passive_singular_third}\n1.p.: {subjunctive_passive_plural_first}\n2.p.: {subjunctive_passive_plural_second}\n3.p.: {subjunctive_passive_plural_third}")

    return em
  return None

def conjugator_aorist(verb_json, description):
  if (verb_json):
    tense = verb_json["aorist"]

    indicative = tense["indicative"]
    imperative = tense["imperative"]
    optative = tense["optative"]
    subjunctive = tense["subjunctive"]

    indicative_active = indicative["active"]
    indicative_middle = indicative["middle"]
    indicative_passive = indicative["passive"]

    imperative_active = imperative["active"]
    imperative_middle = imperative["middle"]
    imperative_passive = imperative["passive"]

    optative_active = optative["active"]
    optative_middle = optative["middle"]
    optative_passive = optative["passive"]

    subjunctive_active = subjunctive["active"]
    subjunctive_middle = subjunctive["middle"]
    subjunctive_passive = subjunctive["passive"]

    indicative_active_singular = indicative_active["singular"]
    indicative_active_plural = indicative_active["plural"]
    indicative_middle_singular = indicative_middle["singular"]
    indicative_middle_plural = indicative_middle["plural"]
    indicative_passive_singular = indicative_passive["singular"]
    indicative_passive_plural = indicative_passive["plural"]

    indicative_active_singular_first = indicative_active_singular["first"]
    indicative_active_singular_second = indicative_active_singular["second"]
    indicative_active_singular_third = indicative_active_singular["third"]
    indicative_active_plural_first = indicative_active_plural["first"]
    indicative_active_plural_second = indicative_active_plural["second"]
    indicative_active_plural_third = indicative_active_plural["third"]

    indicative_middle_singular_first = indicative_middle_singular["first"]
    indicative_middle_singular_second = indicative_middle_singular["second"]
    indicative_middle_singular_third = indicative_middle_singular["third"]
    indicative_middle_plural_first = indicative_middle_plural["first"]
    indicative_middle_plural_second = indicative_middle_plural["second"]
    indicative_middle_plural_third = indicative_middle_plural["third"]

    indicative_passive_singular_first = indicative_passive_singular["first"]
    indicative_passive_singular_second = indicative_passive_singular["second"]
    indicative_passive_singular_third = indicative_passive_singular["third"]
    indicative_passive_plural_first = indicative_passive_plural["first"]
    indicative_passive_plural_second = indicative_passive_plural["second"]
    indicative_passive_plural_third = indicative_passive_plural["third"]

    imperative_active_singular = imperative_active["singular"]
    imperative_active_plural = imperative_active["plural"]
    imperative_middle_singular = imperative_middle["singular"]
    imperative_middle_plural = imperative_middle["plural"]
    imperative_passive_singular = imperative_passive["singular"]
    imperative_passive_plural = imperative_passive["plural"]

    imperative_active_singular_first = imperative_active_singular["first"]
    imperative_active_singular_second = imperative_active_singular["second"]
    imperative_active_singular_third = imperative_active_singular["third"]
    imperative_active_plural_first = imperative_active_plural["first"]
    imperative_active_plural_second = imperative_active_plural["second"]
    imperative_active_plural_third = imperative_active_plural["third"]

    imperative_middle_singular_first = imperative_middle_singular["first"]
    imperative_middle_singular_second = imperative_middle_singular["second"]
    imperative_middle_singular_third = imperative_middle_singular["third"]
    imperative_middle_plural_first = imperative_middle_plural["first"]
    imperative_middle_plural_second = imperative_middle_plural["second"]
    imperative_middle_plural_third = imperative_middle_plural["third"]

    imperative_passive_singular_first = imperative_passive_singular["first"]
    imperative_passive_singular_second = imperative_passive_singular["second"]
    imperative_passive_singular_third = imperative_passive_singular["third"]
    imperative_passive_plural_first = imperative_passive_plural["first"]
    imperative_passive_plural_second = imperative_passive_plural["second"]
    imperative_passive_plural_third = imperative_passive_plural["third"]

    optative_active_singular = optative_active["singular"]
    optative_active_plural = optative_active["plural"]
    optative_middle_singular = optative_middle["singular"]
    optative_middle_plural = optative_middle["plural"]
    optative_passive_singular = optative_passive["singular"]
    optative_passive_plural = optative_passive["plural"]

    optative_active_singular_first = optative_active_singular["first"]
    optative_active_singular_second = optative_active_singular["second"]
    optative_active_singular_third = optative_active_singular["third"]
    optative_active_plural_first = optative_active_plural["first"]
    optative_active_plural_second = optative_active_plural["second"]
    optative_active_plural_third = optative_active_plural["third"]

    optative_middle_singular_first = optative_middle_singular["first"]
    optative_middle_singular_second = optative_middle_singular["second"]
    optative_middle_singular_third = optative_middle_singular["third"]
    optative_middle_plural_first = optative_middle_plural["first"]
    optative_middle_plural_second = optative_middle_plural["second"]
    optative_middle_plural_third = optative_middle_plural["third"]

    optative_passive_singular_first = optative_passive_singular["first"]
    optative_passive_singular_second = optative_passive_singular["second"]
    optative_passive_singular_third = optative_passive_singular["third"]
    optative_passive_plural_first = optative_passive_plural["first"]
    optative_passive_plural_second = optative_passive_plural["second"]
    optative_passive_plural_third = optative_passive_plural["third"]

    subjunctive_active_singular = subjunctive_active["singular"]
    subjunctive_active_plural = subjunctive_active["plural"]
    subjunctive_middle_singular = subjunctive_middle["singular"]
    subjunctive_middle_plural = subjunctive_middle["plural"]
    subjunctive_passive_singular = subjunctive_passive["singular"]
    subjunctive_passive_plural = subjunctive_passive["plural"]

    subjunctive_active_singular_first = subjunctive_active_singular["first"]
    subjunctive_active_singular_second = subjunctive_active_singular["second"]
    subjunctive_active_singular_third = subjunctive_active_singular["third"]
    subjunctive_active_plural_first = subjunctive_active_plural["first"]
    subjunctive_active_plural_second = subjunctive_active_plural["second"]
    subjunctive_active_plural_third = subjunctive_active_plural["third"]

    subjunctive_middle_singular_first = subjunctive_middle_singular["first"]
    subjunctive_middle_singular_second = subjunctive_middle_singular["second"]
    subjunctive_middle_singular_third = subjunctive_middle_singular["third"]
    subjunctive_middle_plural_first = subjunctive_middle_plural["first"]
    subjunctive_middle_plural_second = subjunctive_middle_plural["second"]
    subjunctive_middle_plural_third = subjunctive_middle_plural["third"]

    subjunctive_passive_singular_first = subjunctive_passive_singular["first"]
    subjunctive_passive_singular_second = subjunctive_passive_singular["second"]
    subjunctive_passive_singular_third = subjunctive_passive_singular["third"]
    subjunctive_passive_plural_first = subjunctive_passive_plural["first"]
    subjunctive_passive_plural_second = subjunctive_passive_plural["second"]
    subjunctive_passive_plural_third = subjunctive_passive_plural["third"]

    inf_active = tense["infinitive"]["active"]
    inf_middle = tense["infinitive"]["middle"]
    inf_passive = tense["infinitive"]["passive"]

    em = discord.Embed(title=description, color = discord.Color.blue())
    if (inf_active or inf_middle or inf_passive):
      em.add_field(name = "Aorist Infinitives", value =f"Active: {inf_active}\nMiddle: {inf_middle}\nPassive: {inf_passive}")
    if (indicative_active_singular_first or indicative_active_singular_second or indicative_active_singular_third or indicative_active_plural_first or indicative_active_plural_second or indicative_active_plural_third):
      em.add_field(name = "Aorist Indicative Active", value =f"1.s.: {indicative_active_singular_first}\n2.s.: {indicative_active_singular_second}\n3.s.: {indicative_active_singular_third}\n1.p.: {indicative_active_plural_first}\n2.p.: {indicative_active_plural_second}\n3.p.: {indicative_active_plural_third}")
    if (indicative_middle_singular_first or indicative_middle_singular_second or indicative_middle_singular_third or indicative_middle_plural_first or indicative_middle_plural_second or indicative_middle_plural_third):
      em.add_field(name = "Aorist Indicative Middle", value =f"1.s.: {indicative_middle_singular_first}\n2.s.: {indicative_middle_singular_second}\n3.s.: {indicative_middle_singular_third}\n1.p.: {indicative_middle_plural_first}\n2.p.: {indicative_middle_plural_second}\n3.p.: {indicative_middle_plural_third}")
    if (indicative_passive_singular_first or indicative_passive_singular_second or indicative_passive_singular_third or indicative_passive_plural_first or indicative_passive_plural_second or indicative_passive_plural_third):
      em.add_field(name = "Aorist Indicative Passive", value =f"1.s.: {indicative_passive_singular_first}\n2.s.: {indicative_passive_singular_second}\n3.s.: {indicative_passive_singular_third}\n1.p.: {indicative_passive_plural_first}\n2.p.: {indicative_passive_plural_second}\n3.p.: {indicative_passive_plural_third}")

    if (imperative_active_singular_first or imperative_active_singular_second or imperative_active_singular_third or imperative_active_plural_first or imperative_active_plural_second or imperative_active_plural_third):
      em.add_field(name = "Aorist Imperative Active", value =f"1.s.: {imperative_active_singular_first}\n2.s.: {imperative_active_singular_second}\n3.s.: {imperative_active_singular_third}\n1.p.: {imperative_active_plural_first}\n2.p.: {imperative_active_plural_second}\n3.p.: {imperative_active_plural_third}")
    if (imperative_middle_singular_first or imperative_middle_singular_second or imperative_middle_singular_third or imperative_middle_plural_first or imperative_middle_plural_second or imperative_middle_plural_third):
      em.add_field(name = "Aorist Imperative Middle", value =f"1.s.: {imperative_middle_singular_first}\n2.s.: {imperative_middle_singular_second}\n3.s.: {imperative_middle_singular_third}\n1.p.: {imperative_middle_plural_first}\n2.p.: {imperative_middle_plural_second}\n3.p.: {imperative_middle_plural_third}")
    if (imperative_passive_singular_first or imperative_passive_singular_second or imperative_passive_singular_third or imperative_passive_plural_first or imperative_passive_plural_second or imperative_passive_plural_third):
      em.add_field(name = "Aorist Imperative Passive", value =f"1.s.: {imperative_passive_singular_first}\n2.s.: {imperative_passive_singular_second}\n3.s.: {imperative_passive_singular_third}\n1.p.: {imperative_passive_plural_first}\n2.p.: {imperative_passive_plural_second}\n3.p.: {imperative_passive_plural_third}")

    if (optative_active_singular_first or optative_active_singular_second or optative_active_singular_third or optative_active_plural_first or optative_active_plural_second or optative_active_plural_third):
      em.add_field(name = "Aorist Optative Active", value =f"1.s.: {optative_active_singular_first}\n2.s.: {optative_active_singular_second}\n3.s.: {optative_active_singular_third}\n1.p.: {optative_active_plural_first}\n2.p.: {optative_active_plural_second}\n3.p.: {optative_active_plural_third}")
    if (optative_middle_singular_first or optative_middle_singular_second or optative_middle_singular_third or optative_middle_plural_first or optative_middle_plural_second or optative_middle_plural_third):
      em.add_field(name = "Aorist Optative Middle", value =f"1.s.: {optative_middle_singular_first}\n2.s.: {optative_middle_singular_second}\n3.s.: {optative_middle_singular_third}\n1.p.: {optative_middle_plural_first}\n2.p.: {optative_middle_plural_second}\n3.p.: {optative_middle_plural_third}")
    if (optative_passive_singular_first or optative_passive_singular_second or optative_passive_singular_third or optative_passive_plural_first or optative_passive_plural_second or optative_passive_plural_third):
      em.add_field(name = "Aorist Optative Passive", value =f"1.s.: {optative_passive_singular_first}\n2.s.: {optative_passive_singular_second}\n3.s.: {optative_passive_singular_third}\n1.p.: {optative_passive_plural_first}\n2.p.: {optative_passive_plural_second}\n3.p.: {optative_passive_plural_third}")

    if (subjunctive_active_singular_first or subjunctive_active_singular_second or subjunctive_active_singular_third or subjunctive_active_plural_first or subjunctive_active_plural_second or subjunctive_active_plural_third):
      em.add_field(name = "Aorist subjunctive Active", value =f"1.s.: {subjunctive_active_singular_first}\n2.s.: {subjunctive_active_singular_second}\n3.s.: {subjunctive_active_singular_third}\n1.p.: {subjunctive_active_plural_first}\n2.p.: {subjunctive_active_plural_second}\n3.p.: {subjunctive_active_plural_third}")
    if (subjunctive_middle_singular_first or subjunctive_middle_singular_second or subjunctive_middle_singular_third or subjunctive_middle_plural_first or subjunctive_middle_plural_second or subjunctive_middle_plural_third):
      em.add_field(name = "Aorist subjunctive Middle", value =f"1.s.: {subjunctive_middle_singular_first}\n2.s.: {subjunctive_middle_singular_second}\n3.s.: {subjunctive_middle_singular_third}\n1.p.: {subjunctive_middle_plural_first}\n2.p.: {subjunctive_middle_plural_second}\n3.p.: {subjunctive_middle_plural_third}")
    if (subjunctive_passive_singular_first or subjunctive_passive_singular_second or subjunctive_passive_singular_third or subjunctive_passive_plural_first or subjunctive_passive_plural_second or subjunctive_passive_plural_third):
      em.add_field(name = "Aorist subjunctive Passive", value =f"1.s.: {subjunctive_passive_singular_first}\n2.s.: {subjunctive_passive_singular_second}\n3.s.: {subjunctive_passive_singular_third}\n1.p.: {subjunctive_passive_plural_first}\n2.p.: {subjunctive_passive_plural_second}\n3.p.: {subjunctive_passive_plural_third}")

    return em
  return None

def conjugator_perfect(verb_json, description):
  if (verb_json):
    tense = verb_json["perfect"]

    indicative = tense["indicative"]
    imperative = tense["imperative"]
    optative = tense["optative"]
    subjunctive = tense["subjunctive"]

    indicative_active = indicative["active"]
    indicative_middle = indicative["middle"]
    indicative_passive = indicative["passive"]

    imperative_active = imperative["active"]
    imperative_middle = imperative["middle"]
    imperative_passive = imperative["passive"]

    optative_active = optative["active"]
    optative_middle = optative["middle"]
    optative_passive = optative["passive"]

    subjunctive_active = subjunctive["active"]
    subjunctive_middle = subjunctive["middle"]
    subjunctive_passive = subjunctive["passive"]

    indicative_active_singular = indicative_active["singular"]
    indicative_active_plural = indicative_active["plural"]
    indicative_middle_singular = indicative_middle["singular"]
    indicative_middle_plural = indicative_middle["plural"]
    indicative_passive_singular = indicative_passive["singular"]
    indicative_passive_plural = indicative_passive["plural"]

    indicative_active_singular_first = indicative_active_singular["first"]
    indicative_active_singular_second = indicative_active_singular["second"]
    indicative_active_singular_third = indicative_active_singular["third"]
    indicative_active_plural_first = indicative_active_plural["first"]
    indicative_active_plural_second = indicative_active_plural["second"]
    indicative_active_plural_third = indicative_active_plural["third"]

    indicative_middle_singular_first = indicative_middle_singular["first"]
    indicative_middle_singular_second = indicative_middle_singular["second"]
    indicative_middle_singular_third = indicative_middle_singular["third"]
    indicative_middle_plural_first = indicative_middle_plural["first"]
    indicative_middle_plural_second = indicative_middle_plural["second"]
    indicative_middle_plural_third = indicative_middle_plural["third"]

    indicative_passive_singular_first = indicative_passive_singular["first"]
    indicative_passive_singular_second = indicative_passive_singular["second"]
    indicative_passive_singular_third = indicative_passive_singular["third"]
    indicative_passive_plural_first = indicative_passive_plural["first"]
    indicative_passive_plural_second = indicative_passive_plural["second"]
    indicative_passive_plural_third = indicative_passive_plural["third"]

    imperative_active_singular = imperative_active["singular"]
    imperative_active_plural = imperative_active["plural"]
    imperative_middle_singular = imperative_middle["singular"]
    imperative_middle_plural = imperative_middle["plural"]
    imperative_passive_singular = imperative_passive["singular"]
    imperative_passive_plural = imperative_passive["plural"]

    imperative_active_singular_first = imperative_active_singular["first"]
    imperative_active_singular_second = imperative_active_singular["second"]
    imperative_active_singular_third = imperative_active_singular["third"]
    imperative_active_plural_first = imperative_active_plural["first"]
    imperative_active_plural_second = imperative_active_plural["second"]
    imperative_active_plural_third = imperative_active_plural["third"]

    imperative_middle_singular_first = imperative_middle_singular["first"]
    imperative_middle_singular_second = imperative_middle_singular["second"]
    imperative_middle_singular_third = imperative_middle_singular["third"]
    imperative_middle_plural_first = imperative_middle_plural["first"]
    imperative_middle_plural_second = imperative_middle_plural["second"]
    imperative_middle_plural_third = imperative_middle_plural["third"]

    imperative_passive_singular_first = imperative_passive_singular["first"]
    imperative_passive_singular_second = imperative_passive_singular["second"]
    imperative_passive_singular_third = imperative_passive_singular["third"]
    imperative_passive_plural_first = imperative_passive_plural["first"]
    imperative_passive_plural_second = imperative_passive_plural["second"]
    imperative_passive_plural_third = imperative_passive_plural["third"]

    optative_active_singular = optative_active["singular"]
    optative_active_plural = optative_active["plural"]
    optative_middle_singular = optative_middle["singular"]
    optative_middle_plural = optative_middle["plural"]
    optative_passive_singular = optative_passive["singular"]
    optative_passive_plural = optative_passive["plural"]

    optative_active_singular_first = optative_active_singular["first"]
    optative_active_singular_second = optative_active_singular["second"]
    optative_active_singular_third = optative_active_singular["third"]
    optative_active_plural_first = optative_active_plural["first"]
    optative_active_plural_second = optative_active_plural["second"]
    optative_active_plural_third = optative_active_plural["third"]

    optative_middle_singular_first = optative_middle_singular["first"]
    optative_middle_singular_second = optative_middle_singular["second"]
    optative_middle_singular_third = optative_middle_singular["third"]
    optative_middle_plural_first = optative_middle_plural["first"]
    optative_middle_plural_second = optative_middle_plural["second"]
    optative_middle_plural_third = optative_middle_plural["third"]

    optative_passive_singular_first = optative_passive_singular["first"]
    optative_passive_singular_second = optative_passive_singular["second"]
    optative_passive_singular_third = optative_passive_singular["third"]
    optative_passive_plural_first = optative_passive_plural["first"]
    optative_passive_plural_second = optative_passive_plural["second"]
    optative_passive_plural_third = optative_passive_plural["third"]

    subjunctive_active_singular = subjunctive_active["singular"]
    subjunctive_active_plural = subjunctive_active["plural"]
    subjunctive_middle_singular = subjunctive_middle["singular"]
    subjunctive_middle_plural = subjunctive_middle["plural"]
    subjunctive_passive_singular = subjunctive_passive["singular"]
    subjunctive_passive_plural = subjunctive_passive["plural"]

    subjunctive_active_singular_first = subjunctive_active_singular["first"]
    subjunctive_active_singular_second = subjunctive_active_singular["second"]
    subjunctive_active_singular_third = subjunctive_active_singular["third"]
    subjunctive_active_plural_first = subjunctive_active_plural["first"]
    subjunctive_active_plural_second = subjunctive_active_plural["second"]
    subjunctive_active_plural_third = subjunctive_active_plural["third"]

    subjunctive_middle_singular_first = subjunctive_middle_singular["first"]
    subjunctive_middle_singular_second = subjunctive_middle_singular["second"]
    subjunctive_middle_singular_third = subjunctive_middle_singular["third"]
    subjunctive_middle_plural_first = subjunctive_middle_plural["first"]
    subjunctive_middle_plural_second = subjunctive_middle_plural["second"]
    subjunctive_middle_plural_third = subjunctive_middle_plural["third"]

    subjunctive_passive_singular_first = subjunctive_passive_singular["first"]
    subjunctive_passive_singular_second = subjunctive_passive_singular["second"]
    subjunctive_passive_singular_third = subjunctive_passive_singular["third"]
    subjunctive_passive_plural_first = subjunctive_passive_plural["first"]
    subjunctive_passive_plural_second = subjunctive_passive_plural["second"]
    subjunctive_passive_plural_third = subjunctive_passive_plural["third"]

    inf_active = tense["infinitive"]["active"]
    inf_middle = tense["infinitive"]["middle"]
    inf_passive = tense["infinitive"]["passive"]

    em = discord.Embed(title=description, color = discord.Color.blue())
    if (inf_active or inf_middle or inf_passive):
      em.add_field(name = "Perfect Infinitives", value =f"Active: {inf_active}\nMiddle: {inf_middle}\nPassive: {inf_passive}")
    if (indicative_active_singular_first or indicative_active_singular_second or indicative_active_singular_third or indicative_active_plural_first or indicative_active_plural_second or indicative_active_plural_third):
      em.add_field(name = "Perfect Indicative Active", value =f"1.s.: {indicative_active_singular_first}\n2.s.: {indicative_active_singular_second}\n3.s.: {indicative_active_singular_third}\n1.p.: {indicative_active_plural_first}\n2.p.: {indicative_active_plural_second}\n3.p.: {indicative_active_plural_third}")
    if (indicative_middle_singular_first or indicative_middle_singular_second or indicative_middle_singular_third or indicative_middle_plural_first or indicative_middle_plural_second or indicative_middle_plural_third):
      em.add_field(name = "Perfect Indicative Middle", value =f"1.s.: {indicative_middle_singular_first}\n2.s.: {indicative_middle_singular_second}\n3.s.: {indicative_middle_singular_third}\n1.p.: {indicative_middle_plural_first}\n2.p.: {indicative_middle_plural_second}\n3.p.: {indicative_middle_plural_third}")
    if (indicative_passive_singular_first or indicative_passive_singular_second or indicative_passive_singular_third or indicative_passive_plural_first or indicative_passive_plural_second or indicative_passive_plural_third):
      em.add_field(name = "Perfect Indicative Passive", value =f"1.s.: {indicative_passive_singular_first}\n2.s.: {indicative_passive_singular_second}\n3.s.: {indicative_passive_singular_third}\n1.p.: {indicative_passive_plural_first}\n2.p.: {indicative_passive_plural_second}\n3.p.: {indicative_passive_plural_third}")

    if (imperative_active_singular_first or imperative_active_singular_second or imperative_active_singular_third or imperative_active_plural_first or imperative_active_plural_second or imperative_active_plural_third):
      em.add_field(name = "Perfect Imperative Active", value =f"1.s.: {imperative_active_singular_first}\n2.s.: {imperative_active_singular_second}\n3.s.: {imperative_active_singular_third}\n1.p.: {imperative_active_plural_first}\n2.p.: {imperative_active_plural_second}\n3.p.: {imperative_active_plural_third}")
    if (imperative_middle_singular_first or imperative_middle_singular_second or imperative_middle_singular_third or imperative_middle_plural_first or imperative_middle_plural_second or imperative_middle_plural_third):
      em.add_field(name = "Perfect Imperative Middle", value =f"1.s.: {imperative_middle_singular_first}\n2.s.: {imperative_middle_singular_second}\n3.s.: {imperative_middle_singular_third}\n1.p.: {imperative_middle_plural_first}\n2.p.: {imperative_middle_plural_second}\n3.p.: {imperative_middle_plural_third}")
    if (imperative_passive_singular_first or imperative_passive_singular_second or imperative_passive_singular_third or imperative_passive_plural_first or imperative_passive_plural_second or imperative_passive_plural_third):
      em.add_field(name = "Perfect Imperative Passive", value =f"1.s.: {imperative_passive_singular_first}\n2.s.: {imperative_passive_singular_second}\n3.s.: {imperative_passive_singular_third}\n1.p.: {imperative_passive_plural_first}\n2.p.: {imperative_passive_plural_second}\n3.p.: {imperative_passive_plural_third}")

    if (optative_active_singular_first or optative_active_singular_second or optative_active_singular_third or optative_active_plural_first or optative_active_plural_second or optative_active_plural_third):
      em.add_field(name = "Perfect Optative Active", value =f"1.s.: {optative_active_singular_first}\n2.s.: {optative_active_singular_second}\n3.s.: {optative_active_singular_third}\n1.p.: {optative_active_plural_first}\n2.p.: {optative_active_plural_second}\n3.p.: {optative_active_plural_third}")
    if (optative_middle_singular_first or optative_middle_singular_second or optative_middle_singular_third or optative_middle_plural_first or optative_middle_plural_second or optative_middle_plural_third):
      em.add_field(name = "Perfect Optative Middle", value =f"1.s.: {optative_middle_singular_first}\n2.s.: {optative_middle_singular_second}\n3.s.: {optative_middle_singular_third}\n1.p.: {optative_middle_plural_first}\n2.p.: {optative_middle_plural_second}\n3.p.: {optative_middle_plural_third}")
    if (optative_passive_singular_first or optative_passive_singular_second or optative_passive_singular_third or optative_passive_plural_first or optative_passive_plural_second or optative_passive_plural_third):
      em.add_field(name = "Perfect Optative Passive", value =f"1.s.: {optative_passive_singular_first}\n2.s.: {optative_passive_singular_second}\n3.s.: {optative_passive_singular_third}\n1.p.: {optative_passive_plural_first}\n2.p.: {optative_passive_plural_second}\n3.p.: {optative_passive_plural_third}")

    if (subjunctive_active_singular_first or subjunctive_active_singular_second or subjunctive_active_singular_third or subjunctive_active_plural_first or subjunctive_active_plural_second or subjunctive_active_plural_third):
      em.add_field(name = "Perfect subjunctive Active", value =f"1.s.: {subjunctive_active_singular_first}\n2.s.: {subjunctive_active_singular_second}\n3.s.: {subjunctive_active_singular_third}\n1.p.: {subjunctive_active_plural_first}\n2.p.: {subjunctive_active_plural_second}\n3.p.: {subjunctive_active_plural_third}")
    if (subjunctive_middle_singular_first or subjunctive_middle_singular_second or subjunctive_middle_singular_third or subjunctive_middle_plural_first or subjunctive_middle_plural_second or subjunctive_middle_plural_third):
      em.add_field(name = "Perfect subjunctive Middle", value =f"1.s.: {subjunctive_middle_singular_first}\n2.s.: {subjunctive_middle_singular_second}\n3.s.: {subjunctive_middle_singular_third}\n1.p.: {subjunctive_middle_plural_first}\n2.p.: {subjunctive_middle_plural_second}\n3.p.: {subjunctive_middle_plural_third}")
    if (subjunctive_passive_singular_first or subjunctive_passive_singular_second or subjunctive_passive_singular_third or subjunctive_passive_plural_first or subjunctive_passive_plural_second or subjunctive_passive_plural_third):
      em.add_field(name = "Perfect subjunctive Passive", value =f"1.s.: {subjunctive_passive_singular_first}\n2.s.: {subjunctive_passive_singular_second}\n3.s.: {subjunctive_passive_singular_third}\n1.p.: {subjunctive_passive_plural_first}\n2.p.: {subjunctive_passive_plural_second}\n3.p.: {subjunctive_passive_plural_third}")

    return em
  return None

def conjugator_pluperfect(verb_json, description):
  if (verb_json):
    tense = verb_json["pluperfect"]

    indicative = tense["indicative"]
    imperative = tense["imperative"]
    optative = tense["optative"]
    subjunctive = tense["subjunctive"]

    indicative_active = indicative["active"]
    indicative_middle = indicative["middle"]
    indicative_passive = indicative["passive"]

    imperative_active = imperative["active"]
    imperative_middle = imperative["middle"]
    imperative_passive = imperative["passive"]

    optative_active = optative["active"]
    optative_middle = optative["middle"]
    optative_passive = optative["passive"]

    subjunctive_active = subjunctive["active"]
    subjunctive_middle = subjunctive["middle"]
    subjunctive_passive = subjunctive["passive"]

    indicative_active_singular = indicative_active["singular"]
    indicative_active_plural = indicative_active["plural"]
    indicative_middle_singular = indicative_middle["singular"]
    indicative_middle_plural = indicative_middle["plural"]
    indicative_passive_singular = indicative_passive["singular"]
    indicative_passive_plural = indicative_passive["plural"]

    indicative_active_singular_first = indicative_active_singular["first"]
    indicative_active_singular_second = indicative_active_singular["second"]
    indicative_active_singular_third = indicative_active_singular["third"]
    indicative_active_plural_first = indicative_active_plural["first"]
    indicative_active_plural_second = indicative_active_plural["second"]
    indicative_active_plural_third = indicative_active_plural["third"]

    indicative_middle_singular_first = indicative_middle_singular["first"]
    indicative_middle_singular_second = indicative_middle_singular["second"]
    indicative_middle_singular_third = indicative_middle_singular["third"]
    indicative_middle_plural_first = indicative_middle_plural["first"]
    indicative_middle_plural_second = indicative_middle_plural["second"]
    indicative_middle_plural_third = indicative_middle_plural["third"]

    indicative_passive_singular_first = indicative_passive_singular["first"]
    indicative_passive_singular_second = indicative_passive_singular["second"]
    indicative_passive_singular_third = indicative_passive_singular["third"]
    indicative_passive_plural_first = indicative_passive_plural["first"]
    indicative_passive_plural_second = indicative_passive_plural["second"]
    indicative_passive_plural_third = indicative_passive_plural["third"]

    imperative_active_singular = imperative_active["singular"]
    imperative_active_plural = imperative_active["plural"]
    imperative_middle_singular = imperative_middle["singular"]
    imperative_middle_plural = imperative_middle["plural"]
    imperative_passive_singular = imperative_passive["singular"]
    imperative_passive_plural = imperative_passive["plural"]

    imperative_active_singular_first = imperative_active_singular["first"]
    imperative_active_singular_second = imperative_active_singular["second"]
    imperative_active_singular_third = imperative_active_singular["third"]
    imperative_active_plural_first = imperative_active_plural["first"]
    imperative_active_plural_second = imperative_active_plural["second"]
    imperative_active_plural_third = imperative_active_plural["third"]

    imperative_middle_singular_first = imperative_middle_singular["first"]
    imperative_middle_singular_second = imperative_middle_singular["second"]
    imperative_middle_singular_third = imperative_middle_singular["third"]
    imperative_middle_plural_first = imperative_middle_plural["first"]
    imperative_middle_plural_second = imperative_middle_plural["second"]
    imperative_middle_plural_third = imperative_middle_plural["third"]

    imperative_passive_singular_first = imperative_passive_singular["first"]
    imperative_passive_singular_second = imperative_passive_singular["second"]
    imperative_passive_singular_third = imperative_passive_singular["third"]
    imperative_passive_plural_first = imperative_passive_plural["first"]
    imperative_passive_plural_second = imperative_passive_plural["second"]
    imperative_passive_plural_third = imperative_passive_plural["third"]

    optative_active_singular = optative_active["singular"]
    optative_active_plural = optative_active["plural"]
    optative_middle_singular = optative_middle["singular"]
    optative_middle_plural = optative_middle["plural"]
    optative_passive_singular = optative_passive["singular"]
    optative_passive_plural = optative_passive["plural"]

    optative_active_singular_first = optative_active_singular["first"]
    optative_active_singular_second = optative_active_singular["second"]
    optative_active_singular_third = optative_active_singular["third"]
    optative_active_plural_first = optative_active_plural["first"]
    optative_active_plural_second = optative_active_plural["second"]
    optative_active_plural_third = optative_active_plural["third"]

    optative_middle_singular_first = optative_middle_singular["first"]
    optative_middle_singular_second = optative_middle_singular["second"]
    optative_middle_singular_third = optative_middle_singular["third"]
    optative_middle_plural_first = optative_middle_plural["first"]
    optative_middle_plural_second = optative_middle_plural["second"]
    optative_middle_plural_third = optative_middle_plural["third"]

    optative_passive_singular_first = optative_passive_singular["first"]
    optative_passive_singular_second = optative_passive_singular["second"]
    optative_passive_singular_third = optative_passive_singular["third"]
    optative_passive_plural_first = optative_passive_plural["first"]
    optative_passive_plural_second = optative_passive_plural["second"]
    optative_passive_plural_third = optative_passive_plural["third"]

    subjunctive_active_singular = subjunctive_active["singular"]
    subjunctive_active_plural = subjunctive_active["plural"]
    subjunctive_middle_singular = subjunctive_middle["singular"]
    subjunctive_middle_plural = subjunctive_middle["plural"]
    subjunctive_passive_singular = subjunctive_passive["singular"]
    subjunctive_passive_plural = subjunctive_passive["plural"]

    subjunctive_active_singular_first = subjunctive_active_singular["first"]
    subjunctive_active_singular_second = subjunctive_active_singular["second"]
    subjunctive_active_singular_third = subjunctive_active_singular["third"]
    subjunctive_active_plural_first = subjunctive_active_plural["first"]
    subjunctive_active_plural_second = subjunctive_active_plural["second"]
    subjunctive_active_plural_third = subjunctive_active_plural["third"]

    subjunctive_middle_singular_first = subjunctive_middle_singular["first"]
    subjunctive_middle_singular_second = subjunctive_middle_singular["second"]
    subjunctive_middle_singular_third = subjunctive_middle_singular["third"]
    subjunctive_middle_plural_first = subjunctive_middle_plural["first"]
    subjunctive_middle_plural_second = subjunctive_middle_plural["second"]
    subjunctive_middle_plural_third = subjunctive_middle_plural["third"]

    subjunctive_passive_singular_first = subjunctive_passive_singular["first"]
    subjunctive_passive_singular_second = subjunctive_passive_singular["second"]
    subjunctive_passive_singular_third = subjunctive_passive_singular["third"]
    subjunctive_passive_plural_first = subjunctive_passive_plural["first"]
    subjunctive_passive_plural_second = subjunctive_passive_plural["second"]
    subjunctive_passive_plural_third = subjunctive_passive_plural["third"]

    inf_active = tense["infinitive"]["active"]
    inf_middle = tense["infinitive"]["middle"]
    inf_passive = tense["infinitive"]["passive"]

    em = discord.Embed(title=description, color = discord.Color.blue())
    if (inf_active or inf_middle or inf_passive):
      em.add_field(name = "Pluperfect Infinitives", value =f"Active: {inf_active}\nMiddle: {inf_middle}\nPassive: {inf_passive}")
    if (indicative_active_singular_first or indicative_active_singular_second or indicative_active_singular_third or indicative_active_plural_first or indicative_active_plural_second or indicative_active_plural_third):
      em.add_field(name = "Pluperfect Indicative Active", value =f"1.s.: {indicative_active_singular_first}\n2.s.: {indicative_active_singular_second}\n3.s.: {indicative_active_singular_third}\n1.p.: {indicative_active_plural_first}\n2.p.: {indicative_active_plural_second}\n3.p.: {indicative_active_plural_third}")
    if (indicative_middle_singular_first or indicative_middle_singular_second or indicative_middle_singular_third or indicative_middle_plural_first or indicative_middle_plural_second or indicative_middle_plural_third):
      em.add_field(name = "Pluperfect Indicative Middle", value =f"1.s.: {indicative_middle_singular_first}\n2.s.: {indicative_middle_singular_second}\n3.s.: {indicative_middle_singular_third}\n1.p.: {indicative_middle_plural_first}\n2.p.: {indicative_middle_plural_second}\n3.p.: {indicative_middle_plural_third}")
    if (indicative_passive_singular_first or indicative_passive_singular_second or indicative_passive_singular_third or indicative_passive_plural_first or indicative_passive_plural_second or indicative_passive_plural_third):
      em.add_field(name = "Pluperfect Indicative Passive", value =f"1.s.: {indicative_passive_singular_first}\n2.s.: {indicative_passive_singular_second}\n3.s.: {indicative_passive_singular_third}\n1.p.: {indicative_passive_plural_first}\n2.p.: {indicative_passive_plural_second}\n3.p.: {indicative_passive_plural_third}")

    if (imperative_active_singular_first or imperative_active_singular_second or imperative_active_singular_third or imperative_active_plural_first or imperative_active_plural_second or imperative_active_plural_third):
      em.add_field(name = "Pluperfect Imperative Active", value =f"1.s.: {imperative_active_singular_first}\n2.s.: {imperative_active_singular_second}\n3.s.: {imperative_active_singular_third}\n1.p.: {imperative_active_plural_first}\n2.p.: {imperative_active_plural_second}\n3.p.: {imperative_active_plural_third}")
    if (imperative_middle_singular_first or imperative_middle_singular_second or imperative_middle_singular_third or imperative_middle_plural_first or imperative_middle_plural_second or imperative_middle_plural_third):
      em.add_field(name = "Pluperfect Imperative Middle", value =f"1.s.: {imperative_middle_singular_first}\n2.s.: {imperative_middle_singular_second}\n3.s.: {imperative_middle_singular_third}\n1.p.: {imperative_middle_plural_first}\n2.p.: {imperative_middle_plural_second}\n3.p.: {imperative_middle_plural_third}")
    if (imperative_passive_singular_first or imperative_passive_singular_second or imperative_passive_singular_third or imperative_passive_plural_first or imperative_passive_plural_second or imperative_passive_plural_third):
      em.add_field(name = "Pluperfect Imperative Passive", value =f"1.s.: {imperative_passive_singular_first}\n2.s.: {imperative_passive_singular_second}\n3.s.: {imperative_passive_singular_third}\n1.p.: {imperative_passive_plural_first}\n2.p.: {imperative_passive_plural_second}\n3.p.: {imperative_passive_plural_third}")

    if (optative_active_singular_first or optative_active_singular_second or optative_active_singular_third or optative_active_plural_first or optative_active_plural_second or optative_active_plural_third):
      em.add_field(name = "Pluperfect Optative Active", value =f"1.s.: {optative_active_singular_first}\n2.s.: {optative_active_singular_second}\n3.s.: {optative_active_singular_third}\n1.p.: {optative_active_plural_first}\n2.p.: {optative_active_plural_second}\n3.p.: {optative_active_plural_third}")
    if (optative_middle_singular_first or optative_middle_singular_second or optative_middle_singular_third or optative_middle_plural_first or optative_middle_plural_second or optative_middle_plural_third):
      em.add_field(name = "Pluperfect Optative Middle", value =f"1.s.: {optative_middle_singular_first}\n2.s.: {optative_middle_singular_second}\n3.s.: {optative_middle_singular_third}\n1.p.: {optative_middle_plural_first}\n2.p.: {optative_middle_plural_second}\n3.p.: {optative_middle_plural_third}")
    if (optative_passive_singular_first or optative_passive_singular_second or optative_passive_singular_third or optative_passive_plural_first or optative_passive_plural_second or optative_passive_plural_third):
      em.add_field(name = "Pluperfect Optative Passive", value =f"1.s.: {optative_passive_singular_first}\n2.s.: {optative_passive_singular_second}\n3.s.: {optative_passive_singular_third}\n1.p.: {optative_passive_plural_first}\n2.p.: {optative_passive_plural_second}\n3.p.: {optative_passive_plural_third}")

    if (subjunctive_active_singular_first or subjunctive_active_singular_second or subjunctive_active_singular_third or subjunctive_active_plural_first or subjunctive_active_plural_second or subjunctive_active_plural_third):
      em.add_field(name = "Pluperfect subjunctive Active", value =f"1.s.: {subjunctive_active_singular_first}\n2.s.: {subjunctive_active_singular_second}\n3.s.: {subjunctive_active_singular_third}\n1.p.: {subjunctive_active_plural_first}\n2.p.: {subjunctive_active_plural_second}\n3.p.: {subjunctive_active_plural_third}")
    if (subjunctive_middle_singular_first or subjunctive_middle_singular_second or subjunctive_middle_singular_third or subjunctive_middle_plural_first or subjunctive_middle_plural_second or subjunctive_middle_plural_third):
      em.add_field(name = "Pluperfect subjunctive Middle", value =f"1.s.: {subjunctive_middle_singular_first}\n2.s.: {subjunctive_middle_singular_second}\n3.s.: {subjunctive_middle_singular_third}\n1.p.: {subjunctive_middle_plural_first}\n2.p.: {subjunctive_middle_plural_second}\n3.p.: {subjunctive_middle_plural_third}")
    if (subjunctive_passive_singular_first or subjunctive_passive_singular_second or subjunctive_passive_singular_third or subjunctive_passive_plural_first or subjunctive_passive_plural_second or subjunctive_passive_plural_third):
      em.add_field(name = "Pluperfect subjunctive Passive", value =f"1.s.: {subjunctive_passive_singular_first}\n2.s.: {subjunctive_passive_singular_second}\n3.s.: {subjunctive_passive_singular_third}\n1.p.: {subjunctive_passive_plural_first}\n2.p.: {subjunctive_passive_plural_second}\n3.p.: {subjunctive_passive_plural_third}")

    return em
  return None

@bot.command(name='info')
async def info(ctx):
  em = discord.Embed(title = "Χαῖρε! I'm a bot that seeks to help ancient greek students.", color = discord.Color.blue())
  em.add_field(name="You can look up words by searching their meaning, nominative singular or declension paradigm (according to Reading Greek method).", value="Type:\n.search <meaning/nominative singular/paradigm>")
  em.add_field(name="You can also help build the lexicon of this humble bot.", value="Type .add_data and follow the instructions thoroughly till the end.")
  em.add_field(name="IMPORTANT!", value="You have 90 seconds to answer me, check twice if you're inputting the right word and the right meaning.\nAdding wrong words will only make me dumb(er), please make me (more) intelligent.")
  em.add_field(name="Oh! Still in progress function!", value="You can also look up verb paradigms, with tenses, infinitives, participles and all that stuff.\nJust type: .verbs and I'll guide you.")
  await ctx.send(embed=em)

@bot.command(name='search')
async def search_verb(ctx, arg):
  
  words = db.session.query(Word).join(NominalNumber, Word.singular_id==NominalNumber.id).filter(or_(Word.paradigm.ilike(f'{arg}%'), Word.meaning.ilike(f'%{arg}%'), NominalNumber.nominative==arg))
  for word in words:
    em = discord.Embed(title = f'{word.singular.nominative} - Paradigm: {word.paradigm}\n({word.meaning})', color = discord.Color.blue())
    em.add_field(name = "Singular", value = f"Nominative: {word.singular.nominative} \n Genitive: {word.singular.genitive} \n Dative: {word.singular.dative} \n Accusative: {word.singular.accusative} \n Vocative: {word.singular.vocative}")
    if word.dual:
        em.add_field(name = "Dual", value = f"Nominative: {word.dual.nominative} \n Genitive: {word.dual.genitive} \n Dative: {word.dual.dative} \n Accusative: {word.dual.accusative} \n Vocative: {word.dual.vocative}")
    if word.plural:
        em.add_field(name = "Plural", value = f"Nominative: {word.plural.nominative} \n Genitive: {word.plural.genitive} \n Dative: {word.plural.dative} \n Accusative: {word.plural.accusative} \n Vocative: {word.plural.vocative}")
    await ctx.send(embed = em)

@bot.command(name='verbs')
async def verbs(ctx):
  em = discord.Embed(title = "You can look up verb paradigms.", color = discord.Color.blue())
  em.add_field(name="Try these:", value=".non_contracteds\n.contracteds\n.irregular_verbs")
  await ctx.send(embed=em)

@bot.command(name='contracteds')
async def contracteds(ctx):
  em = discord.Embed(title = "You can look up contracted conjugation paradigms.", color = discord.Color.blue())
  em.add_field(name="Try these:", value=".contracted_alpha tenses\n.contracted_alpha participle_present\n.contracted_alpha participle_future\n.contracted_alpha participle_aorist\n.contracted_alpha participle_perfect\n.contracted_epsilon tenses\n.contracted_epsilon participle_present\n.contracted_epsilon participle_future\n.contracted_epsilon participle_aorist\n.contracted_epsilon participle_perfect")
  await ctx.send(embed=em)
#\n.contracted_omikron tenses/participle_present/participle_future/participle_aorist/participle_perfect
@bot.command(name='non_contracteds')
async def non_contracteds(ctx):
  em = discord.Embed(title = "You can look up non contracted conjugation paradigms.", color = discord.Color.blue())
  em.add_field(name="Try these:", value=".non_contracted tenses\n.non_contracted participle_present\n.non_contracted participle_future\n.non_contracted participle_aorist\n.non_contracted participle_perfect")
  await ctx.send(embed=em)

@bot.command(name='non_contracted')
async def non_contracted(ctx, arg):
  with open ("paradigms/verbs/regulars/non_contracteds/omega.json", "r", encoding='utf8') as f:
    data = json.load(f)
    if arg.lower() == 'tenses':
      em_present = conjugator_present(data, "Present")
      em_imperfect = conjugator_imperfect(data, "Imperfect")
      em_future = conjugator_future(data, "Future")
      em_aorist = conjugator_aorist(data, "Aorist")
      em_perfect = conjugator_perfect(data, "Perfect")
      em_pluperfect = conjugator_pluperfect(data, "Pluperfect")

      if (em_present):
        await ctx.send(embed=em_present)
      if (em_imperfect):
        await ctx.send(embed=em_imperfect)
      if (em_future):
        await ctx.send(embed=em_future)
      if (em_aorist):
        await ctx.send(embed=em_aorist)
      if (em_perfect):
        await ctx.send(embed=em_perfect)
      if (em_pluperfect):
        await ctx.send(embed=em_pluperfect)

    elif arg.lower() == 'participle_present':
      em_p_m_present_a = declinator(data["present"]["participle"]["active"]["masculine"], "Present Participle Active Masculine")
      em_p_f_present_a = declinator(data["present"]["participle"]["active"]["feminine"], "Present Participle Active Feminine")
      em_p_n_present_a = declinator(data["present"]["participle"]["active"]["neuter"], "Present Participle Active Neuter")
      em_p_m_present_m = declinator(data["present"]["participle"]["middle"]["masculine"], "Present Participle Middle Masculine")
      em_p_f_present_m = declinator(data["present"]["participle"]["middle"]["feminine"], "Present Participle Middle Feminine")
      em_p_n_present_m = declinator(data["present"]["participle"]["middle"]["neuter"], "Present Participle Middle Neuter")
      em_p_m_present_p = declinator(data["present"]["participle"]["passive"]["masculine"], "Present Participle Passive Masculine")
      em_p_f_present_p = declinator(data["present"]["participle"]["passive"]["feminine"], "Present Participle Passive Feminine")
      em_p_n_present_p = declinator(data["present"]["participle"]["passive"]["neuter"], "Present Participle Passive Neuter")
      if (em_p_m_present_a):
        await ctx.send(embed=em_p_m_present_a)
      if (em_p_f_present_a):
        await ctx.send(embed=em_p_f_present_a)
      if (em_p_n_present_a):
        await ctx.send(embed=em_p_n_present_a)
      if (em_p_m_present_m):
        await ctx.send(embed=em_p_m_present_m)
      if (em_p_f_present_m):
        await ctx.send(embed=em_p_f_present_m)
      if (em_p_n_present_m):
        await ctx.send(embed=em_p_n_present_m)
      if (em_p_m_present_p):
        await ctx.send(embed=em_p_m_present_p)
      if (em_p_f_present_p):
        await ctx.send(embed=em_p_f_present_p)
      if (em_p_n_present_p):
        await ctx.send(embed=em_p_n_present_p)

    elif arg.lower() == 'participle_future':
      em_p_m_future_a = declinator(data["future"]["participle"]["active"]["masculine"], "Future Participle Active Masculine")
      em_p_f_future_a = declinator(data["future"]["participle"]["active"]["feminine"], "Future Participle Active Feminine")
      em_p_n_future_a = declinator(data["future"]["participle"]["active"]["neuter"], "Future Participle Active Neuter")
      em_p_m_future_m = declinator(data["future"]["participle"]["middle"]["masculine"], "Future Participle Middle Masculine")
      em_p_f_future_m = declinator(data["future"]["participle"]["middle"]["feminine"], "Future Participle Middle Feminine")
      em_p_n_future_m = declinator(data["future"]["participle"]["middle"]["neuter"], "Future Participle Middle Neuter")
      em_p_m_future_p = declinator(data["future"]["participle"]["passive"]["masculine"], "Future Participle Passive Masculine")
      em_p_f_future_p = declinator(data["future"]["participle"]["passive"]["feminine"], "Future Participle Passive Feminine")
      em_p_n_future_p = declinator(data["future"]["participle"]["passive"]["neuter"], "Future Participle Passive Neuter")
      if (em_p_m_future_a):
        await ctx.send(embed=em_p_m_future_a)
      if (em_p_f_future_a):
        await ctx.send(embed=em_p_f_future_a)
      if (em_p_n_future_a):
        await ctx.send(embed=em_p_n_future_a)
      if (em_p_m_future_m):
        await ctx.send(embed=em_p_m_future_m)
      if (em_p_f_future_m):
        await ctx.send(embed=em_p_f_future_m)
      if (em_p_n_future_m):
        await ctx.send(embed=em_p_n_future_m)
      if (em_p_m_future_p):
        await ctx.send(embed=em_p_m_future_p)
      if (em_p_f_future_p):
        await ctx.send(embed=em_p_f_future_p)
      if (em_p_n_future_p):
        await ctx.send(embed=em_p_n_future_p)

    elif arg.lower() == 'participle_aorist':
      em_p_m_aorist_a = declinator(data["aorist"]["participle"]["active"]["masculine"], "Aorist Participle Active Masculine")
      em_p_f_aorist_a = declinator(data["aorist"]["participle"]["active"]["feminine"], "Aorist Participle Active Feminine")
      em_p_n_aorist_a = declinator(data["aorist"]["participle"]["active"]["neuter"], "Aorist Participle Active Neuter")
      em_p_m_aorist_m = declinator(data["aorist"]["participle"]["middle"]["masculine"], "Aorist Participle Middle Masculine")
      em_p_f_aorist_m = declinator(data["aorist"]["participle"]["middle"]["feminine"], "Aorist Participle Middle Feminine")
      em_p_n_aorist_m = declinator(data["aorist"]["participle"]["middle"]["neuter"], "Aorist Participle Middle Neuter")
      em_p_m_aorist_p = declinator(data["aorist"]["participle"]["passive"]["masculine"], "Aorist Participle Passive Masculine")
      em_p_f_aorist_p = declinator(data["aorist"]["participle"]["passive"]["feminine"], "Aorist Participle Passive Feminine")
      em_p_n_aorist_p = declinator(data["aorist"]["participle"]["passive"]["neuter"], "Aorist Participle Passive Neuter")
      if (em_p_m_aorist_a):
        await ctx.send(embed=em_p_m_aorist_a)
      if (em_p_f_aorist_a):
        await ctx.send(embed=em_p_f_aorist_a)
      if (em_p_n_aorist_a):
        await ctx.send(embed=em_p_n_aorist_a)
      if (em_p_m_aorist_m):
        await ctx.send(embed=em_p_m_aorist_m)
      if (em_p_f_aorist_m):
        await ctx.send(embed=em_p_f_aorist_m)
      if (em_p_n_aorist_m):
        await ctx.send(embed=em_p_n_aorist_m)
      if (em_p_m_aorist_p):
        await ctx.send(embed=em_p_m_aorist_p)
      if (em_p_f_aorist_p):
        await ctx.send(embed=em_p_f_aorist_p)
      if (em_p_n_aorist_p):
        await ctx.send(embed=em_p_n_aorist_p)

    elif arg.lower() == 'participle_perfect':
      em_p_m_perfect_a = declinator(data["perfect"]["participle"]["active"]["masculine"], "Perfect Participle Active Masculine")
      em_p_f_perfect_a = declinator(data["perfect"]["participle"]["active"]["feminine"], "Perfect Participle Active Feminine")
      em_p_n_perfect_a = declinator(data["perfect"]["participle"]["active"]["neuter"], "Perfect Participle Active Neuter")
      em_p_m_perfect_m = declinator(data["perfect"]["participle"]["middle"]["masculine"], "Perfect Participle Middle Masculine")
      em_p_f_perfect_m = declinator(data["perfect"]["participle"]["middle"]["feminine"], "Perfect Participle Middle Feminine")
      em_p_n_perfect_m = declinator(data["perfect"]["participle"]["middle"]["neuter"], "Perfect Participle Middle Neuter")
      em_p_m_perfect_p = declinator(data["perfect"]["participle"]["passive"]["masculine"], "Perfect Participle Passive Masculine")
      em_p_f_perfect_p = declinator(data["perfect"]["participle"]["passive"]["feminine"], "Perfect Participle Passive Feminine")
      em_p_n_perfect_p = declinator(data["perfect"]["participle"]["passive"]["neuter"], "Perfect Participle Passive Neuter")
      if (em_p_m_perfect_a):
        await ctx.send(embed=em_p_m_perfect_a)
      if (em_p_f_perfect_a):
        await ctx.send(embed=em_p_f_perfect_a)
      if (em_p_n_perfect_a):
        await ctx.send(embed=em_p_n_perfect_a)
      if (em_p_m_perfect_m):
        await ctx.send(embed=em_p_m_perfect_m)
      if (em_p_f_perfect_m):
        await ctx.send(embed=em_p_f_perfect_m)
      if (em_p_n_perfect_m):
        await ctx.send(embed=em_p_n_perfect_m)
      if (em_p_m_perfect_p):
        await ctx.send(embed=em_p_m_perfect_p)
      if (em_p_f_perfect_p):
        await ctx.send(embed=em_p_f_perfect_p)
      if (em_p_n_perfect_p):
        await ctx.send(embed=em_p_n_perfect_p)

@bot.command(name='contracted_alpha')
async def contracted_alpha(ctx, arg):
  with open ("paradigms/verbs/regulars/contracteds/alpha.json", "r", encoding='utf8') as f:
    data = json.load(f)
    if arg.lower() == 'tenses':
      em_present = conjugator_present(data, "Present")
      em_imperfect = conjugator_imperfect(data, "Imperfect")
      em_future = conjugator_future(data, "Future")
      em_aorist = conjugator_aorist(data, "Aorist")
      em_perfect = conjugator_perfect(data, "Perfect")
      em_pluperfect = conjugator_pluperfect(data, "Pluperfect")

      if (em_present):
        await ctx.send(embed=em_present)
      if (em_imperfect):
        await ctx.send(embed=em_imperfect)
      if (em_future):
        await ctx.send(embed=em_future)
      if (em_aorist):
        await ctx.send(embed=em_aorist)
      if (em_perfect):
        await ctx.send(embed=em_perfect)
      if (em_pluperfect):
        await ctx.send(embed=em_pluperfect)

    elif arg.lower() == 'participle_present':
      em_p_m_present_a = declinator(data["present"]["participle"]["active"]["masculine"], "Present Participle Active Masculine")
      em_p_f_present_a = declinator(data["present"]["participle"]["active"]["feminine"], "Present Participle Active Feminine")
      em_p_n_present_a = declinator(data["present"]["participle"]["active"]["neuter"], "Present Participle Active Neuter")
      em_p_m_present_m = declinator(data["present"]["participle"]["middle"]["masculine"], "Present Participle Middle Masculine")
      em_p_f_present_m = declinator(data["present"]["participle"]["middle"]["feminine"], "Present Participle Middle Feminine")
      em_p_n_present_m = declinator(data["present"]["participle"]["middle"]["neuter"], "Present Participle Middle Neuter")
      em_p_m_present_p = declinator(data["present"]["participle"]["passive"]["masculine"], "Present Participle Passive Masculine")
      em_p_f_present_p = declinator(data["present"]["participle"]["passive"]["feminine"], "Present Participle Passive Feminine")
      em_p_n_present_p = declinator(data["present"]["participle"]["passive"]["neuter"], "Present Participle Passive Neuter")
      if (em_p_m_present_a):
        await ctx.send(embed=em_p_m_present_a)
      if (em_p_f_present_a):
        await ctx.send(embed=em_p_f_present_a)
      if (em_p_n_present_a):
        await ctx.send(embed=em_p_n_present_a)
      if (em_p_m_present_m):
        await ctx.send(embed=em_p_m_present_m)
      if (em_p_f_present_m):
        await ctx.send(embed=em_p_f_present_m)
      if (em_p_n_present_m):
        await ctx.send(embed=em_p_n_present_m)
      if (em_p_m_present_p):
        await ctx.send(embed=em_p_m_present_p)
      if (em_p_f_present_p):
        await ctx.send(embed=em_p_f_present_p)
      if (em_p_n_present_p):
        await ctx.send(embed=em_p_n_present_p)

    elif arg.lower() == 'participle_future':
      em_p_m_future_a = declinator(data["future"]["participle"]["active"]["masculine"], "Future Participle Active Masculine")
      em_p_f_future_a = declinator(data["future"]["participle"]["active"]["feminine"], "Future Participle Active Feminine")
      em_p_n_future_a = declinator(data["future"]["participle"]["active"]["neuter"], "Future Participle Active Neuter")
      em_p_m_future_m = declinator(data["future"]["participle"]["middle"]["masculine"], "Future Participle Middle Masculine")
      em_p_f_future_m = declinator(data["future"]["participle"]["middle"]["feminine"], "Future Participle Middle Feminine")
      em_p_n_future_m = declinator(data["future"]["participle"]["middle"]["neuter"], "Future Participle Middle Neuter")
      em_p_m_future_p = declinator(data["future"]["participle"]["passive"]["masculine"], "Future Participle Passive Masculine")
      em_p_f_future_p = declinator(data["future"]["participle"]["passive"]["feminine"], "Future Participle Passive Feminine")
      em_p_n_future_p = declinator(data["future"]["participle"]["passive"]["neuter"], "Future Participle Passive Neuter")
      if (em_p_m_future_a):
        await ctx.send(embed=em_p_m_future_a)
      if (em_p_f_future_a):
        await ctx.send(embed=em_p_f_future_a)
      if (em_p_n_future_a):
        await ctx.send(embed=em_p_n_future_a)
      if (em_p_m_future_m):
        await ctx.send(embed=em_p_m_future_m)
      if (em_p_f_future_m):
        await ctx.send(embed=em_p_f_future_m)
      if (em_p_n_future_m):
        await ctx.send(embed=em_p_n_future_m)
      if (em_p_m_future_p):
        await ctx.send(embed=em_p_m_future_p)
      if (em_p_f_future_p):
        await ctx.send(embed=em_p_f_future_p)
      if (em_p_n_future_p):
        await ctx.send(embed=em_p_n_future_p)

    elif arg.lower() == 'participle_aorist':
      em_p_m_aorist_a = declinator(data["aorist"]["participle"]["active"]["masculine"], "Aorist Participle Active Masculine")
      em_p_f_aorist_a = declinator(data["aorist"]["participle"]["active"]["feminine"], "Aorist Participle Active Feminine")
      em_p_n_aorist_a = declinator(data["aorist"]["participle"]["active"]["neuter"], "Aorist Participle Active Neuter")
      em_p_m_aorist_m = declinator(data["aorist"]["participle"]["middle"]["masculine"], "Aorist Participle Middle Masculine")
      em_p_f_aorist_m = declinator(data["aorist"]["participle"]["middle"]["feminine"], "Aorist Participle Middle Feminine")
      em_p_n_aorist_m = declinator(data["aorist"]["participle"]["middle"]["neuter"], "Aorist Participle Middle Neuter")
      em_p_m_aorist_p = declinator(data["aorist"]["participle"]["passive"]["masculine"], "Aorist Participle Passive Masculine")
      em_p_f_aorist_p = declinator(data["aorist"]["participle"]["passive"]["feminine"], "Aorist Participle Passive Feminine")
      em_p_n_aorist_p = declinator(data["aorist"]["participle"]["passive"]["neuter"], "Aorist Participle Passive Neuter")
      if (em_p_m_aorist_a):
        await ctx.send(embed=em_p_m_aorist_a)
      if (em_p_f_aorist_a):
        await ctx.send(embed=em_p_f_aorist_a)
      if (em_p_n_aorist_a):
        await ctx.send(embed=em_p_n_aorist_a)
      if (em_p_m_aorist_m):
        await ctx.send(embed=em_p_m_aorist_m)
      if (em_p_f_aorist_m):
        await ctx.send(embed=em_p_f_aorist_m)
      if (em_p_n_aorist_m):
        await ctx.send(embed=em_p_n_aorist_m)
      if (em_p_m_aorist_p):
        await ctx.send(embed=em_p_m_aorist_p)
      if (em_p_f_aorist_p):
        await ctx.send(embed=em_p_f_aorist_p)
      if (em_p_n_aorist_p):
        await ctx.send(embed=em_p_n_aorist_p)

    elif arg.lower() == 'participle_perfect':
      em_p_m_perfect_a = declinator(data["perfect"]["participle"]["active"]["masculine"], "Perfect Participle Active Masculine")
      em_p_f_perfect_a = declinator(data["perfect"]["participle"]["active"]["feminine"], "Perfect Participle Active Feminine")
      em_p_n_perfect_a = declinator(data["perfect"]["participle"]["active"]["neuter"], "Perfect Participle Active Neuter")
      em_p_m_perfect_m = declinator(data["perfect"]["participle"]["middle"]["masculine"], "Perfect Participle Middle Masculine")
      em_p_f_perfect_m = declinator(data["perfect"]["participle"]["middle"]["feminine"], "Perfect Participle Middle Feminine")
      em_p_n_perfect_m = declinator(data["perfect"]["participle"]["middle"]["neuter"], "Perfect Participle Middle Neuter")
      em_p_m_perfect_p = declinator(data["perfect"]["participle"]["passive"]["masculine"], "Perfect Participle Passive Masculine")
      em_p_f_perfect_p = declinator(data["perfect"]["participle"]["passive"]["feminine"], "Perfect Participle Passive Feminine")
      em_p_n_perfect_p = declinator(data["perfect"]["participle"]["passive"]["neuter"], "Perfect Participle Passive Neuter")
      if (em_p_m_perfect_a):
        await ctx.send(embed=em_p_m_perfect_a)
      if (em_p_f_perfect_a):
        await ctx.send(embed=em_p_f_perfect_a)
      if (em_p_n_perfect_a):
        await ctx.send(embed=em_p_n_perfect_a)
      if (em_p_m_perfect_m):
        await ctx.send(embed=em_p_m_perfect_m)
      if (em_p_f_perfect_m):
        await ctx.send(embed=em_p_f_perfect_m)
      if (em_p_n_perfect_m):
        await ctx.send(embed=em_p_n_perfect_m)
      if (em_p_m_perfect_p):
        await ctx.send(embed=em_p_m_perfect_p)
      if (em_p_f_perfect_p):
        await ctx.send(embed=em_p_f_perfect_p)
      if (em_p_n_perfect_p):
        await ctx.send(embed=em_p_n_perfect_p)

@bot.command(name='contracted_epsilon')
async def contracted_epsilon(ctx, arg):
  with open ("paradigms/verbs/regulars/contracteds/epsilon.json", "r", encoding='utf8') as f:
    data = json.load(f)
    if arg.lower() == 'tenses':
      em_present = conjugator_present(data, "Present")
      em_imperfect = conjugator_imperfect(data, "Imperfect")
      em_future = conjugator_future(data, "Future")
      em_aorist = conjugator_aorist(data, "Aorist")
      em_perfect = conjugator_perfect(data, "Perfect")
      em_pluperfect = conjugator_pluperfect(data, "Pluperfect")

      if (em_present):
        await ctx.send(embed=em_present)
      if (em_imperfect):
        await ctx.send(embed=em_imperfect)
      if (em_future):
        await ctx.send(embed=em_future)
      if (em_aorist):
        await ctx.send(embed=em_aorist)
      if (em_perfect):
        await ctx.send(embed=em_perfect)
      if (em_pluperfect):
        await ctx.send(embed=em_pluperfect)

    elif arg.lower() == 'participle_present':
      em_p_m_present_a = declinator(data["present"]["participle"]["active"]["masculine"], "Present Participle Active Masculine")
      em_p_f_present_a = declinator(data["present"]["participle"]["active"]["feminine"], "Present Participle Active Feminine")
      em_p_n_present_a = declinator(data["present"]["participle"]["active"]["neuter"], "Present Participle Active Neuter")
      em_p_m_present_m = declinator(data["present"]["participle"]["middle"]["masculine"], "Present Participle Middle Masculine")
      em_p_f_present_m = declinator(data["present"]["participle"]["middle"]["feminine"], "Present Participle Middle Feminine")
      em_p_n_present_m = declinator(data["present"]["participle"]["middle"]["neuter"], "Present Participle Middle Neuter")
      em_p_m_present_p = declinator(data["present"]["participle"]["passive"]["masculine"], "Present Participle Passive Masculine")
      em_p_f_present_p = declinator(data["present"]["participle"]["passive"]["feminine"], "Present Participle Passive Feminine")
      em_p_n_present_p = declinator(data["present"]["participle"]["passive"]["neuter"], "Present Participle Passive Neuter")
      if (em_p_m_present_a):
        await ctx.send(embed=em_p_m_present_a)
      if (em_p_f_present_a):
        await ctx.send(embed=em_p_f_present_a)
      if (em_p_n_present_a):
        await ctx.send(embed=em_p_n_present_a)
      if (em_p_m_present_m):
        await ctx.send(embed=em_p_m_present_m)
      if (em_p_f_present_m):
        await ctx.send(embed=em_p_f_present_m)
      if (em_p_n_present_m):
        await ctx.send(embed=em_p_n_present_m)
      if (em_p_m_present_p):
        await ctx.send(embed=em_p_m_present_p)
      if (em_p_f_present_p):
        await ctx.send(embed=em_p_f_present_p)
      if (em_p_n_present_p):
        await ctx.send(embed=em_p_n_present_p)

    elif arg.lower() == 'participle_future':
      em_p_m_future_a = declinator(data["future"]["participle"]["active"]["masculine"], "Future Participle Active Masculine")
      em_p_f_future_a = declinator(data["future"]["participle"]["active"]["feminine"], "Future Participle Active Feminine")
      em_p_n_future_a = declinator(data["future"]["participle"]["active"]["neuter"], "Future Participle Active Neuter")
      em_p_m_future_m = declinator(data["future"]["participle"]["middle"]["masculine"], "Future Participle Middle Masculine")
      em_p_f_future_m = declinator(data["future"]["participle"]["middle"]["feminine"], "Future Participle Middle Feminine")
      em_p_n_future_m = declinator(data["future"]["participle"]["middle"]["neuter"], "Future Participle Middle Neuter")
      em_p_m_future_p = declinator(data["future"]["participle"]["passive"]["masculine"], "Future Participle Passive Masculine")
      em_p_f_future_p = declinator(data["future"]["participle"]["passive"]["feminine"], "Future Participle Passive Feminine")
      em_p_n_future_p = declinator(data["future"]["participle"]["passive"]["neuter"], "Future Participle Passive Neuter")
      if (em_p_m_future_a):
        await ctx.send(embed=em_p_m_future_a)
      if (em_p_f_future_a):
        await ctx.send(embed=em_p_f_future_a)
      if (em_p_n_future_a):
        await ctx.send(embed=em_p_n_future_a)
      if (em_p_m_future_m):
        await ctx.send(embed=em_p_m_future_m)
      if (em_p_f_future_m):
        await ctx.send(embed=em_p_f_future_m)
      if (em_p_n_future_m):
        await ctx.send(embed=em_p_n_future_m)
      if (em_p_m_future_p):
        await ctx.send(embed=em_p_m_future_p)
      if (em_p_f_future_p):
        await ctx.send(embed=em_p_f_future_p)
      if (em_p_n_future_p):
        await ctx.send(embed=em_p_n_future_p)

    elif arg.lower() == 'participle_aorist':
      em_p_m_aorist_a = declinator(data["aorist"]["participle"]["active"]["masculine"], "Aorist Participle Active Masculine")
      em_p_f_aorist_a = declinator(data["aorist"]["participle"]["active"]["feminine"], "Aorist Participle Active Feminine")
      em_p_n_aorist_a = declinator(data["aorist"]["participle"]["active"]["neuter"], "Aorist Participle Active Neuter")
      em_p_m_aorist_m = declinator(data["aorist"]["participle"]["middle"]["masculine"], "Aorist Participle Middle Masculine")
      em_p_f_aorist_m = declinator(data["aorist"]["participle"]["middle"]["feminine"], "Aorist Participle Middle Feminine")
      em_p_n_aorist_m = declinator(data["aorist"]["participle"]["middle"]["neuter"], "Aorist Participle Middle Neuter")
      em_p_m_aorist_p = declinator(data["aorist"]["participle"]["passive"]["masculine"], "Aorist Participle Passive Masculine")
      em_p_f_aorist_p = declinator(data["aorist"]["participle"]["passive"]["feminine"], "Aorist Participle Passive Feminine")
      em_p_n_aorist_p = declinator(data["aorist"]["participle"]["passive"]["neuter"], "Aorist Participle Passive Neuter")
      if (em_p_m_aorist_a):
        await ctx.send(embed=em_p_m_aorist_a)
      if (em_p_f_aorist_a):
        await ctx.send(embed=em_p_f_aorist_a)
      if (em_p_n_aorist_a):
        await ctx.send(embed=em_p_n_aorist_a)
      if (em_p_m_aorist_m):
        await ctx.send(embed=em_p_m_aorist_m)
      if (em_p_f_aorist_m):
        await ctx.send(embed=em_p_f_aorist_m)
      if (em_p_n_aorist_m):
        await ctx.send(embed=em_p_n_aorist_m)
      if (em_p_m_aorist_p):
        await ctx.send(embed=em_p_m_aorist_p)
      if (em_p_f_aorist_p):
        await ctx.send(embed=em_p_f_aorist_p)
      if (em_p_n_aorist_p):
        await ctx.send(embed=em_p_n_aorist_p)

    elif arg.lower() == 'participle_perfect':
      em_p_m_perfect_a = declinator(data["perfect"]["participle"]["active"]["masculine"], "Perfect Participle Active Masculine")
      em_p_f_perfect_a = declinator(data["perfect"]["participle"]["active"]["feminine"], "Perfect Participle Active Feminine")
      em_p_n_perfect_a = declinator(data["perfect"]["participle"]["active"]["neuter"], "Perfect Participle Active Neuter")
      em_p_m_perfect_m = declinator(data["perfect"]["participle"]["middle"]["masculine"], "Perfect Participle Middle Masculine")
      em_p_f_perfect_m = declinator(data["perfect"]["participle"]["middle"]["feminine"], "Perfect Participle Middle Feminine")
      em_p_n_perfect_m = declinator(data["perfect"]["participle"]["middle"]["neuter"], "Perfect Participle Middle Neuter")
      em_p_m_perfect_p = declinator(data["perfect"]["participle"]["passive"]["masculine"], "Perfect Participle Passive Masculine")
      em_p_f_perfect_p = declinator(data["perfect"]["participle"]["passive"]["feminine"], "Perfect Participle Passive Feminine")
      em_p_n_perfect_p = declinator(data["perfect"]["participle"]["passive"]["neuter"], "Perfect Participle Passive Neuter")
      if (em_p_m_perfect_a):
        await ctx.send(embed=em_p_m_perfect_a)
      if (em_p_f_perfect_a):
        await ctx.send(embed=em_p_f_perfect_a)
      if (em_p_n_perfect_a):
        await ctx.send(embed=em_p_n_perfect_a)
      if (em_p_m_perfect_m):
        await ctx.send(embed=em_p_m_perfect_m)
      if (em_p_f_perfect_m):
        await ctx.send(embed=em_p_f_perfect_m)
      if (em_p_n_perfect_m):
        await ctx.send(embed=em_p_n_perfect_m)
      if (em_p_m_perfect_p):
        await ctx.send(embed=em_p_m_perfect_p)
      if (em_p_f_perfect_p):
        await ctx.send(embed=em_p_f_perfect_p)
      if (em_p_n_perfect_p):
        await ctx.send(embed=em_p_n_perfect_p)

@bot.command(name='contracted_omikron')
async def contracted_omikron(ctx):
  with open ("paradigms/verbs/regulars/contracteds/omikron.json", "r", encoding='utf8') as f:
    data = json.load(f)

    present = data["present"]
    present_indicative = present["indicative"]
    present_imperative = present["imperative"]

    present_indicative_active = present_indicative["active"]
    present_indicative_middle = present_indicative["middle"]

    present_imperative_active = present_imperative["active"]
    present_imperative_middle = present_imperative["middle"]

    present_indicative_active_1s = present_indicative_active["singular"]["first"]
    present_indicative_active_2s = present_indicative_active["singular"]["second"]
    present_indicative_active_3s = present_indicative_active["singular"]["third"]
    present_indicative_active_1p = present_indicative_active["plural"]["first"]
    present_indicative_active_2p = present_indicative_active["plural"]["second"]
    present_indicative_active_3p = present_indicative_active["plural"]["third"]

    present_indicative_middle_1s = present_indicative_middle["singular"]["first"]
    present_indicative_middle_2s = present_indicative_middle["singular"]["second"]
    present_indicative_middle_3s = present_indicative_middle["singular"]["third"]
    present_indicative_middle_1p = present_indicative_middle["plural"]["first"]
    present_indicative_middle_2p = present_indicative_middle["plural"]["second"]
    present_indicative_middle_3p = present_indicative_middle["plural"]["third"]
    
    present_imperative_active_2s = present_imperative_active["singular"]["second"]
    present_imperative_active_2p = present_imperative_active["plural"]["second"]

    present_imperative_middle_2s = present_imperative_middle["singular"]["second"]
    present_imperative_middle_2p = present_imperative_middle["plural"]["second"]

    em = discord.Embed(title="Contracted conjugation -όω (δηλῶ/δηλοῦμαι)", color=discord.Color.blue())
    em.add_field(name="Present Indicative Active", value=f"1.s.: {present_indicative_active_1s}\n2.s.: {present_indicative_active_2s}\n3.s.: {present_indicative_active_3s}\n1.p.: {present_indicative_active_1p}\n2.p.: {present_indicative_active_2p}\n3.p.: {present_indicative_active_3p}")
    em.add_field(name="Present Indicative Middle", value=f"1.s.: {present_indicative_middle_1s}\n2.s.: {present_indicative_middle_2s}\n3.s.: {present_indicative_middle_3s}\n1.p.: {present_indicative_middle_1p}\n2.p.: {present_indicative_middle_2p}\n3.p.: {present_indicative_middle_3p}")
    em.add_field(name="Present Imperative Active", value=f"2.s.: {present_imperative_active_2s}\n2.p.: {present_imperative_active_2p}")
    em.add_field(name="Present Imperative Middle", value=f"2.s.: {present_imperative_middle_2s}\n2.p.: {present_imperative_middle_2p}")
    await ctx.send(embed=em)

@bot.command(name='irregular_verbs')
async def irregular_verbs(ctx):
  em = discord.Embed(title="You can look up irregular verbs conjugations.", color = discord.Color.blue())
  em.add_field(name="Try these:", value=".eimi")
  await ctx.send(embed=em)

@bot.command(name='eimi')
async def eimi(ctx):
  with open ("paradigms/verbs/irregulars/eimi.json", "r", encoding='utf8') as f:
    data = json.load(f)

    em_present = conjugator_present(data, "Present")
    em_imperfect = conjugator_imperfect(data, "Imperfect")
    em_future = conjugator_future(data, "Future")
    em_aorist = conjugator_aorist(data, "Aorist")
    em_perfect = conjugator_perfect(data, "Perfect")
    em_pluperfect = conjugator_pluperfect(data, "Pluperfect")

    em_p_m_present_a = declinator(data["present"]["participle"]["active"]["masculine"], "Present Participle Active Masculine")
    em_p_f_present_a = declinator(data["present"]["participle"]["active"]["feminine"], "Present Participle Active Feminine")
    em_p_n_present_a = declinator(data["present"]["participle"]["active"]["neuter"], "Present Participle Active Neuter")

    em_p_m_future_m = declinator(data["future"]["participle"]["middle"]["masculine"], "Future Participle Middle Masculine")
    em_p_f_future_m = declinator(data["future"]["participle"]["middle"]["feminine"], "Future Participle Middle Feminine")
    em_p_n_future_m = declinator(data["future"]["participle"]["middle"]["neuter"], "Future Participle Middle Neuter")

    if (em_present):
      await ctx.send(embed=em_present)
    if (em_imperfect):
      await ctx.send(embed=em_imperfect)
    if (em_future):
      await ctx.send(embed=em_future)
    if (em_aorist):
      await ctx.send(embed=em_aorist)
    if (em_perfect):
      await ctx.send(embed=em_perfect)
    if (em_pluperfect):
      await ctx.send(embed=em_pluperfect)
    if (em_p_m_present_a):
      await ctx.send(embed=em_p_m_present_a)
    if (em_p_f_present_a):
      await ctx.send(embed=em_p_f_present_a)
    if (em_p_n_present_a):
      await ctx.send(embed=em_p_n_present_a)
    if (em_p_m_future_m):
      await ctx.send(embed=em_p_m_future_m)
    if (em_p_f_future_m):
      await ctx.send(embed=em_p_f_future_m)
    if (em_p_n_future_m):
      await ctx.send(embed=em_p_n_future_m)

bot.run(TOKEN)