function reverseWords(s: string): string {
    return s.split(" ").map(s => s.split("").reverse().join("")).join(" ");
};
