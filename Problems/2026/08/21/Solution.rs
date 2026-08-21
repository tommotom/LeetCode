impl Solution {
    pub fn find_kth_smallest(mut coins: Vec<i32>, k: i32) -> i64 {
        fn gcd(mut a: i64, mut b: i64) -> i64 {
            while b != 0 {
                (a, b) = (b, a % b);
            }
            a
        }

        coins.sort_unstable();

        let n = coins.len();
        let m = 1usize << n;
        let mut left = k as i64;
        let mut right = coins[0] as i64 * k as i64 + 1;

        let mut bit_count = vec![0; m];
        let mut lcm = vec![0i64; m];

        for mask in 1..m {
            let mut cur_lcm = 1i64;

            for (i, &coin) in coins.iter().enumerate() {
                if mask >> i & 1 == 1 {
                    let coin = coin as i64;
                    let tmp = cur_lcm / gcd(cur_lcm, coin);

                    if tmp <= right / coin {
                        cur_lcm = tmp * coin;
                    } else {
                        cur_lcm = right + 1;
                        break;
                    }

                    bit_count[mask] += 1;
                }
            }

            lcm[mask] = cur_lcm;
        }

        let count = |x: i64| -> i64 {
            let mut res = 0i64;

            for mask in 1..m {
                if lcm[mask] <= x {
                    if bit_count[mask] & 1 == 1 {
                        res += x / lcm[mask];
                    } else {
                        res -= x / lcm[mask];
                    }
                }
            }

            res
        };

        while left < right {
            let mid = (left + right) / 2;

            if count(mid) >= k as i64 {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        left
    }
}
