impl Solution {
    pub fn number_of_paths(grid: Vec<Vec<i32>>, k: i32) -> i32 {
        let grid: Vec<Vec<usize>> = grid.iter().map(|g| g.iter().map(|num| *num as usize).collect()).collect();
        let k = k as usize;

        let m = grid.len();
        let n = grid[0].len();
        let mut mods = vec![vec![vec![0; k]; n]; m];
        for i in 0..m {
            for j in 0..n {
                if i == 0 && j == 0 {
                    mods[i][j][grid[i][j] % k] += 1;
                    continue;
                }
                if i > 0 {
                    for l in 0..k {
                        let mut MOD = (l + grid[i][j]) % k;
                        mods[i][j][MOD] += mods[i-1][j][l];
                        mods[i][j][MOD] %= 1000000007;
                    }
                }
                if j > 0 {
                    for l in 0..k {
                        let mut MOD = (l + grid[i][j]) % k;
                        mods[i][j][MOD] += mods[i][j-1][l];
                        mods[i][j][MOD] %= 1000000007;
                    }
                }
            }
        }
        mods[m-1][n-1][0] as i32
    }
}
