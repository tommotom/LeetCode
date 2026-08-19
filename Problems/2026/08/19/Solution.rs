use std::collections::HashMap;

impl Solution {
    pub fn max_number_of_families(n: i32, mut reserved_seats: Vec<Vec<i32>>) -> i32 {
        fn helper(reserved: &Vec<bool>) -> i32 {
            let mut valid = true;
            for seat in 1..9 {
                if reserved[seat] {
                    valid = false;
                    break;
                }
            }
            if valid {
                return 2;
            }

            valid = true;
            for seat in 1..5 {
                if reserved[seat] {
                    valid = false;
                    break;
                }
            }

            if valid {
                return 1;
            }
            valid = true;
            for seat in 3..7 {
                if reserved[seat] {
                    valid = false;
                    break;
                }
            }

            if valid {
                return 1;
            }

            valid = true;
            for seat in 5..9 {
                if reserved[seat] {
                    valid = false;
                    break;
                }
            }

            if valid {
                return 1;
            }

            0
        }

        let mut map = HashMap::new();
        for reserved in reserved_seats {
            map.entry(reserved[0]).or_insert(Vec::new()).push(reserved[1]);
        }
        let mut ans = 2 * n;
        for val in map.values() {
            let mut reserved = vec![false; 10];
            for i in val {
                reserved[*i as usize -1] = true;
            }
            ans -= (2 - helper(&reserved));
        }
        ans
    }
}
