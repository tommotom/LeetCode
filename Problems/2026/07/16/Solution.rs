impl Solution {
    pub fn gcd_sum(nums: Vec<i32>) -> i64 {
        fn gcd(a: i32, b: i32) -> i32 {
            if a < b {
                return gcd(b, a);
            }
            if b == 0 {
                return a;
            }
            gcd(b, a % b)
        }
        let mut p = Vec::new();
        let mut mx = 0;
        for num in nums {
            mx = mx.max(num);
            p.push(gcd(mx, num));
        }
        p.sort();
        let n = p.len();
        let mut arr = Vec::new();
        for i in 0..(n/2) {
            arr.push(gcd(p[n-i-1], p[i]) as i64);
        }
        arr.iter().sum()
    }
}
