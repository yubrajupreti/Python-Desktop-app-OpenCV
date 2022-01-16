import os
from tkinter import *
import getpass
from tkinter import messagebox


import sqlite3
#import pyttsx3

#engine = pyttsx3.init('sapi5')
#voices= engine.getProperty('voices') #getting details of current voice
#engine.setProperty('voice', voices[2].id)
# value=login.active_user
# from GUIedit import user

# active_user=user()
# print(active_user)

# if active_user !='':

# conn = sqlite3.connect("hito_login.db")
# c = conn.cursor()
# c.execute("SELECT email FROM User WHERE username=:active_user",{'active_user':active_user})
# user_email = c.fetchall()
# print(user_email[0][0])

intro = '''This awesome personality test was first introduced by Japanese psychologists ‘Tadahiko Nagao’ in the year 2000 on one of his books, Kokology: The Game of Self-Discovery. This test has proven to be successful for most of
the people who took part in this test. It’s your turn now.
'''
cube_personality_test = [

    {
        'Intro': "\n\n--------------- ::The Cube Test:: ----------------\n\n\nImagine you are in a desert and you see a cube there.\nDo you see it?",
        'Question': ['How large is the cube?', 'What is it made of?', 'Where exactly is it in the desert?'],
        'choose':[{
            'answer': ['The cube is large.', 'The cube is small.'],
        },
            {
            'answer': ['Solid.', 'Not solid.'],
        },
            {
            'answer': ['Buried under the sand.', 'Standing on top of sand.', 'Floating in the air.', 'Spinning or moving.'],
        },

        ],
        'Result':[{
            'result': ['-You are probably a confident person. You could be a good manager as well.', '-You are a shy and modest person. You are quiet and dont like to be noticed at parties.'],
        },
            {
            'result': ["\n-You are a fully- formed individual who's hard to manipulate.", '\n-Your inner world and attitude to life are still forming into their correct shape.'],
        },
            {
            'result': ['\n-You like to plan things and think ahead.', '\n-You are a pragmatic person who knows exactly what you do and what you want from the life.', '\n-You are an artistic personality with great imagination.', '\n-You think outside the box and are not always ready to agree with conventions and sterotypes.'],
        },

        ],

    },
    {
        'Intro': "\n\n--------------- ::Ladder:: ----------------\n\n\nAs you are observing the cube, See a ladder also.\n",
        'Question': ['What material is the ladder made from?', 'How tall is it?', 'Where is it in relation to the cube?', 'Where is it in relation to the cube?'],
        'choose':[{
            'answer': ['Same as the cube.', 'Made of steel or hard substance.', 'Made of wood.'],
        },
            {
            'answer': ['Ladder is short.', 'Ladder is tall.'],
        },
            {
            'answer': ['The ladder touches the cube.', 'The ladder is detached from the cube.'],
        },
            {
            'answer': ['Ladder is underneath the cube.', 'Ladder is on the same plane as the cube.', 'Ladder is above the cube.']
        }

        ],
        'Result':[{
            'result': ['\n', '\n', '\n'],

        },
            {
            'result': ['-You like having a small group of friends.\n', '-You are extroverted and keep several friends and acquaintances.\n'],
        },
            {
            'result': ['-You are close to them and may solve problems with their help.\n', '-You more self-assured.\n'],
        },
            {
            'result': ['-Your friends see you as a leader and authoritative figure.', '-You and your friends are equals.', '-You see your friends as the authoritative ones in your life.']
        }
        ],

    },
    {
        'Intro': "\n\n--------------- ::Horse:: ----------------\n\n\nNow, You picture a horse appearing in the desert.\n",
        'Question': ['How far is it from the cube? What is it doing?', 'What does it look like?', 'Is the horse tied up or roaming freely?', 'Is it wearing a saddle?'],
        'choose':[{
            'answer': ['Distant from the cube or moving in the opposite direction.', 'Near or moving closer.'],
        },
            {
            'answer': ['A Strong brown/black/white horse.', 'A shiny Pegasus or a unicorn.'],
        },
            {
            'answer': ['The horse is tied up.', 'The horse is roaming freely.'],
        },

            {
            'answer': ['Yes.', 'No.'],
        },

        ],
        'Result':[{
            'result': ['\n-The horse is your ideal partner\nYou are feeling distant from your current partner, or far away from reaching your ideal one.\n', '\n-The horse is your ideal partner\nYour relationship is with you partner is good, or you are an understanding and a caring person.\n'],
        },
            {
            'result': ['-You want a dependable family partner who you can reply on.\n', '-You are likely dreaming about someone you will never have, or a celebrity.\n'],
        },
            {
            'result': ["-You dictate what your partner does, who they're friends with, and more. \nRegardless of how you feel about what your partner does, who your partner is friends with, \nor anything else, if you're telling them what they are and aren't allowed to do in terms of those things, you're likely being too controlling.\n", '-You are submissive in nature, you obey your partner to avoid argument\n'],
        },
            {
            'result': ['-You trust your partner and feel protected near them.\n', '-You view your partner as uncontrollable, unpredictable\n'],
        },


        ],

    },
    {
        'Intro': "\n\n--------------- ::Flower:: ----------------\n\n\nCan you picture any flower in the desert?\n",
        'Question': ['Where are they situated compared to the cube?', 'How many of them do you see in there?'],
        'choose':[{
            'answer': ['Flowers are near the cube.', 'Flowers are away from the cube.'],
        },
            {
            'answer': ['Just one flower.', 'Colorful garden of flowers.'],
        },

        ],
        'Result':[{
            'result': ['-You wish for a close relationship with your children, or you already have one.\n', '-You do not particularly care about the distance between you and your children.\n'],
        },
            {
            'result': ['-You are not so good with kids, you will probably have only one child.\n', '-You have a strong feelings about kids, you are likely to have multiple kids in near future.\n'],
        }
        ],

    },
    {
        'Intro': "\n\n--------------- ::Thunderstorm:: ----------------\n\n\nAnd now the thunderstorm begins.Think of it in detail.\n",
        'Question': ['Is it violent/big or calm/small ?', 'What is the distance between the storm and the cube?'],
        'choose':[
            {
                'answer': ['Violent.', 'Calm.'],
            },
            {
                'answer': ['Far.', 'Near.', 'Directly above your head.'],
            },

        ],
        'Result':[
            {
                'result': ['-The storm is all about your stress levels., You do not react well to stressful situations and you are probably dealing with bad stress right now.\n', '-The storm is all about your stress levels. You do not stress easily and everyone else taking this test hates you for it\n'],
            },
            {
                'result': ['-You are living life with little worry.\n', '-You are ready to face what lies ahead.\n', '-You feel like your troubles are currently overwhelming you.\n'],
            },

        ],

    },
]



