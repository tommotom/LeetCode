impl Solution {
    pub fn compare_version(version1: String, version2: String) -> i32 {
        let v1: Vec<i32> = version1.split('.').map(|s| s.parse().unwrap()).collect();
        let v2: Vec<i32> = version2.split('.').map(|s| s.parse().unwrap()).collect();
        let (mut i1, mut i2) = (0, 0);
        while i1 < v1.len() || i2 < v2.len() {
            let num1 = if i1 < v1.len() {v1[i1]} else {0};
            let num2 = if i2 < v2.len() {v2[i2]} else {0};
            if num1 < num2 {
                return -1
            } else if num1 > num2 {
                return 1
            }
            i1 += 1;
            i2 += 1;
        }
        0
    }
}
