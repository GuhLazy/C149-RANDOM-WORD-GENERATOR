from tkinter import*
root = Tk()

root.title("Random Word Genearator")
root.geometry("500x500")

generated_random_word = Label(root, text="")

def random_number ():
    alpha_list = ("a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z")
    random_no1= random.randint(1,26)
    random_no2 = (5)
    random_no3 = (19)
    random_no4 = (25)
    random_no5 = (16)
