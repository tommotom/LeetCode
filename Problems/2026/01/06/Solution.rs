// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
//
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn max_level_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut res = vec![i32::MIN, 0];
        let mut cur = 0;
        let mut q = Vec::new();
        let mut new_q = Vec::new();

        q.push((root.unwrap(), 1));
        while let Some((node, level)) = q.pop() {
            cur += node.borrow().val;

            if let Some(left) = node.borrow().left.clone() {
                new_q.push((left, level + 1));
            }

            if let Some(right) = node.borrow().right.clone() {
                new_q.push((right, level + 1));
            }

            if q.is_empty() {
                std::mem::swap(&mut q, &mut new_q);
                if res[0] < cur {
                    res[0] = cur;
                    res[1] = level;
                }
                cur = 0;
            }
        }

        res[1]
    }
}
