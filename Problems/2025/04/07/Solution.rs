use std::collections::HashSet;

impl Solution {
    pub fn can_partition(nums: Vec<i32>) -> bool {
        let sum: i32 = nums.clone().into_iter().sum();
        if sum % 2 == 1 {
            return false;
        }
        let target = sum / 2;
        let mut isReachable = HashSet::new();
        isReachable.insert(0);

        for num in nums {
            let mut reached = HashSet::new();
            for prev in &isReachable {
                if prev <= &target {
                    reached.insert(prev + num);
                }
            }
            for r in reached {
                isReachable.insert(r);
            }
        }

        isReachable.contains(&target)
    }
}
