from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length == self.capacity:
            # full
            new_cur = self.current.next
            # delete cur
            self.storage.delete(self.current)
            # set new current
            self.current = new_cur
            # insert before new_cur
            new_cur.insert_after(item)
            self.storage.length += 1

            # if new_cur == self.storage.head:
            #     self.storage.add_to_head(item)
            # else:
            #     new_cur.insert_before(item)
            #     self.storage.length += 1
            # # return print(self.current.prev.value)
        else:
            # availability
            self.storage.add_to_tail(item)
            self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        cur = self.storage.head
        while cur.next != None:
            list_buffer_contents.append(cur.value)
            cur = cur.next
        list_buffer_contents.append(cur.value)

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
