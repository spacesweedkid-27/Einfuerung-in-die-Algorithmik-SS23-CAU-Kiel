class Queue:
    """
    Class representing a Queue.
    """
    def __init__(self):
        """
        Constructor of an empty Queue.
        """
        self.list = []

    def is_empty(self):
        """
        Checks if the list storing the queue is empty, and returns the answer.
        """
        return self.list == []

    def enqueue(self, obj):
        """
        Enqueues an object into the Queue.
        :param obj: Object to be enqueued into the queue.
        """
        self.list += [obj]

    def dequeue(self):
        """
        Dequeues the top (oldest) element and returns it.
        :return: Top object of queue
        """
        # Is the queue empty?
        # Then return None as it is empty.
        if self.is_empty():
            return None
        # Store the current top value. It doesn't have to be copied because self.list[1:] creates a new list (but with
        # references to the old objects).
        val = self.list[0]
        # Update the queue as it has the top element removed now.
        self.list = self.list[1:]
        return val

    def top(self):
        """
        Returns top (oldest) element of queue.
        :return: Top element
        """
        return self.list[0]

    def __str__(self):
        """
        Used for debugging, just converts the list into a string and returns that string.
        :return: String representation of list
        """
        return str(self.list)


q = Queue()
q.list = [1, 2, 3]
q.enqueue(2)
q.enqueue(5)

print(q.top())      # -> 1
print(q.dequeue())  # -> 1
print(q.dequeue())  # -> 2
print(q.dequeue())  # -> 3
print(q.dequeue())  # -> 2

print(q.is_empty())
print(q.dequeue())  # -> 5
print(q.is_empty())
print(q.dequeue())  # -> None as the queue is empty now.
