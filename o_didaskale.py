# bot.py
import os
import json
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
  print("Ready!")

@bot.command(name='info')
async def info(ctx):
  em = discord.Embed(title = "Χαῖρε! I'm a bot that seeks to help ancient greek students.", color = discord.Color.blue())
  em.add_field(name="You can look up declension paradigms, verb paradigms, articles, pronouns, adjectives, etc.\nTry these:", value="!articles\n!pronouns\n!nouns\n!adjectives\n!verbs")
  await ctx.send(embed=em)

@bot.command(name='pronouns')
async def pronouns(ctx):
  em = discord.Embed(title = "You can look up all sorts of pronouns.", color = discord.Color.blue())
  em.add_field(name="Try these:", value="!ego\n!sy")
  await ctx.send(embed=em)

@bot.command(name='nouns')
async def nouns(ctx):
  em = discord.Embed(title = "You can look up declension paradigms according to Learning Greek division.", color = discord.Color.blue())
  em.add_field(name="Try these:", value="!1a\n!1b\n!1c\n!1d1\n!1d2\n!2a\n!2b\n!3a1\n!3a2\n!3b\n!3c\n!3d1\n!3d2\n!3e1\n!3e2\n!3f\n!3g\n!irregular_nouns")
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
  em.add_field(name="Try these:", value="!non_contracted\n!contracteds\n!irregular_verbs")
  await ctx.send(embed=em)

@bot.command(name='contracteds')
async def contracteds(ctx):
  em = discord.Embed(title = "You can look up contracted conjugation paradigms.", color = discord.Color.blue())
  em.add_field(name="Try these:", value="!contracted_alpha\n!contracted_epsilon\n!contracted_omikron")
  await ctx.send(embed=em)

@bot.command(name='non_contracted')
async def non_contracted(ctx):
  with open ("paradigms/verbs/regulars/non_contracteds/omega.json", "r", encoding='utf8') as f:
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

    em = discord.Embed(title="Non-contracted conjugation -ω (παύω/παύομαι)", color=discord.Color.blue())
    em.add_field(name="Present Indicative Active", value=f"1.s.: {present_indicative_active_1s}\n2.s.: {present_indicative_active_2s}\n3.s.: {present_indicative_active_3s}\n1.p.: {present_indicative_active_1p}\n2.p.: {present_indicative_active_2p}\n3.p.: {present_indicative_active_3p}")
    em.add_field(name="Present Indicative Middle", value=f"1.s.: {present_indicative_middle_1s}\n2.s.: {present_indicative_middle_2s}\n3.s.: {present_indicative_middle_3s}\n1.p.: {present_indicative_middle_1p}\n2.p.: {present_indicative_middle_2p}\n3.p.: {present_indicative_middle_3p}")
    em.add_field(name="Present Imperative Active", value=f"2.s.: {present_imperative_active_2s}\n2.p.: {present_imperative_active_2p}")
    em.add_field(name="Present Imperative Middle", value=f"2.s.: {present_imperative_middle_2s}\n2.p.: {present_imperative_middle_2p}")
    await ctx.send(embed=em)

@bot.command(name='contracted_alpha')
async def contracted_alpha(ctx):
  with open ("paradigms/verbs/regulars/contracteds/alpha.json", "r", encoding='utf8') as f:
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

    em = discord.Embed(title="Contracted conjugation -άω (ὁρῶ/ὁρῶμαι)", color=discord.Color.blue())
    em.add_field(name="Present Indicative Active", value=f"1.s.: {present_indicative_active_1s}\n2.s.: {present_indicative_active_2s}\n3.s.: {present_indicative_active_3s}\n1.p.: {present_indicative_active_1p}\n2.p.: {present_indicative_active_2p}\n3.p.: {present_indicative_active_3p}")
    em.add_field(name="Present Indicative Middle", value=f"1.s.: {present_indicative_middle_1s}\n2.s.: {present_indicative_middle_2s}\n3.s.: {present_indicative_middle_3s}\n1.p.: {present_indicative_middle_1p}\n2.p.: {present_indicative_middle_2p}\n3.p.: {present_indicative_middle_3p}")
    em.add_field(name="Present Imperative Active", value=f"2.s.: {present_imperative_active_2s}\n2.p.: {present_imperative_active_2p}")
    em.add_field(name="Present Imperative Middle", value=f"2.s.: {present_imperative_middle_2s}\n2.p.: {present_imperative_middle_2p}")
    await ctx.send(embed=em)

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

