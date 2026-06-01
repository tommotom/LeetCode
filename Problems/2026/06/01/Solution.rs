impl Solution {
    pub fn minimum_cost(mut cost: Vec<i32>) -> i32 {
        cost.sort();
        let mut ans = 0;
        let mut i = cost.len() - 1;
        while i < usize::MAX {
            if i > 1 {
                ans += cost[i] + cost[i-1];
                i -= 3;
            } else {
                ans += cost[i];
                i -= 1;
            }
        }
        ans
    }
}
