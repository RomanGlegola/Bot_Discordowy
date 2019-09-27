import random
import re

def rzucamy(dane):
    lista_enterow = re.split(r'/( +[^/])*', dane)
    lista_enterow = list(filter(None, lista_enterow))
    for i in range(len(lista_enterow)):
        lista = re.findall(r'[\d\-\+]\d*', lista_enterow[i])
        modyfikator = 0
        for i in range(2, len(lista)):
            modyfikator += int(lista[i])
        yield (f'{rzuc_koscia(int(lista[0]), int(lista[1]), int(modyfikator))}')

def rzuc_koscia(kosci=1, scianki=1, modyfikator=0):
    wysokosc_rzutu = 0
    spis_rzutow = []
    for licz_kosci in range(kosci):
        rzut = 0
        rzut += rzut_koscia(scianki)
        wysokosc_rzutu += rzut
        spis_rzutow.append(rzut)
    return f"{kosci}k{scianki}{czy_modyfikator(modyfikator)} z wynikiem " \
           f"{wysokosc_rzutu + modyfikator} \n" \
           f"Szczegóły: {spis_rzutow}"


def rzut_koscia(scianki=1):
    return random.randint(1, scianki)


def czy_modyfikator(modyfikator):
    if modyfikator > 0:
        return f"+{modyfikator}"
    elif modyfikator == 0:
        return ""
    elif modyfikator < 0:
        return f"{modyfikator}"
