impl Solution {
    pub fn count_permutations(complexity: Vec<i32>) -> i32 {
        let n = complexity.len();
        for i in 1..n {
            if complexity[i] <= complexity[0] {
                return 0;
            }
        }

        let mut ans: i64 = 1;
        for i in 2..n {
            ans = (ans * i as i64) % 1000000007;
        }
        ans as i32
    }
}
