#-=NOTE=- This game is made by playerDefGroup

#Alpha, please don't leak my hard work.
from os import system
from time import sleep
import json
import random
import sys


version = 'Simulat World II v0.16'
versionsave = ''

autosave = 'True'
asavet = 10

fn=0
ln=0
age=0
gdr=0
bio=0
hunger=0
bladder=0
hygiene=0
energy=0
comfort=0
fun=0
cash=0
day=0
cheats=0
mood=0
oneeds=0
oldsave=0
difficulty=0

def loadsettings():
    global autosave
    global asavet
    
    try:
        system('cls')
        with open('settings.json', 'r') as saves:
            settings = json.load(saves)
            autosave = (settings['Autosave'])
            asavet = (settings['Autosave Interval'])
        print('Loaded Custom Settings.')
        sleep(1)
    except:
        print('Unable to load Custom Settings.')
        sleep(1)
    finally:
        menu()
        
def savesettings():
    global autosave
    global asavet
    savesettings = {'This is a save file of Settings.':'','Autosave':autosave,'Autosave Interval':asavet}
    
    with open('settings.json', 'w') as saves:
        json.dump(savesettings, saves, indent=4)
    print('Saving Settings Succesful')
    sleep(1)
    menu()

def loadgame():
    system('cls')
    
    global fn
    global ln
    global age
    global gdr
    global bio
    global hunger
    global bladder
    global hygiene
    global energy
    global comfort
    global fun
    global cash
    global day
    global version
    global cheats
    global versionsave
    global difficulty
    
    try:
        with open('save.json', 'r') as ts:
            save = json.load(ts)
            fn = (save['fn'])
            ln = (save['ln'])
            age = (save['age'])
            gdr = (save['gdr'])
            bio = (save['bio'])
            hunger = (save['hunger'])
            bladder = (save['bladder'])
            hygiene = (save['hygiene'])
            energy = (save['energy'])
            comfort = (save['comfort'])
            fun = (save['fun'])
            cash = (save['cash'])
            day = (save['day'])
            cheats = (save['cheats'])
            difficulty = (save['difficulty'])
            
            try:
                global versionsave
                versionsave = (save['version'])
                
                if versionsave == version:
                    system('cls')
                    
                    print('\n\nSave and Game versions are consistent.\nLoading...')
                    sleep(2)
                    mood()
                    
                else:
                    global oldsave
                    system('cls')
                    print('\n\nSave and Game versions: \nSave:', versionsave,'\nGame:', version, '\nAre not consistent.\nLoading such save could contain severe bugs!')
                    lsave = input('Are you sure to load this save file? (yes/no) ')
                    if lsave == 'yes':
                        system('cls')
                        print('Loading...')
                        oldsave = 1
                        sleep(3)
                        mood()
                    else:
                        menu()
            except KeyError:
                system('cls')
                print('\n\nCannot find version info in the save file, meaning that save file can be:')
                print('\nVery old before version info was implemented (Simulat World II v0.15), meaning that loading such save will crash the game.')
                print('\nNot created or modified by Simulat World II, meaning that user or other software could modify save data.')
                print('\n\nLoading such save could contain severe bugs!')
                nesave = input('Are you sure to load this save file? (yes/no) ')
                if nesave == 'yes':
                        system('cls')
                        print('Loading...')
                        oldsave = 1
                        versionsave = 'Unable to read save version.'
                        sleep(3)
                        mood()
                else:
                    menu()
                
    except FileNotFoundError:
        system('cls')
        print('Error, "save.json" not found.')
        sleep(2)
        menu()
    except:
        system('cls')
        print('An error occured whilst trying to load save.json')
        sleep(2)
        menu()

def savegame():
    system('cls')
    global fn
    global ln
    global age
    global gdr
    global bio
    global hunger
    global bladder
    global hygiene
    global energy
    global comfort
    global fun
    global cash
    global day
    global version
    global cheats
    global difficulty
    
    save = {'fn':fn,'ln':ln,'age':age,'gdr':gdr,'bio':bio,
            'hunger':hunger,'bladder':bladder,'hygiene':hygiene,
            'energy':energy,'comfort':comfort,'fun':fun,'cash':cash,
            'day':day,'version':version,'cheats':cheats,'difficulty':difficulty}
    try:
        open ('save.json','r')
        schc = input('Do you want to overwrite an existing save? (y/n) ')
        if schc == 'y':
            with open('save.json', 'w') as ts:
                json.dump(save, ts, indent=4)
            print('Saving Succesful')
            sleep(2)
            panel()
        else:
            panel()
        
        
    except FileNotFoundError:
        with open('save.json', 'w') as ts:
            json.dump(save, ts, indent=4)
            print('Saving Succesful')
    sleep(1)
    panel()


