struct ProductOfNumbers {
    data: Vec<u64>
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl ProductOfNumbers {

    fn new() -> Self {
        return ProductOfNumbers {
            data: Vec::new()
        }
    }

    fn add(&mut self, num: i32) {
        if num == 0 {
            self.data = Vec::new();
        } else if self.data.len() == 0 {
            self.data.push(num as u64);
        } else {
            self.data.push(self.data[self.data.len() - 1] * (num as u64));
        }
    }

    fn get_product(&self, k: i32) -> i32 {
        let k = k as usize;
        let l = self.data.len();
        if k == l {
            return self.data[l - 1] as i32;
        }
        if k > l {
            return 0;
        }

        return (self.data[l - 1] / self.data[l - k - 1]) as i32;
    }
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * let obj = ProductOfNumbers::new();
 * obj.add(num);
 * let ret_2: i32 = obj.get_product(k);
 */
