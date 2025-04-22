impl Solution {
    fn ideal_arrays(n: i32, mx: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut dp = vec![vec![0i64; 10001]; 15];
        let mut pr = vec![vec![0i64; 10001]; 15];
        let mut tot = vec![0i64; 15];

        fn get(la: i32, cn: usize, mx: i32, tot: &mut Vec<i64>) {
            tot[cn] += 1;
            let mut p = la * 2;
            while p <= mx {
                get(p, cn + 1, mx, tot);
                p += la;
            }
        }

        for i in 1..=10000 {
            dp[1][i] = 1;
            pr[1][i] = i as i64;
        }

        for i in 2..15 {
            for j in i..=10000 {
                dp[i][j] = pr[i - 1][j - 1];
                pr[i][j] = (dp[i][j] + pr[i][j - 1]) % MOD;
            }
        }

        for i in 1..=mx {
            get(i, 1, mx, &mut tot);
        }

        let mut ans = mx as i64;
        for i in 2..15 {
            ans = (ans + tot[i] * dp[i][n as usize] % MOD) % MOD;
        }

        ans as i32
    }
}
