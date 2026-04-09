impl Solution {
    pub fn maximum_amount(coins: Vec<Vec<i32>>) -> i32 {
        let m=coins.len();
        let n=coins[0].len();
        let neg=i32::MIN/2;

        let mut dp=vec![[neg;3];n];

        for k in 0..3{
            dp[0][k]=if k>0 {coins[0][0].max(0)} else {coins[0][0]};
        }

        for j in 1..n{
            for k in (0..3).rev(){
                dp[j][k]=dp[j][k].max(dp[j-1][k]+coins[0][j]);
                if k>0{
                    dp[j][k]=dp[j][k].max(dp[j-1][k-1]);
                }
            }
        }

        for i in 1..m{
            let mut ndp=vec![[neg;3];n];

            for j in 0..n{
                for k in (0..3).rev(){
                    if dp[j][k]!=neg{
                        ndp[j][k]=ndp[j][k].max(dp[j][k]+coins[i][j]);
                    }
                    if k>0 && dp[j][k-1]!=neg{
                        ndp[j][k]=ndp[j][k].max(dp[j][k-1]);
                    }
                    if j>0{
                        if ndp[j-1][k]!=neg{
                            ndp[j][k]=ndp[j][k].max(ndp[j-1][k]+coins[i][j]);
                        }
                        if k>0 && ndp[j-1][k-1]!=neg{
                            ndp[j][k]=ndp[j][k].max(ndp[j-1][k-1]);
                        }
                    }
                }
            }
            dp=ndp;
        }

        dp[n-1][2]
    }
}
