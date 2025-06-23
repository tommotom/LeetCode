impl Solution {
    pub fn k_mirror(k: i32, mut n: i32) -> i64 {
        let k = k as i64;
        fn to_arr(k: i64, mut num: i64) -> Vec<i64> {
            let mut arr = Vec::new();
            while num > 0 {
                arr.push(num % k);
                num /= k;
            }
            arr
        }
        fn is_mirror(k: i64, num: i64) -> bool {
            let arr = to_arr(k, num);
            for i in 0..(arr.len()/2) {
                if arr[i] != arr[arr.len()-i-1] {
                    return false;
                }
            }
            true
        }
        fn next(num: i64) -> i64 {
            let mut arr = to_arr(10, num);
            let n = arr.len();
            let mut i = (n - 1) / 2;

            while i >= 0 {
                let d = arr[i];
                if d < 9 {
                    arr[i] = d + 1;
                    arr[n-i-1] = d + 1;
                    while i < (n-1) / 2 {
                        i += 1;
                        arr[i] = 0;
                        arr[n-i-1] = 0;
                    }
                    return to_num(arr);
                }
                if i == 0 {
                    break;
                }
                i -= 1;
            }
            10_i64.pow(n as u32) + 1
        }
        fn to_num(arr: Vec<i64>) -> i64 {
            let mut ret = 0;
            for a in arr {
                ret *= 10;
                ret += a;
            }
            ret
        }

        let mut num = 1 as i64;
        let mut ans = 0;
        while n > 0 {
            if is_mirror(10, num) && is_mirror(k, num) {
                ans += num;
                n -= 1;
            }
            num = next(num);
        }
        ans
    }
}