@bot.command(name='1a')
async def first_1a(ctx):

  with open ("paradigms/nouns/first_declension/1a.json", "r", encoding='utf8') as f:
    data = json.load(f)

    singular = data["singular"]
    plural = data["plural"]

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

    em = discord.Embed(title = "Nouns in Pure η (1a)", color = discord.Color.blue())
    em.add_field(name = "Singular", value = f"Nominative: {singular_nominative} \n Genitive: {singular_genitive} \n Dative: {singular_dative} \n Accusative: {singular_accusative} \n Vocative: {singular_vocative}")
    em.add_field(name = "Plural", value = f"Nominative: {plural_nominative} \n Genitive: {plural_genitive} \n Dative: {plural_dative} \n Accusative: {plural_accusative} \n Vocative: {plural_vocative}")
    await ctx.send(embed = em)

@bot.command(name='1b')
async def first_1b(ctx):

  with open ("paradigms/nouns/first_declension/1b.json", "r", encoding='utf8') as f:
    data = json.load(f)

    singular = data["singular"]
    plural = data["plural"]

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

    em = discord.Embed(title = "Nouns in Pure α (1b)", color = discord.Color.blue())
    em.add_field(name = "Singular", value = f"Nominative: {singular_nominative} \n Genitive: {singular_genitive} \n Dative: {singular_dative} \n Accusative: {singular_accusative} \n Vocative: {singular_vocative}")
    em.add_field(name = "Plural", value = f"Nominative: {plural_nominative} \n Genitive: {plural_genitive} \n Dative: {plural_dative} \n Accusative: {plural_accusative} \n Vocative: {plural_vocative}")
    await ctx.send(embed = em)

@bot.command(name='1c')
async def first_1c(ctx):

  with open ("paradigms/nouns/first_declension/1c.json", "r", encoding='utf8') as f:
    data = json.load(f)

    singular = data["singular"]
    plural = data["plural"]

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

    em = discord.Embed(title = "Nouns in Impure α (1c)", color = discord.Color.blue())
    em.add_field(name = "Singular", value = f"Nominative: {singular_nominative} \n Genitive: {singular_genitive} \n Dative: {singular_dative} \n Accusative: {singular_accusative} \n Vocative: {singular_vocative}")
    em.add_field(name = "Plural", value = f"Nominative: {plural_nominative} \n Genitive: {plural_genitive} \n Dative: {plural_dative} \n Accusative: {plural_accusative} \n Vocative: {plural_vocative}")
    await ctx.send(embed = em)

@bot.command(name='1d1')
async def first_1d1(ctx):

  with open ("paradigms/nouns/first_declension/1d1.json", "r", encoding='utf8') as f:
    data = json.load(f)

    singular = data["singular"]
    plural = data["plural"]

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

    em = discord.Embed(title = "Masculine nouns -ης (1d1)", color = discord.Color.blue())
    em.add_field(name = "Singular", value = f"Nominative: {singular_nominative} \n Genitive: {singular_genitive} \n Dative: {singular_dative} \n Accusative: {singular_accusative} \n Vocative: {singular_vocative}")
    em.add_field(name = "Plural", value = f"Nominative: {plural_nominative} \n Genitive: {plural_genitive} \n Dative: {plural_dative} \n Accusative: {plural_accusative} \n Vocative: {plural_vocative}")
    await ctx.send(embed = em)

@bot.command(name='1d2')
async def first_1d2(ctx):

  with open ("paradigms/nouns/first_declension/1d2.json", "r", encoding='utf8') as f:
    data = json.load(f)

    singular = data["singular"]
    plural = data["plural"]

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

    em = discord.Embed(title = "Masculine nouns -ας (1d2)", color = discord.Color.blue())
    em.add_field(name = "Singular", value = f"Nominative: {singular_nominative} \n Genitive: {singular_genitive} \n Dative: {singular_dative} \n Accusative: {singular_accusative} \n Vocative: {singular_vocative}")
    em.add_field(name = "Plural", value = f"Nominative: {plural_nominative} \n Genitive: {plural_genitive} \n Dative: {plural_dative} \n Accusative: {plural_accusative} \n Vocative: {plural_vocative}")
    await ctx.send(embed = em)

