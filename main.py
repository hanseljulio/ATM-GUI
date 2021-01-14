from Account import *
from tkinter import *
from tkinter import messagebox


root = Tk()
root.geometry("300x300")
root.title("Main")
root.resizable(False, False)

lines = []


def transferMoneyCalc():
    print(loggeduser.getMoney())
    if (moneyOut.get() <= 0):
        messagebox.showerror(title="Transfer failed", message="Invalid balance")
    else:
        test = int(loggeduser.getMoney()) - moneyOut.get()
        loggeduser.setMoney(str(test))
        messagebox.showinfo(title="Transfer Successful", message="Transfer Successful\n New balance: ${}".format(loggeduser.getMoney()))
        transferwindow.destroy()
        newwindow.destroy()
        newWindow(loggeduser)

    print(loggeduser.getMoney())


def withdrawMoneyCalc():
    print(loggeduser.getMoney())
    if (moneyWithdraw.get() <= 0):
        messagebox.showerror(title="Withdraw failed", message="Invalid balance")
    else:
        test = int(loggeduser.getMoney()) - moneyWithdraw.get()
        loggeduser.setMoney(str(test))
        messagebox.showinfo(title="Withdraw Successful", message="Transfer Successful\n New balance: ${}".format(loggeduser.getMoney()))
        withdrawwindow.destroy()
        newwindow.destroy()
        newWindow(loggeduser)

    print(loggeduser.getMoney())


def transferMoney():
    global transferwindow
    transferwindow = Toplevel(root)
    transferwindow.title("Transfer")
    transferwindow.geometry("400x550")

    transferToWho = Label(transferwindow, text="   Where are you transferring to?", fg="black", font=("arial", 12))
    transferToWho.grid(row=0, column=0)

    labelaccount = Label(transferwindow, text="Account number", fg="black", font=("arial", 12))
    labelaccount.grid(row=1, column=0)

    accountBox = Entry(transferwindow, textvariable=account)
    accountBox.grid(row=1, column=1)

    labeltransfer = Label(transferwindow, text="Amount to transfer", fg="black", font=("arial", 12))
    labeltransfer.grid(row=2, column=0)

    transferBox = Entry(transferwindow, textvariable=moneyOut)
    transferBox.grid(row=2, column=1)

    confirmbutton = Button(transferwindow, text="CONFIRM", fg="black", bg="yellow", relief=RIDGE, font=("arial", 12, "bold"), command=transferMoneyCalc)
    confirmbutton.grid(row=3, column=0)


def withdrawMoney():
    global withdrawwindow
    withdrawwindow = Toplevel(root)
    withdrawwindow.title("Withdraw")
    withdrawwindow.geometry("400x550")

    howmuch = Label(withdrawwindow, text="      How much are you withdrawing?", fg="black", font=("arial", 12))
    howmuch.grid(row=0, column=0)

    labelwithdraw = Label(withdrawwindow, text="Withdraw amount", fg="black", font=("arial", 12))
    labelwithdraw.grid(row=1, column=0)

    withdrawBox = Entry(withdrawwindow, textvariable=moneyWithdraw)
    withdrawBox.grid(row=1, column=1)

    confirmbutton = Button(withdrawwindow, text="CONFIRM", fg="black", bg="yellow", relief=RIDGE, font=("arial", 12, "bold"), command=withdrawMoneyCalc)
    confirmbutton.grid(row=3, column=0)


def settingsChanger():
    for i in range(len(lines)):
        if (lines[i] == username.get()):
            lines[i] = newUsername.get()
            loggeduser.setName(newUsername.get())
        elif (lines[i] == password.get()):
            lines[i] = newPassword.get()
            loggeduser.setPassword(newPassword.get())


    file = open("data.txt", "w")
    for i in range(len(lines)):
        file.write(lines[i])
        file.write("\n")
    lines.clear()
    file.close()

    managewindow.destroy()
    newwindow.destroy()
    newWindow(loggeduser)


