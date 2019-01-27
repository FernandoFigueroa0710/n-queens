from n-queens-backtracking import solve


def test_nqueens():
    assert solve(0, 4, []) == 2
    assert solve(0, 8, []) == 92
