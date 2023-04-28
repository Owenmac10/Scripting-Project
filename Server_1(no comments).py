import zmq


banned_words = {"poo": "flowers", "but": "butterflies", "baxtard": "bubbles"}

context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.bind("tcp://*:5587")



while True:
    message = socket.recv().decode()
    print("Received message: %s" % message)

    # A for loop is set up to iterate over the received messages
    for word in message.split():
        if word in banned_words:
            print("Banned word detected you cant use this word: %s" % word)
            message = message.replace(word, banned_words[word])
            print("Cleaned message: %s" % message)
            print(type(message))
