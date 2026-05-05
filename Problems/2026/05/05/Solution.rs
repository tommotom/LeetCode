impl Solution {
    pub fn rotate_right(head: Option<Box<ListNode>>, k: i32) -> Option<Box<ListNode>> {
        if head.is_none() || k == 0 { return head; }

        let mut head = head;
        let mut len = 0;
        let mut curr = &head;

        while let Some(node) = curr {
            len += 1;
            curr = &node.next;
        }

        let k = k % len;
        if k == 0 { return head; }

        let mut curr = head.as_mut().unwrap();
        for _ in 0..(len - k - 1) {
            curr = curr.next.as_mut().unwrap();
        }

        let mut new_head = curr.next.take();
        let mut tail = new_head.as_mut().unwrap();

        while tail.next.is_some() {
            tail = tail.next.as_mut().unwrap();
        }
        tail.next = head;

        new_head
    }
}
