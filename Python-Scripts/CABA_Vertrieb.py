

def preis_real_t(preis_nominal_t, inf_index_t):
    return preis_nominal_t / inf_index_t

def inf_index_t():
    result = inf[0]+1
    quartal = Q
    while quartal > 0:
        result = result * inf[quartal]+1
    return result

def inf:


def ma_real_t:
    return ma_nominal_t / inf_index_t

def ma_wirksam_t:
    return ( ma_real_t * (1-nh)) + ( ma_wirksam_t-1 * nh )

def mef(ma_wirksam_t, erloes_t-1):
    value = ma_wirksam_t/erloes_t-1
    if (value <= 0):
        return -20

    if (value > 0.02 && value <= 0.04):
        way = (value-0.02)/(0.08-0.04)
        return -10 + ( way * (10))

    if (value > 0.04 && value <= 0.06):
        way = (value-0.04)/(0.06-0.04)
        return 0 + ( way * (4))

    if (alue > 0.06 && value <= 0.08):
        way = (value-0.06)/(0.08-0.06)
        return 4 + ( way * (7-4))

    if (value > 0.08 && value <= 0.1):
        way = (value-0.08)/(0.1-0.08)
        return 7 + ( way * (9-7))

    if (value > 0.1 && value <= 0.12):
        way = (value-0.1)/(0.12-0.1)
        return 9 + ( way * (11-9))

    if (alue > 0.12 && value <= 0.14):
        way = (value-0.12)/(0.14-0.12)
        return 11 + ( way * (13-11))

    if (value > 0.14 && value <= 0.17):
        way = (value-0.14)/(0.17-0.14)
        return 13 + ( way * (15-13))

    if (value > 0.17 && value <= 0.2):
        way = (value-0.17)/(0.2-0.17)
        return 15 + ( way * (17-15))

def preis_wirksam_t:
    return preis_real_t / (1+mef_t) * (1+pef_t) + (preis_real_t - preis_real_t-1)**2 / stueck

def paf():
    value = preis_wirksam_t
    if (value <= 4.5):
        return -20

    if (value > 4.5 && value <= 5):
        way = (value-4.5)/(5-4.5)
        return 950 - ( way * (950-800))

    if (value > 5 && value <= 5.5):
        way = (value-5)/(5.5-5)
        return 800 - ( way * (800-600))

    if (alue > 5.5 && value <= 6):
        way = (value-5.5)/(6-5.5)
        return 600 - ( way * (600-470))

    if (value > 6 && value <= 6.5):
        way = (value-6)/(6.5-6)
        return 470 - ( way * (470-450))

    if (value > 6.5 && value <= 7):
        way = (value-6.5)/(7-6.5)
        return 450 - ( way * (450-430))

    if (alue > 7 && value <= 7.5):
        way = (value-7)/(7.5-7)
        return 430 - ( way * (430-330))

    if (value > 7.5 && value <= 8):
        way = (value-7.5)/(8-7.5)
        return 330 - ( way * (330-250))

    if (value > 8 && value <= 8.5):
        way = (value-8)/(8.5-8)
        return 250 - ( way * (250-150))

    if (value > 8.5 && value <= 9):
        way = (value-8.5)/(9-8.5)
        return 150 - ( way * (150))

def korr_t(mittlerer_preis_wirksam_t, preis_wirksam_t):
    if preis_wirksam_t <= mittlerer_preis_wirksam_t:
        return 1
    else:
        return (mittlerer_preis_wirksam_t/preis_wirksam_t)**2

def absetzbare_menge(t):
    return paf(t)*k_index(t)*s_index(t)*korr(t)+defizit(t)

def abgesetzte_menge(t):
    if absetzbare_menge(t) < (produzierte_menge(t)+lager_menge(t)):
        return absetzbare_menge
    else:
        return (produzierte_menge(t)+lager_menge(t))

def marktanteil(t):
    return abgesetzte_menge(t) / abgesetzte_menge_aller_unternehmen(t)

def umsatzanteil(t):
    return umsatz(t) / umsatz_aller_unternehmen(t)

def lagerkosten:
    return lager_bestand(t) * 0.5
