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
    pub fn nodes_between_critical_points(head: Option<Box<ListNode>>) -> Vec<i32> {
        let Some(mut prev) = head.as_deref() else {
            return vec![-1, -1];
        };
        let Some(mut cur) = prev.next.as_deref() else {
            return vec![-1, -1];
        };

        let (mut i, mut first, mut last, mut min) = (1, -1, -1, i32::MAX);

        while let Some(next) = cur.next.as_deref() {
            let is_critical = (cur.val > prev.val && cur.val > next.val) || (cur.val < prev.val && cur.val < next.val);

            if is_critical {
                if first == -1 {
                    first = i;
                } else {
                    min = min.min(i - last);
                }
                last = i;
            }

            prev = cur;
            cur = next;
            i += 1;
        }

        if min == i32::MAX {
            vec![-1, -1]
        } else {
            vec![min, last - first]
        }
    }
}
