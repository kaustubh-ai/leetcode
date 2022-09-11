def min_moves_to_seat(seats: list[int], students: list[int]) -> int:
    seats.sort(), students.sort()

    return sum(abs(i - j) for i, j in zip(seats, students))


print(min_moves_to_seat([3, 1, 5], [2, 7, 4]))
# https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/
