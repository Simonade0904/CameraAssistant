class ListingTreeQuestion:
    def __init__(self, question, func, yes = None, no = None):
        self.question = question
        self.yes = yes
        self.no = no
        self.func = func

    def setYes(self, yes):
        self.yes = yes

    def setNo(self, no):
        self.no = no

    def setQuestion(self, question):
        self.question = question

class ListingTreeObjects:
    def __init__(self, objects = []):
        self.objects = objects
        self.yes = None
        self.no = None

    def addObject(self, newObject):
        self.objects.append(newObject)

def printTree(tree, prefix=''):
    try:
        if tree.yes == None and tree.no == None:
            try:
                print(f"---{tree.question}---")
            except AttributeError:
                try:
                    print(' '.join([prefix,f"There are {len(tree.objects)} objects"]))
                except AttributeError:
                    print(' '.join([prefix],"None here"))
        else:
            print(' '.join([prefix,f"---{tree.question}---"]))
            yesPrefix = ''.join([prefix,'->'])
            noPrefix = ''.join([prefix,'-x'])
            printTree(tree.yes, yesPrefix)
            printTree(tree.no, noPrefix)
    except:
        print("There might be a problem with the tree structure.")

def recursiveBuild(obj, tree):
    if tree.yes == None and tree.no == None:
        tree.addObject(obj)
    else:
        if tree.func(obj):
            recursiveBuild(obj, tree.yes)
        else:
            recursiveBuild(obj, tree.no)

def buildTree(objectList, treeBeginning):
    for obj in objectList:
        recursiveBuild(obj, treeBeginning)

def float_with_exception(value):
    floatVal = 0
    try:
        floatVal = float(value)
    except ValueError as e:
        floatVal = 200
    return floatVal

def generateTreeTemplate():
    Q1 = ListingTreeQuestion('Would you like to keep the budget within 100 dollars? Say yes to limit budget, say no to only look at items above 100 dollars.',lambda x: float_with_exception(x.price) <= 100)
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

if __name__ == '__main__':
    printTree(generateTreeTemplate())