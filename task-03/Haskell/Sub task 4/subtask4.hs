import System.IO
import Control.Monad (when)

printDiamond :: Handle -> Int -> IO ()
printDiamond outputFile n
  | n < 1 = hPutStrLn outputFile "Number should be greater than 1"
  | otherwise = do
      let mid = n `div` 2

      -- Upper part of the diamond
      mapM_ (printLine outputFile mid) [1,3..n]

      -- Lower part of the diamond
      if even n
      then mapM_ (printLine outputFile (mid - 1)) (reverse [1,3..(n-1)])
      else mapM_ (printLine outputFile mid) (reverse [1,3..(n-2)])

printLine :: Handle -> Int -> Int -> IO ()
printLine outputFile mid i = do
  let spaces = mid - (i `div` 2)
  hPutStrLn outputFile (replicate spaces ' ' ++ replicate i '*')

main :: IO ()
main = do
  inputFile <- openFile "input.txt" ReadMode
  outputFile <- openFile "output.txt" WriteMode

  input <- hGetLine inputFile
  let n = read input :: Int

  printDiamond outputFile n

  hClose inputFile
  hClose outputFile
  
  putStrLn "File transfer was successful"

