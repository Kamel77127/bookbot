
def main(book):
    
    textook = readthebook(book)
    charlist , counter = countLetter(textook)
    my_list = sorted_list(charlist)
    

    print("________BEGINNING OF REPORT____________")

    print(f"{counter} words found in document")

    for ch in my_list:
       print(f"The {ch['char']} character was found {ch['num']} times")

    print("_______________END OF REPORT_______________")


def readthebook(book):
    with open(f"books/{book}") as f:
        book = f.read()
        return book


def countLetter(book):
  charlist = {}
  counter = len(book.split())
  for c in book:
   if c.isalpha():
        lower = c.lower()
        if lower not in charlist:
            charlist[lower] = 1
        else:
            charlist[lower] += 1
   else:
       c.replace(c , "")
  return charlist , counter



def sort_on(dic):
    return dic["num"]



def sorted_list(dic):
  sorted_list = []
  for ch in dic:
     
     sorted_list.append({"char" : ch , "num" : dic[ch]})
  sorted_list.sort(reverse=True , key=sort_on)
  return sorted_list
    

main("frankenstein.txt")
        

