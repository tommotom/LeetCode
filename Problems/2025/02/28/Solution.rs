impl Solution {
    pub fn shortest_common_supersequence(str1: String, str2: String) -> String {
        let m = str1.len();
        let n = str2.len();
        let str1 = str1.as_bytes();
        let str2 = str2.as_bytes();

        let mut dp = vec![vec![0; n + 1]; m + 1];

        for i in 1..=m {
            for j in 1..=n {
                if str1[i - 1] == str2[j - 1] {
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                } else {
                    dp[i][j] = dp[i - 1][j].max(dp[i][j - 1]);
                }
            }
        }

        let mut i = m;
        let mut j = n;
        let mut result = Vec::new();

        while i > 0 && j > 0 {
            if str1[i - 1] == str2[j - 1] {
                result.push(str1[i - 1]);
                i -= 1;
                j -= 1;
            } else if dp[i - 1][j] > dp[i][j - 1] {
                result.push(str1[i - 1]);
                i -= 1;
            } else {
                result.push(str2[j - 1]);
                j -= 1;
            }
        }

        while i > 0 {
            result.push(str1[i - 1]);
            i -= 1;
        }

        while j > 0 {
            result.push(str2[j - 1]);
            j -= 1;
        }

        result.reverse();

        String::from_utf8(result).unwrap()
    }
}
