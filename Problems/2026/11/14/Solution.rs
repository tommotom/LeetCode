impl Solution {
    pub fn minimum_sum_subarray(nums: Vec<i32>, l: i32, r: i32) -> i32 {
        let (l, r) = (l as usize, r as usize);
        let mut cum = Vec::new();
        let mut sum = 0;
        cum.push(sum);
        for num in nums {
            sum += num;
            cum.push(sum);
        }
        let mut ans = i32::MAX;
        for j in l..cum.len() {
            for i in (if j > r {(j-r)} else {0})..=(j-l) {
                if cum[j] - cum[i] > 0 {
                    ans = ans.min(cum[j] - cum[i]);
                }
            }
        }
        if ans == i32::MAX {-1} else {ans}
    }
}
