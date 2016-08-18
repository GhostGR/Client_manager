# Name        : Costumer Management software
# Version     : V1.0
# Author      : Lykourgos Tanious
# Description :       CM.py is a script that manages costumer information
#               and previous transactions and interactions through a command
#               line interface using MySQL databases.
# Read licence.txt
# Copyright (c) 2016 Lykourgos Tanious


# importing and initializing colorama
# to support ansi terminal coloring in windows
import sqlite3 as sqlite
import colorama
import sys
from tabulate import tabulate
colorama.init()

# Connecting to DB
con = sqlite.connect("Clients.db")
cur = con.cursor()


# CMD function
class CMD:
    Exit = ["exit", "stop", "quit", "terminate", "end"]

    def pbanner(self):
        print(colorama.Fore.GREEN + colorama.Style.BRIGHT +
              "###############################################\n"
              "#          __          ___          ___       #\n"
              "#         /#/          |**\        /**|       #\n"
              "#        /#/           |* *\      /* *|       #\n"
              "#        \#\           |*  *\    /*  *|       #\n"
              "#         \#\          |*   *\__/*   *|       #\n"
              "#=============================================#\n"
              "#       Costumer management CMD utility       #\n"
              "#=============================================#\n"
              "#  Author  : Lykourgos Tanious                #\n"
              "#  Version : V1.0                             #\n"
              "#---------------------------------------------#\n"
              "#     Copyright (c) 2016 Lykourgos Tanious    #\n"
              "#---------------------------------------------#\n"
              "#     Type help to see available commands     #\n"
              "###############################################\n")

    def phelp(self):
        print(colorama.Fore.BLUE + colorama.Style.BRIGHT +
              "   banner        - Shows the main banner.                         \n"
              "   help          - Shows this.                                    \n"
              "   exit          - Terminates this application, other commands can\n"
              "                   also be used(stop, quit, end, terminate).      \n"
              "   format        - Formats database file with required tables.    \n"
              "   clients       - Lists clients in the database.                 \n"
              "   jobs          - Lists all jobs in the database.                \n"
              "   new client    - Adds a new client to the database.             \n"
              "   new job       - Creates a new job for a client.                \n"
              "   edit client   - Edit  an existing client record.               \n"
              "   edit job      - Edit an existing job.                          \n"
              "   delete client - Deletes a client.                              \n"
              "   delete job    - Deletes a job.                                 \n"
              "   erase         - Deletes all data and tables from the database. \n")

    def cli_delete(self):
        headers = ["ID", "First name", "Last name", "Cellphone", "Phone number", "Address", "Email", "Notes"]
        print(colorama.Fore.WHITE + colorama.Back.BLUE)
        did = input("What is the ID of the client :  ")
        cur.execute("SELECT * FROM clients WHERE ID = ?", did)
        dat = cur.fetchone()
        try:
            print(tabulate([dat], headers=headers, tablefmt="fancy_grid"))
            ans = input("Are you sure you want to delete the above client? (YES) :  ")
            if ans == "YES":
                cur.execute("DELETE FROM Clients WHERE ID = ?", str(did))
                print(colorama.Fore.GREEN + colorama.Style.BRIGHT + colorama.Back.RESET)
                print(colorama.Fore.YELLOW + colorama.Style.BRIGHT + "Done!")
                con.commit()
            else:
                print(colorama.Fore.RED + colorama.Style.BRIGHT + "Aborting!")
        except:
            print(colorama.Fore.RED + colorama.Style.BRIGHT + "Failed to delete client! is the ID correct?")

    def job_delete(self):
        headers = ["JID", "UID", "DATE", "LAPTOP", "SPECS", "COST", "DESCRIPTION", "NOTES", "COMPLETED"]
        print(colorama.Fore.WHITE + colorama.Back.BLUE)
        did = input("What is the ID of the job :  ")
        cur.execute("SELECT * FROM jobs WHERE JID = ?", did)
        dat = cur.fetchone()
        try:
            print(tabulate([dat], headers=headers, tablefmt="fancy_grid"))
            ans = input("Are you sure you want to delete the above job? (YES) :   ")
            if ans == "YES":
                cur.execute("DELETE FROM jobs WHERE JID = ?", str(did))
                print(colorama.Fore.GREEN + colorama.Style.BRIGHT + colorama.Back.RESET)
                print(colorama.Fore.YELLOW + colorama.Style.BRIGHT + "Done!")
                con.commit()
            else:
                print(colorama.Fore.RED + colorama.Style.BRIGHT + "Aborting!")
        except:
            print(colorama.Fore.RED + colorama.Style.BRIGHT + "Failed to delete job! is the ID correct?")

    def cli_edit(self):
        print(colorama.Fore.WHITE + colorama.Back.BLUE)
        cid = input("Client ID :   ")
        print("  1. First name \n"
              "  2. Last name  \n"
              "  3. Cell number\n"
              "  4. Home number\n"
              "  5. Address    \n"
              "  6. Email      \n"
              "  7. Notes      \n")
        field = input("Select column :  ")
        if field == "1":
            field = "FIRST_NAME"
        elif field == "2":
            field = "LAST_NAME"
        elif field == "3":
            field = "CELL_NUMBER"
        elif field == "4":
            field = "HOME_NUMBER"
        elif field == "5":
            field = "ADDRESS"
        elif field == "6":
            field = "EMAIL"
        elif field == "7":
            field = "NOTES"
        else:
            print(colorama.Fore.RED + colorama.Style.BRIGHT + "Invalid input !" + colorama.Fore.GREEN +
                  colorama.Style.BRIGHT)
            return
        dat = input("Data to input :  ")
        cur.execute("UPDATE Clients SET {} = ? WHERE ID = ?;".format(field), (dat, cid))
        con.commit()
        print(colorama.Fore.GREEN + colorama.Style.BRIGHT + colorama.Back.RESET)

    def job_edit(self):
        print(colorama.Fore.WHITE + colorama.Back.BLUE)
        did = input("Job ID :   ")
        print("  1. Date       \n"
              "  2. Laptop     \n"
              "  3. Specs      \n"
              "  4. Cost       \n"
              "  5. Description\n"
              "  6. Notes      \n"
              "  7. Completed  \n")
        field = input("Select column :  ")
        if field == "1":
            field = "DATE"
        elif field == "2":
            field = "LAPTOP"
        elif field == "3":
            field = "SPECS"
        elif field == "4":
            field = "COST"
        elif field == "5":
            field = "DESCRIPTION"
        elif field == "6":
            field = "NOTES"
        elif field == "7":
            field = "COMPLETED"
        else:
            print(colorama.Fore.RED + colorama.Style.BRIGHT + "Invalid input !" + colorama.Fore.GREEN +
                  colorama.Style.BRIGHT)
            return
        dat = input("Data to input :  ")
        cur.execute("UPDATE jobs SET {} = ? WHERE JID = ?;".format(field), (dat, did))
        con.commit()
        print(colorama.Fore.GREEN + colorama.Style.BRIGHT + colorama.Back.RESET)

    def cli_new(self):
        try:
            print(colorama.Fore.WHITE + colorama.Back.BLUE)
            fname = input("First Name  : ")
            lname = input("Last Name   : ")
            cnum = input("Cell Number : ")
            hnum = input("Home Number : ")
            addr = input("Address     : ")
            email = input("Email       : ")
            notes = input("Notes       : ")
            print("\n" + colorama.Fore.GREEN + colorama.Back.RESET)
            cur.execute("INSERT INTO Clients(ID, FIRST_NAME, LAST_NAME, CELL_NUMBER, HOME_NUMBER, ADDRESS, "
                        "EMAIL, NOTES) VALUES(NULL, ?, ?, ?, ?, ?, ? ,?);", (fname, lname, cnum, hnum, addr,
                                                                             email, notes))
            con.commit()
            print(colorama.Fore.YELLOW + colorama.Style.BRIGHT + "Client saved!")
        except:
            print(colorama.Fore.RED + colorama.Style.BRIGHT + "Unable to Create client! Have you "
                                                              "formatted the database ?")

    def job_new(self):
        try:
            print(colorama.Fore.WHITE + colorama.Back.BLUE)
            uid = input("User ID     : ")
            date = input("Date        : ")
            laptop = input("Laptop      : ")
            specs = input("Specs       : ")
            cost = input("Cost        : ")
            desc = input("Description : ")
            note = input("Notes       : ")
            completed = input("Completed   : ")
            print("\n" + colorama.Fore.GREEN + colorama.Back.RESET)
            cur.execute("INSERT INTO jobs(JID, ID, DATE, LAPTOP, SPECS, COST, DESCRIPTION, NOTES,  "
                        "COMPLETED) VALUES(NULL, ?, ?, ?, ?, ?, ? ,?, ?);", (uid, date, laptop, specs,
                                                                             cost, desc, note, completed))
            con.commit()
            print(colorama.Fore.YELLOW + colorama.Style.BRIGHT + "Job saved!")
        except:
            print(colorama.Fore.RED + colorama.Style.BRIGHT + "Unable to create job! Have you "
                                                              "formatted the database ?")
    def clients(self):
        headers = ["ID", "First name", "Last name", "Cellphone", "Phone number", "Address", "Email", "Notes"]
        try:
            cur.execute("SELECT * FROM clients")
            data = str(cur.fetchall())
            thing = data.replace('[(', '')
            thing = thing.replace(')]', '')
            thing = thing.replace("'", '')
            thing = thing.replace('(', '')
            list1 = thing.split('), ')
            c = 0
            for item in list1:
                list1[c] = item.split(', ')
                c += 1
            print(tabulate(list1, headers=headers, tablefmt="fancy_grid"))
        except:
            print(colorama.Fore.RED + colorama.Style.BRIGHT + "Unable to show clients! Have you "
                                                              "formatted the database ?")

    def jobs(self):
        headers = ["JID", "UID", "DATE", "LAPTOP", "SPECS", "COST", "DESCRIPTION", "NOTES", "COMPLETED"]
        try:
            cur.execute("SELECT * FROM jobs")
            data = str(cur.fetchall())
            thing = data.replace('[(', '')
            thing = thing.replace(')]', '')
            thing = thing.replace("'", '')
            thing = thing.replace('(', '')
            list1 = thing.split('), ')
            c = 0
            for item in list1:
                list1[c] = item.split(', ')
                c += 1
            print(tabulate(list1, headers=headers, tablefmt="fancy_grid"))
        except:
            print(colorama.Fore.RED + colorama.Style.BRIGHT + "Unable to show jobs! Have you "
                                                              "formatted the database ?")

    def erase(self):
        while True:
            print(colorama.Fore.RED + colorama.Style.BRIGHT)
            a = input("Are you sure you want to erase the database ? (YES/NO)")
            if a == "YES":
                try:
                    cur.execute("DROP TABLE clients")
                    cur.execute("DROP TABLE jobs")
                    print(colorama.Fore.YELLOW + colorama.Style.BRIGHT + "Done!")
                    break
                except:
                    print(colorama.Fore.RED + colorama.Style.BRIGHT + "Unable to delete!"
                                                                      " is the database already empty ?")
                    break
            elif a == "NO":
                break

    def format(self):
        try:
            cur.execute("CREATE TABLE clients("
                        "ID INTEGER PRIMARY KEY NOT NULL,"
                        "FIRST_NAME TEXT NOT NULL,"
                        "LAST_NAME TEXT NOT NULL,"
                        "CELL_NUMBER INT,"
                        "HOME_NUMBER INT,"
                        "ADDRESS TEXT,"
                        "EMAIL TEXT,"
                        "NOTES TEXT)")
            cur.execute("CREATE TABLE jobs("
                        "JID INTEGER PRIMARY KEY NOT NULL,"
                        "ID INTEGER NOT NULL,"
                        "DATE TEXT,"
                        "LAPTOP BOOL,"
                        "SPECS TEXT,"
                        "COST FLOAT,"
                        "DESCRIPTION TEXT,"
                        "NOTES TEXT,"
                        "COMPLETED BOOL,"
                        "FOREIGN KEY (ID) REFERENCES clients(ID))")
            con.commit()
            print(colorama.Fore.YELLOW + colorama.Style.BRIGHT + "Done!")
        except:
            print(colorama.Fore.RED + colorama.Style.BRIGHT + "Could not complete operation(Table "
                                                              "might be already formatted!)")

    def inpt(self, inp):
        if inp in self.Exit:
            if con:
                con.close()
                print(colorama.Fore.RED + colorama.Style.BRIGHT + "Connection closed!")
            print(colorama.Fore.RED + colorama.Style.BRIGHT + "Goodbye! ")
            sys.exit(0)
        elif inp == "banner":
            self.pbanner()
        elif inp == "help":
            self.phelp()
        elif inp == "delete client":
            self.cli_delete()
        elif inp == "delete job":
            self.job_delete()
        elif inp == "edit client":
            self.cli_edit()
        elif inp == "edit job":
            self.job_edit()
        elif inp == "new client":
            self.cli_new()
        elif inp == "new job":
            self.job_new()
        elif inp == "clients":
            self.clients()
        elif inp == "jobs":
            self.jobs()
        elif inp == "erase":
            self.erase()
        elif inp == "format":
            self.format()
        else:
            print(colorama.Fore.RED + colorama.Style.BRIGHT + "Invalid input! Type help to show commands.")


# Main Function
def main():
    cm = CMD()
    cm.pbanner()
    while True:
        print(colorama.Fore.GREEN + colorama.Style.BRIGHT)
        inp = input("CM>> ")
        cm.inpt(inp)

main()
