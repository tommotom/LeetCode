struct Bank {
    accounts: Vec<i64>
}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Bank {

    fn new(balance: Vec<i64>) -> Self {
        Self {
            accounts: balance
        }
    }

    fn is_valid(&self, account: i32) -> bool {
        0 < account && account <= self.accounts.len() as i32
    }

    fn to_i(&mut self, account: i32) -> usize {
        account as usize - 1
    }

    fn transfer(&mut self, account1: i32, account2: i32, money: i64) -> bool {
        if !self.is_valid(account1) || !self.is_valid(account2) {
            return false;
        }
        if !self.withdraw(account1, money) || !self.deposit(account2, money) {
            return false;
        }
        true
    }

    fn deposit(&mut self, account: i32, money: i64) -> bool {
        if !self.is_valid(account) {
            return false;
        }
        let i = self.to_i(account);
        self.accounts[i] += money;
        true
    }

    fn withdraw(&mut self, account: i32, money: i64) -> bool {
        if !self.is_valid(account) {
            return false;
        }
        let i = self.to_i(account);
        if self.accounts[i] < money {
            return false;
        }
        self.accounts[i] -= money;
        true
    }
}

/**
 * Your Bank object will be instantiated and called as such:
 * let obj = Bank::new(balance);
 * let ret_1: bool = obj.transfer(account1, account2, money);
 * let ret_2: bool = obj.deposit(account, money);
 * let ret_3: bool = obj.withdraw(account, money);
 */
