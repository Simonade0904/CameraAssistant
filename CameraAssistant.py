from ScrapeGoodwill import generateGoodwillObj
from ScrapeEbay import generateEbayObj
import pickle

def scrapeWithCache(brand):
    try:
        goodwillObjects = generateGoodwillObj(brand)
        ebayObjects = generateEbayObj(brand)
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


# a = 1
# def main():
#     initial = input("Hello! Welcome to the Camera Assistant. Press q to quit and press any key to start!")
