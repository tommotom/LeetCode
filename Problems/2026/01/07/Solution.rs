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
    pub fn max_product(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        const MOD: i64 = 1_000_000_007;

        fn sum(node: &Option<Rc<RefCell<TreeNode>>>) -> i64 {
            node.as_ref().map_or(0, |n| {
                let n = n.borrow();
                n.val as i64 + sum(&n.left) + sum(&n.right)
            })
        }

        fn dfs(node: &Option<Rc<RefCell<TreeNode>>>, total: i64, best: &mut i64) -> i64 {
            node.as_ref().map_or(0, |n| {
                let n = n.borrow();
                let subtree_sum = n.val as i64 + dfs(&n.left, total, best) + dfs(&n.right, total, best);
                *best = (*best).max(subtree_sum * (total - subtree_sum));
                subtree_sum
            })
        }

        let total = sum(&root);
        let mut best = 0;
        dfs(&root, total, &mut best);
        (best % MOD) as i32
    }
}
