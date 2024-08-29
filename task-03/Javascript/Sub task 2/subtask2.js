const fs = require('fs');

const inputFilename = 'input.txt';
const outputFilename = 'output.txt';

// Read the content of input.txt
fs.readFile(inputFilename, 'utf8', (err, data) => {
    if (err) {
        console.error(`Error reading file: ${err.message}`);
        return;
    }

    // Write the content to output.txt
    fs.writeFile(outputFilename, data, (err) => {
        if (err) {
            console.error(`Error writing to file: ${err.message}`);
            return;
        }

        console.log(`Content successfully written to ${outputFilename}`);
    });
});