@bot.command(name='2a')
async def second_2a(ctx):

  with open ("paradigms/nouns/second_declension/2a.json", "r", encoding='utf8') as f:
    data = json.load(f)

    singular = data["singular"]
    plural = data["plural"]

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

    em = discord.Embed(title = "Masculine and Feminine nouns (2a)", color = discord.Color.blue())
    em.add_field(name = "Singular", value = f"Nominative: {singular_nominative} \n Genitive: {singular_genitive} \n Dative: {singular_dative} \n Accusative: {singular_accusative} \n Vocative: {singular_vocative}")
    em.add_field(name = "Plural", value = f"Nominative: {plural_nominative} \n Genitive: {plural_genitive} \n Dative: {plural_dative} \n Accusative: {plural_accusative} \n Vocative: {plural_vocative}")
    await ctx.send(embed = em)

@bot.command(name='2b')
async def second_2b(ctx):

  with open ("paradigms/nouns/second_declension/2b.json", "r", encoding='utf8') as f:
    data = json.load(f)

    singular = data["singular"]
    plural = data["plural"]

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

    em = discord.Embed(title = "Neuter nouns (2b)", color = discord.Color.blue())
    em.add_field(name = "Singular", value = f"Nominative: {singular_nominative} \n Genitive: {singular_genitive} \n Dative: {singular_dative} \n Accusative: {singular_accusative} \n Vocative: {singular_vocative}")
    em.add_field(name = "Plural", value = f"Nominative: {plural_nominative} \n Genitive: {plural_genitive} \n Dative: {plural_dative} \n Accusative: {plural_accusative} \n Vocative: {plural_vocative}")
    await ctx.send(embed = em)

@bot.command(name='3a1')
async def third_3a1(ctx):

  with open ("paradigms/nouns/third_declension/3a1.json", "r", encoding='utf8') as f:
    data = json.load(f)

    singular = data["singular"]
    plural = data["plural"]

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

    em = discord.Embed(title = "3a1", color = discord.Color.blue())
    em.add_field(name = "Singular", value = f"Nominative: {singular_nominative} \n Genitive: {singular_genitive} \n Dative: {singular_dative} \n Accusative: {singular_accusative} \n Vocative: {singular_vocative}")
    em.add_field(name = "Plural", value = f"Nominative: {plural_nominative} \n Genitive: {plural_genitive} \n Dative: {plural_dative} \n Accusative: {plural_accusative} \n Vocative: {plural_vocative}")
    await ctx.send(embed = em)

@bot.command(name='3a2')
async def third_3a2(ctx):

  with open ("paradigms/nouns/third_declension/3a2.json", "r", encoding='utf8') as f:
    data = json.load(f)

    singular = data["singular"]
    plural = data["plural"]

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

    em = discord.Embed(title = "3a2", color = discord.Color.blue())
    em.add_field(name = "Singular", value = f"Nominative: {singular_nominative} \n Genitive: {singular_genitive} \n Dative: {singular_dative} \n Accusative: {singular_accusative} \n Vocative: {singular_vocative}")
    em.add_field(name = "Plural", value = f"Nominative: {plural_nominative} \n Genitive: {plural_genitive} \n Dative: {plural_dative} \n Accusative: {plural_accusative} \n Vocative: {plural_vocative}")
    await ctx.send(embed = em)

@bot.command(name='3b')
async def third_3b(ctx):

  with open ("paradigms/nouns/third_declension/3b.json", "r", encoding='utf8') as f:
    data = json.load(f)

    singular = data["singular"]
    plural = data["plural"]

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

    em = discord.Embed(title = "3b", color = discord.Color.blue())
    em.add_field(name = "Singular", value = f"Nominative: {singular_nominative} \n Genitive: {singular_genitive} \n Dative: {singular_dative} \n Accusative: {singular_accusative} \n Vocative: {singular_vocative}")
    em.add_field(name = "Plural", value = f"Nominative: {plural_nominative} \n Genitive: {plural_genitive} \n Dative: {plural_dative} \n Accusative: {plural_accusative} \n Vocative: {plural_vocative}")
    await ctx.send(embed = em)

