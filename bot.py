import discord
import os

def initialize_bot():
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')
        await client.get_channel(550732056813109250).send('I live again!')
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        # commands only accessible to me
        if str(message.author) == os.environ.get('DISCORD_MASTER'):
            if message.content.startswith('$bedtime'):
                await message.channel.send('Zzz...')
                await client.close()
            elif message.content.startswith('$blue_time'):
                blue_role = message.guild.get_role(743951005670047774) # 743951005670047774 <- CIS # 761278431513804910 <- BOT
                members = message.guild.members
                await message.channel.send('Bark! (blueing the server)')
                for member in members:
                    if member.top_role is None or member.top_role < blue_role:
                        new_roles = member.roles
                        new_roles.append(blue_role)
                        await message.author.edit(reason='The hour of BLUE is upon us', roles=new_roles)
                await message.channel.send('Bork! (The server has been blued)')

        if message.content.startswith('$speak'):
            await message.channel.send("Bark!")
            print(str(message.author.id))

        elif message.content.startswith('$fetch'):
            roles = message.guild.roles
            requested_roles = filter(lambda item: f' {item.name}' in message.content, roles)
            existing_roles = message.author.roles

            for role in requested_roles:
                if role < message.author.top_role:
                    existing_roles.append(role)
            await message.author.edit(reason='Requested roles!', roles=existing_roles)
            await message.channel.send('Bark! (all appropriate roles given!)')

        # elif message.content.startswith("$logs"):
        #     async for entry in message.guild.audit_logs(limit=10):
        #         print()
        #         print(entry)

    # @client.event
    # async def on_message_delete(message):
    #     await message.channel.send(f'{message.author.mention} :eyes:')
    #     print(f'{message.content} \n\n ~ {message.author.name}')


    return client

if __name__ == '__main__':
    client = initialize_bot()
    client.run(os.environ.get('DISCORD_TOKEN'))