impl Solution {
    pub fn asteroids_destroyed(mass: i32, asteroids: Vec<i32>) -> bool {
        let mut asteroids: Vec<i64> = asteroids.iter().map(|&a| a as i64).collect();
        asteroids.sort();
        let mut mass = mass as i64;
        for a in asteroids {
            if a > mass {
                return false;
            }
            mass += a;
        }
        true
    }
}
