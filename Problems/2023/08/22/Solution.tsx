function convertToTitle(columnNumber: number): string {
    const arr = [];
    while (columnNumber > 0) {
        const tmp = (columnNumber - 1) % 26;
        arr.push(String.fromCharCode(tmp + "A".charCodeAt(0)));
        columnNumber = (columnNumber - tmp - 1) / 26;
    }
    return arr.reverse().join("");
};
