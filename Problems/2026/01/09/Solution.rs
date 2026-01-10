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
use std::collections::HashMap;
impl Solution {
    pub fn subtree_with_all_deepest(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        fn helper(node: Option<Rc<RefCell<TreeNode>>>) -> (Option<Rc<RefCell<TreeNode>>>, i32) {
            match node {
                None => (None, 0),
                Some(n) => {
                    let left = helper(n.borrow().left.clone());
                    let right = helper(n.borrow().right.clone());

                    match left.1.cmp(&right.1) {
                        std::cmp::Ordering::Greater => (left.0, left.1 + 1),
                        std::cmp::Ordering::Less => (right.0, right.1 + 1),
                        std::cmp::Ordering::Equal => (Some(n.clone()), left.1 + 1),
                    }
                }
            }
        }

        helper(root).0
    }
}
