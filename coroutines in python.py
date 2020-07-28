def searcher():
    import  time
    #some 4 seconds will be consumed in task
    book="This a fantastic book and also good knowledgable."
    time.sleep(4)

    while True:
        text= (yield )
        if text in book:
            print(" text in the book")

        else:
            print("Text is not in the book")

search = searcher()
print("Search started")
next(search)
print("Next method run")
search.send("book")
search.send("dev")

search.close()
