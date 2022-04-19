class ListingTreeQuestion:
    def __init__(self, question, yes = None, no = None):
        self.question = question
        self.yes = yes
        self.no = no

    def setYes(self, yes):
        self.yes = yes

    def setNo(self, no):
        self.no = no
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

Q2 = ListingTreeQuestion("Question 2")
Q3 = ListingTreeQuestion("Question 3")
Q1 = ListingTreeQuestion("Question 1")
Q1.setYes(Q2)
Q1.setNo(Q3)
Obj1 = ListingTreeObjects()
Obj2 = ListingTreeObjects()
Obj3 = ListingTreeObjects()
Obj4 = ListingTreeObjects()
Q2.setYes(Obj1)
Q3.setNo(Obj2)
Q2.setNo(Obj3)
Q3.setYes(Obj4)
printTree(Q1)