def manageWindowDestroyer():
    managewindow.destroy()


def changeSettings():
    global managewindow
    managewindow = Toplevel(root)
    managewindow.title("Manage account settings")
    managewindow.geometry("400x550")

    manageMenu = Label(managewindow, text="   Enter your new information", fg="black", font=("arial", 12))
    manageMenu.grid(row=0, column=0)

    labelnewUser = Label(managewindow, text="Account name", fg="black", font=("arial", 12))
    labelnewUser.grid(row=1, column=0)

    newUser = Entry(managewindow, textvariable=newUsername)
    newUser.grid(row=1, column=1)

    labelnewPass = Label(managewindow, text="Account password", fg="black", font=("arial", 12))
    labelnewPass.grid(row=2, column=0)

    newPass = Entry(managewindow, textvariable=newPassword)
    newPass.grid(row=2, column=1)

    confirmbutton = Button(managewindow, text="CONFIRM", fg="black", bg="yellow", relief=RIDGE, font=("arial", 12, "bold"), command=settingsChanger)
    confirmbutton.grid(row=4, column=0)

    cancelbutton = Button(managewindow, text="CANCEL", fg="black", bg="yellow", relief=RIDGE, font=("arial", 12, "bold"), command=manageWindowDestroyer)
    cancelbutton.grid(row=5, column=0)


def newWindow(loggeduser):
    global newwindow
    newwindow = Toplevel(root)
    newwindow.title("Menu")
    newwindow.geometry("400x550")

    hello = Label(newwindow, text="   Welcome back, {}. Your balance is ${}\n What would you like to do today?".format(loggeduser.getName(), loggeduser.getMoney()), fg="black", font=("arial", 12))
    hello.grid(row=0, column=0)

    transferbutton = Button(newwindow, text="Transfer money", fg="black", bg="yellow", relief=RIDGE, font=("arial", 12, "bold"), command=transferMoney)
    transferbutton.grid(row=2, column=0)

    withdrawbutton = Button(newwindow, text="Withdraw money", fg="black", bg="yellow", relief=RIDGE, font=("arial", 12, "bold"), command=withdrawMoney)
    withdrawbutton.grid(row=3, column=0)

    managebutton = Button(newwindow, text="Change account credentials", fg="black", bg="yellow", relief=RIDGE, font=("arial", 12, "bold"), command=changeSettings)
    managebutton.grid(row=4, column=0)



def openMenu():
    global loggeduser
    money = 0

    file = open("data.txt", "r")
    userFound = False
    passFound = False


    for line in file:
        lines.append(line[:-1])

    file.close()

    print(lines)

    for i in range(len(lines)):
        if (username.get() == lines[i]):
            print()
            userFound = True
            if (password.get() == lines[i + 1]):
                print()
                passFound = True
                money = lines[i + 2]

    if (userFound == True and passFound == True):
        loggeduser = Account(username.get(), password.get(), money)
        newWindow(loggeduser)
    elif (userFound == True and passFound == False):
        messagebox.showerror(title="Wrong Password", message="Wrong Password - try again")
    elif (userFound == False):
        messagebox.showerror(title="User not found", message="Username not found")


# Storage
username = StringVar(root)
password = StringVar(root)
account = StringVar(root)
moneyOut = IntVar(root)
moneyWithdraw = IntVar(root)
newUsername = StringVar(root)
newPassword = StringVar(root)




# Design - Login
labelname = Label(root, text="Name", fg="black", font=("arial", 12))
labelname.grid(row=1, column=0)

name = Entry(root, textvariable=username).grid(row=1, column=1)

labelpass = Label(root, text="Password", fg="black", font=("arial", 12))
labelpass.grid(row=2, column=0)

passBox = Entry(root, show="*", textvariable=password).grid(row=2, column=1)

button = Button(root, text="Sign in", fg="black", bg="yellow", relief=RIDGE, font=("arial", 12, "bold"), command=openMenu)
button.grid(row=5, column=1)

root.mainloop()