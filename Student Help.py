import time
import calendar
import random
from tabulate import tabulate
import matplotlib.pyplot as pl
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer


def sound():
    mixer.init()                                                                                                        # initiation of sound
    mixer.music.load('D:\Som\Student Management\salamisound-7587855-double-beep-beep-as-e-g.mp3')                       # path of the music file


def alarm():
    print("\n" * 2)
    print(" " * 10, "Alarm Page")
    print("\n" * 2)
    hour = int(input("Enter hour:"))                                                                                    # specific time of the alarm
    minn = int(input("Enter min:"))
    sec = 0
    task = input("Enter task name:")
    n = 5                                                                                                               # no. of times the alarm will run
    print("The alarm is set for", str(hour) + ":" + str(minn))

    while True:
        if time.localtime().tm_hour == hour and time.localtime().tm_min == minn and time.localtime().tm_sec == sec:     # condition for time
            print("It's time for", task)
            break
    sound()
    while n > 0:
        mixer.music.play()
        time.sleep(1)
        n = n - 1

    sn = input("Press S for snooze:")                                                                                   #option for snooze
    if sn == "S":
        n = 3
        time.sleep(120)
        while n > 0:
            mixer.music.play()
            n = n - 1
    else:
        exit()


def s_calendar(year, month):                                                                                            #option for calender
    print("\n" * 2)
    c = calendar.TextCalendar(calendar.SUNDAY)
    st = c.formatmonth(year, month)
    print(st)


def grading():                                                                                                          #grading to analyse grades
    print("\n" * 2)
    print(" " * 10, "Grading Page")
    print("\n" * 2)
    g_r = input("Enter your grading style [If 10 point: Ten, If Percentage : Percent]:")
    if g_r == "Ten":
        target = float(input("Enter your target:"))
        subs = int(input("Enter your number of subjects:"))
        nos = subs
        s_counter = 0
        losi = []
        while subs > 0:
            s_name = input("Enter your subject:")
            s_target = float(input("Enter your subject target:"))
            s_c_m = float(input("Enter your current marks:"))
            sl = []
            sl.append(s_name)
            sl.append(s_target)
            sl.append(s_c_m)
            losi.append(sl)
            s_counter = s_counter + s_c_m
            if s_c_m >= s_target:
                print("You have achieved your target of", s_target)
            else:
                print("You have not achieved your target of", s_target)
            subs = subs - 1
        print(tabulate(losi, headers=['Subject Name', 'Current Marks', 'Target']))
        c_m = s_counter / nos
        if 10 >= c_m >= target > 0 and target <= 10:
            print("You have achieved your target of", target, ". Enjoy and work even harder")
        else:
            print("You have not achieved your target.")
    elif g_r == "Percent":
        target = float(input("Enter your target:"))
        subs = int(input("Enter your number of subjects:"))
        nos = subs
        s_counter = 0
        losi = []
        while subs > 0:
            s_name = input("Enter your subject:")
            s_target = float(input("Enter your subject target:"))
            s_c_m = float(input("Enter your current marks:"))
            sl = []
            sl.append(s_name)
            sl.append(s_target)
            sl.append(s_c_m)
            losi.append(sl)
            s_counter = s_counter + s_c_m
            if s_c_m >= s_target:
                print("You have achieved your target of", s_target)
            else:
                print("You have not achieved your target of", s_target)
            subs = subs - 1
        print(tabulate(losi, headers=['Subject Name', 'Current Marks', 'Target']))
        c_m = s_counter / nos
        if target <= c_m <= 10 and 10 >= target > 0:
            print("You have achieved your target of", target, ". Enjoy and work even harder")
        else:
            print("You have not achieved your target.")
    else:
        exit()


def reminders():                                                                                                        #reminder for storing reminders
    print("\n" * 2)
    print(" " * 10, "Reminders")
    print("\n" * 5)
    print("What do you want to do?")
    urgent = []
    semi_urgent = []
    imp = []
    print("1. Read a note")
    print("2. Write a note")
    print("3. Remove a note")
    od = int(input("Enter your no.:"))
    if od == 1:
        em = input("Enter the importance (Urgent/ Semi Urgent /Important:")
        if em == "Urgent":
            for a in urgent:
                print(a)
        elif em == "Semi Urgent":
            for a in semi_urgent:
                print(a)
        elif em == "Important":
            for a in imp:
                print(a)
        else:
            print("Wrong option")
    elif od == 2:
        em = input("Enter the importance (Urgent/ Semi Urgent /Important:")
        if em == "Urgent":
            it = input("Enter the note:")
            urgent.append(it)
        elif em == "Semi Urgent":
            it = input("Enter the note:")
            semi_urgent.append(it)
        elif em == "Important":
            it = input("Enter the note:")
            imp.append(it)
        else:
            print("Wrong option")
    elif od == 3:
        em = input("Enter the importance (Urgent/ Semi Urgent /Important:")
        if em == "Urgent":
            it = input("Enter the note:")
            urgent.remove(it)
        elif em == "Semi Urgent":
            it = input("Enter the note:")
            semi_urgent.remove(it)
        elif em == "Important":
            it = input("Enter the note:")
            imp.remove(it)
        else:
            print("Wrong option")
    else:
        exit()