root = Tk()
root.title("HITO")
root.geometry("1360x690+0+0")
root.minsize(1280, 690)
title = Label(root, text="Personality Test", font=("times new roman", 30, "bold"), bg="green", fg="yellow", bd=10, relief=GROOVE)
title.pack(fill = X, expand = False)

def test(x, i, j):
    a = x
    a -= 1
    j -= 1
    global answer
    answer += cube_personality_test[i]['Result'][j]['result'][a]
    if l1:
        l1.destroy()
    if l2:
        l2.destroy()
    if btn1:
        btn1.destroy()
    if btn2:
        btn2.destroy()
    if btn3:
        btn3.destroy()
    if btn4:
        btn4.destroy()

    return root.quit()


def test1(x, i, j):
    a = x
    a -= 1
    j -= 1
    global answer
    answer += cube_personality_test[i]['Result'][j]['result'][a]
    if l1:
        l1.destroy()
    if l2:
        l2.destroy()
    if l1:
        l1.destroy()
    if l2:
        l2.destroy()
    if btn1:
        btn1.destroy()
    if btn2:
        btn2.destroy()
    if btn3:
        btn3.destroy()
    if btn4:
        btn4.destroy()
    return root.quit()


def test2(x, i, j):
    a = x
    a -= 1
    j -= 1
    global answer
    answer += cube_personality_test[i]['Result'][j]['result'][a]
    if l1:
        l1.destroy()
    if l2:
        l2.destroy()
    if btn1:
        btn1.destroy()
    if btn2:
        btn2.destroy()
    if btn3:
        btn3.destroy()
    if btn4:
        btn4.destroy()
    return root.quit()

