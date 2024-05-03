


class books():
    def __init__ (self, book):
        self.book=book

    def add(self,book):
        f=open("kitobnomi.txt", "a")
        f.write(book)
        f.close()
    def read(self):
        f=open("kitobnomi.txt", "r")
        contents=f.read()
        print(contents)
        f.close()
mybook=books("")
print(mybook.add("kitoblar qo'shildi"))
print(mybook.read())