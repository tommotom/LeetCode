impl Solution {
    pub fn min_moves2(mut nums: Vec<i32>) -> i32 {
        fn median(numbers: &mut Vec<i32>) -> Option<i32> {
            let len = numbers.len();
            if len == 0 {
                return None;
            }

            numbers.sort_by(|a, b| a.partial_cmp(b).unwrap());

            if len % 2 == 1 {
                Some(numbers[len / 2])
            } else {
                let mid = len / 2;
                Some(((numbers[mid - 1] + numbers[mid]) as f64 / 2.0).round() as i32)
            }
        }
        let m = median(&mut nums).unwrap();
        let mut ans = 0;
        for num in nums {
            ans += (num - m).abs() as i32;
        }
        ans
    }
}
