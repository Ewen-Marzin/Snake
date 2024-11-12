from snakefinal import new_snake

def test_new_snake_sans_manger_pomme() :
    assert new_snake([(0,0), (0,1), (0,2)], (0,1), (2,2)) == ([(0,1), (0,2), (0,3)], (2,2))

def test_new_snake_avec_manger_pomme(): 
    assert new_snake([(0,0), (0,1), (0,2)], (0,1), (0,3))[0] == [(0,0),(0,1), (0,2), (0,3)]
