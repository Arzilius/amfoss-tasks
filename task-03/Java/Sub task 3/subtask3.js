function printDiamond(n) {
    if (n < 1) {
        console.log("Number should be greater than 1");
        return;
    }

    const mid = Math.floor(n / 2);

    // Upper part of the diamond
    for (let i = 1; i <= n; i += 2) {
        // Calculate and print leading spaces
        const spaces = mid - Math.floor(i / 2);
        console.log(" ".repeat(spaces) + "*".repeat(i));
    }

    // Lower part of the diamond
    if (n % 2 === 0) {
        for (let i = n - 1; i >= 1; i -= 2) {
            // Calculate and print leading spaces with a slight shift for asymmetry
            const spaces = mid - Math.floor(i / 2) + 1;
            console.log(" ".repeat(spaces - 1) + "*".repeat(i));
        }
    } else {
        for (let i = n - 2; i >= 1; i -= 2) {
            const spaces = mid - Math.floor(i / 2);
            console.log(" ".repeat(spaces) + "*".repeat(i));
        }
    }
}

// Example usage
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

readline.question("Enter the number of rows for the diamond: ", n => {
    printDiamond(parseInt(n));
    readline.close();
});

