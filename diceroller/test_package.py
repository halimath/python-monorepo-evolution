from diceroller import Roll

def test_roll_single_die():
    for _ in range(10000):
        r = Roll('d20')
        assert r.value >= 1
        assert r.value <= 20

def test_roll_multiple_dice():
    for _ in range(10000):
        r = Roll('3d8')
        assert r.value >= 3
        assert r.value <= 24