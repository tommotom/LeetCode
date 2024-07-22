function sortPeople(names: string[], heights: number[]): string[] {
    return names.map((el, i) => [heights[i], el]).sort((a, b) => Number(b[0]) - Number(a[0])).map(el => el[1]) as string[];
};
