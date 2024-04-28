# You have a browser of one tab where you start on the homepage and you can visit
# another url, get back in the history number of steps or move forward in
# the history number of steps.


# BrowserHistory(string homepage) Initializes the object with the homepage
# of the browser.

# void visit(string url) Visits url from the current page. It clears up all the
# forward history.

# string back(int steps) Move steps back in history. If you can only return x
# steps in the history and steps > x, you will return only x steps. Return the
# current url after moving back in history at most steps.

# string forward(int steps) Move steps forward in history. If you can only
# forward x steps in the history and steps > x, you will forward only x steps.
# Return the current url after forwarding in history at most steps.

# CAN BE IMPLEMENTED WITH ARRAY WITH BETTER BIG-O



from typing import Optional, cast


class Node:
    def __init__(self, val):
        self.url = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = Node(homepage)


    def visit(self, url: str) -> None:
        new_node = Node(url)
        new_node.prev = self.current
        self.current.next = new_node
        self.current = self.current.next

    def back(self, steps: int) -> str:
        i = 0
        current = self.current

        while i != steps and current.prev != None:
            current = current.prev
            i += 1
        self.current = current
        return current.url


    def forward(self, steps: int) -> str:
        i = 0
        current = self.current

        while i != steps and current.next != None:
            current = current.next
            i += 1
        self.current = current
        return current.url


list = BrowserHistory('home')
list.visit('new')
list.visit('google')
list.visit('facebook')
list.visit('amazon')

list.back(3)
list.forward(3)

print(list.current.url)
