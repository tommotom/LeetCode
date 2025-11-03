impl Solution {
    // Complexity:
    // Time O(mn) and Space O(mn).
    pub fn count_unguarded(
        m: i32,
        n: i32,
        guards: Vec<Vec<i32>>,
        walls: Vec<Vec<i32>>,
    ) -> i32 {
        let mut result = m * n;
        let m = m as usize;
        let n = n as usize;

        // grid[r][c]:=
        // 0 if it is free,
        // 7 if there is a guard or wall,
        // bit 1 is set if it is watched from row direction,
        // bit 2 is set if it is watched from column direction.
        let mut grid = vec![vec![0_u8; n]; m];

        for wall in walls.iter() {
            let r0 = wall[0] as usize;
            let c0 = wall[1] as usize;
            grid[r0][c0] = 7;
        }
        result -= walls.len() as i32;

        for guard in guards.iter() {
            let r0 = guard[0] as usize;
            let c0 = guard[1] as usize;
            grid[r0][c0] ^= 4;

            for r in r0..m {
                if grid[r][c0] & 1 != 0 {
                    break;
                }
                grid[r][c0] ^= 1;
                result -= (grid[r][c0] >> 1 & 1 ^ 1) as i32;
            }
            for r in (0..r0).rev() {
                if grid[r][c0] & 1 != 0 {
                    break;
                }
                grid[r][c0] ^= 1;
                result -= (grid[r][c0] >> 1 & 1 ^ 1) as i32;
            }
            for c in c0..n {
                if grid[r0][c] & 2 != 0 {
                    break;
                }
                grid[r0][c] ^= 2;
                result -= (grid[r0][c] & 1 ^ 1) as i32;
            }
            for c in (0..c0).rev() {
                if grid[r0][c] & 2 != 0 {
                    break;
                }
                grid[r0][c] ^= 2;
                result -= (grid[r0][c] & 1 ^ 1) as i32;
            }
        }

        result
    }
}
