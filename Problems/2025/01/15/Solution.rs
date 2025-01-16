impl Solution {
    fn count_bit(mut num: i32) -> i32 {
        let mut ret = 0;
        while num > 0 {
            ret += num % 2;
            num /= 2;
        }
        ret
    }

    pub fn minimize_xor(mut num1: i32, mut num2: i32) -> i32 {
        let mut bits1 = Self::count_bit(num1.clone());
        let mut bits2 = Self::count_bit(num2.clone());

        let mut bit_arr = [0; 32];
        let mut i = 31;
        while num1 > 0 {
            bit_arr[i] = num1 % 2;
            num1 /= 2;
            i -= 1;
        }

        let mut ans = 0;
        for j in 0..32 {
            ans *= 2;
            if bit_arr[j] == 0 {
                if bits2 == 32 - j as i32 {
                    ans += 1;
                    bits2 -= 1;
                }
            } else if bits2 > 0 {
                ans += 1;
                bits2 -= 1;
            }
        }
        ans
    }
}
