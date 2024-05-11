'''
You are given N number of intervals, where each interval contains two integers denoting the start time and the end time for the interval.

The task is to merge all the overlapping intervals and return the list of merged intervals sorted by increasing order of their start time.

Two intervals [A,B] and [C,D] are said to be overlapping with each other if there is at least one integer that is covered by both of them.

For example:

For the given 5 intervals - [1, 4], [3, 5], [6, 8], [10, 12], [8, 9].

Since intervals [1, 4] and [3, 5] overlap with each other, we will merge them into a single interval as [1, 5].

Similarly, [6, 8] and [8, 9] overlap, merge them into [6,9].

Interval [10, 12] does not overlap with any interval.

Final List after merging overlapping intervals: [1, 5], [6, 9], [10, 12].
'''

class Solution:

    def merge_intervals(self, intervals):
        intervals.sort()
        output = []

        for i in intervals:
            if not output or output[-1][1] < i[0]:
                output.append(i)
            else:
                output[-1][1] = i[1]

        return output


if __name__ == "__main__":
    print(Solution().merge_intervals([[1, 4], [3, 5], [6, 8], [10, 12], [8, 9]]))