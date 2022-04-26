from ScrapeGoodwill import generateGoodwillObj
from ScrapeEbay import generateEbayObj
from Listing import Listing
from ListingTree import ListingTreeQuestion, ListingTreeObjects, printTree, buildTree, generateTreeTemplate
import pickle

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
        decision = input(question)
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

# def itemsBrowser(selectedObjects):
#     while True:
#         selectedObjects

def main():
    print("Welcome to the CAMERA ASSISTANT! We will help you find cameras, especially film cameras, that you love!")
    brand = toLowerCase(input('Which brand of film camera would you like to explore? You can try typing Canon, Nikon, or Minolta. These are all reputable brands.'))

    cameraObjects = []

    if checkIsCached(brand):
        if ask(f"Looks like we have stored some data for the brand '{brand}''. Would you like to use the locally stored data? "):
            cameraObjects = retrieveFromCache(brand)
        else:
            print("Very well, we will go online and find information about this brand.")
            cameraObjects = scrapeWithCache(brand)
    else:
        print("Great choice! We will go online and find information about this brand.")
        cameraObjects = scrapeWithCache(brand)

    questionTree = generateTreeTemplate()
    buildTree(cameraObjects, questionTree)
    
    selectedObjects = exploreTree(questionTree)
    print(selectedObjects)

if __name__ == '__main__':
    main()