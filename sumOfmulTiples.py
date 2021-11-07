def calculate_sum(a, N):
    m = N / a
    sum = m * (m + 1) / 2
    ans = a * sum
    print("Sum of multiples of ", a,
          " up to ", N, " = ", ans)
    calculate_sum(7, 49)