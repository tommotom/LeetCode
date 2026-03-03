impl Solution {
    pub fn find_kth_bit(n: i32, k: i32) -> char {
        fn helper(org: Vec<char>) -> Vec<char> {
            let mut ret = org.clone();
            ret.push('1');
            for c in org.into_iter().rev() {
                ret.push(if c == '1' {'0'} else {'1'});
            }
            ret
        }
        let mut arr = vec!['0'];
        for _ in 0..n {
            arr = helper(arr);
        }
        arr[k as usize - 1]
    }
}
