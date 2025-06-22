# coding exercise
'how many days,weeks and months left if we live upto 90 years from now'
'input->current age'
'output->_ days, _ weeks and _ months are left '
'1 year=365 days,  1 year=52 weeks,  1 year=12 months'
ip = int(input("enter ur current age in years: "))
ly = 90-ip
days = ly * 365
weeks = ly * 52
months = ly * 12
print(f"{days} days, {weeks} weeks and {months} months are left")
