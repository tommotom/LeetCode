impl Solution {
    pub fn possible_string_count(word: String, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = word.len();
        let mut cnt = 1;
        let mut freq: Vec<i32> = Vec::new();
        let word_chars: Vec<char> = word.chars().collect();

        for i in 1..n {
            if word_chars[i] == word_chars[i - 1] {
                cnt += 1;
            } else {
                freq.push(cnt);
                cnt = 1;
            }
        }
        freq.push(cnt);

        let mut ans: i64 = 1;
        for &o in &freq {
            ans = ans * o as i64 % MOD;
        }

        if freq.len() >= k as usize {
            return ans as i32;
        }

        let k_usize = k as usize;
        let mut f = vec![0; k_usize];
        let mut g = vec![1; k_usize];
        f[0] = 1;

        for &num in &freq {
            let mut f_new = vec![0; k_usize];
            for j in 1..k_usize {
                f_new[j] = g[j - 1];
                if j as i32 - num - 1 >= 0 {
                    f_new[j] = (f_new[j] - g[j - num as usize - 1] + MOD) % MOD;
                }
            }
            let mut g_new = vec![0; k_usize];
            g_new[0] = f_new[0];
            for j in 1..k_usize {
                g_new[j] = (g_new[j - 1] + f_new[j]) % MOD;
            }
            f = f_new;
            g = g_new;
        }

        ((ans - g[k_usize - 1] as i64 + MOD) % MOD) as i32
    }
}
