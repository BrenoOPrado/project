import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    assert encrypt_message('exemplo1teste', 7) == 'olpmexe_etset1'
    assert encrypt_message('exemplo1teste', 8) == 'etset_1olpmexe'
    assert encrypt_message('teste', 9) == 'etset'
    assert encrypt_message('teste', -1) == 'etset'
    with pytest.raises(TypeError):
        encrypt_message(3, 'error_test')
