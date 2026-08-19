impl Solution {
    pub fn largest_integer(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let k = k as usize;
        let mut counter = vec![0; 51];
        for num in &nums {
            counter[*num as usize] += 1;
        }
        if n == k {
            for num in (0..51).rev() {
                if counter[num] > 0 {
                    return num as i32;
                }
            }
            return -1;
        }
        if k == 1 {
            for num in (0..51).rev() {
                if counter[num] == 1 {
                    return num as i32;
                }
            }
            return -1;
        }
        let head = nums[0] as usize;
        let tail = nums[n-1] as usize;
        let h_v = if counter[head] == 1 {head as i32} else {-1};
        let t_v = if counter[tail] == 1 {tail as i32} else {-1};
        h_v.max(t_v)
    }
}
