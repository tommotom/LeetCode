impl Solution {
    pub fn number_of_ways(corridor: String) -> i32 {
        let corridor: Vec<char> = corridor.chars().collect();
        let mut seats = corridor.iter().filter(|&c| *c == 'S').count();
        if seats == 0 || seats % 2 == 1 {
            return 0;
        }
        let mut ans: i64 = 1;
        let mut count = 0;
        let mut plants = 0;
        for c in corridor {
            if c == 'S' {
                count += 1;
            } else if seats > 2 && count == 2 {
                plants += 1;
            }

            if count == 3 {
                ans = (ans * (plants + 1)) % 1000000007;
                plants = 0;
                count = 1;
                seats -= 2;
            }
        }
        ans as i32
    }
}
