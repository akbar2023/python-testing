def total_with_tip(bill, percentage):
  tip =  (percentage/100)*bill
  
  if (tip > 500):
    tip = 500

  total = bill + tip

  if(total<5):
    total = 5

  return round(total, 2)

def test_120classic():
  assert total_with_tip(100, 20) == 120