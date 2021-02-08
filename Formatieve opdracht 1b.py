from tkinter import *
import random
import json


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

        startknop = Button(self.menuscherm, text='start', command=lambda:[self.menuscherm.destroy(),self.setupraden()], bg='#202125', fg='White', font=('arial', 20), width=7, borderwidth=0)
        startknop.pack(padx=20, pady=10)

        settingsknop = Button(self.menuscherm, text='settings', command=lambda:[self.menuscherm.destroy(),self.settings()], bg='#202125', fg='White', font=('arial', 20), width=7, borderwidth=0)
        settingsknop.pack(padx=20)

        regelsknop = Button(self.menuscherm, text='Regels', command=lambda:[self.menuscherm.destroy(),self.regels()], bg='#202125', fg='White', font=('arial', 20), width=7, borderwidth=0)
        regelsknop.pack(padx=20, pady=10)

        exitknop = Button(self.menuscherm, text='exit', command=self.quit, bg='#202125', fg='White', font=('arial', 20), width=7, borderwidth=0)
        exitknop.pack(padx=20)


    def setupraden(self):
        """Maakt een spelscherm aan voor versie van raden en roept de class mastermind op als er geraden wordt. (12X)"""
        self.raadkans = 1

        self.mainspelscherm = Frame(self.scherm, bg=self.background2)
        self.mainspelscherm.place(x=475, y=50, height=765, width=580)

        zetvak = Frame(self.mainspelscherm, bg=self.background2, highlightbackground="black", highlightthickness=1)
        zetvak.place(x=0, y=0, height=60, width=450)

        for x in range(0,4):
            xvalue = 30 + 100 * x
            zet = Label(zetvak, text='?????', bg=self.background2, fg='Black', font=('ariel', 11), width=10, height=2)
            zet.place(x=xvalue, y=10)

        for y in range(0, 12):
            yvalue = 80 + 50 * y
            raadvak = Frame(self.mainspelscherm, bg=self.background2, highlightbackground="black", highlightthickness=1)
            raadvak.place(x=0, y=yvalue, height=50, width=450)

            for x in range(0, 4):
                xvalue = 30 + 100 * x
                raad = Label(raadvak, text='0', bg=self.background2, fg='Black', font=('ariel', 11), width=10)
                raad.place(x=xvalue, y=10)

            controlevak = Frame(self.mainspelscherm, bg=self.background2, highlightbackground="black", highlightthickness=1)
            controlevak.place(x=500, y=yvalue, height=50, width=50)

            controle1 = Label(controlevak, text='0', bg=self.background2, fg='Black', font=('ariel', 5), width=4)
            controle1.place(x=0, y=0)

            controle2 = Label(controlevak, text='0', bg=self.background2, fg='Black', font=('ariel', 5), width=4)
            controle2.place(x=0, y=25)

            controle3 = Label(controlevak, text='0', bg=self.background2, fg='Black', font=('ariel', 5), width=4)
            controle3.place(x=25, y=0)

            controle4 = Label(controlevak, text='0', bg=self.background2, fg='Black', font=('ariel', 5), width=4)
            controle4.place(x=25, y=25)


        self.raadbutton = Button(self.mainspelscherm, text='Raad', command=lambda: mastermind.klikraden(self), bg='#202125', fg='White', font=('arial', 15), width=7, borderwidth=0)
        self.raadbutton.place(x=100, y=700)

        self.opgeefbutton = Button(self.mainspelscherm, text='Geef op', command=lambda: [mastermind.einde(self), self.eindescherm.config(text='Helaas!\nU heeft verloren.')], bg='#202125', fg='White', font=('arial', 15), width=7, borderwidth=0)
        self.opgeefbutton.place(x=300, y=700)

        mastermind.radenopzet(self)


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


