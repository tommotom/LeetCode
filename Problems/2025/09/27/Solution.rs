impl Solution {
    pub fn largest_triangle_area(points: Vec<Vec<i32>>) -> f64 {
        fn area(a: &Vec<i32>, b: &Vec<i32>, c: &Vec<i32>) -> f64 {
            ((a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])) as f64).abs() / 2.0
        }
        let mut ans: f64 = 0.0;
        for i in 0..(points.len()-2) {
            for j in (i+1)..(points.len()-1) {
                for k in (j+1)..points.len() {
                    ans = ans.max(area(&points[i], &points[j], &points[k]));
                }
            }
        }
        ans
    }
}
