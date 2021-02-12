from tkinter import *
import random
import csv
import itertools


def controleren(gok, code):
    XVwaardes = [0, 0]
    gokkopie = gok[:]
    codekopie = code[:]

    for value in range(0, len(gok)):
        if gok[value] == code[value]:
            XVwaardes[0] += 1
            gokkopie.pop(value)
            gokkopie.insert(value, 'None')
            codekopie.pop(value)
            codekopie.insert(value, 'enoN')

    for value in range(0, len(gokkopie)):
        if gokkopie[value] in codekopie:
            XVwaardes[1] += 1
            codekopie.pop(value)
            codekopie.insert(value, 'enoN')

    return XVwaardes

def verkleinen(mogelijkheden, gok, XVwaardes):
    nieuwemogelijkheden = []
    for mogelijkheid in mogelijkheden:
        if XVwaardes == mastermindzetten(self, gok, mogelijkheid):
            nieuwemogelijkheden.append(mogelijkheid)

    return nieuwemogelijkheden


class GUI:
    """Start de GUI op en roept het spel op (als aangevraagd)."""
    def __init__(self, parent):
        """"Start het menu op"""
        try:
            self.background1
        except:
            self.background1='#0186ff'
        try:
            self.background2
        except:
            self.background2 = '#00ffaa'
        self.parent = parent
        self.scherm = Frame(self.parent)
        self.scherm.config(bg=self.background1)
        self.scherm.pack(fill='both', expand=True)

        self.menu()

    def menu(self):
        """Start het menu op en geeft de mogelijkheid om te starten, settings te veranderen en te stoppen."""
        self.menuscherm = Frame(self.scherm, bg=self.background1)
        self.menuscherm.place(x=1300, y=400)

        startknop = Button(self.menuscherm, text='start', command=lambda:[self.menuscherm.destroy(),self.spelvorm()], bg='#202125', fg='White', font=('arial', 20), width=7, borderwidth=0)
        startknop.pack(padx=20, pady=10)

        settingsknop = Button(self.menuscherm, text='settings', command=lambda:[self.menuscherm.destroy(),self.settings()], bg='#202125', fg='White', font=('arial', 20), width=7, borderwidth=0)
        settingsknop.pack(padx=20)

        regelsknop = Button(self.menuscherm, text='Regels', command=lambda:[self.menuscherm.destroy(),self.regels()], bg='#202125', fg='White', font=('arial', 20), width=7, borderwidth=0)
        regelsknop.pack(padx=20, pady=10)

        exitknop = Button(self.menuscherm, text='exit', command=self.quit, bg='#202125', fg='White', font=('arial', 20), width=7, borderwidth=0)
        exitknop.pack(padx=20)

    def spelvorm(self):
        """Laat de speler kiezen of ze willen raden of zetten"""
        self.spelvormscherm = Frame(self.scherm, bg=self.background2)
        self.spelvormscherm.place(x=575, y=350, height=165, width=380)

        kieslabel = Label(self.spelvormscherm, text='Wilt u raden of kiezen?', bg=self.background2, font=('arial', 15))
        kieslabel.place(x=87, y=20)

        raadbutton = Button(self.spelvormscherm, text='Raden', command=lambda:[self.spelvormscherm.destroy(), self.setupraden()], bg='#202125', fg='White', font=('arial', 15), width=7, borderwidth=0)
        raadbutton.place(x=75, y=85)

        kiesbutten = Button(self.spelvormscherm, text='Kiezen', command=lambda:[self.spelvormscherm.destroy(), self.setupkiezen()], bg='#202125', fg='White', font=('arial', 15), width=7, borderwidth=0)
        kiesbutten.place(x=225, y=85)


    def setupraden(self):
        """Maakt een spelscherm aan voor versie van raden en roept de class mastermind raden op."""
        self.raadkans = 1

        self.radenspelscherm = Frame(self.scherm, bg=self.background2)
        self.radenspelscherm.place(x=475, y=50, height=765, width=580)

        zetvak = Frame(self.radenspelscherm, bg=self.background2, highlightbackground="black", highlightthickness=1)
        zetvak.place(x=0, y=0, height=60, width=450)

        for x in range(0,4):
            xvalue = 30 + 100 * x
            zet = Label(zetvak, text='?????', bg=self.background2, fg='Black', font=('ariel', 11), width=10, height=2)
            zet.place(x=xvalue, y=10)

        for y in range(0, 12):
            yvalue = 80 + 50 * y
            raadvak = Frame(self.radenspelscherm, bg=self.background2, highlightbackground="black", highlightthickness=1)
            raadvak.place(x=0, y=yvalue, height=50, width=450)

            for x in range(0, 4):
                xvalue = 30 + 100 * x
                raad = Label(raadvak, text='0', bg=self.background2, fg='Black', font=('ariel', 11), width=10)
                raad.place(x=xvalue, y=10)

            controlevak = Frame(self.radenspelscherm, bg=self.background2, highlightbackground="black", highlightthickness=1)
            controlevak.place(x=500, y=yvalue, height=50, width=50)

            controle1 = Label(controlevak, text='0', bg=self.background2, fg='Black', font=('ariel', 5), width=4)
            controle1.place(x=0, y=0)

            controle2 = Label(controlevak, text='0', bg=self.background2, fg='Black', font=('ariel', 5), width=4)
            controle2.place(x=0, y=25)

            controle3 = Label(controlevak, text='0', bg=self.background2, fg='Black', font=('ariel', 5), width=4)
            controle3.place(x=25, y=0)

            controle4 = Label(controlevak, text='0', bg=self.background2, fg='Black', font=('ariel', 5), width=4)
            controle4.place(x=25, y=25)


        self.raadbutton = Button(self.radenspelscherm, text='Raad', command=lambda: mastermindraden.klikraden(self), bg='#202125', fg='White', font=('arial', 15), width=7, borderwidth=0)
        self.raadbutton.place(x=100, y=700)

        self.opgeefbutton = Button(self.radenspelscherm, text='Geef op', command=self.radenopgeven, bg='#202125', fg='White', font=('arial', 15), width=7, borderwidth=0)
        self.opgeefbutton.place(x=300, y=700)

        mastermindraden.radenopzet(self)

    def setupkiezen(self):
        """Maakt een spelscherm aan voor versie van kiezen en roept de class mastermind kiezen op."""
        self.raadkans = 1

        self.kiezenspelscherm = Frame(self.scherm, bg=self.background2)
        self.kiezenspelscherm.place(x=475, y=50, height=765, width=580)

        zetvak = Frame(self.kiezenspelscherm, bg=self.background2, highlightbackground="black", highlightthickness=1)
        zetvak.place(x=0, y=620, height=60, width=450)

        self.zet1 = Button(zetvak, text='?????', command=lambda:mastermindzetten.kiesplekken(self, 1, True), bg=self.background2, fg='Black', font=('ariel', 11), width=10, borderwidth=0)
        self.zet1.place(x=30, y=18)

        self.zet2 = Button(zetvak, text='?????', command=lambda: mastermindzetten.kiesplekken(self, 2, True), bg=self.background2, fg='Black', font=('ariel', 11), width=10, borderwidth=0)
        self.zet2.place(x=130, y=18)

        self.zet3 = Button(zetvak, text='?????', command=lambda: mastermindzetten.kiesplekken(self, 3, True), bg=self.background2, fg='Black', font=('ariel', 11), width=10, borderwidth=0)
        self.zet3.place(x=230, y=18)

        self.zet4 = Button(zetvak, text='?????', command=lambda: mastermindzetten.kiesplekken(self, 4, True), bg=self.background2, fg='Black', font=('ariel', 11), width=10, borderwidth=0)
        self.zet4.place(x=330, y=18)

        for y in range(0, 12):
            yvalue = 50 * y
            raadvak = Frame(self.kiezenspelscherm, bg=self.background2, highlightbackground="black", highlightthickness=1)
            raadvak.place(x=0, y=yvalue, height=50, width=450)

            for x in range(0, 4):
                xvalue = 30 + 100 * x
                raad = Label(raadvak, text='0', bg=self.background2, fg='Black', font=('ariel', 11), width=10)
                raad.place(x=xvalue, y=10)

            controlevak = Frame(self.kiezenspelscherm, bg=self.background2, highlightbackground="black", highlightthickness=1)
            controlevak.place(x=500, y=yvalue, height=50, width=50)

            controle1 = Label(controlevak, text='0', bg=self.background2, fg='Black', font=('ariel', 5), width=4)
            controle1.place(x=0, y=0)

            controle2 = Label(controlevak, text='0', bg=self.background2, fg='Black', font=('ariel', 5), width=4)
            controle2.place(x=0, y=25)

            controle3 = Label(controlevak, text='0', bg=self.background2, fg='Black', font=('ariel', 5), width=4)
            controle3.place(x=25, y=0)

            controle4 = Label(controlevak, text='0', bg=self.background2, fg='Black', font=('ariel', 5), width=4)
            controle4.place(x=25, y=25)

        self.volgendebutton = Button(self.kiezenspelscherm, text='Volgende', command=lambda:mastermindzetten.klikkiezen(self), bg='#202125', fg='White', font=('arial', 15), width=8, borderwidth=0)
        self.volgendebutton.place(x=100, y=700)

        self.opgeefbutton = Button(self.kiezenspelscherm, text='Geef op', command=self.kiezenopgeven, bg='#202125', fg='White', font=('arial', 15), width=8, borderwidth=0)
        self.opgeefbutton.place(x=300, y=700)

        self.infoscherm = Label(self.scherm, bg=self.background1, fg='Black', font=('ariel', 20))
        self.infoscherm.place(x=1150, y=400)

        mastermindzetten.opzet(self)

    def radenopgeven(self):
        self.opgegeven = True
        mastermindraden.einde(self)
        self.eindescherm.config(text='Helaas!\nU heeft verloren.')

    def kiezenopgeven(self):
        self.parent.destroy()


    def settings(self):
        """Laat spelers settings aanpassen"""
        self.settingsscherm = Frame(self.scherm, bg=self.background1)
        self.settingsscherm.pack(fill='both', expand=True)

        settingsscherm = Frame(self.settingsscherm, bg=self.background2)
        settingsscherm.place(x=400, y=200, height=200, width=732)

        kleurlabel = Label(settingsscherm, text='Kleur', bg='#fff000', fg='Black', font=('ariel', 12), width=10, height=2)
        kleurlabel.place(x=50, y=10)

        kleurbutton = Button(settingsscherm, text='standaard', bg='#fff000', fg='Black', font=('arial', 12), width=15, height=2, borderwidth=0)
        kleurbutton.place(x=175, y=10)

        label2 = Label(settingsscherm, text='Kleur', bg='#fff000', fg='Black', font=('ariel', 12), width=10, height=2)
        label2.place(x=400, y=10)

        button2 = Button(settingsscherm, text='standaard', bg='#fff000', fg='Black', font=('arial', 12), width=15, height=2, borderwidth=0)
        button2.place(x=525, y=10)


        applybutton = Button(self.settingsscherm, text='Apply', command=lambda:[self.settingsscherm.destroy(),self.savesettings()], bg='#fff000', fg='Black', font=('arial', 15), width=7, borderwidth=0)
        applybutton.place(x=750, y=500)

        cancelbutton = Button(self.settingsscherm, text='Cancel', command=lambda:[self.settingsscherm.destroy(),self.menu()], bg='#fff000', fg='Black', font=('arial', 15), width=7, borderwidth=0)
        cancelbutton.place(x=650, y=500)

    def savesettings(self):
        """Laat spelers de aangepaste settings opslaan"""
        self.scherm.config(bg=self.background1)
        self.menu()

    def regels(self):
        """Laat de regels zien."""
        return

    def quit(self):
        """Sluit het spel volledig af."""
        self.parent.destroy()


