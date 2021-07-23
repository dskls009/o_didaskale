# bot.py
import os
import json
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
  print("Ready!")

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
  em.add_field(name="You can look up declension paradigms, verb paradigms, articles, pronouns, adjectives, etc.\nTry these:", value="!articles\n!pronouns\n!nouns\n!adjectives\n!verbs")
  em.add_field(name="To look up words, type:", value="!search <class> <word>\n<class> would be noun, adjective, pronoun, verb, etc.\nReminder:\n-αυ/ευ/ου = -au/eu/ou\nη/ε = e\nω/ο = o\nυ = y\nγγ/γκ/γχ = ng/nk/nkh\nῥ = rh")
  await ctx.send(embed=em)

@bot.command(name='search')
async def search(ctx, arg1, arg2):
  with open (f"lexicon/{arg1.lower()}s/{arg2.lower()}.json", "r", encoding='utf8') as f:
    data = json.load(f)
    em = declinator(data, arg2.capitalize())
    await ctx.send(embed = em)

@bot.command(name='pronouns')
async def pronouns(ctx):
  em = discord.Embed(title = "You can look up all sorts of pronouns.", color = discord.Color.blue())
  em.add_field(name="Try these:", value="!ego\n!sy")
  await ctx.send(embed=em)

@bot.command(name='nouns')
async def nouns(ctx):
  em = discord.Embed(title = "You can look up declension paradigms according to Reading Greek division.", color = discord.Color.blue())
  em.add_field(name="Try these:", value="!1a\n!1b\n!1c\n!1d1\n!1d2\n!2a\n!2b\n!3a1\n!3a2\n!3b\n!3c\n!3d1\n!3d2\n!3e1\n!3e2\n!3f\n!3g\n!3h\n!irregular_nouns")
  await ctx.send(embed=em)

@bot.command(name='irregular_nouns')
async def irregular_nouns(ctx):
  em = discord.Embed(title="You can look up the irregular nouns declension.", color = discord.Color.blue())
  em.add_field(name="Try these:", value="!zeus\n!naus\n!graus")
  await ctx.send(embed=em)

@bot.command(name='articles')
async def articles(ctx):
  em = discord.Embed(title = "You can look up the articles declension.", color = discord.Color.blue())
  em.add_field(name="Try these:", value="!masculine\n!feminine\n!neuter")
  await ctx.send(embed=em)

@bot.command(name='adjectives')
async def adjectives(ctx):
  em = discord.Embed(title = "You can look up adjectives declension paradigms.", color = discord.Color.blue())
  em.add_field(name="Try these:", value="!os_a_on\n!os_e_on\n!on_on\n!es_es")
  await ctx.send(embed=em)

@bot.command(name='verbs')
async def verbs(ctx):
  em = discord.Embed(title = "You can look up verb paradigms.", color = discord.Color.blue())
  em.add_field(name="Try these:", value="!non_contracteds\n!contracteds\n!irregular_verbs")
  await ctx.send(embed=em)

@bot.command(name='contracteds')
async def contracteds(ctx):
  em = discord.Embed(title = "You can look up contracted conjugation paradigms.", color = discord.Color.blue())
  em.add_field(name="Try these:", value="!contracted_alpha tenses\n!contracted_alpha participle_present\n!contracted_alpha participle_future\n!contracted_alpha participle_aorist\n!contracted_alpha participle_perfect")
  await ctx.send(embed=em)
#\n!contracted_epsilon tenses/participle_present/participle_future/participle_aorist/participle_perfect\n!contracted_omikron tenses/participle_present/participle_future/participle_aorist/participle_perfect
@bot.command(name='non_contracteds')
async def non_contracteds(ctx):
  em = discord.Embed(title = "You can look up contracted conjugation paradigms.", color = discord.Color.blue())
  em.add_field(name="Try these:", value="!non_contracted tenses\n!non_contracted participle_present\n!non_contracted participle_future\n!non_contracted participle_aorist\n!non_contracted participle_perfect")
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
async def contracted_epsilon(ctx):
  with open ("paradigms/verbs/regulars/contracteds/epsilon.json", "r", encoding='utf8') as f:
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

    em = discord.Embed(title="Contracted conjugation -έω (ποιῶ/ποιοῦμαι)", color=discord.Color.blue())
    em.add_field(name="Present Indicative Active", value=f"1.s.: {present_indicative_active_1s}\n2.s.: {present_indicative_active_2s}\n3.s.: {present_indicative_active_3s}\n1.p.: {present_indicative_active_1p}\n2.p.: {present_indicative_active_2p}\n3.p.: {present_indicative_active_3p}")
    em.add_field(name="Present Indicative Middle", value=f"1.s.: {present_indicative_middle_1s}\n2.s.: {present_indicative_middle_2s}\n3.s.: {present_indicative_middle_3s}\n1.p.: {present_indicative_middle_1p}\n2.p.: {present_indicative_middle_2p}\n3.p.: {present_indicative_middle_3p}")
    em.add_field(name="Present Imperative Active", value=f"2.s.: {present_imperative_active_2s}\n2.p.: {present_imperative_active_2p}")
    em.add_field(name="Present Imperative Middle", value=f"2.s.: {present_imperative_middle_2s}\n2.p.: {present_imperative_middle_2p}")
    await ctx.send(embed=em)

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
  em.add_field(name="Try these:", value="!eimi")
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

