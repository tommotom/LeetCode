function longestPalindrome(s: string): string {
    function isPalindrome(s: string): boolean {
        let i = 0, j = s.length - 1;
        while (i < j) {
            if (s.charAt(i++) !== s.charAt(j--)) {
                return false;
            }
        }
        return true;
    }

    let len = s.length;
    while (len > 0) {
        for (let i = 0; i < s.length - len + 1; i++) {
            if (isPalindrome(s.substring(i, i+len))) {
                return s.substring(i, i+len);
            }
        }
        len--;
    }
    return ""
};