@bot.command(name='3c')
async def third_3c(ctx):

  with open ("paradigms/nouns/third_declension/3c.json", "r", encoding='utf8') as f:
    data = json.load(f)

    singular = data["singular"]
    plural = data["plural"]

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

    em = discord.Embed(title = "3c", color = discord.Color.blue())
    em.add_field(name = "Singular", value = f"Nominative: {singular_nominative} \n Genitive: {singular_genitive} \n Dative: {singular_dative} \n Accusative: {singular_accusative} \n Vocative: {singular_vocative}")
    em.add_field(name = "Plural", value = f"Nominative: {plural_nominative} \n Genitive: {plural_genitive} \n Dative: {plural_dative} \n Accusative: {plural_accusative} \n Vocative: {plural_vocative}")
    await ctx.send(embed = em)

@bot.command(name='3d1')
async def third_3d1(ctx):

  with open ("paradigms/nouns/third_declension/3d1.json", "r", encoding='utf8') as f:
    data = json.load(f)

    singular = data["singular"]
    plural = data["plural"]

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

    em = discord.Embed(title = "3d1", color = discord.Color.blue())
    em.add_field(name = "Singular", value = f"Nominative: {singular_nominative} \n Genitive: {singular_genitive} \n Dative: {singular_dative} \n Accusative: {singular_accusative} \n Vocative: {singular_vocative}")
    em.add_field(name = "Plural", value = f"Nominative: {plural_nominative} \n Genitive: {plural_genitive} \n Dative: {plural_dative} \n Accusative: {plural_accusative} \n Vocative: {plural_vocative}")
    await ctx.send(embed = em)

@bot.command(name='3d2')
async def third_3d2(ctx):

  with open ("paradigms/nouns/third_declension/3d2.json", "r", encoding='utf8') as f:
    data = json.load(f)

    singular = data["singular"]

    singular_nominative = singular["nominative"]
    singular_genitive = singular["genitive"]
    singular_dative = singular["dative"]
    singular_accusative = singular["accusative"]
    singular_vocative = singular["vocative"]

    em = discord.Embed(title = "3d2", color = discord.Color.blue())
    em.add_field(name = "Singular", value = f"Nominative: {singular_nominative} \n Genitive: {singular_genitive} \n Dative: {singular_dative} \n Accusative: {singular_accusative} \n Vocative: {singular_vocative}")
    await ctx.send(embed = em)

@bot.command(name='3e1')
async def third_3e1(ctx):

  with open ("paradigms/nouns/third_declension/3e1.json", "r", encoding='utf8') as f:
    data = json.load(f)

    singular = data["singular"]
    plural = data["plural"]

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

    em = discord.Embed(title = "3e1", color = discord.Color.blue())
    em.add_field(name = "Singular", value = f"Nominative: {singular_nominative} \n Genitive: {singular_genitive} \n Dative: {singular_dative} \n Accusative: {singular_accusative} \n Vocative: {singular_vocative}")
    em.add_field(name = "Plural", value = f"Nominative: {plural_nominative} \n Genitive: {plural_genitive} \n Dative: {plural_dative} \n Accusative: {plural_accusative} \n Vocative: {plural_vocative}")
    await ctx.send(embed = em)

@bot.command(name='3e2')
async def third_3e2(ctx):

  with open ("paradigms/nouns/third_declension/3e2.json", "r", encoding='utf8') as f:
    data = json.load(f)

    singular = data["singular"]
    plural = data["plural"]

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

    em = discord.Embed(title = "3e2", color = discord.Color.blue())
    em.add_field(name = "Singular", value = f"Nominative: {singular_nominative} \n Genitive: {singular_genitive} \n Dative: {singular_dative} \n Accusative: {singular_accusative} \n Vocative: {singular_vocative}")
    em.add_field(name = "Plural", value = f"Nominative: {plural_nominative} \n Genitive: {plural_genitive} \n Dative: {plural_dative} \n Accusative: {plural_accusative} \n Vocative: {plural_vocative}")
    await ctx.send(embed = em)

