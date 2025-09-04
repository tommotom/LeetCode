impl Solution {
    pub fn find_closest(x: i32, y: i32, z: i32) -> i32 {
        let dx = (x - z).abs();
        let dy = (y - z).abs();
        if dx < dy {
            return 1;
        } else if dx > dy {
            return 2;
        } else {
            return 0;
        }
    }
}
