// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
//
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn delete_middle(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut vals = Vec::new();
        let mut cur = &head;

        while let Some(node) = cur {
            vals.push(node.val);
            cur = &node.next;
        }

        if vals.len() == 1 {
            return None;
        }

        let m = vals.len() / 2;
        vals.remove(m);

        let mut dummy = Box::new(ListNode::new(0));
        let mut tail = &mut dummy;

        for val in vals {
            tail.next = Some(Box::new(ListNode::new(val)));
            tail = tail.next.as_mut().unwrap();
        }

        dummy.next
    }
}