class mastermindraden:
    """Hier staan alle aanpassingen in die aan de GUI worden aangepast en de code voor de AI die moet zetten."""
    def radenopzet(self):
        """Kiest een set random kleuren en checkt uit vorige spellen of dit een slimme keuze is. (Kan nooit 3 of 4 keer dezelfde kleur zijn.)"""
        kleurlist = ['White', 'Silver', 'Blue', 'Green', 'Yellow', 'Orange', 'Red', 'Pink']
        self.raadkleuren = []

        for value in range(0, 4):
            kleur = kleurlist[random.randint(0, 7)]
            if kleur in self.raadkleuren:
                while self.raadkleuren.count(kleur) > 1:
                    kleur = kleurlist[random.randint(0, 7)]
            self.raadkleuren.append(kleur)


        mastermindraden.raden(self)

    def klikraden(self):
        """Houd bij hoevaak er is geraden en stopt het spel als er te vaak geraden wordt. (meer dan 12 keer)"""
        self.raadkans += 1
        if self.raadkans >= 13:
            mastermindraden.einde(self)
            self.eindescherm.config(text='Helaas!\nU heeft verloren.')
        else:
            mastermindraden.raden(self)

    def raden(self):
        """Plaats buttons zodat de speler kan raden"""
        self.goedeplaats = 0
        self.verkeerdeplaats = 0
        yvalue1 = 680 - self.raadkans * 50

        actievekans = Frame(self.radenspelscherm, bg=self.background2, highlightbackground="black", highlightthickness=2)
        actievekans.place(x=0, y=yvalue1, height=50, width=450)

        self.raadplek1 = Button(actievekans, text='0', command=lambda:mastermindraden.raadplekken(self, 1), bg=self.background2, fg='Black', font=('ariel', 11), width=10, borderwidth=0)
        self.raadplek1.place(x=30, y=10)

        self.raadplek2 = Button(actievekans, text='0', command=lambda:mastermindraden.raadplekken(self, 2), bg=self.background2, fg='Black', font=('ariel', 11), width=10, borderwidth=0)
        self.raadplek2.place(x=130, y=10)

        self.raadplek3 = Button(actievekans, text='0', command=lambda:mastermindraden.raadplekken(self, 3), bg=self.background2, fg='Black', font=('ariel', 11), width=10, borderwidth=0)
        self.raadplek3.place(x=230, y=10)

        self.raadplek4 = Button(actievekans, text='0', command=lambda:mastermindraden.raadplekken(self, 4), bg=self.background2, fg='Black', font=('ariel', 11), width=10, borderwidth=0)
        self.raadplek4.place(x=330, y=10)

        if self.raadkans != 1:
            kleuren = []
            self.kleur1 = self.raadlist1[-1]
            self.kleur2 = self.raadlist2[-1]
            self.kleur3 = self.raadlist3[-1]
            self.kleur4 = self.raadlist4[-1]
            kleuren.append(self.kleur1)
            kleuren.append(self.kleur2)
            kleuren.append(self.kleur3)
            kleuren.append(self.kleur4)

            if self.raadkans == 2:
                self.eerstegok = kleuren[:]
            elif self.raadkans == 3:
                self.tweedegok = kleuren[:]

            yvalue2 = 680 - (self.raadkans - 1) * 50
            raadvak = Frame(self.radenspelscherm, bg=self.background2, highlightbackground="black", highlightthickness=1)
            raadvak.place(x=0, y=yvalue2, height=50, width=450)

            for x in range(0, len(kleuren)):
                xvalue1 = 30 + 100 * x
                kleur1 = kleuren[x]
                kleur2 = kleuren[x]
                if kleur2 == '0':
                    kleur2 = 'Black'

                raad = Label(raadvak, text=kleur1, bg=self.background2, fg=kleur2, font=('ariel', 11), width=10)
                raad.place(x=xvalue1, y=10)

            raadkleuren = self.raadkleuren[:]
            indexlist = []
            for value in range(0, 4):
                if kleuren[value] == raadkleuren[value]:
                    self.goedeplaats += 1
                    kleuren.pop(value)
                    kleuren.insert(value, 'enoN')
                    raadkleuren.pop(value)
                    raadkleuren.insert(value, 'None')
                else:
                    continue

            for value in range(0, len(kleuren)):
                if kleuren[value] in raadkleuren:
                    self.verkeerdeplaats += 1
                    raadkleuren.remove(kleuren[value])
                else:
                    continue



            if self.goedeplaats == 4:
                mastermindraden.einde(self)
                self.eindescherm.config(text='Gefeliciteerd!\nU heeft gewonnen!')
            elif self.goedeplaats > 0 or self.verkeerdeplaats > 0:
                controlevak = Frame(self.radenspelscherm, bg=self.background2, highlightbackground="black",  highlightthickness=1)
                controlevak.place(x=500, y=yvalue2, height=50, width=50)

                for value1 in range(0,3):
                    if value1 == 0:
                        value2 = self.goedeplaats
                        value3 = 0
                        value4 = 'X'
                    elif value1 == 1:
                        value2 = self.verkeerdeplaats + self.goedeplaats
                        value3 = self.goedeplaats
                        value4 = 'V'
                    elif value1 == 2:
                        if self.goedeplaats + self.verkeerdeplaats < 4:
                            value2 = 4
                            value3 = self.verkeerdeplaats + self.goedeplaats
                            value4 = '0'
                        else:
                            continue

                    for value in range(value3, value2):
                        if value == 0 or value == 2:
                            xvalue2 = 0
                        elif value == 1 or value == 3:
                            xvalue2 = 25

                        if value == 0 or value == 1:
                            yvalue3 = 0
                        elif value == 2 or value == 3:
                            yvalue3 = 25

                        controle = Label(controlevak, text=value4, bg=self.background2, fg='Black', font=('ariel', 5), width=4)
                        controle.place(x=xvalue2, y=yvalue3)

        raadlist = ['White', 'Silver', 'Blue', 'Green', 'Yellow', 'Orange', 'Red', 'Pink', '0']
        self.raadlist1 = raadlist[:]
        self.raadlist2 = raadlist[:]
        self.raadlist3 = raadlist[:]
        self.raadlist4 = raadlist[:]

    def raadplekken(self, plek):
        """Veranderd de kleuren van de knoppen."""
        if plek == 1:
            if self.raadlist1[-1] == '0':
                self.raadlist1.pop(-1)
            self.raadplek1.config(text=self.raadlist1[0], fg=self.raadlist1[0])
            self.raadlist1.append(self.raadlist1[0])
            self.raadlist1.pop(0)
        elif plek == 2:
            if self.raadlist2[-1] == '0':
                self.raadlist2.pop(-1)
            self.raadplek2.config(text=self.raadlist2[0], fg=self.raadlist2[0])
            self.raadlist2.append(self.raadlist2[0])
            self.raadlist2.pop(0)
        elif plek == 3:
            if self.raadlist3[-1] == '0':
                self.raadlist3.pop(-1)
            self.raadplek3.config(text=self.raadlist3[0], fg=self.raadlist3[0])
            self.raadlist3.append(self.raadlist3[0])
            self.raadlist3.pop(0)
        elif plek == 4:
            if self.raadlist4[-1] == '0':
                self.raadlist4.pop(-1)
            self.raadplek4.config(text=self.raadlist4[0], fg=self.raadlist4[0])
            self.raadlist4.append(self.raadlist4[0])
            self.raadlist4.pop(0)
        return

    def einde(self):
        """Maakt het eindscherm aan en geeft aan of de speler hee gewonnen of verloren."""
        yvalue = 680 - self.raadkans * 50

        raadvak = Frame(self.radenspelscherm, bg=self.background2, highlightbackground="black", highlightthickness=1)
        raadvak.place(x=0, y=yvalue, height=50, width=450)

        for x in range(0, 4):
            xvalue = 30 + 100 * x
            raad = Label(raadvak, text='0', bg=self.background2, fg='Black', font=('ariel', 11), width=10)
            raad.place(x=xvalue, y=10)

        zetvak = Frame(self.radenspelscherm, bg=self.background2, highlightbackground="black", highlightthickness=2)
        zetvak.place(x=0, y=0, height=60, width=450)

        for x in range(0, 4):
            xvalue = 30 + 100 * x
            zet = Label(zetvak, text=self.raadkleuren[x], bg=self.background2, fg=self.raadkleuren[x], font=('ariel', 11), width=10, height=2)
            zet.place(x=xvalue, y=10)

        self.eindescherm = Label(self.scherm, bg=self.background1, fg='Black', font=('ariel', 20))
        self.eindescherm.place(x=1150, y=400)

        self.raadbutton.place_forget()
        self.opgeefbutton.place_forget()

        terugbutton = Button(self.radenspelscherm, text='Terug', command=lambda: [GUI.menu(self), self.radenspelscherm.destroy(), self.eindescherm.destroy()], bg='#202125', fg='White', font=('arial', 15), width=7, borderwidth=0)
        terugbutton.place(x=200, y=700)

        try:
            self.eerstegok
        except:
            self.eerstegok = []
        try:
            self.tweedegok
        except:
            self.tweedegok = []

        try:
            if self.opgegeven == True:
                geraden = False
        except:
            if self.raadkans >= 13:
                geraden = False
            else:
                geraden = True

        if self.raadkans >= 13:
            gokkansen = 12
        else:
            gokkansen = self.raadkans - 1

        dict = {'eerste gok': self.eerstegok, 'tweede gok': self.tweedegok, 'antwoord': self.raadkleuren, 'geraden': geraden, 'gok kansen': gokkansen}

        with open('MastermindGames.CSV', 'a') as mastermindcsv:
            data = csv.DictWriter(mastermindcsv, fieldnames=['eerste gok', 'tweede gok', 'antwoord', 'geraden', 'gok kansen'])
            data.writerow(dict)
            

        return

