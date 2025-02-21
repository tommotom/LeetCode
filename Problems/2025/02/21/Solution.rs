use std::{cell::RefCell, collections::HashSet, rc::Rc};

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
struct FindElements {
    values: HashSet<i32>,
}

macro_rules! node_as_ref {
    ($node:expr) => {
        $node
        .as_ref()
        .map(|root| root.borrow())
        .as_ref()
        .map(|umm| &**umm)
    }
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl FindElements {

    fn new(root: Option<Rc<RefCell<TreeNode>>>) -> Self {
        let mut values = HashSet::new();

        fn dfs_set_node(node: Option<&TreeNode>, value: i32, values: &mut HashSet<i32>) {
            let Some(node) = node else {
                return
            };
            values.insert(value);
            dfs_set_node(node_as_ref!(node.left), value * 2 + 1, values);
            dfs_set_node(node_as_ref!(node.right), value * 2 + 2, values);
        }

        dfs_set_node(node_as_ref!(root), 0, &mut values);

        Self { values }
    }

    fn find(&self, target: i32) -> bool {
        self.values.contains(&target)
    }
}

/**
 * Your FindElements object will be instantiated and called as such:
 * let obj = FindElements::new(root);
 * let ret_1: bool = obj.find(target);
 */
