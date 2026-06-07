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
use std::collections::{HashSet,HashMap};
impl Solution {
    pub fn create_binary_tree(descriptions: Vec<Vec<i32>>) -> Option<Rc<RefCell<TreeNode>>> {
        let mut map = HashMap::new(); let mut set = HashSet::new();
        let mut get = |v| { map.entry(v).or_insert_with(|| Rc::new(RefCell::new(TreeNode::new(v)))).clone() };
        for d in descriptions {
            let child = get(d[1]);
            let mut parent = get(d[0]); let mut parent = parent.borrow_mut();
            set.insert(d[1]);
            *(if d[2] > 0 { &mut parent.left } else { &mut parent.right }) = Some(child)
        }
        map.into_values().find(|v| !set.contains(&v.borrow().val))
    }
}
