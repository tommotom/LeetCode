function countSeniors(details: string[]): number {
    return details.filter(str => Number(str.substring(11,13)) > 60).length;
};