def newgame():
    global fn
    global ln
    global age
    global gdr
    global bio
    global hunger
    global bladder
    global hygiene
    global energy
    global comfort
    global fun
    global cash
    global day
    global cheats
    global asavet
    global autosave
    global difficulty
    
    system('cls')
    
    print('Difficulty\n\n')
    print('1 - Normal Difficulty; suitable for regular players. (x1 Loss of moods, cost of food, etc.)')
    print('2 - Hard Difficulty; suitable for hardcore players. (x2 Loss of moods, cost of food, etc.)')
    difsel = input('Selection: ')
    if difsel == 1:
        difficulty = 1
    if difsel == 2:
        difficulty = 2
    
    system('cls')
    debg = input('Debug? (y/n) ')
    if debg == 'y':
        fn = 'DEBUG'
        ln = 'DEBUG'
        age = 'DEBUG'
        gdr = 'DEBUG'
        bio = 'DEBUG MODE ACTIVATED'
        
        hunger = 100
        bladder = 100
        hygiene = 100
        energy = 100
        comfort = 100
        day = 0
        fun = 100
        cash = random.randint(100,2000)
        cheats = 'False'
        
        mood()
        
    print('Customize your Simulat.')
    fn = input('First Name: ')
    ln = input('Last Name: ')
    age = input('Age: ')
    gdr = input('Gender: ')
    bio = str(input('Biography (optional): '))
    if bio == '':
        bio = 'none'
    sleep(1)
    system('cls')
    print('PREVIEW:\n\nFirst Name: ',fn,'\nLast Name:', ln,'\nAge:', age,'\nGender:', gdr,'\nBiography:', bio,'\n\nIs it right?')
    ngcfr = input('(yes/no) ')
    if ngcfr == 'yes':
        hunger = 100
        bladder = 100
        hygiene = 100
        energy = 100
        comfort = 100
        day = 0
        fun = 100
        cash = random.randint(100,2000)
        cheats = 'False'
        autosave = 'True'

        mood()
    else:
        newgame()

def dayadd():
    global day
    global mood
    global hunger
    global bladder
    global hygiene
    global energy
    global comfort
    global fun
    day += 1

    hunger -= random.randint(2,6)
    bladder -= random.randint(2,6)
    hygiene -= random.randint(2,6)
    energy -= random.randint(2,6)
    comfort -= random.randint(2,6)
    fun -= random.randint(2,6)
    mood()

def mood():
    global oneeds
    global mood
    
    oneeds = hunger+bladder+hygiene+energy+comfort+fun
    if oneeds >= 0:
        mood = 'Dying'
    if oneeds >= 50:
        mood = 'Necgleted'
    if oneeds >= 100:
        mood = 'Unsatisfied'
    if oneeds >= 300:
        mood = 'Fine'
    if oneeds >= 500:
        mood = 'Happy'
    if oneeds >= 550:
        mood = 'Very Happy'
    panel()

def panel():
    system('cls')
    
    global hunger
    global bladder
    global hygiene
    global energy
    global comfort
    global fun
    global cash
    global day
    global fn
    global ln
    global age
    global asavet
    global mood
    global cheats
    global version
    global versionsave
    global oldsave
    global autosave
    global difficulty
    
    if autosave == 'True':
        if asavet <= 0:
            system('cls')
            sleep(random.randint(4,6))
            print('Out of memory.\n\n\nPossible problems:\nAutosave Interval set below 0.\nBecause developer said so.')
            sleep(3)
            menu()
            savegame()

    print(version)
    if oldsave == 1:
        print('You are playing on an Old save file. Your game may be unstable.\nSave Version:', versionsave)
    if cheats == 'True':
        print('\nCHEATS ENABLED')
    if difficulty == 1:
        print('Difficulty: Normal')
    else:
        print('Difficulty: Hard')
    
    
    print('\n\nDay: ',day)
    print('\nSimulat Data:',fn ,ln,'/', age)
    print('Mood: ',mood)
    print('\nNeeds:','\n\tBladder:', bladder,'\n\tComfort:', comfort,'\n\tEnergy:', energy,'\n\tFun:', fun,'\n\tHunger:', hunger,'\n\tHygiene:', hygiene)
    print('\n\nInteractions:\n\tshop - Go shopping.\n\tcook - Cook some food.\n\t')
    pnlchc = input('Selection: ')
    if pnlchc == 'save':
        savegame()
    if pnlchc == 'menu':
        system('cls')
        mchc = input('Are you sure to exit to main menu? (y/n) ')
        if mchc == 'y':
            menu()
        else:
            panel()
    
    if pnlchc == 'skip':
        dayadd()
    if pnlchc == 'cheat.mmd':
        cheats = 'True'
        
        hunger = 100
        bladder = 100
        hygiene = 100
        energy = 100
        comfort = 100
        fun = 100
        mood()
        
    if pnlchc == 'cook':
        cook()
    
    else:
        system('cls')
        print('Invalid command.')
        sleep(1)
        panel()

