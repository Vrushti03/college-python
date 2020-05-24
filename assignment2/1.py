class student:
  def __init__(self):
    print('Student created.')

  def __del__(self):
    print('Destructor called. Student deleted.')

obj = student()
del obj