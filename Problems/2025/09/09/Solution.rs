use std::collections::VecDeque;

const MOD: i32 = 1000000007;

impl Solution {
    pub fn people_aware_of_secret(n: i32, delay: i32, forget: i32) -> i32 {
        let n = n as usize;
        let delay = delay as usize;
        let forget = forget as usize;

        let mut know: VecDeque<(usize, i32)> = VecDeque::new();
        let mut share: VecDeque<(usize, i32)> = VecDeque::new();
        know.push_back((1, 1));
        let mut know_cnt = 1;
        let mut share_cnt = 0;

        for i in 2..=n {
            if let Some(&(day, count)) = know.front() {
                if day == i - delay {
                    let (day, count) = know.pop_front().unwrap();
                    know_cnt = (know_cnt - count + MOD) % MOD;
                    share_cnt = (share_cnt + count) % MOD;
                    share.push_back((day, count));
                }
            }

            if let Some(&(day, count)) = share.front() {
                if day == i - forget {
                    let (_, count) = share.pop_front().unwrap();
                    share_cnt = (share_cnt - count + MOD) % MOD;
                }
            }

            if !share.is_empty() {
                know_cnt = (know_cnt + share_cnt) % MOD;
                know.push_back((i, share_cnt));
            }
        }

        (know_cnt + share_cnt) % MOD
    }
}
