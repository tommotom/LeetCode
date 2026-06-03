impl Solution {
    pub fn earliest_finish_time(land_start_time: Vec<i32>, land_duration: Vec<i32>, water_start_time: Vec<i32>, water_duration: Vec<i32>) -> i32 {
        fn is_overlapped(s1: i32, e1: i32, s2: i32, e2: i32) -> bool {
            !(e1 <= s2 || e2 <= s1)
        }

        let mut ans = i32::MAX;
        for i in 0..land_start_time.len() {
            for j in 0..water_start_time.len() {
                let s1 = land_start_time[i];
                let e1 = s1 + land_duration[i];
                let s2 = water_start_time[j];
                let e2 = s2 + water_duration[j];
                if is_overlapped(s1, e1, s2, e2) {
                    let can1 = e1 + water_duration[j];
                    let can2 = e2 + land_duration[i];
                    ans = ans.min(can1.min(can2));
                } else {
                    ans = ans.min(e1.max(e2));
                }
            }
        }
        ans
    }
}
