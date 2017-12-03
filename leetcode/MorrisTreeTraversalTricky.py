# https://codefights.com/interview-practice/task/jAKLMWLu8ynBhYsv6/description
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def kthSmallestInBST(t, k):
    
    count = 0
    
    # Morris preorder traversal
    while t != None:
        # print(count, t.value)
        # Done with the left branch. Visit myself now.
        if t.left == None:
            count += 1
            if count == k:
                cand = t.value
                return cand           # yay, done!
            t = t.right
        else:
            # find the in-order predecessor
            # I am the last guy in the left branch you need to visit. After you visit me, I open up route to yourself and your right branch!
            pred = t.left
            while pred.right != None and pred.right != t:
                pred = pred.right
            
            if pred.right == t:
                count += 1
                if count == k:
                    cand = t.value
                    return cand           # yay, done!
                # Backthreaded, and we are back. We must visit.
                # Time to unlink and part ways.
                # Left section done. Can explore right now.
                pred.right = None
                t = t.right                
            else:
                # Exploring the left. Let's backthread so we can find our way back when we are done.
                pred.right = t
                t = t.left
