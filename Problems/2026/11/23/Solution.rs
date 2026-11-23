struct ProductOfNumbers {
    q: Vec<u64>
}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl ProductOfNumbers {

    fn new() -> Self {
        ProductOfNumbers {
            q: Vec::new()
        }
    }

    fn add(&mut self, num: i32) {
        if num == 0 {
            self.q = Vec::new();
        } else if self.q.len() == 0 {
            self.q.push(num as u64);
        } else {
            self.q.push(self.q[self.q.len() - 1] * num as u64);
        }
    }

    fn get_product(&self, k: i32) -> i32 {
        let k = k as usize;
        let l = self.q.len();
        if l == k {
            return self.q[l-1] as i32;
        } else if k > l {
            return 0;
        }
        (self.q[l - 1] / self.q[l - k - 1]) as i32
    }
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * let obj = ProductOfNumbers::new();
 * obj.add(num);
 * let ret_2: i32 = obj.get_product(k);
 */
