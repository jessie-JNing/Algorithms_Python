from Stack import Stack

class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t


    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key



def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree


def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

def inorder(tree):
      if tree != None:
          inorder(tree.getLeftChild())
          print(tree.getRootVal())
          inorder(tree.getRightChild())


def printexp(tree):
      sVal = ""
      if tree:
          sVal = '(' + printexp(tree.getLeftChild())
          sVal = sVal + str(tree.getRootVal())
          sVal = sVal + printexp(tree.getRightChild())+')'
      return sVal



if __name__=="__main__":
    r = BinaryTree('a')
    print "root:", (r.getRootVal())

    r.insertLeft('b')
    print "left child:", (r.getLeftChild().getRootVal())

    r.insertRight('c')
    print "right child:", (r.getRightChild().getRootVal())

    r.getRightChild().setRootVal('hello')
    print "Reset root:", (r.getRightChild().getRootVal())

    pt = buildParseTree("( ( 10 + 5 ) * 3 )")
    pt.postorder()  #defined and explained in the next section

