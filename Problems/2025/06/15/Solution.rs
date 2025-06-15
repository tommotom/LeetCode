impl Solution {
    pub fn max_diff(mut num: i32) -> i32 {
        let mut max = num; let mut min = num;

        let mut arr = Vec::new();
        while num > 0 {
            arr.push(num % 10);
            num /= 10;
        }
        arr = arr.into_iter().rev().collect();

        for x in 0..10 {
            for y in 0..10 {
                if y == 0 && arr[0] == x {
                    continue;
                }

                let mut n = 0;
                for d in &arr {
                    n *= 10;
                    if *d == x {
                        n += y
                    } else {
                        n += *d;
                    }
                }
                max = max.max(n);
                if n > 0 {
                    min = min.min(n);
                }
            }
        }

        max - min
    }
}
