impl Solution {
    pub fn min_domino_rotations(tops: Vec<i32>, bottoms: Vec<i32>) -> i32 {
        let n = tops.len();
        let mut a = tops[0];
        let mut b = bottoms[0];
        let mut rotates = [0, 0, 0, 0]; // topA, tobB, bottomA, bottomB
        for i in 0..n {
            if rotates[0] != -1 && tops[i] != a {
                if bottoms[i] == a {
                    rotates[0] += 1;
                } else {
                    rotates[0] = -1;
                }
            }
            if rotates[1] != -1 && tops[i] != b {
                if bottoms[i] == b {
                    rotates[1] += 1;
                } else {
                    rotates[1] = -1;
                }
            }
            if rotates[2] != -1 && bottoms[i] != a {
                if tops[i] == a {
                    rotates[2] += 1;
                } else {
                    rotates[2] = -1;
                }
            }
            if rotates[3] != -1 && bottoms[i] != b {
                if tops[i] == b {
                    rotates[3] += 1;
                } else {
                    rotates[3] = -1;
                }
            }
        }
        if rotates.iter().sum::<i32>() == -4 {
            return -1;
        }
        rotates.into_iter().filter(|a| *a != -1).reduce(|a, b| a.min(b)).unwrap()
    }
}
