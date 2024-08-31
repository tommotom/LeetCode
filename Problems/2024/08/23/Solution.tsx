function fractionAddition(exp: string): string {
    const gcd = (n, m) => m ? gcd(m, n % m) : n;
    const lcm = (a, b) => a * b / gcd(a, b);
    const zero = '0'.charCodeAt(0);
    const nine = '9'.charCodeAt(0);
    const isDigit = s => zero <= s.charCodeAt(0) && s.charCodeAt(0) <= nine;
    let i = 0;
    const ns = [], ds = [];
    while (i < exp.length) {
        let sign = 1;
        if (exp.charAt(i) === '+') {
            i++;
        } else if (exp.charAt(i) === '-') {
            sign *= -1;
            i++;
        }
        let j = i;
        while (isDigit(exp.charAt(j))) {
            j++;
        }
        ns.push(Number(exp.substring(i, j)) * sign);
        i = j + 1;
        j = i;
        while (isDigit(exp.charAt(j))) {
            j++;
        }
        ds.push(Number(exp.substring(i, j)));
        i = j
    }

    const D = ds.reduce((a, b) => lcm(a, b));

    let N = 0;
    for (let i = 0; i < ns.length; i++) {
        N += (D / ds[i]) * ns[i];
    }

    const num = gcd(Math.abs(N), D);
    return [N/num, '/', D/num].join('');
};
