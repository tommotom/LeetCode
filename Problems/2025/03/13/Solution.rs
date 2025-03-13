impl Solution {
    pub fn min_zero_array(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> i32 {
        let n = nums.len();
        let mut sum = 0;
        let mut k = 0;
        let mut diff = vec![0; n+1];

        for i in 0..n {
            while sum + diff[i] < nums[i] {
                k += 1;
                if k > queries.len() {
                    return -1;
                }
                let l = queries[k-1][0] as usize;
                let r = queries[k-1][1] as usize;
                let v = queries[k-1][2];

                if r >= i {
                    diff[l.max(i)] += v;
                    diff[r+1] -= v;
                }
            }
            sum += diff[i];
        }
        k as i32
    }
}
