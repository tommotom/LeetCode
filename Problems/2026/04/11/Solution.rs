use std::collections::HashMap;
use std::collections::VecDeque;

impl Solution {
    pub fn minimum_distance(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut map: HashMap<i32, VecDeque<usize>> = HashMap::new();
        let mut ans = i32::MAX;
        for i in 0..n {
            let mut arr = map.entry(nums[i]).or_insert(VecDeque::new());
            arr.push_back(i);
            if arr.len() == 3 {
                ans = ans.min(((arr[1] - arr[0]) + (arr[2] - arr[1]) + (arr[2] - arr[0])) as i32);
                arr.pop_front();
            }
        }
        if ans == i32::MAX { -1 } else { ans }
    }
}
