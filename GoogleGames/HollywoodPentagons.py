def findNsum(nums, target, N, result, results):
    if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:  # early termination
        return
    if N == 2: # two pointers solve sorted 2-sum problem
        l,r = 0,len(nums)-1
        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                results.append(result + [nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
            elif s < target:
                l += 1
            else:
                r -= 1
    else: # recursively reduce N
        for i in range(len(nums)-N+1):
            if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)


nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179]
perfCubes = [8, 27, 64, 125]

sets = []
findNsum(nums, 540, 5, [], sets)

for s in sets:
    curr = 0
    for n in s:
        n = [int(x) for x in str(n)]
        curr += sum(n)
    if curr in perfCubes:
        print(s)
        print(s[0]*s[1]*s[2]*s[3]*s[4])

ans = [2, 101, 113, 151, 173]
print(2*101*113*151*173)