@bot.command(name='3f')
async def third_3f(ctx):

  with open ("paradigms/nouns/third_declension/3f.json", "r", encoding='utf8') as f:
    data = json.load(f)

    singular = data["singular"]
    plural = data["plural"]

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

    em = discord.Embed(title = "3f", color = discord.Color.blue())
    em.add_field(name = "Singular", value = f"Nominative: {singular_nominative} \n Genitive: {singular_genitive} \n Dative: {singular_dative} \n Accusative: {singular_accusative} \n Vocative: {singular_vocative}")
    em.add_field(name = "Plural", value = f"Nominative: {plural_nominative} \n Genitive: {plural_genitive} \n Dative: {plural_dative} \n Accusative: {plural_accusative} \n Vocative: {plural_vocative}")
    await ctx.send(embed = em)

@bot.command(name='3g')
async def third_3g(ctx):

  with open ("paradigms/nouns/third_declension/3g.json", "r", encoding='utf8') as f:
    data = json.load(f)

    singular = data["singular"]
    plural = data["plural"]

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

    em = discord.Embed(title = "3g", color = discord.Color.blue())
    em.add_field(name = "Singular", value = f"Nominative: {singular_nominative} \n Genitive: {singular_genitive} \n Dative: {singular_dative} \n Accusative: {singular_accusative} \n Vocative: {singular_vocative}")
    em.add_field(name = "Plural", value = f"Nominative: {plural_nominative} \n Genitive: {plural_genitive} \n Dative: {plural_dative} \n Accusative: {plural_accusative} \n Vocative: {plural_vocative}")
    await ctx.send(embed = em)

@bot.command(name='zeus')
async def zeus(ctx):

  with open ("paradigms/nouns/irregulars/zeus.json", "r", encoding='utf8') as f:
    data = json.load(f)

    singular = data["singular"]

    singular_nominative = singular["nominative"]
    singular_genitive = singular["genitive"]
    singular_dative = singular["dative"]
    singular_accusative = singular["accusative"]
    singular_vocative = singular["vocative"]

    em = discord.Embed(title = "Ζεύς", color = discord.Color.blue())
    em.add_field(name = "Singular", value = f"Nominative: {singular_nominative} \n Genitive: {singular_genitive} \n Dative: {singular_dative} \n Accusative: {singular_accusative} \n Vocative: {singular_vocative}")
    await ctx.send(embed = em)

@bot.command(name='naus')
async def naus(ctx):

  with open ("paradigms/nouns/irregulars/naus.json", "r", encoding='utf8') as f:
    data = json.load(f)

    singular = data["singular"]
    plural = data["plural"]

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

    em = discord.Embed(title = "ναῦς", color = discord.Color.blue())
    em.add_field(name = "Singular", value = f"Nominative: {singular_nominative} \n Genitive: {singular_genitive} \n Dative: {singular_dative} \n Accusative: {singular_accusative} \n Vocative: {singular_vocative}")
    em.add_field(name = "Plural", value = f"Nominative: {plural_nominative} \n Genitive: {plural_genitive} \n Dative: {plural_dative} \n Accusative: {plural_accusative} \n Vocative: {plural_vocative}")
    await ctx.send(embed = em)

@bot.command(name='graus')
async def graus(ctx):

  with open ("paradigms/nouns/irregulars/graus.json", "r", encoding='utf8') as f:
    data = json.load(f)

    singular = data["singular"]
    plural = data["plural"]

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

    em = discord.Embed(title = "γραῦς", color = discord.Color.blue())
    em.add_field(name = "Singular", value = f"Nominative: {singular_nominative} \n Genitive: {singular_genitive} \n Dative: {singular_dative} \n Accusative: {singular_accusative} \n Vocative: {singular_vocative}")
    em.add_field(name = "Plural", value = f"Nominative: {plural_nominative} \n Genitive: {plural_genitive} \n Dative: {plural_dative} \n Accusative: {plural_accusative} \n Vocative: {plural_vocative}")
    await ctx.send(embed = em)

