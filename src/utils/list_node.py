class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def from_list(values):
        """从列表创建链表"""
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    @staticmethod
    def to_list(head):
        """将链表转换为列表"""
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        return values