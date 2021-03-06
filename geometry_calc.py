from os import system, name
from modules.banners import PlaneGeo_banner, SolidGeo_banner, main_banner
from modules.PlaneGeometry.Triangle.menu import __triangle__
from modules.PlaneGeometry.Square.execute import Execute_Square
from modules.PlaneGeometry.Rectangle.execute import Execute_Rectangle
from modules.SolidGeometry.Cube.execute import Execute_Cube
from modules.SolidGeometry.RectangularPrism.execute import Execute_RectangularPrism
from modules.SolidGeometry.Sphere.execute import Execute_Sphere
from rich import print
import colorama
colorama.init()


def clear(): 

	# for windows 
	if name == 'nt': 
		_ = system('cls') 

	# for mac and linux(here, os.name is 'posix') 
	else: 
		_ = system('clear')

def MainMenu():
    clear()
    main_banner() #print banner and geometry calc menu
    def select_mainmenu():
        try:
            select_menu = int(input("\n\t  Select from the menu [ 1 | 2 | 3 | 99 ] : "))
            
            if select_menu == 1:
                PlaneGeo_Menu()

            elif select_menu == 2:
                SolidGeo_Menu()

            elif select_menu == 3:
                About_Menu()

            elif select_menu == 99:
                print("\n\n\t  Thank you for using Geometry Calc :)")
                exit()

            else:
                print("\n\t  [red][ERROR][/red] Select the menu correctly !")
                select_mainmenu()

        except ValueError:
            print("\n\t  [red][ERROR][/red] Your selection is invalid. Repeat again !")
            select_mainmenu()

        except KeyboardInterrupt:
            print("\n\n\t  Thank you for using Geometry Calc :)")
            exit()
    select_mainmenu()

def PlaneGeo_Menu():
    clear()
    PlaneGeo_banner() #print banner and plane geometry menu
    def select_planegeo_menu():
        try:
            select_planegeo = int(input("\n\t  Select from the menu : "))

            if select_planegeo == 1:    #square
                clear()
                Execute_Square()    # calculate square
                PlaneGeo_Menu()

            elif select_planegeo == 2:  #rectangle
                clear()
                Execute_Rectangle() # calculate rectangle
                PlaneGeo_Menu()

            elif select_planegeo == 3:  #triangle
                clear()
                __triangle__()  # go to triangle calc submenu
                PlaneGeo_Menu()

            elif select_planegeo == 99:
                clear()
                MainMenu()

            else:
                print("\n\t  [red][ERROR][/red] Select the menu correctly !")
                select_planegeo_menu()

        except ValueError:
            print("\n\t  [red][ERROR][/red] Your selection is invalid. Repeat again !")
            select_planegeo_menu()

        except KeyboardInterrupt:
            print("\n\n\t  Thank you for using Geometry Calc :)")
            exit()
    select_planegeo_menu()

def SolidGeo_Menu():
    clear()
    SolidGeo_banner() #print banner and solid geometry menu
    def select_solidgeo_menu():
        try:
            select_solidgeo = int(input("\n\t  Select from the menu : "))

            if select_solidgeo == 1: #cube
                clear()
                Execute_Cube()  #calculate cube
                SolidGeo_Menu()

            elif select_solidgeo == 2: #Rectangular Prism
                clear()
                Execute_RectangularPrism()  #calculate rectangular prism
                SolidGeo_Menu()

            elif select_solidgeo == 3: # sphere
                clear()
                #input("Sphere calc in development. Press <enter> to continue\n")
                Execute_Sphere()   #calculate sphere
                SolidGeo_Menu()

            elif select_solidgeo == 99:
                clear()
                MainMenu()

            else:
                print("\n\t  [red][ERROR][/red] Select the menu correctly !")
                select_solidgeo_menu()

        except ValueError:
            print("\n\t  [red][ERROR][/red] Your selection is invalid. Repeat again !")
            select_solidgeo_menu()

        except KeyboardInterrupt:
            print("\n\n\t  Thank you for using Geometry Calc :)")
            exit()
    select_solidgeo_menu()

def About_Menu():
    try:
        from modules.about import printabout
        clear()
        printabout()
        MainMenu()

    except KeyboardInterrupt:
        print("\n\n\t  Thank you for using Geometric Calc :)")
        exit()

if __name__ == "__main__":
    MainMenu()