impl Solution {
    pub fn count_trapezoids(points: Vec<Vec<i32>>) -> i32 {
        fn pow_mod(a: i64, b: i64, m: i64) -> i64 {
            if b == 0  {
                1
            } else if b % 2 == 0 {
                let d = pow_mod(a, b/2, m);
                (d * d) % m
            } else {
                (a * pow_mod(a, b-1, m)) % m
            }
        }

        fn combination(mut n: i64, c: i64, m: i64) -> i64 {
            let mut upe = 1;
            let mut dow = 1;
            for i in 1..c + 1 {
                upe = upe * n % m;
                dow = dow * i % m;

                n -= 1;
            }
            upe * pow_mod(dow, m-2, m) % m
        }

        let m: i64 = 1000000007;
        let mut points: Vec<Vec<i64>> = points.iter().map(|point| point.iter().map(|&p| p as i64).collect()).collect();
        points.sort_by(|a, b| a[1].cmp(&b[1]));
        let mut seen: i64 = 0;
        let mut ans: i64 = 0;
        let mut y = points[0][1];
        let mut cur: i64 = 0;
        for point in points {
            if y != point[1] {
                let d = combination(cur, 2, m);
                ans = (ans + seen * d) % m;
                seen = (seen + d) % m;
                cur = 0;
                y = point[1];
            }
            cur += 1;
        }
        let d = combination(cur, 2, m);
        ans = (ans + seen * d) % m;
        ans as i32
    }
}
