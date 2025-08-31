impl Solution {
    pub fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {
        fn to_usize(c: &char) -> usize {
            *c as usize - '1' as usize
        }


        for row in &board {
            let mut seen = [false; 9];
            for r in row {
                if *r == '.' {
                    continue;
                }
                let i = to_usize(r);
                if seen[i] {
                    return false;
                }
                seen[i] = true;
            }
        }

        for c in 0..9 {
            let mut seen = [false; 9];
            for r in 0..9 {
                if board[r][c] == '.' {
                    continue;
                }
                let i = to_usize(&board[r][c]);
                if seen[i] {
                    return false;
                }
                seen[i] = true;
            }
        }

        for r in 0..3 {
            for c in 0..3 {
                let mut seen = [false; 9];
                for i in 0..9 {
                    let rr = r * 3 + i / 3;
                    let cc = c * 3 + i % 3;
                    if board[rr][cc] == '.' {
                        continue;
                    }
                    let j = to_usize(&board[rr][cc]);
                    if seen[j] {
                        return false;
                    }
                    seen[j] = true;
                }
            }
        }

        true
    }
}