class mastermind:
    """Hier staan alle aanpassingen in die aan de GUI worden aangepast en de code om voor de AI"""
    def radenopzet(self):
        """Kiest een set random kleuren en checkt uit vorige spellen of dit een slimme keuze is. (Kan nooit 3 of 4 keer dezelfde kleur zijn."""
        kleurlist = ['White', 'Silver', 'Blue', 'Green', 'Yellow', 'Orange', 'Red', 'Pink']
        self.raadkleuren = []

        for value in range(0, 4):
            kleur = kleurlist[random.randint(0, 7)]
            if kleur in self.raadkleuren:
                while self.raadkleuren.count(kleur) > 1:
                    kleur = kleurlist[random.randint(0, 7)]
            self.raadkleuren.append(kleur)



        mastermind.raden(self)

    def klikraden(self):
        """Houd bij hoevaak er is geraden en stopt het spel als er te vaak geraden wordt. (meer dan 12 keer)"""
        self.raadkans += 1
        if self.raadkans >= 13:
            self.parent.destroy()
        else:
            mastermind.raden(self)

    def raden(self):
        """Plaats buttons zodat de speler kan raden"""
        self.goedeplaats = 0
        self.verkeerdeplaats = 0
        yvalue1 = 680 - self.raadkans * 50

        actievekans = Frame(self.mainspelscherm, bg=self.background2, highlightbackground="black", highlightthickness=2)
        actievekans.place(x=0, y=yvalue1, height=50, width=450)

        self.raadplek1 = Button(actievekans, text='0', command=lambda:mastermind.raadplekken(self, 1), bg=self.background2, fg='Black', font=('ariel', 11), width=10, borderwidth=0)
        self.raadplek1.place(x=30, y=10)

        self.raadplek2 = Button(actievekans, text='0', command=lambda:mastermind.raadplekken(self, 2), bg=self.background2, fg='Black', font=('ariel', 11), width=10, borderwidth=0)
        self.raadplek2.place(x=130, y=10)

        self.raadplek3 = Button(actievekans, text='0', command=lambda:mastermind.raadplekken(self, 3), bg=self.background2, fg='Black', font=('ariel', 11), width=10, borderwidth=0)
        self.raadplek3.place(x=230, y=10)

        self.raadplek4 = Button(actievekans, text='0', command=lambda:mastermind.raadplekken(self, 4), bg=self.background2, fg='Black', font=('ariel', 11), width=10, borderwidth=0)
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

            yvalue2 = 680 - (self.raadkans - 1) * 50
            raadvak = Frame(self.mainspelscherm, bg=self.background2, highlightbackground="black", highlightthickness=1)
            raadvak.place(x=0, y=yvalue2, height=50, width=450)

            for x in range(0, len(kleuren)):
                xvalue1 = 30 + 100 * x
                raad = Label(raadvak, text=kleuren[x], bg=self.background2, fg=kleuren[x], font=('ariel', 11), width=10)
                raad.place(x=xvalue1, y=10)

            for value in range(0, len(kleuren)):
                if self.raadkleuren.count(kleuren[value]) > 0:
                    if kleuren[value] == self.raadkleuren[value]:
                        self.goedeplaats += 1
                    else:
                        if value == 0:
                            if self.raadkleuren.count(kleuren[value]) < kleuren.count(kleuren[value]):
                                continue
                            else:
                                self.verkeerdeplaats += 1
                        elif value == 1:
                            if self.raadkleuren.count(kleuren[value]) < kleuren.count(kleuren[value]):
                                continue
                            elif kleuren[value] == kleuren[0] and self.raadkleuren.count(kleuren[value]) < 2:
                                continue
                            else:
                                self.verkeerdeplaats += 1
                        elif value == 2:
                            if self.raadkleuren.count(kleuren[value]) < kleuren.count(kleuren[value]):
                                continue
                            elif kleuren[value] == kleuren[0] and self.raadkleuren.count(kleuren[value]) < 2:
                                continue
                            elif kleuren[value] == kleuren[1] and self.raadkleuren.count(kleuren[value]) < 2:
                                continue
                            elif kleuren[value] == kleuren[0] and kleuren[value] == kleuren[1] and self.raadkleuren.count(kleuren[value]) < 3:
                                continue
                            else:
                                self.verkeerdeplaats += 1
                        elif value == 3:
                            if kleuren[value] == kleuren[0] and self.raadkleuren.count(kleuren[value]) < 2:
                                continue
                            elif kleuren[value] == kleuren[1] and self.raadkleuren.count(kleuren[value]) < 2:
                                continue
                            elif kleuren[value] == kleuren[2] and self.raadkleuren.count(kleuren[value]) < 2:
                                continue
                            elif kleuren[value] == kleuren[0] and kleuren[value] == kleuren[1] and self.raadkleuren.count(kleuren[value]) < 3:
                                continue
                            elif kleuren[value] == kleuren[0] and kleuren[value] == kleuren[2] and self.raadkleuren.count(kleuren[value]) < 3:
                                continue
                            elif kleuren[value] == kleuren[1] and kleuren[value] == kleuren[2] and self.raadkleuren.count(kleuren[value]) < 3:
                                continue
                            elif kleuren[value] == kleuren[0] and kleuren[value] == kleuren[1] and kleuren[value] == kleuren[2] and self.raadkleuren.count(kleuren[value]) < 4:
                                continue
                            else:
                                self.verkeerdeplaats += 1

            if self.goedeplaats == 4:
                mastermind.einde(self)
                self.eindescherm.config(text='Gefeliciteerd!\nU heeft gewonnen!')
            elif self.goedeplaats > 0 or self.verkeerdeplaats > 0:
                controlevak = Frame(self.mainspelscherm, bg=self.background2, highlightbackground="black",  highlightthickness=1)
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

        raadlist = ['White', 'Silver', 'Blue', 'Green', 'Yellow', 'Orange', 'Red', 'Pink']
        self.raadlist1 = raadlist[:]
        self.raadlist2 = raadlist[:]
        self.raadlist3 = raadlist[:]
        self.raadlist4 = raadlist[:]

    def raadplekken(self, plek):
        """Veranderd de knoppen terug naar labels met de ingevoerde kleuren."""
        if plek == 1:
            self.raadplek1.config(text=self.raadlist1[0], fg=self.raadlist1[0])
            self.raadlist1.append(self.raadlist1[0])
            self.raadlist1.pop(0)
        elif plek == 2:
            self.raadplek2.config(text=self.raadlist2[0], fg=self.raadlist2[0])
            self.raadlist2.append(self.raadlist2[0])
            self.raadlist2.pop(0)
        elif plek == 3:
            self.raadplek3.config(text=self.raadlist3[0], fg=self.raadlist3[0])
            self.raadlist3.append(self.raadlist3[0])
            self.raadlist3.pop(0)
        elif plek == 4:
            self.raadplek4.config(text=self.raadlist4[0], fg=self.raadlist4[0])
            self.raadlist4.append(self.raadlist4[0])
            self.raadlist4.pop(0)
        return

    def einde(self):
        """Maakt het eindscherm aan en geeft aan of de speler hee gewonnen of verloren."""
        yvalue = 680 - self.raadkans * 50

        raadvak = Frame(self.mainspelscherm, bg=self.background2, highlightbackground="black", highlightthickness=1)
        raadvak.place(x=0, y=yvalue, height=50, width=450)

        for x in range(0, 4):
            xvalue = 30 + 100 * x
            raad = Label(raadvak, text='0', bg=self.background2, fg='Black', font=('ariel', 11), width=10)
            raad.place(x=xvalue, y=10)

        zetvak = Frame(self.mainspelscherm, bg=self.background2, highlightbackground="black", highlightthickness=2)
        zetvak.place(x=0, y=0, height=60, width=450)

        for x in range(0, 4):
            xvalue = 30 + 100 * x
            zet = Label(zetvak, text=self.raadkleuren[x], bg=self.background2, fg=self.raadkleuren[x], font=('ariel', 11), width=10, height=2)
            zet.place(x=xvalue, y=10)

        self.eindescherm = Label(self.scherm, bg=self.background1, fg='Black', font=('ariel', 20))
        self.eindescherm.place(x=1150, y=400)

        self.raadbutton.place_forget()
        self.opgeefbutton.place_forget()

        terugbutton = Button(self.mainspelscherm, text='Terug', command=lambda: [GUI.menu(self), self.mainspelscherm.destroy(), self.eindescherm.destroy()], bg='#202125', fg='White', font=('arial', 15), width=7, borderwidth=0)
        terugbutton.place(x=200, y=700)

        with open('MastermindGames', 'r+') as mastermindjson:
            data = json.load(mastermindjson)
            data.update({'kleurcode': 'Yellow, Pink, Blue, Silver',
                        'Kans 1': 'Blue, Blue, Blue, Pink',
                        'Aantal kansen': 1})
            

        return


    def zetten(self):
        return





if __name__ == '__main__':
    root = Tk()
    root.configure(bg='Blue1')
    root.attributes('-fullscreen', True)
    GUI(root)
    root.mainloop()

