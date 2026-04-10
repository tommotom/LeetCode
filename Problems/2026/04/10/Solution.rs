impl Solution {
    pub fn minimum_distance(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut ans = -1;
        for i in 2..n {
            for j in 1..i {
                for k in 0..j {
                    if nums[i] == nums[j] && nums[j] == nums[k] {
                        let dist = (i as i32 - j as i32).abs() + (j as i32 - k as i32).abs() + (k as i32 - i as i32).abs();
                        if ans == -1 {
                            ans = dist
                        } else {
                            ans = ans.min(dist);
                        }
                    }
                }
            }
        }
        ans
    }
}
