#EXERCISE NO. 6 - STACK
#Alinea Grace M. Del Mundo
#github.com/aubreybaes
#This program sorts your playlist  either by name (alphabetical order) or by time (from the recently added up to the the oldest one)
# and displays the currently playing song and the next song at the same time

class Stack:
    def __init__(self):
        self.items = ["Bugs Bunny",
                      "Scooby-Doo",
                      "Tom and Jerry",
                      "Mickey Mouse",
                      "Johnny Bravo",
                      "Spongebob SquarePants",
                      "Snoopy",
                      "Donald Duck",
                      "Popeye",
                      "Dexter's Laboratory",
                      "Winnie-the-Pooh",
                      "Dragonball Z",
                      "Super Mario",]
        self.items2 = sorted(self.items)  #to peek the sorted items in the original list
        self.items3 = self.items2[::-1]   #to peek the reversed original list

    def sort(self):
        return sorted(self.items2)
    def reverse(self):
        return self.items2[::-1]
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peekname(self):
        return self.items3[len(self.items)-1]
    def peeknamenext(self):
        return self.items3[len(self.items)-2]
    def peektime(self):
        return self.items[len(self.items)-1]
    def peektimenext(self):
        return self.items[len(self.items)-2]
    def size(self):
        return len(self.items)




if __name__ == "__main__":
    alea = Stack()
    print "Cartoon Characters"
    print "There are",alea.size(),"cartoons characters"
    x = input("Sort by:\n1. Name(A-Z)\n2.Time(new-old)\n\tEnter your choice: ")
    if x == 1:
        while alea.size() >= 2:
            print "Now Watching ",alea.peekname()
            print "Next cartoon is ",alea.peeknamenext(), "\n - - - - - - - - - - - - - - - - - - "
            alea.pop()
    elif x == 2:
        while aub.size() >= 2:
            print "Now Watching ",alea.peektime()
            print "Next cartoon is ", alea.peektimenext(), "\n - - - - - - - - - - - - - - - - - - "
            alea.pop()
    else:
        print "INVALID SORTING"
        



