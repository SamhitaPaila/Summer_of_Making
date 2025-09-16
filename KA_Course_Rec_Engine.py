# Recommends a Khan Academy coures based of grade level and favorite subject.
# Only for grades 1 to 12.

# Course options to choose from for recommendations.

life_skills = "Finatial Literacy"
comp = "Pixar in a Box"
grammar = "Grammar"
grade_math = " grade math"
high_math = "Trigonometry"
mid_sci = "Middle school "
high_sci = "High school "
economics = "Finance and capital markets"
hist = "World History"
test = "MCAT"
read = " grade reading & vocabulary"
vocab = " grade reading & vocab"


# Collect user attributes to inform recommendation.

while True:
    try:
        grade = int(input("What grade are you in? "))
    except ValueError:
        print("Not valid grade.")
        continue
    if grade >= 1 and grade <= 12:
        break
    else:
        print("Not valid grade.")
   
while True:
    try:
        fav_sub = input("What is your favorite subject " + 
                    "(computing, life skills, math, " + 
                    "biology, physics, chemistry, " + 
                    "economics, history, test prep, " + 
                    "language arts)? ")
        if fav_sub != "computing" and fav_sub != "ecomonics" and \
        fav_sub != "math" and fav_sub != "biology" and fav_sub != "chemistry" \
        and fav_sub != "economics" and fav_sub != "history" and \
        fav_sub != "test prep" and fav_sub != "language arts":
            print ("Not valid subject")
            continue
        else:
            break
    except ValueError:
        print ("Not valid subject")


# Make a course recommendation based on the user's attributes.
rec = ""
link = ""

# Computing
if fav_sub == "computing":
    rec = comp
    link = "https://www.khanacademy.org/computing/pixar"

# Life Skills
if fav_sub == "life skills":
    rec = life_skills
# Math
if grade >= 1 and grade <= 8 and fav_sub == "math":
    if grade == 1:
        suf = "st"
    elif grade == 2:
        suf = "nd"
    elif grade == 3:
        suf = "rd"
    else:
        suf = "th"
    rec = str(grade) + suf + grade_math
if grade >=9 and fav_sub == "math":
    rec = high_math

# Science
if grade <= 8 and fav_sub == "biology":
    rec = mid_sci + fav_sub
if grade <= 8 and fav_sub == "physics":
    rec = mid_sci + fav_sub
if grade <= 8 and fav_sub == "chemistry":
    rec = mid_sci + fav_sub
if grade >= 9 and fav_sub == "biology":
    rec = high_sci + fav_sub
if grade >= 9 and fav_sub == "physics":
    rec = high_sci + fav_sub
if grade >= 9 and fav_sub == "chemistry":
    rec = high_sci + fav_sub

# Economics
if fav_sub == "economics":
    rec = ecomonics

# History
if fav_sub == "history":
    rec = hist

# Test Prep
if fav_sub == "test prep":
    rec = test

# Language Arts
if grade >= 2 and grade <= 5 and fav_sub == "language arts":
    if grade == 2:
        suf = "nd"
    elif grade == 3:
        suf = "rd"
    else:
        suf = "th"
    rec = str(grade) + suf + read
elif grade > 6 and grade <= 10 and fav_sub == "language arts":
    suf = "th"
    rec = str(grade) + suf + vocab
elif grade > 10 or grade == 1 and fav_sub == "language arts":
    rec = grammar


# Khan Academy course recommendation.

if fav_sub == "computing" or fav_sub == "ecomonics" or \
fav_sub == "math" or fav_sub == "biology" or fav_sub == "chemistry" \
or fav_sub == "economics" or fav_sub == "history" or \
fav_sub == "test prep" or fav_sub == "language arts":
    print()
    print("We recommend the Khan Academy course: " + rec)
    print("Link: " + link)
