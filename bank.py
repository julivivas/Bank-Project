balance = 0 
initial_balance = 0 
depost_amount = 0
withdrawal_amount = 0
deposit_count = 0
withdrawal_count = 0
penalty_amount = 0
penalty_count = 0
flag = True

BORDER_COUNT = 25
STAR_BORDER = "*" * BORDER_COUNT
DASH_BORDER = "-" * BORDER_COUNT


print(("\n" + STAR_BORDER + "\nWelcome to Banco Popular!\n" + STAR_BORDER))


#Account Setup

print(("\n" + DASH_BORDER + "\nAccount Setup\n" + DASH_BORDER + "\n"))
name = input("Account name: ")

while balance <= 0:
	input_string = input("Starting Balance: $")
	
	
	try:
		
		input_float = float(input_string)
		if input_float >= 0:
			if input_string == format(input_float, '.0f') or input_string == format(input_float, '.2f'):
				balance = input_float
				
		else:
			continue
			
	except ValueError:
		continue

print("\nWelcome new account member !\n"
f'Account {name} created with starting balance: ${balance:.2f}')
	
initial_balance = balance


while True:

  if balance <= 0:
    choice = input("\nSelect option:\n"
                   "(1) Deposit funds\n"
                   "(2) Withdraw funds\n"
                   "(3) View bank account balance\n")
    flag = False
        
  elif balance >= 0:
    choice = input("\nSelect option:\n"
                   "(1) Deposit funds\n"
                   "(2) Withdraw funds\n"
                   "(3) View bank account balance\n"
                   "(4) Close account\n")
    flag = True              
                   
  if choice == '1':
  	print("\n" + DASH_BORDER + "\nDeposit Funds\n" + DASH_BORDER)
  	
  	
  	try:
  				deposit_input = input("Amount to deposit: $")
  				dpeosit_float = float(deposit_input)
  				if dpeosit_float <= 0:
  					print("Transcation Failed. Invalid amount deposit.")
  				if dpeosit_float > 0 :
  					 if deposit_input == format(dpeosit_float, '.0f') or deposit_input == format(dpeosit_float, '.2f') :
  							deposit_count += 1
  							balance += dpeosit_float
  							print(f"Account Name: {name}")
  							print(f'Deposit Amount: {dpeosit_float:.2f}')
  							print(f'New Balance: {balance:.2f}')
  					 else:
  							print("Transcaction Failed. Invalid amount deposit.")
  				
  				
  				
  	except:
  			print("Transcaction Failed. Invalid amount deposit.")
  elif choice == '2':
  	print('\n' + DASH_BORDER + "\nWithdrawl Funds\n" + DASH_BORDER)
  	
  	while True:
  		
  		try:
  			withdrawal_input = input("Amount to withdraw: $")
  			withdrawal_float = float(withdrawal_input)
  			if withdrawal_float <= 0 :
  				print("Transaction Failed. Invalid amount deposit.")
  				break
  			if withdrawal_float > 0:
  				if withdrawal_input == format(withdrawal_float, '.0f') or withdrawal_input == format(withdrawal_float, '.2f'):
  				#Overdraft
  					temp_balance = balance - withdrawal_float
  					
  					if temp_balance <= -5000:
  						print('Transaction Failed. Withdrawal amount exceeds overdraft limit.')
  						break
  						
  					elif temp_balance <= -1000 and temp_balance >= -5000:
  						print("Withdrawl amount is greater than account balance. Overdraft penalty of 3% applied.")
  						penalty_amount = 0.3 * withdrawal_float
  						penalty_count += 1
  						
  					elif -1000 < temp_balance  < -100:
  						print('Withdrawal amount is greater than accoutn balance. Overdraft penalty of 1% applied.')
  						penalty_amount = 0.1 * withdrawal_float
  						penalty_count += 1
  						
  					elif -100 <= temp_balance:
  						penalty_amount = 0
  						
  					withdrawal_count += 1
  					balance -= (withdrawal_float + penalty_amount)
  					print(f'Account Name: {name}')
  					print(f'Withdrawal Amount: ${withdrawal_float:.2f}')
  					print(f'Penalties: ${penalty_amount:.2f}')
  					print(f'New Balance: ${balance:.2f}')
  					
  					
  					print("Currency Withdrawn: ")
  					x = withdrawal_float
  					dollar_100 = int(x // 100)
  					if dollar_100 > 0:
  						print("$100s:", dollar_100)
  					dollar_50 = int(x % 100 // 50)
  					if dollar_50 > 0:
  						print("$50s:", dollar_50)
  					dollar_20 = int(x % 100 % 50 // 20)
  					if dollar_20 > 0:
  						print("$20s", dollar_20)
  					dollar_10 = int( x % 100 % 50 % 20 // 10)
  					if dollar_10 > 0:
  						print("$10s:" ,dollar_10)
  					dollar_5 = int(x % 100 % 50 % 20 % 10 // 5)
  					if dollar_5 > 0:
  						print("$5s:", dollar_5)
  					dollar_1 = int(x % 100 % 50 % 20 % 10 % 5)
  					if dollar_1 > 0:
  						print("$1s:", dollar_1)
  					x *= 100
  					q = int(x % 100 // 25)
  					if q > 0 :
  						print("quarters:", q)
  					d = int(x % 100 % 25 // 10)
  					if d > 0:
  						print('dimes:', d)
  					n = int(x % 100 % 25 % 10 // 5)
  					if n > 0 :
  						print('nickels:', n)
  					p = int(x % 100 % 25 % 10 % 5)
  					if p > 0:
  						print('pennies:', p)
  						
  					break
  					
  			
  					
  					
  					
  					
  				else:
  					print('Transaction Failed. Invalid withdrawal amount.')
  					break
  				
  				
  		except ValueError:
  			print("Transction Failed. Invalid withdrawal amount.")
  			break
  			
  elif choice == '3':
  	print("\n" + DASH_BORDER + '\nAccount Balance\n' + DASH_BORDER)		
  	print(f'Account Name: {name}')
  	print(f"Balance: ${balance:.2f}")
  	
  
  	
  elif choice == '4' and flag:
  	
  	
  	#Calculate percentage change in balance
  	percentage_change = (balance - initial_balance) * 100 / (initial_balance)
  	
  	
  	print("\n" + STAR_BORDER + '\nClosing Account\n' + STAR_BORDER)
  	print('\n' + DASH_BORDER + '\nFinal Account Statement\n' + DASH_BORDER)
  	print(f'Initial balance: ${initial_balance:.2f}')
  	print(f'Final balance: ${balance:.2f} (+{percentage_change:.2f}%)')
  	print(f'Deposit count: {deposit_count}')
  	print(f'Withdrawal count: {withdrawal_count}')
  	print(f'Overdraft penalty count: {penalty_count}')
  	
  	break

 			
					
					
					
					
					
  
  
  
  
print("\nThank you for banking with Banco Popular !")