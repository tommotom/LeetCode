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
use std::collections::VecDeque;
impl Solution {
    pub fn largest_values(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut ans = Vec::new();

        let mut q = VecDeque::new();
        if let Some(r) = root {
            q.push_back(r);
        }

        while !q.is_empty() {
            let mut level_max = i32::MIN;
            for _ in 0..q.len() {
                let node = q.pop_front().unwrap();
                let node_ref = node.borrow();
                level_max = level_max.max(node_ref.val);
                if let Some(left) = &node_ref.left {
                    q.push_back(left.clone());
                }
                if let Some(right) = &node_ref.right {
                    q.push_back(right.clone());
                }
            }
            ans.push(level_max);
        }

        return ans;
    }
}
