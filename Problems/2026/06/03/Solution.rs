impl Solution {
    pub fn earliest_finish_time(land_start_time: Vec<i32>, land_duration: Vec<i32>, water_start_time: Vec<i32>, water_duration: Vec<i32>) -> i32 {
        fn helper(s1: &Vec<i32>, d1: &Vec<i32>, s2: &Vec<i32>, d2: &Vec<i32>) -> i32 {
            let mut finish1 = i32::MAX;
            for i in 0..s1.len() {
                finish1 = finish1.min(s1[i] + d1[i]);
            }
            let mut finish2 = i32::MAX;
            for i in 0..s2.len() {
                finish2 = finish2.min(finish1.max(s2[i]) + d2[i]);
            }
            finish2
        }

        helper(&land_start_time, &land_duration, &water_start_time, &water_duration).min(helper(&water_start_time, &water_duration, &land_start_time, &land_duration))
    }
}
