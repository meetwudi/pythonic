while True:
    try:
        x = int(raw_input('Please input a integer'))
    except ValueError:
        print "Oops!"
