impl Solution {
    pub fn sum_counts(nums: Vec<i32>) -> i32 {
        let mut ans = 0;
        for i in 0..nums.len() {
            let mut counter = vec![0; 101];
            for j in i..nums.len() {
                counter[nums[j] as usize] += 1;
                let n = counter.iter().filter(|&x| *x > 0).count() as i32;
                ans += n * n;
            }
            counter[nums[i] as usize] -= 1;
        }
        ans
    }
}
