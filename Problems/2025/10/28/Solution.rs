impl Solution {
    pub fn count_valid_selections(nums: Vec<i32>) -> i32 {
        fn is_valid(mut nums: Vec<i32>, mut d: i32, mut i: usize) -> bool {
            while 0 <= i && i < nums.len() {
                if nums[i] > 0 {
                    nums[i] -= 1;
                    d = d * -1;
                }
                i = ((i as i32) + d) as usize;
            }
            nums.iter().sum::<i32>() == 0
        }
        let mut ans = 0;
        for i in 0..nums.len() {
            if nums[i] == 0 {
                if is_valid(nums.clone(), 1, i) {
                    ans += 1;
                }
                if is_valid(nums.clone(), -1, i) {
                    ans += 1;
                }
            }
        }
        ans
    }
}
