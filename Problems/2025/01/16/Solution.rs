impl Solution {
    fn to_bit_arr(num: i32) -> [i32; 32] {
        let mut ret = [0; 32];
        for i in 0..32 {
            let bit = 1 << (31-i);
            if (bit & num) > 0 {
                ret[i] = 1;
            }
        }
        ret
    }

    fn sum(a: [i32; 32], b: [i32; 32]) -> [i32; 32] {
        let mut ret = [0; 32];
        for i in 0..32 {
            ret[i] = a[i] + b[i];
        }
        ret
    }

    pub fn xor_all_nums(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let m = nums1.len() as i32;
        let n = nums2.len() as i32;
        let bit_arr1: [i32; 32] = nums1.into_iter().map(|num| Self::to_bit_arr(num)).reduce(|a, b| Self::sum(a, b)).unwrap();
        let bit_arr2: [i32; 32] = nums2.into_iter().map(|num| Self::to_bit_arr(num)).reduce(|a, b| Self::sum(a, b)).unwrap();
        let mut ans = 0;
        for i in 0..32 {
            ans *= 2;
            let zero1 = m - bit_arr1[i];
            let one1 = bit_arr1[i];
            let zero2 = n - bit_arr2[i];
            let one2 = bit_arr2[i];
            ans += (zero1 * one2 + one1 * zero2) % 2;
        }
        ans
    }
}
