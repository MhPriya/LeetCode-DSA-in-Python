class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result =[]
    
        def backtrack(start, path, target_remaining):
            if target_remaining == 0:
                result.append(path[:])  # Found valid combination
                return
            for i in range(start, len(candidates)):
                # Step 2: Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target_remaining:
                    break  # Prune: no point in continuing
                # Step 3: Choose the current number and move forward
                path.append(candidates[i])
                backtrack(i + 1, path, target_remaining - candidates[i])
                path.pop()  # Backtrack

        backtrack(0, [], target)
        return result


        