@bot.command(name='1a')
async def first_1a(ctx):

  with open ("paradigms/nouns/first_declension/1a.json", "r", encoding='utf8') as f:
    data = json.load(f)
    em = declinator(data, "(1a)")
    await ctx.send(embed = em)

@bot.command(name='1b')
async def first_1b(ctx):

  with open ("paradigms/nouns/first_declension/1b.json", "r", encoding='utf8') as f:
    data = json.load(f)
    em = declinator(data, "(1b)")
    await ctx.send(embed = em)

@bot.command(name='1c')
async def first_1c(ctx):

  with open ("paradigms/nouns/first_declension/1c.json", "r", encoding='utf8') as f:
    data = json.load(f)
    em = declinator(data, "(1c)")
    await ctx.send(embed = em)

@bot.command(name='1d1')
async def first_1d1(ctx):

  with open ("paradigms/nouns/first_declension/1d1.json", "r", encoding='utf8') as f:
    data = json.load(f)
    em = declinator(data, "(1d.1)")
    await ctx.send(embed = em)

@bot.command(name='1d2')
async def first_1d2(ctx):

  with open ("paradigms/nouns/first_declension/1d2.json", "r", encoding='utf8') as f:
    data = json.load(f)
    em = declinator(data, "(1d.2)")
    await ctx.send(embed = em)

@bot.command(name='2a')
async def second_2a(ctx):

  with open ("paradigms/nouns/second_declension/2a.json", "r", encoding='utf8') as f:
    data = json.load(f)
    em = declinator(data, "(2a)")
    await ctx.send(embed = em)

@bot.command(name='2b')
async def second_2b(ctx):

  with open ("paradigms/nouns/second_declension/2b.json", "r", encoding='utf8') as f:
    data = json.load(f)
    em = declinator(data, "(2b)")
    await ctx.send(embed = em)

@bot.command(name='3a1')
async def third_3a1(ctx):

  with open ("paradigms/nouns/third_declension/3a1.json", "r", encoding='utf8') as f:
    data = json.load(f)
    em = declinator(data, "(3a.1)")
    await ctx.send(embed = em)

@bot.command(name='3a2')
async def third_3a2(ctx):

  with open ("paradigms/nouns/third_declension/3a2.json", "r", encoding='utf8') as f:
    data = json.load(f)
    em = declinator(data, "(3a.2)")
    await ctx.send(embed = em)

@bot.command(name='3b')
async def third_3b(ctx):

  with open ("paradigms/nouns/third_declension/3b.json", "r", encoding='utf8') as f:
    data = json.load(f)
    em = declinator(data, "(3b)")
    await ctx.send(embed = em)

@bot.command(name='3c')
async def third_3c(ctx):

  with open ("paradigms/nouns/third_declension/3c.json", "r", encoding='utf8') as f:
    data = json.load(f)
    em = declinator(data, "(3c)")
    await ctx.send(embed = em)

@bot.command(name='3d1')
async def third_3d1(ctx):

  with open ("paradigms/nouns/third_declension/3d1.json", "r", encoding='utf8') as f:
    data = json.load(f)
    em = declinator(data, "(3d.1)")
    await ctx.send(embed = em)

@bot.command(name='3d2')
async def third_3d2(ctx):

  with open ("paradigms/nouns/third_declension/3d2.json", "r", encoding='utf8') as f:
    data = json.load(f)
    em = declinator(data, "(3d.2)")
    await ctx.send(embed = em)

