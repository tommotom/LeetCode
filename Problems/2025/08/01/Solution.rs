impl Solution {
    pub fn generate(num_rows: i32) -> Vec<Vec<i32>> {
        let mut ans = vec![vec![1]];
        for _ in 1..num_rows {
            let mut next = vec![1];
            let last = ans.len()-1;
            for i in 1..ans[last].len() {
                next.push(ans[last][i-1] + ans[last][i]);
            }
            next.push(1);
            ans.push(next);
        }
        ans
    }
}
