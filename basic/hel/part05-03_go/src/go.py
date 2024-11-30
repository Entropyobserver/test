def who_won(game_board: list) -> int:
    player1_count = sum(cell == 1 for row in game_board for cell in row)
    player2_count = sum(cell == 2 for row in game_board for cell in row)
    if player1_count > player2_count:
        return 1
    elif player2_count > player1_count:
        return 2
    else:
        return 0

# 测试用例
def test_who_won():
    # 测试用例1：玩家1获胜
    game_board1 = [
        [1, 2, 1],
        [1, 0, 2],
        [1, 2, 0]
    ]
    assert who_won(game_board1) == 1, "测试用例1失败"

    # 测试用例2：玩家2获胜
    game_board2 = [
        [2, 2, 1],
        [1, 2, 2],
        [1, 2, 0]
    ]
    assert who_won(game_board2) == 2, "测试用例2失败"

    # 测试用例3：平局
    game_board3 = [
        [1, 2, 1],
        [2, 1, 2],
        [2, 1, 2]
    ]
    assert who_won(game_board3) == 0, "测试用例3失败"

    print("所有测试用例通过")

# 运行测试
test_who_won()