@bot.command(name='3e1')
async def third_3e1(ctx):

  with open ("paradigms/nouns/third_declension/3e1.json", "r", encoding='utf8') as f:
    data = json.load(f)
    em = declinator(data, "(3e.1)")
    await ctx.send(embed = em)

@bot.command(name='3e2')
async def third_3e2(ctx):

  with open ("paradigms/nouns/third_declension/3e2.json", "r", encoding='utf8') as f:
    data = json.load(f)
    em = declinator(data, "(3e.2)")
    await ctx.send(embed = em)

@bot.command(name='3f')
async def third_3f(ctx):

  with open ("paradigms/nouns/third_declension/3f.json", "r", encoding='utf8') as f:
    data = json.load(f)
    em = declinator(data, "(3f)")
    await ctx.send(embed = em)

@bot.command(name='3g')
async def third_3g(ctx):

  with open ("paradigms/nouns/third_declension/3g.json", "r", encoding='utf8') as f:
    data = json.load(f)
    em = declinator(data, "(3g)")
    await ctx.send(embed = em)

@bot.command(name='3h')
async def third_3h(ctx):

  with open ("paradigms/nouns/third_declension/3h.json", "r", encoding='utf8') as f:
    data = json.load(f)
    em = declinator(data, "(3h)")
    await ctx.send(embed = em)

@bot.command(name='zeus')
async def zeus(ctx):

  with open ("paradigms/nouns/irregulars/zeus.json", "r", encoding='utf8') as f:
    data = json.load(f)
    em = declinator(data, "Ζεύς")
    await ctx.send(embed = em)

@bot.command(name='naus')
async def naus(ctx):

  with open ("paradigms/nouns/irregulars/naus.json", "r", encoding='utf8') as f:
    data = json.load(f)
    em = declinator(data, "Ναῦς")
    await ctx.send(embed = em)

@bot.command(name='graus')
async def graus(ctx):

  with open ("paradigms/nouns/irregulars/graus.json", "r", encoding='utf8') as f:
    data = json.load(f)
    em = declinator(data, "Γραῦς")
    await ctx.send(embed = em)

@bot.command(name='masculine')
async def masculine(ctx):

  with open ("paradigms/articles/masculine.json", "r", encoding='utf8') as f:
    data = json.load(f)
    em = declinator(data, "Masculine Article")
    await ctx.send(embed = em)

@bot.command(name='feminine')
async def feminine(ctx):

  with open ("paradigms/articles/feminine.json", "r", encoding='utf8') as f:
    data = json.load(f)
    em = declinator(data, "Feminine Article")
    await ctx.send(embed = em)

@bot.command(name='neuter')
async def neuter(ctx):

  with open ("paradigms/articles/neuter.json", "r", encoding='utf8') as f:
    data = json.load(f)
    em = declinator(data, "Neuter Article")
    await ctx.send(embed = em)

@bot.command(name='os_e_on')
async def os_e_on(ctx):

  with open ("paradigms/adjectives/os_e_on.json", "r", encoding='utf8') as f:
    data = json.load(f)
    em = declinator(data, "Three-form Adjective -ος/-η/-ον")
    await ctx.send(embed = em)

@bot.command(name='os_a_on')
async def os_a_on(ctx):

  with open ("paradigms/adjectives/os_a_on.json", "r", encoding='utf8') as f:
    data = json.load(f)
    em = declinator(data, "Three-form Adjective -ος/-α/-ον")
    await ctx.send(embed = em)

@bot.command(name='on_on')
async def on_on(ctx):

  with open ("paradigms/adjectives/on_on.json", "r", encoding='utf8') as f:
    data = json.load(f)
    em = declinator(data, "Two-form Adjective -ων/-ον")
    await ctx.send(embed = em)

@bot.command(name='es_es')
async def es_es(ctx):

  with open ("paradigms/adjectives/es_es.json", "r", encoding='utf8') as f:
    data = json.load(f)
    em = declinator(data, "Two-form Adjective -ης/ες")
    await ctx.send(embed = em)

@bot.command(name='ego')
async def ego(ctx):

  with open ("paradigms/pronouns/ego.json", "r", encoding='utf8') as f:
    data = json.load(f)
    em = declinator(data, "First Person Pronoun")
    await ctx.send(embed = em)

@bot.command(name='sy')
async def sy(ctx):

  with open ("paradigms/pronouns/sy.json", "r", encoding='utf8') as f:
    data = json.load(f)
    em = declinator(data, "Second Person Pronoun")
    await ctx.send(embed = em)

bot.run(TOKEN)