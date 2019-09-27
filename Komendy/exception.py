import datetime

data = datetime.datetime.now()


def wyjatek_ogolny(message):
    with open('BazaDanych/Błędy.txt', 'a') as bledy:
        bledy.write(f'{message.author} [{data.hour}:{data.minute} '
                    f'{data.day}-{data.month}-{data.year}] {message.content.lower()} \n')


def czysc():
    godzina = 2
    kanal = 'kości'
    if godzina == data.hour:
        return f'{kanal.channel.purge()}'
