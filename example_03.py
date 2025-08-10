# Given list is [2, 3, 6, 6, 5]. The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score

def find_runner_up_score(arr):
    max_value = 0 
    second_max = 0
    for i in range(len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]    
        elif arr[i] > second_max and arr[i]!=max_value:
            second_max = arr[i]   
    return second_max
            

def findRunnerUpScore(arr):
    scores = list(set(arr))
    scores.sort(reverse=True)
    print(scores)
    return scores[1]

my_list = [2, 3, 6, 6, 5]
result = find_runner_up_score(my_list)
result1 = findRunnerUpScore(my_list)
print(result)
print(result1)
