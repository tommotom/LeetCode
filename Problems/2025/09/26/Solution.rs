impl Solution {
    pub fn triangle_number(mut nums: Vec<i32>) -> i32 {
        if nums.len() < 3 {
            return 0;
        }
        nums.sort();
        let mut ans = 0;
        for i in 0..(nums.len()-2) {
            if nums[i] == 0 {
                continue;
            }
            let mut k = i+2;
            for j in (i+1)..(nums.len()-1) {
                while k + 1 < nums.len() && nums[k+1] < nums[i] + nums[j] {
                    k += 1;
                }
                if nums[k] < nums[i] + nums[j] {
                    ans += (k - j) as i32;
                }
            }
        }
        ans
    }
}
