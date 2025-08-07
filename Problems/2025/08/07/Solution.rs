fn dp(fruits: &Vec<Vec<i32>>, n: usize) -> i32 {
    let mut prev = vec![i32::MIN; n];
    let mut curr = vec![i32::MIN; n];

    prev[n - 1] = fruits[0][n - 1];
    for i in 1..n - 1 {
        for j in (n - 1 - i).max(i + 1)..n {
            let mut best = prev[j];
            if j > 0 {
                best = best.max(prev[j - 1]);
            }
            if j + 1 < n {
                best = best.max(prev[j + 1]);
            }
            curr[j] = best + fruits[i][j];
        }
        std::mem::swap(&mut prev, &mut curr);
    }
    prev[n - 1]
}

impl Solution {
    pub fn max_collected_fruits(mut fruits: Vec<Vec<i32>>) -> i32 {
        let n = fruits.len();
        let mut ans = (0..n).map(|i| fruits[i][i]).sum::<i32>();

        ans += dp(&fruits, n);
        for i in 0..n {
            for j in 0..i {
                let tmp = fruits[i][j];
                fruits[i][j] = fruits[j][i];
                fruits[j][i] = tmp;
            }
        }
        ans += dp(&fruits, n);
        ans
    }
}