@bot.command(name='masculine')
async def masculine(ctx):

  with open ("paradigms/articles/masculine.json", "r", encoding='utf8') as f:
    data = json.load(f)

    singular = data["singular"]
    plural = data["plural"]

    singular_nominative = singular["nominative"]
    singular_genitive = singular["genitive"]
    singular_dative = singular["dative"]
    singular_accusative = singular["accusative"]

    plural_nominative = plural["nominative"]
    plural_genitive = plural["genitive"]
    plural_dative = plural["dative"]
    plural_accusative = plural["accusative"]

    em = discord.Embed(title = "Masculine Article", color = discord.Color.blue())
    em.add_field(name = "Singular", value = f"Nominative: {singular_nominative} \n Genitive: {singular_genitive} \n Dative: {singular_dative} \n Accusative: {singular_accusative}")
    em.add_field(name = "Plural", value = f"Nominative: {plural_nominative} \n Genitive: {plural_genitive} \n Dative: {plural_dative} \n Accusative: {plural_accusative}")
    await ctx.send(embed = em)

@bot.command(name='feminine')
async def feminine(ctx):

  with open ("paradigms/articles/feminine.json", "r", encoding='utf8') as f:
    data = json.load(f)

    singular = data["singular"]
    plural = data["plural"]

    singular_nominative = singular["nominative"]
    singular_genitive = singular["genitive"]
    singular_dative = singular["dative"]
    singular_accusative = singular["accusative"]

    plural_nominative = plural["nominative"]
    plural_genitive = plural["genitive"]
    plural_dative = plural["dative"]
    plural_accusative = plural["accusative"]

    em = discord.Embed(title = "Feminine Article", color = discord.Color.blue())
    em.add_field(name = "Singular", value = f"Nominative: {singular_nominative} \n Genitive: {singular_genitive} \n Dative: {singular_dative} \n Accusative: {singular_accusative}")
    em.add_field(name = "Plural", value = f"Nominative: {plural_nominative} \n Genitive: {plural_genitive} \n Dative: {plural_dative} \n Accusative: {plural_accusative}")
    await ctx.send(embed = em)

@bot.command(name='neuter')
async def neuter(ctx):

  with open ("paradigms/articles/neuter.json", "r", encoding='utf8') as f:
    data = json.load(f)

    singular = data["singular"]
    plural = data["plural"]

    singular_nominative = singular["nominative"]
    singular_genitive = singular["genitive"]
    singular_dative = singular["dative"]
    singular_accusative = singular["accusative"]

    plural_nominative = plural["nominative"]
    plural_genitive = plural["genitive"]
    plural_dative = plural["dative"]
    plural_accusative = plural["accusative"]

    em = discord.Embed(title = "Neuter Article", color = discord.Color.blue())
    em.add_field(name = "Singular", value = f"Nominative: {singular_nominative} \n Genitive: {singular_genitive} \n Dative: {singular_dative} \n Accusative: {singular_accusative}")
    em.add_field(name = "Plural", value = f"Nominative: {plural_nominative} \n Genitive: {plural_genitive} \n Dative: {plural_dative} \n Accusative: {plural_accusative}")
    await ctx.send(embed = em)

@bot.command(name='os_e_on')
async def os_e_on(ctx):

  with open ("paradigms/adjectives/os_e_on.json", "r", encoding='utf8') as f:
    data = json.load(f)

    singular = data["singular"]
    plural = data["plural"]

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

    em = discord.Embed(title = "Three-form adjectives -ος/-η/-ον", color = discord.Color.blue())
    em.add_field(name = "Singular", value = f"Nominative: {singular_nominative} \n Genitive: {singular_genitive} \n Dative: {singular_dative} \n Accusative: {singular_accusative} \n Vocative: {singular_vocative}")
    em.add_field(name = "Plural", value = f"Nominative: {plural_nominative} \n Genitive: {plural_genitive} \n Dative: {plural_dative} \n Accusative: {plural_accusative} \n Vocative: {plural_vocative}")
    await ctx.send(embed = em)

@bot.command(name='os_a_on')
async def os_a_on(ctx):

  with open ("paradigms/adjectives/os_a_on.json", "r", encoding='utf8') as f:
    data = json.load(f)

    singular = data["singular"]
    plural = data["plural"]

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

    em = discord.Embed(title = "Three-form adjectives -ος/-α/-ον", color = discord.Color.blue())
    em.add_field(name = "Singular", value = f"Nominative: {singular_nominative} \n Genitive: {singular_genitive} \n Dative: {singular_dative} \n Accusative: {singular_accusative} \n Vocative: {singular_vocative}")
    em.add_field(name = "Plural", value = f"Nominative: {plural_nominative} \n Genitive: {plural_genitive} \n Dative: {plural_dative} \n Accusative: {plural_accusative} \n Vocative: {plural_vocative}")
    await ctx.send(embed = em)

