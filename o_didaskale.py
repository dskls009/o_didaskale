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
  em.add_field(name="You can look up declension paradigms, verb paradigms, articles and adjectives.\nTry these:", value="!nouns\n!articles\n!adjectives\n!verbs")
  await ctx.send(embed=em)

@bot.command(name='nouns')
async def nouns(ctx):
    em = discord.Embed(title = "You can look up declension paradigms according to Learning Greek division.\nTry these:", value="!1a\n!1b\n!1c\n!1d1\n!1d2\n!2a\n!2b\n!3a1\n!3a2\n!3b\n!3c\n!3d1\n!3d2\n!3e1\n!3e2\n!3f\n!3g\n!irregular_nouns")
    await ctx.send(embed=em)

@bot.command(name='irregular_nouns')
async def irregular_nouns(ctx):
    em = discord.Embed(title="You can look up the irregular nouns declension.\nTry these:", value="!zeus\n!naus")
    await ctx.send(embed=em)

@bot.command(name='articles')
async def articles(ctx):
    em = discord.Embed(title = "You can look up the articles declension.\nTry these:", value="!masculine\n!feminine\n!neuter")
    await ctx.send(embed=em)

@bot.command(name='adjectives')
async def adjectives(ctx):
    em = discord.Embed(title = "You can look up adjectives declension paradigms.\nTry these:", value="!os_a_on\n!os_e_on\n!on_on\n!es_es")
    await ctx.send(embed=em)

@bot.command(name='verbs')
async def verbs(ctx):
    em = discord.Embed(title = "You can look up verb paradigms.\nTry these:", value="!non_contracted\n!contracted\n!irregular_verbs")
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

    em = discord.Embed(title = "1a", color = discord.Color.blue())
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

    em = discord.Embed(title = "1b", color = discord.Color.blue())
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

    em = discord.Embed(title = "1c", color = discord.Color.blue())
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

    em = discord.Embed(title = "1d1", color = discord.Color.blue())
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

    em = discord.Embed(title = "1d2", color = discord.Color.blue())
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

    em = discord.Embed(title = "2a", color = discord.Color.blue())
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

    em = discord.Embed(title = "2b", color = discord.Color.blue())
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

    em = discord.Embed(title = "Zeus", color = discord.Color.blue())
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

    em = discord.Embed(title = "Naus", color = discord.Color.blue())
    em.add_field(name = "Singular", value = f"Nominative: {singular_nominative} \n Genitive: {singular_genitive} \n Dative: {singular_dative} \n Accusative: {singular_accusative} \n Vocative: {singular_vocative}")
    em.add_field(name = "Plural", value = f"Nominative: {plural_nominative} \n Genitive: {plural_genitive} \n Dative: {plural_dative} \n Accusative: {plural_accusative} \n Vocative: {plural_vocative}")
    await ctx.send(embed = em)

bot.run(TOKEN)