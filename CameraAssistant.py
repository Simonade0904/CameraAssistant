from ScrapeGoodwill import generateGoodwillObj
from ScrapeEbay import generateEbayObj
from Listing import Listing
from ListingTree import ListingTreeQuestion, ListingTreeObjects, printTree
import pickle

def scrapeWithCache(brand):
    try:
        goodwillObjects = []
        ebayObjects = []
        try:
            goodwillObjects = generateGoodwillObj(brand)
        except:
            print("Sorry! We did not get camera information from Goodwill. It's not your fault. If you want, please try again later.")
        try:
            ebayObjects = generateEbayObj(brand)
        except:
            print("Sorry! We did not get camera information from eBay. It's not your fault. If you want, please try again later.")
        allObjects = goodwillObjects + ebayObjects
        f = open(f"{brand}.p","wb")
        pickle.dump(allObjects, f)
        f.close()
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

def recursiveBuild(obj, tree):
    if tree.yes == None and tree.no == None:
        tree.addObject(obj)
    else:
        if tree.func(obj):
            print("got a true")
            recursiveBuild(obj, tree.yes)
        else:
            print("got a false")
            recursiveBuild(obj, tree.no)

def buildTree(objectList, treeBeginning):
    for obj in objectList:
        recursiveBuild(obj, treeBeginning)

def generateTreeTemplate():
    Q1 = ListingTreeQuestion('Would you like to keep the budget within 100 dollars? Say yes to limit budget, say no to only look at items above 100 dollars.',lambda x: float(x.price) <= 100)
    Q2_1 = ListingTreeQuestion('Would you like to buy from auctions or fixed-price listings? Say yes to try auctions, say no to stick with fixed-price listings.', lambda x: x.buying_type == 'auction')
    Q2_2 = ListingTreeQuestion('Would you like to buy from auctions or fixed-price listings? Say yes to try auctions, say no to stick with fixed-price listings.', lambda x: x.buying_type == 'auction')
    ObjList1 = ListingTreeObjects([])
    ObjList2 = ListingTreeObjects([])
    ObjList3 = ListingTreeObjects([])
    ObjList4 = ListingTreeObjects([])
    Q1.setYes(Q2_1)
    Q1.setNo(Q2_2)
    Q2_1.setYes(ObjList1)
    Q2_1.setNo(ObjList2)
    Q2_2.setYes(ObjList3)
    Q2_2.setNo(ObjList4)
    return Q1

def main():
    questionTree = generateTreeTemplate()
    printTree(questionTree)
    print('\n')
    testList = retrieveFromCache('canon')
    buildTree(testList, questionTree)
    printTree(questionTree)

if __name__ == '__main__':
    main()