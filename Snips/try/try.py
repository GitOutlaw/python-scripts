
try:
    f = open('Snips/try/data/test_file.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print('File Opening...')
    print(f.read())
    f.close()
finally:
    print("Exiting...")
