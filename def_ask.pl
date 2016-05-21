def ask_ok(prompt, retry=4, complain='yes or no'):
	while True:
		ok = input(prompt)
		if ok in ('yes','y'):
			return True
		if ok in ('no','n'):
			return False
		retry = retry - 1
		if retry < 0:
			raise OSError('No User')
		print(complain)

asking = ask_ok
asking