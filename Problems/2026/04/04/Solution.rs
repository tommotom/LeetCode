impl Solution {
    pub fn decode_ciphertext(encoded_text: String, rows: i32) -> String {
        let rows = rows as usize;
        let cols = encoded_text.len() / rows;
        let mut matrix: Vec<Vec<char>> = Vec::new();
        let mut row = Vec::new();
        for c in encoded_text.chars() {
            row.push(c);
            if row.len() == cols {
                matrix.push(row);
                row = Vec::new();
            }
        }
        let mut decode = Vec::new();
        for c in 0..cols {
            let mut i = 0;
            while i < rows && c + i < cols {
                decode.push(matrix[i][c+i]);
                i += 1;
            }
        }
        decode.into_iter().collect::<String>().trim_end().to_string()
    }
}
