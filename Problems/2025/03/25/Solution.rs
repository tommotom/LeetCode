impl Solution {
    pub fn check_valid_cuts(n: i32, mut rectangles: Vec<Vec<i32>>) -> bool {
        rectangles.sort_by(|a, b| if a[0] == b[0] {a[2].cmp(&b[2])} else {a[0].cmp(&b[0])});
        let mut count = 0;
        let mut l = 0;
        let mut line = 0;
        for r in 1..rectangles.len() {
            while l < r && rectangles[l][2] <= rectangles[r][0] {
                l += 1;
            }
            if l == r {
                line += 1;
            }
        }
        if line > 1 {
            return true;
        }

        rectangles.sort_by(|a, b| if a[1] == b[1] {a[3].cmp(&b[3])} else {a[1].cmp(&b[1])});
        count = 0;
        l = 0;
        line = 0;
        for r in 1..rectangles.len() {
            while l < r && rectangles[l][3] <= rectangles[r][1] {
                l += 1;
            }
            if l == r {
                line += 1;
            }
        }
        if line > 1 {
            return true;
        }
        false
    }
}
