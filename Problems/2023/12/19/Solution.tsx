function imageSmoother(img: number[][]): number[][] {
    const dir = [[0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1], [-1,0], [-1,1]], ans = [];
    for (let i = 0; i < img.length; i++) {
        ans.push([]);
        for (let j = 0; j < img[0].length; j++) {
            let sum = img[i][j], cell = 1;
            for (const [I, J] of dir) {
                if (0 <= i+I && i+I < img.length && 0 <= j+J && j+J < img[0].length) {
                    sum += img[i+I][j+J];
                    cell++;
                }
            }
            ans[i].push(Math.floor(sum / cell));
        }
    }
    return ans;
};