def sleep_chart():                                                                                                      #sleep for sleep monitoring
    print("\n" * 2)
    print(" " * 10, "Sleep Chart")
    print("\n" * 2)
    x_ax = ["Required"]
    y_ax = [8.0]
    n = 1
    while n < 8:
        day = input("Enter the date (28/08):")
        sleep = float(input("Enter the amount of sleep you took (in hours):"))
        x_ax.append(day)
        y_ax.append(sleep)
        n += 1
    pl.bar(x_ax, y_ax, width=0.2, color=['blue', 'green', 'green', 'green', 'green', 'green', 'green', 'green', ])
    pl.xlabel("Date")
    pl.ylabel("Sleep (in hours)")
    pl.show()


def phone_book():
    print(" " * 10, "Phone book")
    print("\n" * 2)
    pb = {}
    print("What would you like to do?")
    print("1. Search a number")
    print("2. Add a number")
    print("3. Remove a number")
    print("4. Print all numbers")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        p_n = input("Enter the name:")
        if p_n in pb:
            print("Number:",pb[p_n])
        else:
            print("Name not found")
    elif choice == 2:
        name = input("Enter the name:")
        number = input("Enter the number:")
        pb[name] = number
    elif choice == 3:
        name = input("Enter the name:")
        if name in pb:
            del pb[name]
        else:
            print("Name not found")
    elif choice == 4:
        for name in pb:
            print(name,pb[name])
    else:
        exit()


def diary():                                                                                                            #diary for recordings daily moments
    if not os.path.exists("Diary"):
        os.mkdir("Diary")
    os.chdir("Diary")
    print("\n" * 2)
    print(" " * 10, "Welcome to your diary")
    print("\n" * 2)
    print("What do you want to do?")
    print("1. Read an entry")
    print("2. Write an entry")
    print("3. Remove an entry")
    od = int(input("Enter your no.:"))
    if od == 1:
        date = input("Enter the date:")
        dn = date + ".txt"
        f = open(dn,"r")
        print(f.read())
    elif od == 2:
        date = input("Enter the date:")
        dn = date + ".txt"
        f = open(dn, "w")
        info = input("Start here:")
        f.write(info)
        f.close()
    elif od == 3:
        date = input("Enter the date:")
        dn = date + ".txt"
        if os.path.exists(dn):
            os.remove(dn)
        else:
            print("The file does not exist")
    else:
        exit()


def study_notes():                                                                                                      #notes for storing subject notes
    if not os.path.exists("Notes"):
        os.mkdir("Notes")
        os.chdir("Notes")
    else:
        os.chdir("Notes")
    print("\n" * 2)
    print(" " * 10, "Notes Page")
    print("\n" * 2)
    print("What do you want to do?")
    print("1. Read your notes")
    print("2. Write notes")
    print("3. Delete your notes")
    print('\n')
    op = (int(input("Enter your option:")))
    print('\n')
    if op == 1:
        r_sn = input("Enter the name of subject:")
        r_scn = input("Enter the name of chapter:")
        r_ctn = input("Enter the name of topic:")
        os.chdir(r_sn)
        os.chdir(r_scn)
        fr = open(r_ctn + ".txt", 'r')
        print('\n')
        r = fr.read()
        print(r)
        fr.close()
    elif op == 2:
        w_sn = input("Enter the name of subject:")
        w_scn = input("Enter the name of chapter:")
        w_ctn = input("Enter the name of topic:")
        if not os.path.exists(w_sn):
            os.mkdir(w_sn)
        os.chdir(w_sn)
        if not os.path.exists(w_scn):
            os.mkdir(w_scn)
        os.chdir(w_scn)
        sf = open(w_ctn + ".txt", 'a')
        content = input('Write your notes:\n')
        sf.write(content)
    elif op == 3:
        print("What do you want to delete?")
        print("1. Delete subject")
        print("2. Delete note")
        print("3. Delete topic")
        d = int(input("Enter your option"))
        if d == 1:
            sdc = input("Subject:")
            if os.path.exists(sdc):
                os.remove(sdc)
        elif d == 2:
            sdc = input("Subject:")
            cdc = input("Subject:")
            os.chdir(sdc)
            if os.path.exists(cdc):
                os.remove(cdc)
        elif d == 3:
            sdc = input("Subject:")
            cdc = input("Chapter:")
            tdc = input("Topic:")
            os.chdir(sdc)
            os.chdir(cdc)
            if os.path.exists(tdc+".txt"):
                os.remove(tdc+".txt")
        else:
            exit()
    else:
        exit()


