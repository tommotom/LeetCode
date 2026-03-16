impl Solution {
    pub fn get_biggest_three(grid: Vec<Vec<i32>>) -> Vec<i32> {
        let (n, m) = (grid.len(), grid[0].len());
        let mut rslt = [0;3];
        for i in 0..n {
            for j in 0..m {
                Self::modify(&mut rslt, grid[i][j]);
                let mut k = 1usize;
                while i + 2*k < n && j + k < m && j >= k {
                    let mut s = grid[i][j] + grid[i+k][j-k] + grid[i+2*k][j] + grid[i+k][j+k];
                    s += (1..k).map(|t| grid[i+t][j-t] + grid[i+t][j+t] + grid[i+2*k-t][j-t] + grid[i+2*k-t][j+t]).sum::<i32>();
                    Self::modify(&mut rslt, s);
                    k += 1;
                }
            }
        }
        rslt.into_iter().filter(|i| *i > 0).collect::<Vec<i32>>()
    }

    fn modify(a: &mut [i32;3], n:i32) {
        if n > a[2] && n != a[0] && n != a[1] {
            if n > a[0] {a[2] = a[1]; a[1] = a[0]; a[0] = n;}
            else if n > a[1] {a[2] = a[1]; a[1] = n;}
            else {a[2] = n;}
        }
    }
}