@bot.command(name='on_on')
async def on_on(ctx):

  with open ("paradigms/adjectives/on_on.json", "r", encoding='utf8') as f:
    data = json.load(f)

    singular = data["singular"]
    plural = data["plural"]

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

    em = discord.Embed(title = "Two-form adjectives -ων/-ον", color = discord.Color.blue())
    em.add_field(name = "Singular", value = f"Nominative: {singular_nominative} \n Genitive: {singular_genitive} \n Dative: {singular_dative} \n Accusative: {singular_accusative} \n Vocative: {singular_vocative}")
    em.add_field(name = "Plural", value = f"Nominative: {plural_nominative} \n Genitive: {plural_genitive} \n Dative: {plural_dative} \n Accusative: {plural_accusative} \n Vocative: {plural_vocative}")
    await ctx.send(embed = em)

@bot.command(name='es_es')
async def es_es(ctx):

  with open ("paradigms/adjectives/es_es.json", "r", encoding='utf8') as f:
    data = json.load(f)

    singular = data["singular"]
    plural = data["plural"]

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

    em = discord.Embed(title = "Two-form adjectives -ης/-ες", color = discord.Color.blue())
    em.add_field(name = "Singular", value = f"Nominative: {singular_nominative} \n Genitive: {singular_genitive} \n Dative: {singular_dative} \n Accusative: {singular_accusative} \n Vocative: {singular_vocative}")
    em.add_field(name = "Plural", value = f"Nominative: {plural_nominative} \n Genitive: {plural_genitive} \n Dative: {plural_dative} \n Accusative: {plural_accusative} \n Vocative: {plural_vocative}")
    await ctx.send(embed = em)

@bot.command(name='ego')
async def ego(ctx):

  with open ("paradigms/pronouns/ego.json", "r", encoding='utf8') as f:
    data = json.load(f)

    singular = data["singular"]
    plural = data["plural"]

    singular_nominative = singular["nominative"]
    singular_genitive = singular["genitive"]
    singular_dative = singular["dative"]
    singular_accusative = singular["accusative"]

    plural_nominative = plural["nominative"]
    plural_genitive = plural["genitive"]
    plural_dative = plural["dative"]
    plural_accusative = plural["accusative"]

    em = discord.Embed(title = "First person (ἐγώ)", color = discord.Color.blue())
    em.add_field(name = "Singular", value = f"Nominative: {singular_nominative} \n Genitive: {singular_genitive} \n Dative: {singular_dative} \n Accusative: {singular_accusative}")
    em.add_field(name = "Plural", value = f"Nominative: {plural_nominative} \n Genitive: {plural_genitive} \n Dative: {plural_dative} \n Accusative: {plural_accusative}")
    await ctx.send(embed = em)

@bot.command(name='sy')
async def sy(ctx):

  with open ("paradigms/pronouns/sy.json", "r", encoding='utf8') as f:
    data = json.load(f)

    singular = data["singular"]
    plural = data["plural"]

    singular_nominative = singular["nominative"]
    singular_genitive = singular["genitive"]
    singular_dative = singular["dative"]
    singular_accusative = singular["accusative"]

    plural_nominative = plural["nominative"]
    plural_genitive = plural["genitive"]
    plural_dative = plural["dative"]
    plural_accusative = plural["accusative"]

    em = discord.Embed(title = "Second person (σύ)", color = discord.Color.blue())
    em.add_field(name = "Singular", value = f"Nominative: {singular_nominative} \n Genitive: {singular_genitive} \n Dative: {singular_dative} \n Accusative: {singular_accusative}")
    em.add_field(name = "Plural", value = f"Nominative: {plural_nominative} \n Genitive: {plural_genitive} \n Dative: {plural_dative} \n Accusative: {plural_accusative}")
    await ctx.send(embed = em)

bot.run(TOKEN)