class mastermindzetten:
    """Hier staan alle aanpassingen in die aan de GUI worden aangepast en de code voor de AI die moet raden."""
    def opzet(self):
        kleurlist = ['White', 'Silver', 'Blue', 'Green', 'Yellow', 'Orange', 'Red', 'Pink']
        allecominaties = list(itertools.product(kleurlist, repeat=4))
        allecominatieslijst = [list(option) for option in allecominaties]

        # geheimecode = ['Silver', 'Red', 'Green', 'Red']

        eerstegok = []
        for x in range(0, 3):
            if x == 0:
                kleur12 = random.choice(kleurlist)
                eerstegok.append(kleur12)
                eerstegok.append(kleur12)
            else:
                kleur34 = random.choice(kleurlist)
                while kleur34 in eerstegok:
                    kleur34 = random.choice(kleurlist)
                eerstegok.append(kleur34)

        kieslist = ['White', 'Silver', 'Blue', 'Green', 'Yellow', 'Orange', 'Red', 'Pink', '0']
        self.kieslist1 = kieslist[:]
        self.kieslist2 = kieslist[:]
        self.kieslist3 = kieslist[:]
        self.kieslist4 = kieslist[:]

        mastermindzetten.kiezen(self)

    def klikkiezen(self):
        if self.raadkans == 1:
            if self.kieslist1[-1] == '0' or self.kieslist3[-1] == '0' or self.kieslist2[-1] == '0' or self.kieslist4[-1] == '0':
                self.infoscherm.config(text='Dit is geen gelidige code.\nVoer een geldige code in.')
                return
            else:
                self.infoscherm.config(text='')

        self.raadkans += 1
        mastermindzetten.kiezen(self)

    def kiezen(self):
        if self.raadkans == 2:
            self.kleurlist = []
            self.kleurlist.append(self.kieslist1[-1])
            self.kleurlist.append(self.kieslist2[-1])
            self.kleurlist.append(self.kieslist3[-1])
            self.kleurlist.append(self.kieslist4[-1])

            zetvak = Frame(self.kiezenspelscherm, bg=self.background2, highlightbackground="black", highlightthickness=1)
            zetvak.place(x=0, y=620, height=60, width=450)

            for x in range(0, 4):
                xvalue = 30 + 100 * x
                zet = Label(zetvak, text=self.kleurlist[x], bg=self.background2, fg=self.kleurlist[x], font=('ariel', 11), width=10)
                zet.place(x=xvalue, y=18)

            kleurlist = ['White', 'Silver', 'Blue', 'Green', 'Yellow', 'Orange', 'Red', 'Pink']
            allecominaties = list(itertools.product(['White', 'Silver', 'Blue', 'Green', 'Yellow', 'Orange', 'Red', 'Pink'], repeat=4))
            allecominatieslijst = [list(option) for option in allecominaties]

            self.eerstegok = []
            for x in range(0, 3):
                if x == 0:
                    kleur12 = random.choice(kleurlist)
                    self.eerstegok.append(kleur12)
                    self.eerstegok.append(kleur12)
                else:
                    kleur34 = random.choice(kleurlist)
                    while kleur34 in self.eerstegok:
                        kleur34 = random.choice(kleurlist)
                    self.eerstegok.append(kleur34)

            raadvak = Frame(self.kiezenspelscherm, bg=self.background2, highlightbackground="black", highlightthickness=1)
            raadvak.place(x=0, y=0, height=50, width=450)

            for x in range(0, 4):
                xvalue = 30 + 100 * x
                raad = Label(raadvak, text=self.eerstegok[x], bg=self.background2, fg=self.eerstegok[x], font=('ariel', 11), width=10)
                raad.place(x=xvalue, y=10)

            self.controle = controleren(self.eerstegok, self.kleurlist)

            while True:
                mastermindzetten.kieslijsten(self)

                controlevak = Frame(self.kiezenspelscherm, bg=self.background2, highlightbackground="black", highlightthickness=1)
                controlevak.place(x=500, y=0, height=50, width=50)

                self.controlebuttonlb = Button(controlevak, text='0', command=lambda:mastermindzetten.kiesplekken(self, 1, False), bg=self.background2, fg='Black', font=('ariel', 5), width=3, height=2, borderwidth=0)
                self.controlebuttonlb.place(x=0, y=0)

                self.controlebuttonrb = Button(controlevak, text='0', command=lambda: mastermindzetten.kiesplekken(self, 2, False), bg=self.background2, fg='Black', font=('ariel', 5), width=3, height=2, borderwidth=0)
                self.controlebuttonrb.place(x=25, y=0)

                self.controlebuttonlo = Button(controlevak, text='0', command=lambda: mastermindzetten.kiesplekken(self, 3, False), bg=self.background2, fg='Black', font=('ariel', 5), width=3, height=2, borderwidth=0)
                self.controlebuttonlo.place(x=0, y=25)

                self.controlebuttonro = Button(controlevak, text='0', command=lambda: mastermindzetten.kiesplekken(self, 4, False), bg=self.background2, fg='Black', font=('ariel', 5), width=3, height=2, borderwidth=0)
                self.controlebuttonro.place(x=25, y=25)

                self.controlevalues =[0, 0]
                if self.kieslist1[-1] == 'X':
                    self.controlevalues[0] += 1
                elif self.kieslist1[-1] == 'V':
                    self.controlevalues[-1] += 1
                if self.kieslist2[-1] == 'X':
                    self.controlevalues[0] += 1
                elif self.kieslist2[-1] == 'V':
                    self.controlevalues[-1] += 1
                if self.kieslist3[-1] == 'X':
                    self.controlevalues[0] += 1
                elif self.kieslist3[-1] == 'V':
                    self.controlevalues[-1] += 1
                if self.kieslist4[-1] == 'X':
                    self.controlevalues[0] += 1
                elif self.kieslist4[-1] == 'V':
                    self.controlevalues[-1] += 1

                if self.controlevalues == self.controle:
                    break
                else:
                    continue



        # if self.raadkans != 1:
        #     return


    def kieslijsten(self):
        kieslist = ['X', 'V', '0']
        self.kieslist1 = kieslist[:]
        self.kieslist2 = kieslist[:]
        self.kieslist3 = kieslist[:]
        self.kieslist4 = kieslist[:]

    def kiesplekken(self, x, value):
        if x == 1:
            if self.kieslist1[-1] == '0' and value == True:
                self.kieslist1.pop(-1)
                self.zet1.config(text=self.kieslist1[0], fg=self.kieslist1[0])
            if value == False:
                self.controlebuttonlb.config(text=self.kieslist1[0])
            self.kieslist1.append(self.kieslist1[0])
            self.kieslist1.pop(0)
        elif x == 2:
            if self.kieslist2[-1] == '0' and value == True:
                self.kieslist2.pop(-1)
                self.zet2.config(text=self.kieslist2[0], fg=self.kieslist2[0])
            try:
                self.controlebuttonrb.config(text=self.kieslist2[0])
            except:
                False
            self.kieslist2.append(self.kieslist2[0])
            self.kieslist2.pop(0)
        elif x == 3:
            if self.kieslist3[-1] == '0' and value == True:
                self.kieslist3.pop(-1)
                self.zet3.config(text=self.kieslist3[0], fg=self.kieslist3[0])
            try:
                self.controlebuttonlo.config(text=self.kieslist3[0])
            except:
                False
            self.kieslist3.append(self.kieslist3[0])
            self.kieslist3.pop(0)
        elif x == 4:
            if self.kieslist4[-1] == '0' and value == True:
                self.kieslist4.pop(-1)
                self.zet4.config(text=self.kieslist4[0], fg=self.kieslist4[0])
            try:
                self.controlebuttonro.config(text=self.kieslist4[0])
            except:
                False
            self.kieslist4.append(self.kieslist4[0])
            self.kieslist4.pop(0)




if __name__ == '__main__':
    root = Tk()
    root.configure(bg='Blue1')
    root.attributes('-fullscreen', True)
    GUI(root)
    root.mainloop()

