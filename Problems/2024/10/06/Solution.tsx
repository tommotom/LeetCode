function areSentencesSimilar(sentence1: string, sentence2: string): boolean {
    let arr1 = sentence1.split(' '), arr2 = sentence2.split(' ');

    if (arr1.length < arr2.length) {
        const tmp = arr1;
        arr1 = arr2;
        arr2 = tmp;
    }

    let inserted = false, i = 0, j = 0;
    while (i < arr1.length && j < arr2.length) {
        if (arr1[i] !== arr2[j]) {
            if (inserted) {
                return false;
            }
            inserted = true;
            while (arr1.length - i > arr2.length - j) {
                i++;
            }
            if (arr1[i] !== arr2[j]) {
                return false;
            }
        }
        i++;
        j++;
    }

    if (i === arr1.length && j === arr2.length) {
        return true;
    }

    if (inserted) {
        return false;
    }

    return j === arr2.length;
};
