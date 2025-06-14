impl Solution {
    pub fn min_max_difference(mut num: i32) -> i32 {
        let mut arr = Vec::new();
        while num > 0 {
            arr.push(num % 10);
            num /= 10;
        }
        let mut max_target = -1;
        let mut min_target = -1;
        let mut max = 0;
        let mut min = 0;
        while arr.len() > 0 {
            let d = arr.pop().unwrap();
            if max_target == -1 && d != 9 {
                max_target = d;
            }
            if min_target == -1 && d != 0 {
                min_target = d;
            }
            max *= 10;
            min *= 10;
            if d == max_target {
                max += 9;
            } else {
                max += d;
            }
            if d == min_target {
                min += 0;
            } else {
                min += d;
            }
        }
        max - min
    }
}
