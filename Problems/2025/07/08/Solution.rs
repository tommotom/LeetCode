impl Solution {
    pub fn max_value(mut events: Vec<Vec<i32>>, k: i32) -> i32 {
        let k = k as usize;
        events.sort_by(|a, b| a[0].cmp(&b[0]));
        let mut dp = vec![vec![-1; events.len()]; k+1];

        fn dfs(i: usize, count: usize, events: &Vec<Vec<i32>>, dp: &mut Vec<Vec<i32>>) -> i32 {
            if count == 0 || i == events.len() {
                return 0;
            }
            if dp[count][i] != -1 {
                return dp[count][i];
            }
            let j = bisectRight(events, events[i][1]);
            dp[count][i] = dfs(i+1, count, events, dp).max(events[i][2] + dfs(j, count-1, events, dp));
            dp[count][i]
        }

        fn bisectRight(events: &Vec<Vec<i32>>, target: i32) -> usize {
            let (mut l, mut r) = (0, events.len());
            while l < r {
                let m = l + (r - l) / 2;
                if events[m][0] <= target {
                    l = m + 1;
                } else {
                    r = m;
                }
            }
            l
        }

        dfs(0, k, &events, &mut dp)
    }
}
