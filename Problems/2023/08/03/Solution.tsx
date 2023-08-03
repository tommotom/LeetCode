function letterCombinations(digits: string): string[] {
    if (digits.length === 0) {
        return [];
    }

    const button: Map<string, string[]> = new Map([
        ['2', ['a', 'b', 'c']],
        ['3', ['d', 'e', 'f']],
        ['4', ['g', 'h', 'i']],
        ['5', ['j', 'k', 'l']],
        ['6', ['m', 'n', 'o']],
        ['7', ['p', 'q', 'r', 's']],
        ['8', ['t', 'u', 'v']],
        ['9', ['w', 'x', 'y', 'z']]
    ]);

    const ans: string[] = [];
    const st: string[] = [];

    function helper(i: number) {
        if (i === digits.length) {
            ans.push(st.join(''));
            return;
        }
        for (const c of button.get(digits[i])) {
            st.push(c);
            helper(i+1);
            st.pop();
        }
    }

    helper(0);

    return ans;
};
