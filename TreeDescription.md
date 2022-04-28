# Description of the data structure

__Data type: Tree__

There are two types of nodes inside the tree: 
1. ListingTreeQuestion: These are the nodes with branches on the tree. A typical ListingTreeQuestion node will represent a yes or no question that will be asked in my app. There will be two branches, “yes” and “no”, each of which contains another question or a leaf node (ListingTreeObjects). Each ListingTreeQuestion also contains a function to help determine if a specific Listing belongs to the "yes" category or a "no" category. This function is extremely useful for sorting all the camera listings in preparation for a human user.
2. ListingTreeObjects: These are effectively the leaf nodes inside the tree. They represent the outcome of going through ListingTreeQuestion in certain directions. Each ListingTreeObjects would store some Listing objects. The Listing objects are saved there by ListingTreeQuestion

There are two ways to go down the tree from the root node (an initial question). In the tree-building phase of the application, the tree would accept a list of Listing objects and one by one, automatically send them down the tree. Each Listing object, depending on its attributes, would be sorted down the chain of ListingTreeQuestions until it reaches a ListingTreeObjects node. At that point, this object will be added to the list of objects contained in the ListingTreeObjects node. That means when an actual user explores the tree by answering questions, the correct Listing objects would wait for them at the end once they reach a ListingTreeObjects node and access its payload.

To accomplish this complex task, there are also some helper functions for the tree classes:
1. printTree -- prints out a tree in human-readable format. Useful for unit testing.
2. buildTree and recursiveBuild -- pre-populates the ListingTreeObjects automatically using camera listing data.
3. generateTreeTemplate -- This is a function that builds a pre-defined tree based on the set of questions we want to ask the users.