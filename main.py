import turtle
import random
import winsound

screen = turtle.Screen()
screen.bgcolor("grey")
screen.title("Game")
FONT = ("arial", 17,"normal")
count_turtle = turtle.Turtle() #countu baştan çalışığ üst üste yazıları binmesin diye fonksiyonun içine koymadık
GRID = 10
COORDİNATS = [20,10,0,-10,-20]
turtle_list = list()
SCORE = 0
score_write = turtle.Turtle()
score_write.up()
score_write.hideturtle()
game_over = False #bunu oyunu durdurmak için bir dedğişken olarak kullanırız
if not game_over:
    winsound.PlaySound('sounddd.wav', winsound.SND_ASYNC)
score_write.color("dark blue")
top_height = screen.window_height()  # bize burada ekranın total yüksekliğini verir
score_write.setpos(0, top_height * 0.9 / 2)  # ve turtle ın pozisyonunu ayarladık
score_write.write(arg="Score: 0", move=False, align="center", font=FONT)
screen.addshape("picturee.gif")
def score_table():

    score_write.color("dark blue")
    score_write.hideturtle()  #turtle gizledik
    score_write.up() #peni hizledik
    top_height = screen.window_height()  # bize burada ekranın total yüksekliğini verir
    score_write.setpos(0, top_height * 0.9 / 2)  # ve turtle ın pozisyonunu ayarladık

    score_write.clear()  # bunu yapmazsak sürekli yazılar üst üste biner
    score_write.write(arg=f"Score: {SCORE}", move=False, align="center", font=FONT)




def make_turtle(x,y):
    grid_trt = turtle.Turtle()
    def handle_clik(x,y):
        print(x,y)
        global SCORE

        SCORE += 1  # global diye belirtmezsek tanımaz
        score_table()


    grid_trt.onclick(handle_clik)
    grid_trt.shapesize(2,2) #yükseklik ve genişlik ölçüleri alır yazılan sayı kadar turtle büyütür
    grid_trt.shape("picturee.gif")
    grid_trt.color("dark green")
    grid_trt.up()
    grid_trt.goto(x*GRID,y*GRID)
    turtle_list.append(grid_trt)
def setup_turtles():   #bütün turtle ları gizledik
    for y in  COORDİNATS:
         for x in COORDİNATS:
             make_turtle(x,y)
def hidden_turle(): #random hernagi bir turtle ekrana gösterdik
    for turt in turtle_list:
        turt.hideturtle()

def show_turtle(): #gizlenen turtle ların ortaya çıkmasını saplar
    if not game_over:

        hidden_turle()
        random.choice(turtle_list).showturtle()
        turtle.ontimer(show_turtle,10) # bu iki parametre alır birini fonksiyon adı ve ikincisi milisaniye cinsinde zamna
        #alır eğer bu fonk. içinde yazmazsam tek bir defa çalışır
        #fonksiyon içinde yazarsamda sürekli bir döngüye girecek ve böylece çalışmış olacak
        #eğer em başta hidden turtle yi çağırmasaydım sürekli ekranda ki turtle sayısı artardı
def countdown(time):#oyunu bitirmek için kullandık
    global game_over

    count_turtle.hideturtle()
    count_turtle.up()
    count_turtle.color("red")
    count_turtle.clear()


    if time>0:

        top_height = screen.window_height()  # bize burada ekranın total yüksekliğini verir
        count_turtle.setpos(0, (top_height * (0.9 / 2))-30)  # ve turtle ın pozisyonunu ayarladık
        count_turtle.clear()
        count_turtle.write(arg=f"Time: {time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda : countdown(time-1),1000) #lamdayı kullanmasakta olur ama daha doğru bir kullaanım sonucta
    else:
        top_heights = screen.window_height()
        count_turtle.clear()
        count_turtle.setpos(0,(top_heights * (0.9 / 2))-330)
        count_turtle.write(arg="Game Over!!!", move=False, align="center", font=("Arial",30,"bold"))
        game_over = True

def start() :
    turtle.tracer(0) #kamlumabağa yerleşirken bir animasyon çıkar amaç burada o animasyonu yok etmek
    setup_turtles()
    hidden_turle()
    show_turtle()
    countdown(10)
    turtle.tracer(1)
start()
turtle.mainloop()