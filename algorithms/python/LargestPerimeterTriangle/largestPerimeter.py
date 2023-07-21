def largestPerimeter(self, A):
    A.sort()
    n = len(A)
    return next(
        (
            A[n - i - 2] + A[n - i - 1] + A[n - i]
            for i in range(1, len(A) - 1)
            if A[n - i - 2] + A[n - i - 1] > A[n - i]
        ),
        0,
    )