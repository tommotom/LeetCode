impl Solution {
    pub fn maximum_value_sum(nums: Vec<i32>, k: i32, _edges: Vec<Vec<i32>>) -> i64 {
        let nums: Vec<i64> = nums.iter().map(|&x| x as i64).collect();
        let k = k as i64;
        let mut sum = 0;
        let mut cnt = 0;
        let mut sacrifice = i64::MAX;
        for &n in nums.iter() {
            let tmp = n ^ k;
            sum += tmp.max(n);
            cnt += if tmp > n { 1 } else { 0 };
            sacrifice = sacrifice.min((n - tmp).abs());
        }
        sum - if cnt % 2 == 1 { sacrifice } else { 0 }
    }
}
