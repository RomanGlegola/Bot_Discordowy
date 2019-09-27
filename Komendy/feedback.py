def sugestie(message):
    import datetime
    data = datetime.datetime.now()
    tresc_feedbacku = message.content.replace('/feedback', '')
    msg = f'Feedback przekazany: {message.author.mention} [{data.hour}:{data.minute} ' \
          f'{data.day}-{data.month}-{data.year}] {tresc_feedbacku}'
    feedback_msg = f'{message.author} [{data.hour}:{data.minute} ' \
                   f'{data.day}-{data.month}-{data.year}] {tresc_feedbacku}'
    with open('BazaDanych/Feedback.txt', 'a') as feedback:
        feedback.write(feedback_msg + '\n')
    return msg


def scenariusze():
    pass


def spotkania():
    pass
