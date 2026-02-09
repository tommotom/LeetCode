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
    pub fn is_balanced(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        fn helper(node: &Option<Rc<RefCell<TreeNode>>>) -> i32 {
            match node {
                None => 0,
                Some(n) => {
                    let n = n.borrow();
                    let left = helper(&n.left);
                    let right = helper(&n.right);
                    if left == -1 || right == -1 {
                        return -1;
                    }
                    if (left - right).abs() > 1 {
                        return -1;
                    }
                    1 + left.max(right)
                }
            }
        }
        helper(&root) != -1
    }
}
