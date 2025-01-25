use std::collections::VecDeque;
use std::collections::HashMap;

impl Solution {
    pub fn lexicographically_smallest_array(nums: Vec<i32>, limit: i32) -> Vec<i32> {
        let mut sorted = nums.clone();
        sorted.sort();
        let mut groups = Vec::new();
        let mut group = VecDeque::new();
        let mut g = 0;
        let mut num_to_group = HashMap::new();
        for i in 0..sorted.len() {
            if i > 0 && sorted[i] - sorted[i-1] > limit {
                groups.push(group);
                group = VecDeque::new();
                g += 1;
            }
            group.push_back(sorted[i]);
            num_to_group.insert(sorted[i], g);
        }
        groups.push(group);

        let mut ans = Vec::new();
        for num in nums {
            if let Some(g) = num_to_group.get(&num) {
                ans.push(groups[*g].pop_front().unwrap());
            }
        }

        ans
    }
}
