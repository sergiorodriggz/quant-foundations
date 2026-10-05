# tests/test_smoke.py
import numpy as np
import pytest

def test_media_basica():
    assert np.mean(np.array([1, 2, 3])) == pytest.approx(2.0)