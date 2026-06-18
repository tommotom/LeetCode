impl Solution {
    pub fn angle_clock(hour: i32, minutes: i32) -> f64 {
        let hour = (hour % 12) as f64;
        let minutes = minutes as f64;
        let a1 = (hour + minutes / 60 as f64) / 12 as f64;
        let a2 = minutes / 60 as f64;
        let angle = if a1 > a2 {a1 - a2} else {a2 - a1};
        angle.min(1 as f64 - angle) * 360 as f64
    }
}
