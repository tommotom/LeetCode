use std::collections::HashMap;

struct FindSumPairs {
    counter1: HashMap<i32, i32>,
    counter2: HashMap<i32, i32>,
    nums2: Vec<i32>
}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl FindSumPairs {

    fn new(nums1: Vec<i32>, nums2: Vec<i32>) -> Self {
        let mut counter1 = HashMap::new();
        let mut counter2 = HashMap::new();
        let mut i_to_num = HashMap::new();
        for num in nums1 {
            *counter1.entry(num).or_insert(0) += 1;
        }
        for (i, num) in nums2.iter().enumerate() {
            *counter2.entry(*num).or_insert(0) += 1;
            i_to_num.insert(i as i32, *num);
        }
        Self {
            counter1,
            counter2,
            nums2
        }
    }

    fn add(&mut self, index: i32, val: i32) {
        let i = index as usize;
        *self.counter2.entry(self.nums2[i]).or_insert(0) -= 1;
        self.nums2[i] += val;
        *self.counter2.entry(self.nums2[i]).or_insert(0) += 1;
    }

    fn count(&mut self, tot: i32) -> i32 {
        let mut ans = 0;
        for (v, c) in self.counter1.iter() {
            ans += *c * *self.counter2.entry(tot-v).or_insert(0);
        }
        ans
    }
}

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * let obj = FindSumPairs::new(nums1, nums2);
 * obj.add(index, val);
 * let ret_2: i32 = obj.count(tot);
 */
