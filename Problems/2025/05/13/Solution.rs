impl Solution {
    pub fn length_after_transformations(s: String, t: i32) -> i32 {
        const MOD: i32 = 1000000007;
        let mut count = [0; 26];
        for c in s.chars() {
            count[(c as u8 - b'a') as usize] += 1;
        }
        for _ in 0..t {
            let mut next = [0; 26];
            next[0] = count[25];
            next[1] = (count[25] + count[0]) % MOD;
            for i in 2..26 {
                next[i] = count[i-1];
            }
            count = next;
        }
        let mut ans = 0;
        for &num in count.iter() {
            ans = (ans + num) % MOD;
        }
        ans
    }
}
