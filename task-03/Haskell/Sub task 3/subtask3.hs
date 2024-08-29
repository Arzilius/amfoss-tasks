import Control.Monad (forM_)

printDiamond :: Int -> IO ()
printDiamond n
  | n < 1 = putStrLn "Number should be greater than 1"
  | otherwise = do
      -- Calculate the middle point
      let mid = n `div` 2

      -- Upper part of the diamond
      forM_ [1,3..n] $ \i -> do
        let spaces = mid - i `div` 2
        putStrLn $ replicate spaces ' ' ++ replicate i '*'

      -- Lower part of the diamond
      if even n
        then forM_ [n-1,n-3..1] $ \i -> do
               let spaces = mid - i `div` 2 + 1 -- Slightly adjust spaces for asymmetry
               putStrLn $ replicate spaces ' ' ++ replicate i '*'
        else forM_ [n-2,n-4..1] $ \i -> do
               let spaces = mid - i `div` 2
               putStrLn $ replicate spaces ' ' ++ replicate i '*'

main :: IO ()
main = do
  putStr "Enter the number of rows for the diamond: "
  input <- getLine
  let n = read input :: Int
  printDiamond(n)

