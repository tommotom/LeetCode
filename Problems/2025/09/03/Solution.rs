impl Solution {
    pub fn number_of_pairs(mut points: Vec<Vec<i32>>) -> i32 {
        points.sort_by(|a, b| if a[0] == b[0] { b[1].cmp(&a[1]) } else { a[0].cmp(&b[0]) });
        let mut ans = 0;
        let n = points.len();
        for i in 1..n {
            for j in 0..i {
                if points[i][0] < points[j][0] || points[i][1] > points[j][1] {
                    continue;
                }
                let mut isValid = true;
                for k in (j+1)..i {
                    if points[i][0] >= points[k][0] && points[k][0] >= points[j][0] && points[i][1] <= points[k][1] && points[k][1] <= points[j][1] {
                        isValid = false;
                        break;
                    }
                }
                if isValid {
                    ans += 1;
                }
            }
        }
        ans
    }
}
