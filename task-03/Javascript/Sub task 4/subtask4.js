const fs = require('fs');

// Function to generate diamond pattern
function printDiamond(n) {
    if (n < 1) {
        return "Number should be greater than 1\n";
    }

    let result = '';
    const mid = Math.floor(n / 2);

    // Upper part of the diamond
    for (let i = 1; i <= n; i += 2) {
        const spaces = mid - Math.floor(i / 2);
        result += ' '.repeat(spaces) + '*'.repeat(i) + '\n';
    }

    // Lower part of the diamond
    if (n % 2 === 0) {
        for (let i = n - 1; i >= 1; i -= 2) {
            const spaces = mid - Math.floor(i / 2) + 1;
            result += ' '.repeat(spaces - 1) + '*'.repeat(i) + '\n';
        }
    } else {
        for (let i = n - 2; i >= 1; i -= 2) {
            const spaces = mid - Math.floor(i / 2);
            result += ' '.repeat(spaces) + '*'.repeat(i) + '\n';
        }
    }

    return result;
}

// Main function
function main() {
    fs.readFile('input.txt', 'utf8', (err, data) => {
        if (err) {
            console.error("Failed to open input.txt:", err);
            return;
        }

        const n = parseInt(data.trim(), 10);
        if (isNaN(n)) {
            console.error("Invalid number in input.txt");
            return;
        }

        const diamond = printDiamond(n);

        fs.writeFile('output.txt', diamond, (err) => {
            if (err) {
                console.error("Failed to write to output.txt:", err);
                return;
            }
            console.log("File transfer was successful");
        });
    });
}

main();

