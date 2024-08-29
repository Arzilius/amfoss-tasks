import System.IO

main :: IO ()
main = do
    let inputFilename = "input.txt"
    let outputFilename = "output.txt"

    -- Read the content of input.txt
    content <- readFile inputFilename

    -- Write the content to output.txt
    writeFile outputFilename content

    putStrLn $ "Content successfully written to " ++ outputFilename

