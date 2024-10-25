function removeSubfolders(folder: string[]): string[] {
    const isSubfolder = (a, b) => {
        if (a.length >= b.length) {
            return false;
        }
        for (let i = 0; i < a.length; i++) {
            if (a.charAt(i) !== b.charAt(i)) {
                return false;
            }
        }
        return b.charAt(a.length) === '/';
    }

    folder.sort();

    const ans = [];

    for (const f of folder) {
        if (ans.length === 0 || !isSubfolder(ans[ans.length-1], f)) {
            ans.push(f);
        }
    }

    return ans;
};
