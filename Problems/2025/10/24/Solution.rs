impl Solution {
    pub fn next_beautiful_number(mut n: i32) -> i32 {
        fn is_beautiful(mut n: i32) -> bool {
            let mut counter = vec![0; 10];
            while n > 0 {
                counter[(n % 10) as usize] += 1;
                n /= 10;
            }
            for i in 0..10 {
                if counter[i] == 0 {
                    continue;
                }
                if counter[i] != i as i32 {
                    return false;
                }
            }
            true
        }
        while !is_beautiful(n+1) {
            n += 1;
        }
        n+1
    }
}
