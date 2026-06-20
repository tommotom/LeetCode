impl Solution {
    pub fn max_building(n: i32, restrictions: Vec<Vec<i32>>) -> i32 {
        let mut r: Vec<Vec<i32>> = restrictions.clone();
        r.push(vec![1, 0]);
        r.sort_by(|a, b| a[0].cmp(&b[0]));
        if r.last().unwrap()[0] != n {
            r.push(vec![n, n - 1]);
        }

        let m = r.len();

        for i in 1..m {
            let dist = r[i][0] - r[i - 1][0];
            r[i][1] = r[i][1].min(r[i - 1][1] + dist);
        }

        for i in (0..m - 1).rev() {
            let dist = r[i + 1][0] - r[i][0];
            r[i][1] = r[i][1].min(r[i + 1][1] + dist);
        }

        let mut ans = 0;
        for i in 0..m - 1 {
            let dist = r[i + 1][0] - r[i][0];
            let best = (dist + r[i][1] + r[i + 1][1]) / 2;
            ans = ans.max(best);
        }

        ans
    }
}
