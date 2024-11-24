import sys
from nanoWizard import nanoWizard

def main():
    #get arguments
    wizard = nanoWizard()
    #pass command as 1 string
    args = ""
    if len(sys.argv) > 1:
        for arg in sys.argv:
            if arg != sys.argv[0]:
                args = args+" "+str(arg)
                
        wizard.runCommand(args)
    else :
        print("enter arguments")


    #
    

if __name__ == "__main__":
    main()