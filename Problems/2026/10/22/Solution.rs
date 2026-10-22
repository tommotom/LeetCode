impl Solution {
    pub fn min_operations(mut nums: Vec<i32>) -> i32 {
        fn helper(nums: Vec<i32>) -> i32 {
            let n = nums.len();
            let mut normal = true;
            let mut rev = true;
            let mut ans = i32::MAX;
            let mut min = 0;
            let mut max = 0;
            for i in 1..n {
                if nums[i] == 0 {
                    min = i;
                }
                if nums[i] == n as i32 - 1 {
                    max = i;
                }
                if nums[i] != 0 && nums[i-1] + 1 != nums[i] {
                    normal = false;
                }
                if nums[i] != n as i32 - 1 && nums[i-1] - 1 != nums[i] {
                    rev = false;
                }
            }
            if normal {
                ans = ans.min(min as i32);
            }
            if rev {
                ans = ans.min(max as i32 + 1);
            }
            ans
        }

        let mut ans = helper(nums.clone());
        nums = nums.into_iter().rev().collect();
        let mut ret = helper(nums);
        if ret != i32::MAX {
            ans = ans.min(ret + 1);
        }
        if ans == i32::MAX {-1} else {ans}
    }
}
