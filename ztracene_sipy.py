print('''

              ..-.--..
           ,','.-`.-.`.
          :.',;'     `.\.
          ||//----,-.--\|
        \`:|/-----`-'--||'/
         \\|:    |:'
          `||      \   |!
          |!|          ;|
          !||:.   --  /|!
         /||!||:.___.|!||\\
        /|!|||!|    |!||!\\:.
     ,'//!||!||!`._.||!||,:\\\\
    : :: |!|||!|    |!||! |!::
    | |! !||!|||`---!|!|| ||!|
    | || |!|||!|    |!||! |!||

''')
print(" Vitej ve hre ZTRACENE SIPY.")
print("****************************")
print("Me jmeno je elf ALTIMORE. Tva mise je najit ztracene stribrne sipy, jedinou zbran, ktera nas muze zachranit v boji proti temným Zlovlkům.\n")
hrajem = True
while hrajem == True:
    odpoved = input('1. Jdes po pesine a nudis se.\n (A) Budes si hvizdat.\n (B) Nejak prekonas nudu a budes tichy.\n')
    while True:
        odpoved = odpoved.upper()
        if odpoved == 'A':
            print('Melodie, kterou jsi piskal byla tak krasna, ze prilakala okridleneho ptaka Enuina. Sedl na cestu primo pred tebe, chvili te zasnene poslouchal, uronil par slz a pak se neslysne vznesl do vzduchu.')
            print('Usel jsi par kroku k mistu, kde ptak usedl a vsiml sis, ze se jeho slzy promenili v stribrite perly. Zvedl jsi je a dal do kapsy.')
            perly = True
            break
        elif odpoved == 'B':
            print('Tise ses proplizil lesem, nikdo te nezahledl. ')
            perly = False
            break
        odpoved = input("Zvol variantu A nebo B. ")

    odpoved = input(' (Pro pokracovani zmacnki ENTER)\n')
    odpoved = input('2. Prisel jsi k prekrasnemu jezeru. Chvili hledis do jeho pruzracnych vod a najednou zahlednes pod vodou pohyb.\n Co udelas? \n (A) Prikrcis se.\n (B) Stojis nehnute a snazis se odhalit o co jde.\n')
    while True:
        odpoved = odpoved.upper()
        if odpoved == 'A':
            print('Ucitil jsi podivnou vuni, magie praska ve vzduchu, ale za nejaky cas tento pocit odezni.')
            prsten = False
            break
        elif odpoved == 'B' and perly == True:
            print('Z hlubin se vynori jezerni pani. Smutne na tebe hledi, natahne ruku a ty z jejiho pohledu vycitis prani. Do ruky ji vlozis perly.')
            print('Pani se na tebe usmeje a vymenou ti poda prsten. Navleknes si ho na prst a v tu chvily ucitis priliv sily proudici tvymi zilami. ')
            print('''
                             ,==.
                             \\\\//
                            .-~~-.
                          ,",-""-.".
                         | |      | |
                         | |      | |
                         ". `,,,-" ,'
                           `   _,-'
                            ''')
            perly = False
            prsten = True
            break
        elif odpoved =='B' and perly == False:
            print('Z hlubin se vynori jezerni pani. Smutne na tebe hledi, natahne ruku a ty z jejiho pohledu vycitis prani. Nevis co mas delat a tak se na ni nervozne usmejes.')
            print('Jezerni pani zacne zpivat smutnou pisen, ktera te omami tak, ze krok za krokem vstupujes do hlubin.')
            print('Hra pro tebe konci. Naveky zustanes v jezernim kralovstvi, tvou rodinu bude muset zachranit nekdo jiny.')
            hrajem = False
            break
        odpoved = input("Zvol variantu A nebo B. ")
    if hrajem == False:
        break
    odpoved = input(' (Pro pokracovani zmacnki ENTER)\n')
    print('''
                           __,='`````'=/__
                          '//  (o) \(o) \ `'         _,-,
                          //|     ,_)   (`\      ,-'`_,-\\
                        ,-~~~\  `'==='  /-,      \==```` \__
                       /        `----'     `\     \       \/
                    ,-`                  ,   \  ,.-\       \\
                   /      ,               \,-`\`_,-`\_,..--'\\
                  ,`    ,/,              ,>,   )     \--`````\\
                  (      `\`---'`  `-,-'`_,<   \      \_,.--'`
                   `.      `--. _,-'`_,-`  |    \\
                    [`-.___   <`_,-'`------(    /
                    (`` _,-\   \ --`````````|--`
                     >-`_,-`\,-` ,          |
                   <`_,'     ,  /\          /
                    `  \/\,-/ `/  \/`\_/V\_/
                       (  ._. )    ( .__. )
                       |      |    |      |
                        \,---_|    |_---./
                        ooOO(_)    (_)OOoo''')
    odpoved = input('3. Pokracujes podel brehu a pak dal cestou mezi kopci. Z blizkeho lesa se na tebe vyriti obrovsky zlobr.\n (A) Pripravis se k boji. \n (B) Utikas domu, tusis, ze bys to nezvladl.\n')
    while True:
        odpoved = odpoved.upper()
        if odpoved == 'A':
            if prsten == True:
                print('Jezerni prsten te posilil, takze jsi obra hrave porazil. V jeho skrysi jsi objevil obrovsky poklad a ztracene sipy. \n Cela vesnice je zachranena a diky pokladu, ktery jsi obci daroval prosperuje a vzkveta.')
                hrajem = False
            if prsten == False:
                print('Obr te porazil, zlamal ti nekolik zeber a kdyz ses prestal hybat, myslel ze je po tobe a nechal te byt. \n Do vesnice ses doplazil s vypetim vsech sil.')
                if perly == True:
                    print('Perly ktere jsi donesl domu ti uhradily vsechny vydaje za lecbu a dokonce sis mohl dovolit i novou zbroj. Muzes si cetu zopakovat, jestli se na to citis.')
                    opakovat = input('Vydas se znovu na cestu (a).\n')
                    if opakovat.lower() != 'a':
                        hrajem = False
                else:
                    hrajem = 'False'
            break
        elif odpoved == 'B':
            if prsten == True:
                print('Vratil ses domu. Diky prstenu je z tebe nejsilnejsi muz ve vesnici. Mnoho mladych elfu se k tobe touzi pridat. \nBrzy na to sestavite druzinu a obra premuzete. V jeho doupeti pak naleznete ztracene sipy a zachranite celou vesnici pred zlovlky.')
            elif perly == True:
                print('Diky perlam jsi muzes dovolit lepsi vybaveni a zopakovat celou cestu. Brzy na to sestavis druzinu a obra premuzes. \nV jeho doupeti pak naleznes ztracene sipy a zachranite celou vesnici pred zlovlky.')
            else:
                print('Tva cesta nebyla moc uspesna. S dobrodruzstvim nadobro skoncujes. Stane se z tebe farmar. \nBrzy se najde ve vasi vesnici jiny dobrodruh, ktery sipy nalezne a zachrani vesnici. \naKdyz mu jednoho dne prodavas brambory a celer, poprosis ho o autogram.')
            hrajem = False
            break
        odpoved = input("Zvol variantu A nebo B. ")