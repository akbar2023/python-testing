import pytest

# function de tips


def total_with_tip(bill, percentage):
  tip =  (percentage/100)*bill
  
  if (tip > 500):
    tip = 500

  total = bill + tip

  if(total<5):
    total = 5

  return round(total, 2)

def test_tip_classic():
  assert total_with_tip(100, 20) == 120

def test_tip_classic():
  assert total_with_tip(100, 0) == 100

def test_tip_max_500():
  assert total_with_tip(100, 501) == 600

def test_tip_min_5():
  assert total_with_tip(2, 0) == 5
  assert total_with_tip(4, 15) == 5

def test_decimal_2():
  assert total_with_tip(2.456, 1) == 5
  assert total_with_tip(10.12, 15) == 11.64

