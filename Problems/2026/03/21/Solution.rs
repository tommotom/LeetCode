impl Solution {
    pub fn reverse_submatrix(mut grid: Vec<Vec<i32>>, x: i32, y: i32, k: i32) -> Vec<Vec<i32>> {
        let (x, y, k) = (x as usize, y as usize, k as usize);
        let m = grid.len();
        let n = grid[0].len();
        let mut a = x;
        let mut b = x + k - 1;
        while a < b {
            for c in 0..k {
                let tmp = grid[a][y + c];
                grid[a][y + c] = grid[b][y + c];
                grid[b][y + c] = tmp;
            }
            a += 1;
            b -= 1;
        }
        grid
    }
}
