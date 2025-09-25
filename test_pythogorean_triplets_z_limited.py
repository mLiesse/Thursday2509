import pytest

from test import solve_pythagorean_triplets_z_limited

def test_pytogorean_triplets_z_limited_zero_entry():
    
    assert solve_pythagorean_triplets_z_limited(0) == []

def test_pytogorean_triplets_z_limited_invalid_entry_type():
    with pytest.raises(TypeError):
        solve_pythagorean_triplets_z_limited("a")