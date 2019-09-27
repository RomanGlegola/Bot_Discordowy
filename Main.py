from discord.ext import commands

client = commands.Bot(command_prefix='!')


@client.event
async def on_message(message):
    # unikamy wpadania bota w pętlę
    if message.author == client.user:
        return

    try:
        komenda = message.content.lower()
        # komenda /help
        if komenda.startswith('/help'.format()):
            from Komendy import help
            msg = help.pomoc()
            await message.channel.send(msg)

        # komenda /feedback
        elif komenda.startswith('/feedback'.format()):
            from Komendy import feedback
            msg = feedback.sugestie(message)
            await message.channel.send(msg)

        # komenda /credits
        if komenda.startswith('/credits'.format()):
            from Komendy import credits
            msg = credits.credit()
            await message.channel.send(msg)

        # komenda /roll
        elif komenda.startswith('/r'.format()):
            from Komendy.roll import rzucamy
            for msg in rzucamy(komenda):
                await message.channel.send(msg)

        # komenda do dodawania i losowania przykładowych scenariuszy
        elif komenda.startswith('/scenario'.format()):
            from Komendy import feedback
            feedback.scenariusze()

        # komenda do dodawania i losowania przykładowych spotkań
        elif komenda.startswith('/event'.format()):
            from Komendy import feedback
            feedback.spotkania()

        # komenda do losowania i odczytywania inicjatywy
        elif komenda.startswith('/initiative'.format()):
            from Komendy import initiative
            initiative.inicjatywa(komenda)

    except:
        msg = '{0.author.mention} wpisałeś błędną komendę. Spróbuj wpisać /help'.format(message)
        from Komendy import exception
        exception.wyjatek_ogolny(message)
        await message.channel.send(msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run('NjI1MDkxMTE5NjI1MTQyMjgy.XYaheA._pt_s3ScvqtrAcyDDxUJIeEAbwU')
