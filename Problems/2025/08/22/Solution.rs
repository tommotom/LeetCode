impl Solution {
    pub fn minimum_area(grid: Vec<Vec<i32>>) -> i32 {
        let (n, m) = (grid.len(), grid[0].len());
        let (mut l, mut u, mut d, mut r) = (0, 0, 0, 0);
        let mut alreadySeen = false;
        for i in 0..n {
            for j in 0..m {
                if grid[i][j] == 1 {
                    if !alreadySeen {
                        alreadySeen = true;
                        l = j;
                        r = j;
                        u = i;
                        d = i;
                    } else {
                        l = l.min(j);
                        r = r.max(j);
                        u = u.min(i);
                        d = d.max(i);
                    }
                }
            }
        }
        ((r - l + 1) * (d - u + 1)) as i32
    }
}
