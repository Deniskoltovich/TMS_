n = int(input())
lst = list(map(int, input().split()))
N = int(input())
for _ in range(n):
    lst.append(None)
answers = []
index = 0
while lst[index] != n:
    answer = [lst[index], lst[index + 1]]
    answers.append(answer)
    if lst[index] > lst[index + 1]:
        lst[index], lst[index + 1] = lst[index + 1], lst[index]
    lst[index + n] = lst[index]
    index += 1

for i in range(N):
    index_inp = int(input()) - 1
    if index_inp < index:
        print(*answers[index_inp])
    else:
        ind = (index_inp - index) % (n - 1)
        print(n, lst[index + 1 + ind])