#Made : VoidAsMad

@slash.slash(name="경고지급", description = "경고를 지급합니다.", guild_ids=[919390564363931738])
@commands.has_permissions(administrator=True)
async def warm(ctx, users : discord.Member, reason):
  dir = db.reference(f'{users.id}/경고')
  warm = dir.get()
  if warm == None:
    warm = 0

  warm = warm + 1
  dir = db.reference(f'{users.id}')
  dir.update({'경고' : warm})

  if warm == 3:
    await ctx.reply(f'{users.name}님이 경고 3회를 다 받으셨으므로 **차단**되었습니다.')
    await users.ban()
    channel = bot.get_channel(963413479266586714)
    embed = discord.Embed(title="경고 3회이상으로 차단", description = f"{users.name}님이 경고 3회로 **차단**되셨습니다", color = 0xFF0000)
    await channel.send(embed=embed)
    return None
    
    
    
  embed = discord.Embed(title="경고를 지급하였습니다.", description = f"{users.name}님의 경고 {warm}/3회", color = 0xFF0000)
  await ctx.reply(embed = embed)
  channel = bot.get_channel(963413479266586714)
  embed = discord.Embed(title="경고 지급", description = f"", color = 0xFF0000)
  embed.add_field(name=f"처리자", value=f"{ctx.author.mention}", inline=False)
  embed.add_field(name=f"유저", value=f"{users.mention}\n", inline=False)
  embed.add_field(name=f"사유", value=f"{reason}", inline=False)
  
  await channel.send(embed=embed)
  