def timer():                                                                                                            #timer for studying adequate amount
    print("\n" * 2)
    print(" " * 10, "Timer Page")
    print("\n" * 2)
    run = input("Start? ")
    r_mins = int(input("Enter minutes:"))
    mins = 0
    if run == "yes":
        while r_mins != mins:
            print(">>>>", r_mins-mins, "minutes left.")
            time.sleep(900)
            mins += 15
        print("Session done!")
        n = 5
        sound()
        while n > 0:
            mixer.music.play()
            time.sleep(2)
            n = n - 1
    else:
        exit()


def schedule():                                                                                                         #schedule for maintaining time
    if not os.path.exists("Schedule"):
        os.mkdir("Schedule")
        os.chdir("Schedule")
    else:
        os.chdir("Schedule")
    print("\n" * 2)
    print(" " * 10, "Schedule Page")
    print("\n" * 2)
    print("What would you like to do?")
    print("1. Reading")
    print("2. Writing")
    print("\n")
    fu = int(input("Option:"))
    if fu == 1:
        print("\n")
        sch = open("schedule.txt", "r")
        s_rl = sch.readlines()
        for sc in s_rl:
            print(sc)
        sch.close()
    elif fu == 2:
        print("\n")
        print("What would you like to do?:")
        print("1. Make a new schedule and remove previous")
        print("2. Edit previous schedule")
        print("\n")
        d = int(input("Enter your choice:"))
        print("\n")
        if d == 1:
            sch = open("schedule.txt", "w")
            lines = []
            lw = input("Would you like to start?:")
            while lw == "Yes":
                line = input()
                if line:
                    lines.append(line)
                else:
                    break
            for ln in lines:
                sch.write(ln)
                sch.write("\n")
            sch.close()
        elif d == 2:
            sch = open("schedule.txt", "a")
            lines = []
            ly = input("Would you like to write?:")
            while ly == "Yes":
                line = input()
                if line:
                    lines.append(line)
                else:
                    break
            for ln in lines:
                sch.write(ln)
                sch.write("\n")
            sch.close()
        else:
            exit()
    else:
        exit()


def budget():
    if not os.path.exists("Budget"):
        os.mkdir("Budget")
        os.chdir("Budget")
    else:
        os.chdir("Budget")
    sp = open("Spend_sheet.txt", "r+")
    dp = open("Deposit_sheet.txt", "r+")
    chb = {}
    initial = 0
    print("\n" * 2)
    print(" " * 10, "Budget Page")
    print("\n" * 2)
    print("What would you like to do?")
    print("1. Check your balance")
    print("2. Spend")
    print("3. Deposit")
    print("\n")
    bg = int(input("Enter your option:"))
    print("\n")
    budo = input("Have you already entered your budget?:")
    print("\n")
    if budo == "No":
        bud = input("Enter your budget:")
        fl = "Budget " + bud
        dp.write(fl)
    elif budo == "Yes":
        for li in dp:
            ite = li.split()
            k = ite[0]
            v = int(ite[1])
            chb[k] = v
        for li in sp:
            ite = li.split()
            k = ite[0]
            v = int(ite[1]) * -1
            chb[k] = v
        if bg == 1:
            print("Transactions :-")
            for ki in chb:
                print(ki, chb[ki])
                initial = initial + chb[ki]
            print("Available balance :", initial)
        elif bg == 2:
            s_k = input("Enter your item:")
            s_v = input("Enter the value:")
            s_kv = s_k + " " + s_v
            sp.write("\n")
            sp.write(s_kv)
        elif bg == 3:
            d_k = input("Enter your item:")
            d_v = input("Enter the value:")
            d_kv = d_k + " " + d_v
            dp.write("\n")
            dp.write(d_kv)
        else:
            exit()
    else:
        exit()


def motivation():
    mf = open("Motivation.txt","r")
    li = mf.readlines()
    print(random.choice(li))


print("\n"*2)
print("-"*60)
print(" " * 10, "WELCOME TO STUDENT HELP MANAGEMENT")
print("-"*60)
print("\n"*2)
motivation()
print("-"*65)
print("\n"*1)
opi = 'y'
while opi == 'y':
    print("\n")
    print("What do you want to do?")
    print("\n")
    print("1. Notes")
    print("2. Grades")
    print("3. Alarm")
    print("4. Sleep Chart")
    print("5. Phonebook")
    print("6. Reminders")
    print("7. Diary")
    print("8. Calender")
    print("9. Timer")
    print("10. Schedule")
    print("11. Budget")
    print("\n" * 1)
    o = int(input("Enter your choice:"))
    if o == 1:
        study_notes()
    elif o == 2:
        grading()
    elif o == 3:
        alarm()
    elif o == 4:
        sleep_chart()
    elif o == 5:
        phone_book()
    elif o == 6:
        reminders()
    elif o == 7:
        diary()
    elif o == 8:
        y = int(input("Enter year:"))
        m = int(input("Enter month:"))
        s_calendar(y, m)
    elif o == 9:
        timer()
    elif o == 10:
        schedule()
    elif o == 11:
        budget()
    opi = input('Do you want to continue (y/n) ?:')
else:
    print("-------------------------------------------Thank You !!!!--------------------------------------------------")
    time.sleep(5)
    exit()
