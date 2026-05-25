impl Solution {
    pub fn can_reach(s: String, min_jump: i32, max_jump: i32) -> bool {
         let n = s.len();
         let min_jump = min_jump as usize;
         let max_jump = max_jump as usize;
         let mut f = vec![0; n];
         let mut pre = vec![0; n];
         f[0] = 1;
         for i in 0..min_jump {
            pre[i] = 1;
         }
         let s: Vec<char> = s.chars().collect();
         for i in min_jump..n {
            let l = i as i32 - max_jump as i32;
            let r = i - min_jump;
            if s[i] == '0' {
                let total = if l <= 0 {pre[r]} else {pre[r] - pre[l as usize - 1]};
                f[i] = if total != 0 {1} else {0};
            }
            pre[i] = pre[i-1] + f[i];
         }
         f[n-1] == 1
    }
}
