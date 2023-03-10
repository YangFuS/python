class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        if self.next:
            return str(self.val) + '->' + self.next.__str__()
        else:
            return str(self.val)


class ListNodeTool:
    def create_ListNode(self, arr: list) -> ListNode | None:
        """
        函数功能：创建链表
        :param arr: 节点列表
        :return: 链表头节点
        """
        if len(arr) == 0:
            return None
        root = ListNode(arr[0])
        cur = root
        for i in range(1, len(arr)):
            tmp = ListNode(arr[i])
            cur.next = tmp
            cur = cur.next
        return root

    def ReverseList(self, pHead: ListNode) -> ListNode | None:
        """
        函数功能：翻转链表
        :param pHead: 待翻转链表
        :return: 翻转后的链表
        """
        pre = None
        cur = pHead
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        """
        将一个节点数为 size 链表 m 位置到 n 位置之间的区间反转，要求时间复杂度 O(n)，空间复杂度 O(1)。
        例如：
        给出的链表为1→2→3→4→5→NULL, m=2,n=4
        1→4→3→2→5→NULL.

        数据范围： 链表长度 0 <size≤1000，0<m≤n≤size，链表中每个节点的值满足 ∣val∣≤1000
        :param head:
        :param m:
        :param n:
        :return:
        """
        res = ListNode(-1)
        res.next = head
        pre = res
        cur = head
        for i in range(1, m):
            pre = cur
            cur = cur.next
        for i in range(m, n):
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = pre.next
            pre.next = tmp
        return res.next

    def EntryNodeOfLoop(self, pHead: ListNode):
        """
        函数功能：查找环的入口节点
        :param pHead: 链表
        :return: 环的入口节点
        """
        # write code here
        if not pHead or not pHead.next:
            return None
        p_slow = pHead
        p_fast = pHead
        while p_fast.next and p_fast.next.next:
            p_slow = p_slow.next
            p_fast = p_fast.next.next
            if p_fast == p_slow:
                break
        if p_fast.next is None or p_fast.next.next is None:
            return None
        p_fast = pHead
        while p_fast != p_slow:
            p_fast = p_fast.next
            p_slow = p_slow.next
        return p_fast


test = [1, 2, 3, 4, 5]
tool = ListNodeTool()
root = tool.create_ListNode(test)
print(root)
print(tool.reverseBetween(root, 2, 4))
