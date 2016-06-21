import math
print (math);

signal_power = 100;
noise_power = 10;
ratio = signal_power/noise_power
print(ratio);

degrees = 45
radians = degrees / 360.0 * 2 * math.pi
print(math.sin(radians))

x = math.sin(30)
print(x);
x = math.exp(math.log(x+1))
print(x);



# print_lyrics();

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.");
    print("I sleep all night and I work all day.");

repeat_lyrics(),print_lyrics();

def print_twice(bruce):
    print(bruce);
    print(bruce);
bruce = "ajay";
print_twice(bruce*4);
print_twice("1"*4);

def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)

#print(cat);
ajay = "ajay";
rao = "rao";
cat_twice(ajay,rao);

len("ajay rao kunjoor");
#Exercise 3.3
def right_justify(s):
   print(" " * (70 - len(s)) + s);

right_justify('allen')

#Exercise 3.4
def do_twice(f,v):
    f(v);
    f(v);

def print_spam(v):
    print(v);

v = "ajay";
do_twice(print_spam,v);

def do_four(f,v):
    do_twice(f,v);
    do_twice(f,v);

w = "rao";
do_four(print_spam,w);

#Exercise 3.5
def one():
    print("+","-"*4,"+","-"*4,"+");
    
def two():
    print("|"," "*4,"|"," "*4,"|");
    
def print_border():
   print ("+", "- " * 4, "+")

def print_row():
   row = "|", " " * 8, "|\n"
   print (row * 4)

def block():
   one(),two(),two(),two(),two(),one(),two(),two(),two(),two(),one();
    
block();
