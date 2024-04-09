function countStudents(students: number[], sandwiches: number[]): number {
    let rearrange = 0;
    while (students.length > rearrange) {
        const s = students.shift();
        if (s === sandwiches[0]) {
            sandwiches.shift();
            rearrange = 0;
        } else {
            students.push(s);
            rearrange++;
        }
    }
    return students.length
};