def cook():
    global hunger
    global fun

    system('cls')
    print(version)
    print('\n\nCook:\n\tBread - $3 / Hunger +8; Fun -3\n\tSandwich - $5 / Hunger +12; Fun -1\n\tChicken Soup - $9 / Hunger +18; Fun +1\n\tSteak - $35 / Hunger +34; Fun +12')
    print('\n\nOrder:\n\tParway - $4 / Hunger +10; Fun -2\n\tMcJohn\'s - $12 / Hunger +17;  Fun -6\n\tPizza - $13 / Hunger +15; Fun +9')

def start():
    system('cls')
    print("""
          
         ███████╗██╗███╗   ███╗██╗   ██╗██╗      █████╗ ████████╗    ██╗    ██╗ ██████╗ ██████╗ ██╗     ██████╗ 
         ██╔════╝██║████╗ ████║██║   ██║██║     ██╔══██╗╚══██╔══╝    ██║    ██║██╔═══██╗██╔══██╗██║     ██╔══██╗
         ███████╗██║██╔████╔██║██║   ██║██║     ███████║   ██║       ██║ █╗ ██║██║   ██║██████╔╝██║     ██║  ██║
         ╚════██║██║██║╚██╔╝██║██║   ██║██║     ██╔══██║   ██║       ██║███╗██║██║   ██║██╔══██╗██║     ██║  ██║
         ███████║██║██║ ╚═╝ ██║╚██████╔╝███████╗██║  ██║   ██║       ╚███╔███╔╝╚██████╔╝██║  ██║███████╗██████╔╝
         ╚══════╝╚═╝╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝        ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═════╝
                                                             __                                        
                                                             II
                                                    (c) playerDef Group
        """)
    sleep(2)
    loadsettings()

def settings():
    system('cls')
    print('Settings Menu\n\nmenu - Goes back to Main Menu\n\n\nSave Settings\nautosave - Autosave Menu')
    setch = input('Selection: ')
    if setch == 'autosave':
        autosavemenu()
    if setch == 'menu':
        savesettings()
        menu()
    else:
        system('cls')
        print('Invalid Command.')
        sleep(1)
        settings()
        
def autosavemenu():
    global autosave
    global asavet
    system('cls')
    print('Autosave Menu\n\n\nAutosave State')
    if autosave == 'True':
        print('Autosave is currently ENABLED.')
    else:
        print('Autosave is currently DISABLED')
    print('\n\n\nAutosave Interval\nAutosave Interval is currently set to:', asavet, 'days.')
    print('\n\n\nCommands:\ntoggle - Toggles Autosave\ninterval - Changes Autosave Interval.\nback - Goes back to Settings Menu.')
    assel = input('Selection: ')
    if assel == 'toggle':
        if autosave == 'True':
            autosave = 'False'
            autosavemenu()
        else:
            autosave = 'True'
            autosavemenu()
    if assel == 'interval':
        
        system('cls')
        print('Autosave Interval is currently set to:', asavet, 'days.')
        try:
            asavet = int(input('Type new interval: '))
            autosavemenu()
        except ValueError:
            system('cls')
            print('Specified Value is not a number.')
            sleep(2)
            autosavemenu()
        

def menu():
    global oldsave
    oldsave=0
    system('cls')
    
    
    print('Simulat World II Main Menu\n\n\nnew - Starts a new game.\nload - Loads a saved game.\nsettings - Opens settings.\nexit - Quit to desktop.')
    menuchoice = input('Choice: ')
    if menuchoice == 'new':
        newgame()
        
    if menuchoice == 'load':
        loadgame()
    
    if menuchoice == 'settings':
        settings()
    
    if menuchoice == 'exit':
        system('cls')
        print('Quitting Game...')
        sleep(2)
        exit()
        
    else:
        system('cls')
        print('Invalid command.')
        sleep(1)
        menu()
        

start()

