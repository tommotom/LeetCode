impl Solution {
    pub fn furthest_distance_from_origin(moves: String) -> i32 {
        let mut free: i32 = 0;
        let mut pos: i32 = 0;
        for m in moves.chars() {
            if m == 'L' {
                pos -= 1;
            } else if m == 'R' {
                pos += 1;
            } else {
                free += 1;
            }
        }
        (pos + free).abs().max((pos - free).abs())
    }
}