answer = ''
print(intro)
for i in range(5):
    j = 0
    # print(cube_personality_test[i]['Intro'])
    for question in cube_personality_test[i]['Question']:
        l1 = Label(root,  text=cube_personality_test[i]['Intro'],font=("times new roman",20,"bold"))
        l1.pack()
        # print(question)
        a = 0
        l2 = Label(root, pady = 45,  text=question,font=("times new roman",18,"bold"))
        l2.pack()

        for choose in cube_personality_test[i]['choose'][j]['answer']:
            # print(choose)
            #
            bek = len(cube_personality_test[i]['choose'][j]['answer'])  # 2
            bek -= 1  # 1
            cho = cube_personality_test[i]['choose'][j]['answer'].index(choose)  # 0 & 1
            if cho == 0:
                ch1 = choose
            if cho == 1:
                ch2 = choose
            if cho == 2:
                ch3 = choose
            if cho == 3:
                ch4 = choose
        print("after answer loop")
        if bek == 1:
            btn1 = Button(root, width = 50, pady = 5, cursor="hand2", command=lambda: test(1, i, j), text=ch1,font=("times new roman",14,"bold"),bg="Green",fg="black")
            btn1.place(relx=.05, rely=.65)
            btn2 = Button(root, width = 50, pady = 5, cursor="hand2", command=lambda: test(2, i, j), text=ch2,font=("times new roman",14,"bold"),bg="Green",fg="black")
            btn2.place(relx=.55, rely=.65)
            btn3 = Button(root, width = 79, pady = 12,  state = "disabled", bg="Green",fg="black")
            btn3.place(relx=.05, rely=.80)
            btn4 = Button(root, width = 79, pady = 12,  state = "disabled", bg="Green",fg="black")
            btn4.place(relx=.55, rely=.80)

            # print(a)
        elif bek == 2:
            btn1 = Button(root, width = 50, pady = 5,  cursor="hand2", command=lambda: test1(1, i, j), text=ch1,font=("times new roman",14,"bold"),bg="Green",fg="black")
            btn1.place(relx=.05, rely=.65)
            btn2 = Button(root, width = 50, pady = 5,  cursor="hand2", command=lambda: test1(2, i, j), text=ch2,font=("times new roman",14,"bold"),bg="Green",fg="black")
            btn2.place(relx=.55, rely=.65)
            btn3 = Button(root, width = 50, pady = 5,  cursor="hand2", command=lambda: test1(3, i, j), text=ch3,font=("times new roman",14,"bold"),bg="Green",fg="black")
            btn3.place(relx=.05, rely=.80)
            btn4 = Button(root, width = 79, pady = 12,  state = "disabled", bg="Green",fg="black")
            btn4.place(relx=.55, rely=.80)
        else:
            btn1 = Button(root, width = 50, pady = 5,  cursor="hand2", command=lambda: test2(1, i, j), text=ch1,font=("times new roman",14,"bold"),bg="Green",fg="black")
            btn1.place(relx=.05, rely=.65)
            btn2 = Button(root, width = 50, pady = 5,  cursor="hand2", command=lambda: test2(2, i, j), text=ch2,font=("times new roman",14,"bold"),bg="Green",fg="black")
            btn2.place(relx=.55, rely=.65)
            btn3 = Button(root, width = 50, pady = 5, cursor="hand2", command=lambda: test2(3, i, j), text=ch3,font=("times new roman",14,"bold"),bg="Green",fg="black")
            btn3.place(relx=.05, rely=.80)
            btn4 = Button(root, width = 50, pady = 5, cursor="hand2", command=lambda: test2(4, i, j), text=ch4,font=("times new roman",14,"bold"),bg="Green",fg="black")
            btn4.place(relx=.55, rely=.80)
        j += 1
        #print(answer)
        # root.after(1000, root.destroy)
        root.mainloop()
root.destroy()

def goMain():
    root.destroy()
    os.system('python home.py')

def mail():
    email=StringVar()

    email_label = Label(root, text="Email",  compound=LEFT,
                       font=("times new roman", 20, "bold")).place(relx=.4, rely=.8)
    email_entry = Entry(root, bd=5, textvariable=email, relief=GROOVE, font=("", 15)).place(relx=.5, rely=.8)
    #import smtplib for mailing and sql for DB

    btn2 = Button(root, width=10, pady=5, command=lambda: send_mail(answer), text="Send",
                  font=("times new roman", 14, "bold"), bg="Green", fg="black")
    btn2.place(relx=.5, rely=.85)

    def send_mail(answer):
        import smtplib

        sender_email = 'apphito@gmail.com'
        # print(user_email[0][0])
        rec_email =email.get()

        password = 'BSZi95V8pyecM7h';
        subject = 'Hi, This is your Hito result'
        body = answer
        message = 'Subject:{}\n\n{}'.format(subject,body)

        server = smtplib.SMTP('smtp.gmail.com',587 )
        server.starttls()
        server.login(sender_email,password)
        print('Login sucessful')
        server.sendmail(sender_email,rec_email,message)
        print('Email has been sent to ', rec_email)

        server.quit()

root = Tk()
root.title("HITO")
root.geometry("1360x680+0+0")
root.minsize(1280, 690)
title = Label(root, text="Personality Test (Result)", font=("times new roman", 30, "bold"), bg="green", fg="yellow", bd=10, relief=GROOVE)
title.pack(fill = X, expand = False)

l1 = Label(root, pady = 65, text=answer, justify = 'left', font=("times new roman", 16, "bold"))
l1.pack()

btn1 = Button(root, width = 10, pady = 5, command = goMain, text = "HOME",font=("times new roman",14,"bold"),bg="Green",fg="black")
btn1.place(relx=.8, rely=.85)

btn2 = Button(root, width = 10, pady = 5, command = lambda: mail(), text = "E-mail",font=("times new roman",14,"bold"),bg="Green",fg="black")
btn2.place(relx=.1, rely=.85)

root.mainloop()
root.quit()


