const MOD: i64 = 1_000_000_007;

struct Fancy {
    raw: Vec<i64>,
    mult: i64,
    add: i64,
}

impl Fancy {

    fn mod_pow(mut a: i64, mut b: i64) -> i64 {

        let mut res = 1i64;
        a %= MOD;

        while b > 0 {

            if b & 1 == 1 {
                res = res * a % MOD;
            }

            a = a * a % MOD;
            b >>= 1;
        }

        res
    }

    fn mod_inv(x: i64) -> i64 {
        Self::mod_pow(x, MOD - 2)
    }

    fn new() -> Self {
        Fancy {
            raw: vec![],
            mult: 1,
            add: 0,
        }
    }

    fn append(&mut self, val: i32) {

        let mut base = (val as i64 - self.add) % MOD;
        base = (base + MOD) % MOD;

        base = base * Self::mod_inv(self.mult) % MOD;

        self.raw.push(base);
    }

    fn add_all(&mut self, inc: i32) {
        self.add = (self.add + inc as i64) % MOD;
    }

    fn mult_all(&mut self, m: i32) {
        self.mult = self.mult * m as i64 % MOD;
        self.add = self.add * m as i64 % MOD;
    }

    fn get_index(&self, idx: i32) -> i32 {

        let i = idx as usize;

        if i >= self.raw.len() {
            return -1;
        }

        ((self.raw[i] * self.mult + self.add) % MOD) as i32
    }
}
