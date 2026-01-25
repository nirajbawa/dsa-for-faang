class Solution:
    def swap(self, arr, l, r):
        if l>=r:
            return
        arr[l], arr[r] = arr[r], arr[l]
        self.swap(arr, l+1, r-1)
    def reverse(self, arr: list, n: int) -> None:
        self.swap(arr, 0, n-1)
        for i in arr:
            print(i, end=",")