import os
import sys
import time
import getpass

text = ""
print("""
  _________              __  .__  _____       
 /   _____/_____   _____/  |_|__|/ ____\__.__.
 \_____  \\____ \ /  _ \   __\  \   __<   |  |
 /        \  |_> >  <_> )  | |  ||  |  \___  |
/_______  /   __/ \____/|__| |__||__|  / ____|
        \/|__|                         \/     
___________.__                                
\__    ___/|  |__   ____   _____   ____       
  |    |   |  |  \_/ __ \ /     \_/ __ \      
  |    |   |   Y  \  ___/|  Y Y  \  ___/      
  |____|   |___|  /\___  >__|_|  /\___  >     
                \/     \/      \/     \/      
   _____                .__  .__              
  /  _  \\ ______ ______ |  | |__| ___________ 
 /  /_\\  \\\____ \\\____ \\|  | |  |/ __ \\_  __ \\
/    |    \\  |_> >  |_> >  |_|  \\  ___/|  | \/
\____|__  /   __/|   __/|____/__|\___  >__|   
        \\/|__|   |__|                \/       
-----------------------------------------------
By SimplyAmazing | Beta Edition\n
Loading.... -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
""")
time.sleep(3)
os.system(f'cmd /c "cls"')
print(f'Spotify Theme Applier (STA) | By SimplyAmazing > v0.2-beta')
print(f'-------------------------------------------------------------\n')
try:
    if not os.path.exists(f"C:/Users/{getpass.getuser()}/AppData/Local/Spotify/"):
        print(f'Spotify Desktop is not installed! You can install it here: https://www.spotify.com/au/download/windows/')
        time.sleep(7)
        exit()
    if not os.path.exists(f"C:/Users/{getpass.getuser()}/.spicetify/"):
        print(f'Spicetify is not installed! You can install it here: https://www.ghacks.net/2019/10/25/how-to-customize-spotify-with-spicetify-cli-themes/')
        time.sleep(7)
        exit()
    counter = []
    for folder in os.listdir(f"C:/Users/{getpass.getuser()}/.spicetify/Themes/"):
        if not len(counter) == 0:
            text = text + ", "
        counter.append("random")
        text = text + folder
    text = text + "."
    if len(counter) == 0:
        print(f'You haven\'t installed a Spicetify theme yet! You can find a bunch of community made ones at: https://github.com/morpheusthewhite/spicetify-themes')
        time.sleep(7)
        exit()
    print("Available Themes: " + text + "\n")
    theme = input("Please enter the NAME of a custom Spotify theme to apply! ")
    if not theme in os.listdir(f"C:/Users/{getpass.getuser()}/.spicetify/Themes/"):
        print(f'That is not a valid Spicetify theme! Please enter a name from the list above!')
        time.sleep(3)
        os.startfile(__file__)
        sys.exit()
    else:
        os.system(f'cmd /c "spicetify config current_theme {theme}"')
        os.system(f'cmd /c "spicetify apply"')
        os.system(f'cmd /c "cls"')
        print(f'Spotify Theme Applier (STA) | By SimplyAmazing > v0.2-beta')
        print(f'-------------------------------------------------------------\n')
        choice = input(f'Your selected theme ({theme}) has been applied! Do you want to close this tool? (Y/N) ')
        if choice.lower() == "y":
            exit()
        elif choice.lower() == "n":
            print(f'\nThe tool will now reload. Please wait...')
            time.sleep(2)
            os.startfile(__file__)
            sys.exit()
        else:
            print(f'\nInvalid choice! Assuming your answer was Y, and closing tool.')
            time.sleep(2)
            exit()
except Exception as e:
    os.system(f'cmd /c "cls"')
    print(f'Spotify Theme Applier (STA) | By SimplyAmazing > v0.2-beta')
    print(f'-------------------------------------------------------------\n')
    print(f'An error occurred that stopped the process from running further.')
    print(f'The error has been printed below, please check the GitHub page for a list of known bugs and fixes: https://github.com/AmAComputerNerd/SpotifyThemeApplier/issues')
    print(f'\nError - {e}')
