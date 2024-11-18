import Book
import ArrayList
import ArrayQueue
import RandomQueue
import DLList
import SLLQueue
import MaxQueue
import time
import ChainedHashTable
import BinarySearchTree
#import BinaryHeap
#import AdjacencyList
 
class BookStore:
    '''
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart.
    '''
 
    def __init__(self):
        self.bookCatalog = None
        self.shoppingCart = MaxQueue.MaxQueue()
        self.bookIndices = ChainedHashTable.ChainedHashTable()
        self.sortedTitleIndices = BinarySearchTree.BinarySearchTree()
 
    def loadCatalog(self, fileName: str):
        '''
            loadCatalog: Read the file filenName and creates the array list with all books.
                book records are separated by  ^. The order is key,
                title, group, rank (number of copies sold) and similar books
        '''
        self.bookCatalog = ArrayList.ArrayList()
        with open(fileName, encoding="utf8") as f:
            # The following line is the time that the computation starts
            start_time = time.time()
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                s = Book.Book(key, title, group, rank, similar)
                self.bookCatalog.append(s)
                #self.bookIndices.add(key, self.bookCatalog.size() - 1)
                self.sortedTitleIndices.add(title, self.bookCatalog.size() - 1)
            # The following line is used to calculate the total time
            # of execution
            elapsed_time = time.time() - start_time
            print(f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")
 
    def setRandomShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = RandomQueue.RandomQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")
 
    def setShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = ArrayQueue.ArrayQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")
 
    def removeFromCatalog(self, i: int):
        '''
        removeFromCatalog: Remove from the bookCatalog the book with the index i
        input:
            i: positive integer
        '''
        # The following line is the time that the computation starts
        start_time = time.time()
        self.bookCatalog.remove(i)
        # The following line is used to calculate the total time
        # of execution
        elapsed_time = time.time() - start_time
        print(f"Remove book {i} from books in {elapsed_time} seconds")
 
    def addBookByIndex(self, i: int):
        '''
        addBookByIndex: Inserts into the playlist the song of the list at index i
        input:
            i: positive integer
        '''
        # Validating the index. Otherwise it  crashes
        if i >= 0 and i < self.bookCatalog.size():
            start_time = time.time()
            s = self.bookCatalog.get(i)
            self.shoppingCart.add(s)
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {s} \n{elapsed_time} seconds")
 
    def searchBookByInfix(self, infix: str, cnt: int = 15):
        '''
        searchBookByInfix: Search all the books that contains infix
        input: 
            infix: A string    
        '''
        start_time = time.time()
        count = 0
 
        for i in self.bookCatalog:
            if infix in i.title:
                count += 1
                print(i)
            if count == cnt:
                break
 
        elapsed_time = time.time() - start_time
        print(f"searchBookByInfix Completed in {elapsed_time} seconds")
 
    def removeFromShoppingCart(self):
        '''
        removeFromShoppingCart: remove one book from the shopping cart
        '''
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            u = self.shoppingCart.remove()
            elapsed_time = time.time() - start_time
            print(f"removeFromShoppingCart {u} Completed in {elapsed_time} seconds")
 
    def getCartBestSeller(self):
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            best_seller = self.shoppingCart.max().title
            elapsed_time = time.time() - start_time
            print(f"getCartBestSeller returned \n{best_seller} \nCompleted in {elapsed_time}seconds")
            return best_seller
        else:
            return None
 
    def addBookByKey(self, key):
        start_time = time.time()
        i = self.bookIndices.find(key)
        if i is not None:
            book = self.bookCatalog.get(i)
            self.shoppingCart.add(book)
            elapsed_time = time.time() - start_time
            print(f"addBookByKey Completed in {elapsed_time} seconds")
            print(f"Added title: {book.title}")
        else:
            elapsed_time = time.time() - start_time
            print(f"addBookByKey Completed in {elapsed_time} seconds")
            print("Book not found...")
 
    def addBookByPrefix(self, prefix):
        if not prefix:
            return None
        i = self.sortedTitleIndices._find_next(prefix)
        if i is not None:
            book = self.bookCatalog.get(i.v)
            n = len(prefix)
            if book.title[0:n] == prefix:
                self.shoppingCart.add(book)
                return book.title
        return None
