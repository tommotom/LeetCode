impl Solution {
    pub fn closest_primes(left: i32, right: i32) -> Vec<i32> {
        let mut prime = vec![true; right as usize +1];
        prime[0] = false;
        prime[1] = false;
        let mut num = 2;
        while num * num <= right {
            if prime[num as usize] {
                let mut i = 2 * num;
                while i < right+1 {
                    prime[i as usize] = false;
                    i += num;
                }
            }
            num += 1;
        }

        prime
            .into_iter()
            .enumerate()
            .skip(left as usize)
            .take(right as usize + 1 - left as usize)
            .filter(|&(_, x)| x)
            .map(|(i, _)| i as i32)
            .collect::<Vec<_>>()
            .windows(2)
            .fold(
                (vec![-1, -1], i32::MAX),
                |(mut result, mut min), x| {
                    let cur = x[1] - x[0];

                    if cur < min {
                        result.copy_from_slice(x);
                        min = cur;
                    }

                    (result, min)
                },
            )
            .0
    }
}
