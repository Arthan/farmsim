from time import sleep

pieniadzei = 100000
zaoraj_poless = False
zasiej_poless = False
zbierz_plonyss = False
plony = 0
cspeed = 60
kspeed = 70

def sklep():
    global cspeed, pieniadzei, kspeed
    print('(1)ciągniki\n(2)kombajny')
    kk = int(input('jaką chcesz sprawdzić kategorie: '))

    if kk == 1:
        print('(1)średni ciągnik => 170KM | 40km/h | 6.8t | [$99.000]\n'
              '(2)duży ciągnik => 305KM | 50km/h | 8.8t | [$245.000]')
        jc = int(input('który chcesz kupić ciągnik: '))

        if jc == 1:
            if pieniadzei >= 99000:
                pieniadzei -= 99000
                cspeed -= 5
            else:
                print('!!!nie możesz tego kupić potrzebujesz jeszcze ', 99000 - pieniadzei)
                sleep(3)
        if jc == 2:
            if pieniadzei >= 245000:
                pieniadzei -= 245000
                cspeed -= 15
            else:
                print('!!! nie możesz tego kupić potrzebujesz jeszcze ', 245000 - pieniadzei)
                sleep(3)

    if kk == 2:
        print('(1)Toliner 4090 HTS => 310KM | 20km/h | 9.8t | [$129.000]'
              '(2)Axial-flow 7150 => 449KM | 30km/h | 15.9t | [$301.500]'
              '(3)TRION  750 => 465KM | 30km/h | 16.9t | [$401.000]')
        jk = int(input('jaki kombajn chcesz kupić: '))

        if jk == 1:
            if pieniadzei >= 129000:
                pieniadzei -= 129000
                kspeed -= 3
            else:
                print('!!! nie możesz kupić potrzebujesz jeszcze ', 129000 - pieniadzei)
                sleep(3)
        if jk == 2:
            if pieniadzei >= 301500:
                pieniadzei -= 301500
                kspeed -= 6
            else:
                print('!!!nie możesz tego kupić potrzebujesz jeszcze ', 301500 - pieniadzei)
                sleep(3)
        if jk == 3:
            if pieniadzei >= 401000:
                pieniadzei -= 401000
                kspeed -= 10
            else:
                print('!!! nie możesz tego kupić potrzebujesz jeszcze ', 40100 - pieniadzei)
                sleep(3)

def zaoraj_pole():
    global zbierz_plonyss, zaoraj_poless, zasiej_poless
    if zbierz_plonyss == True:
        print(f'Oraż pole zajmie ci to {cspeed} sekund')
        zaoraj_poless = True
        sleep(cspeed)
        zbierz_plonyss = False
        zasiej_poless = False
        return True
    else:
        print('!!!Nie masz zebranych plonów!!!')
        return False

def zasiej_pole():
    global zaoraj_poless, zasiej_poless
    if zaoraj_poless == True:
        print(f'Siejesz pole zajmie ci to {cspeed} sekund')
        sleep(cspeed)
        zasiej_poless = True
        zaoraj_poless = False
        return True
    else:
        print('!!!Nie masz zaoranego pola!!!')
        return False

x = 0

def zbierz_plony():
    global zasiej_poless, plony, zbierz_plonyss, x, zaoraj_poless

    if x == 0:
        zasiej_poless = True
        x += 1

    if zasiej_poless == True:
        print(f'Zbierasz plony zajmie ci to {kspeed} sekund')
        sleep(kspeed)
        zbierz_plonyss = True
        zasiej_poless = False
        plony += 1
        plony += 500
        print(plony)
        return True
    else:
        print('!!!Nie masz zasianego pola!!!')
        return False

def sprzedaj_plony():
    global zbierz_plonyss, plony, pieniadzei
    if zbierz_plonyss:
        if plony == 500:
            plony -= 500
            pieniadzei += 1000
        elif plony == 1000:
            plony -= 1000
            pieniadzei += 2000

def info():
    print('\n   >>>INFO<<<\n=>na początku masz juz pole z gotowymi plonami\n=>musisz robić wszystko po kolei\n=>masz mały ciągnik i słaby kombajn'
          '\n=>po zdobyciu pewnej ilości pieniedzy możesz sobie coś kupić w sklepie')

while True:
    print('\n>>>', pieniadzei, '$<<<')
    print(plony)
    print('info\nsklep\nzaoraj pole\nzasiej pole\nzbierz plony\nsprzedaj plony')
    df = input('co chcesz zrobić: ')

    if df == 'zaoraj pole':
        zbierz_plonyss = zaoraj_pole()
    if df == 'zasiej pole':
        zasiej_poless = zasiej_pole()
    if df == 'zbierz plony':
        zbierz_plonyss = zbierz_plony()
    if df == 'info':
        info()
    if df == 'sprzedaj plony':
        sprzedaj_plony()
    if df == 'sklep':
        sklep()
