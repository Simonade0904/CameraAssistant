from ScrapeGoodwill import generateGoodwillObj
from ScrapeEbay import generateEbayObj
from ListingTree import buildTree, generateTreeTemplate
import pickle
import webbrowser as w

# Reference: https://stackoverflow.com/questions/8924173/how-to-print-bold-text-in-python
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def scrapeWithCache(brand):
    print("Fetching camera data, this may take a minute or two ... ")
    try:
        goodwillObjects = []
        ebayObjects = []
        try:
            goodwillObjects = generateGoodwillObj(brand)
            print('Great! We got camera data from ShopGoodwill ... ')
        except:
            print("Sorry! We did not get camera information from Goodwill. It's not your fault. If you want, please try again later.")
        try:
            ebayObjects = generateEbayObj(brand)
            print('Great! We got camera data from eBay ... ')
        except:
            print("Sorry! We did not get camera information from eBay. It's not your fault. If you want, please try again later.")
        allObjects = goodwillObjects + ebayObjects
        f = open(f"{brand}.p","wb")
        pickle.dump(allObjects, f)
        f.close()
        print('Done! Thanks for waiting!')
        return(allObjects)
    except:
        print("Sorry! Our search encountered an error. It's most likely not your fault. Please contact the developer or try again later.")
        quit()

def checkIsCached(brand):
    try:
        f = open(f"{brand}.p", "rb")
        f.close()
        return(True)
    except:
        return(False)


def retrieveFromCache(brand):
    try:
        f = open(f"{brand}.p", "rb")
        allObjects = pickle.load(f)
        f.close()
        return(allObjects)
    except:
        print("Sorry! Our cache retriever encountered an error. It's most likely not your fault. Please contact the developer.")
        quit()

def toLowerCase(brandName):
    return brandName.lower()



def ask(question):
    """
    Accepts a question statement and requests a yes or no answer from the user. Returns the user's answer as a boolean value

    Parameters
    ----------
    question: string

    Returns
    -------
    bool
        A boolean value for the user's answer to the question
    """
    yes_list = ['yes','y','yeah','yep','sure','correct','right','true']
    no_list = ['no','n','nope','nah','na','incorrect','wrong','false']
    while True:
        decision = input(color.BLUE + question + ' ' + color.END)
        if decision in yes_list:
            return True
        elif decision in no_list:
            return False
        else:
            print("Please enter a valid response.")

def exploreTree(tree):
    if tree.yes == None and tree.no == None:
        return tree.objects
    else:
        if ask(tree.question):
            return exploreTree(tree.yes)
        else:
            return exploreTree(tree.no)

def printObjList50(objects):
    if len(objects) <= 50:
        for index, obj in enumerate(objects):
            print(str(index + 1) + ' ' + str(obj) + '\n')
    else:
        for index, obj in enumerate(objects[0:50]):
            print(str(index + 1) + ' ' + str(obj) + '\n')

def printObjListAll(objects):
    for index, obj in enumerate(objects):
        print(str(index + 1) + ' ' + str(obj) + '\n')

def objectDetail(obj):
    while True:
        print(color.BOLD+'\nThis is the item you selected:\n'+color.END + obj.print_full() + '\n')
        command = input(color.BOLD+"What you can type next: \n" +color.END +"\tvisit -- see the item in your browser \n\tback -- go back to the menu with all items\n")
        if command == 'visit':
            w.open(obj.url)
        elif command == 'back':
            print(color.BOLD+color.GREEN+"\nYou are now back to camera recommendation list."+color.END+'\n')
            return
        else:
            print(color.RED+"Invalid command. Please try again."+color.END)


def itemsBrowser(selectedObjects):
    print(color.BOLD+color.GREEN+"\nThank you for the responses! Your camera recommendation list is now ready."+color.END+'\n')

    while True:
        command = input(color.BOLD+"What you can type next: \n" +color.END +"\tlist -- a quick view of your camera recommendation list, up to first 50 items \n\tfull -- your full camera recommendation list \n\ta number such as 23 -- explore the specific listing \n\tdata -- see some data about your recommendations\n\tquit -- quit this application \n")
        if command == 'list':
            printObjList50(selectedObjects)
        elif command == 'full':
            printObjListAll(selectedObjects)
        elif command == 'quit':
            quit()
        else:
            try:
                if int(command) in range(len(selectedObjects)):
                    objectDetail(selectedObjects[int(command)-1])
            except:
                print(color.RED+"Invalid command. Please try again."+color.END)


def main():
    print(color.BOLD+color.UNDERLINE+"\nWelcome to the CAMERA ASSISTANT! We will help you find cameras, especially film cameras, that you love!"+color.END)
    brand = toLowerCase(input(color.BOLD+'\nWhich brand of film camera would you like to explore? You can try typing Canon, Nikon, or Minolta. These are all reputable brands. '+color.END))

    cameraObjects = []

    if checkIsCached(brand):
        if ask(color.BOLD+f"\nLooks like we have stored some data for the brand '{brand}'. Would you like to use the locally stored data? "+color.END):
            cameraObjects = retrieveFromCache(brand)
        else:
            print(color.BOLD+"\nVery well, we will go online and find information about this brand."+color.END)
            cameraObjects = scrapeWithCache(brand)
    else:
        print(color.BOLD+"\nGreat choice! We will go online and find information about this brand."+color.END)
        cameraObjects = scrapeWithCache(brand)

    questionTree = generateTreeTemplate()
    buildTree(cameraObjects, questionTree)
    
    selectedObjects = exploreTree(questionTree)
    itemsBrowser(selectedObjects)

if __name__ == '__main__':
    main()