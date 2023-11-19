from src.minas import inicializarTableroInterno,inicializarTableroVisible,generarMinas,contarCeldasDestapadas,destaparCasilla
import pytest

def test_inicializarTableroInterno():
    assert inicializarTableroInterno() == [["","","","","","","",""],
                                            ["","","","","","","",""],
                                            ["","","","","","","",""],
                                            ["","","","","","","",""],
                                            ["","","","","","","",""],
                                            ["","","","","","","",""],
                                            ["","","","","","","",""],
                                            ["","","","","","","",""]]

def test_inicializarTableroVisible():
    assert inicializarTableroVisible() == [[".",".",".",".",".",".",".","."],
                                            [".",".",".",".",".",".",".","."],
                                            [".",".",".",".",".",".",".","."],
                                            [".",".",".",".",".",".",".","."],
                                            [".",".",".",".",".",".",".","."],
                                            [".",".",".",".",".",".",".","."],
                                            [".",".",".",".",".",".",".","."],
                                            [".",".",".",".",".",".",".","."]]

def test_generarMinas():
    tablero_interno = [["","","","","","","",""],
                       ["","","","","","","",""],
                       ["","","","","","","",""],
                       ["","","","","","","",""],
                       ["","","","","","","",""],
                       ["","","","","","","",""],
                       ["","","","","","","",""],
                       ["","","","","","","",""]]
    minas = generarMinas(tablero_interno)

    assert len(minas) == 10
    for x, y in minas:
        assert 0 <= x <= 7
        assert 0 <= y <= 7

    for x, y in minas:
        assert tablero_interno[y][x] == "*"


def test_contarCeldasDestapadas_tableroVacio():
    tablero_visible = [[".",".",".",".",".",".",".","."],
                        [".",".",".",".",".",".",".","."],
                        [".",".",".",".",".",".",".","."],
                        [".",".",".",".",".",".",".","."],
                        [".",".",".",".",".",".",".","."],
                        [".",".",".",".",".",".",".","."],
                        [".",".",".",".",".",".",".","."],
                        [".",".",".",".",".",".",".","."]]
    assert contarCeldasDestapadas(tablero_visible) == 0

def test_contarCeldasDestapadas_tableroParcialmenteLLeno():
    tablero_visible = [[".",".",".",".",".",".",".","."],
                        [".",".",".",".",".",".",".","."],
                        [".",".",".",".",".",".",".","."],
                        [".",".",".",".",".",".",".","."],
                        [".",".",".",".","1",".","3","."],
                        [".",".","*",".",".",".",".","."],
                        [".",".",".",".",".",".",".","."],
                        [".",".",".",".",".",".",".","."]]
    assert contarCeldasDestapadas(tablero_visible) == 3

def test_destaparCasilla():
    tablero_interno = inicializarTableroInterno()
    tablero_visible = inicializarTableroVisible()

    tablero_interno[0][0] = "*"

    continuar = destaparCasilla(tablero_visible, tablero_interno,1,1)
    assert continuar is True
    assert tablero_visible[1][1] == tablero_interno[1][1]

if __name__ == "__main__":
    pytest.main()
