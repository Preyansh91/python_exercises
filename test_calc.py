import calc
import pytest

def test_calc_total():
	total = calc.calc_total(4,5)
	assert total == 9

def test_calc_multiply():
	result = calc.calc_multiply(2,3)
	assert result == 7


