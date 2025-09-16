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

# Collect user's grade.
while True:
    try:
        grade = int(input("What grade are you in? "))
    except ValueError:
        # If user does not enter an integer
        print("Not valid grade.")
        continue
    # If user enters valid grade, exit loop.
    if grade >= 1 and grade <= 12:
        break
    else:
        print("Not valid grade.")

# Collect user's favorite subject.  
while True:
    try:
        fav_sub = input("What is your favorite subject " + 
                    "(computing, life skills, math, " + 
                    "biology, physics, chemistry, " + 
                    "economics, history, test prep, " + 
                    "language arts)? ")
        # If user does not input one of the given subjects, let the user know and ask question again.
        if fav_sub != "computing" and fav_sub != "ecomonics" and \
        fav_sub != "math" and fav_sub != "biology" and fav_sub != "chemistry" \
        and fav_sub != "economics" and fav_sub != "history" and \
        fav_sub != "test prep" and fav_sub != "language arts":
            print ("Not valid subject")
            continue
        # If user inputs one of the given subjects, exit loop.
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
    link = "https://www.khanacademy.org/college-careers-more/financial-literacy"
# Math
if grade >= 1 and grade <= 8 and fav_sub == "math":
    # Sets suffix to match the grade number.
    if grade == 1:
        suf = "st"
        link = "https://www.khanacademy.org/math/cc-1st-grade-math"
    elif grade == 2:
        suf = "nd"
        link = "https://www.khanacademy.org/math/cc-2nd-grade-math"
    elif grade == 3:
        suf = "rd"
        link = "https://www.khanacademy.org/math/cc-third-grade-math"
    else:
        suf = "th"
    rec = str(grade) + suf + grade_math
    # Link for fourth to eighth grade.
    if grade == 4:
        link = "https://www.khanacademy.org/math/cc-fourth-grade-math"
    elif grade == 5:
        link = "https://www.khanacademy.org/math/cc-fifth-grade-math"
    elif grade == 6:
        link = "https://www.khanacademy.org/math/cc-sixth-grade-math"
    elif grade == 7:
        link = "https://www.khanacademy.org/math/cc-seventh-grade-math"
    elif grade == 8:
        link = "https://www.khanacademy.org/math/cc-eighth-grade-math"
if grade >=9 and fav_sub == "math":
    rec = high_math
    link = "https://www.khanacademy.org/math/trigonometry"

# Science
if grade <= 8 and fav_sub == "biology":
    rec = mid_sci + fav_sub
    link = "https://www.khanacademy.org/science/ms-biology"
if grade <= 8 and fav_sub == "physics":
    rec = mid_sci + fav_sub
    link = "https://www.khanacademy.org/science/ms-physics"
if grade <= 8 and fav_sub == "chemistry":
    rec = mid_sci + fav_sub
    link = "https://www.khanacademy.org/science/ms-chemistry"
if grade >= 9 and fav_sub == "biology":
    rec = high_sci + fav_sub
    link = "https://www.khanacademy.org/science/hs-biology"
if grade >= 9 and fav_sub == "physics":
    rec = high_sci + fav_sub
    link = "https://www.khanacademy.org/science/hs-physics"
if grade >= 9 and fav_sub == "chemistry":
    rec = high_sci + fav_sub
    link = "https://www.khanacademy.org/science/hs-chemistry"

# Economics
if fav_sub == "economics":
    rec = economics
    link = "https://www.khanacademy.org/economics-finance-domain/core-finance"

# History
if fav_sub == "history":
    rec = hist
    link = "https://www.khanacademy.org/humanities/world-history"

# Test Prep
if fav_sub == "test prep":
    rec = test
    link = "https://www.khanacademy.org/test-prep/mcat"

# Language Arts
if grade >= 2 and grade <= 5 and fav_sub == "language arts":
    # Sets suffix to math the grade number.
    if grade == 2:
        suf = "nd"
        link = "https://www.khanacademy.org/ela/cc-2nd-reading-vocab"
    elif grade == 3:
        suf = "rd"
        link = "https://www.khanacademy.org/ela/cc-3rd-reading-vocab"
    else:
        suf = "th"
    rec = str(grade) + suf + read
elif grade > 6 and grade <= 10 and fav_sub == "language arts":
    suf = "th"
    rec = str(grade) + suf + vocab
    # Links for grades four to ten.
    if grade == 4:
        link = "https://www.khanacademy.org/ela/cc-4th-reading-vocab"
    elif grade == 5:
        link = "https://www.khanacademy.org/ela/cc-5th-reading-vocab"
    elif grade == 6:
        link = "https://www.khanacademy.org/ela/new-6th-grade-reading-and-vocabulary"
    elif grade == 7:
        link = "https://www.khanacademy.org/ela/cc-7th-reading-vocab"
    elif grade == 8:
        link = "https://www.khanacademy.org/ela/8th-grade-reading-and-vocabulary"
    elif grade == 9:
        link = "https://www.khanacademy.org/ela/cc-9th-reading-vocab"
    elif grade == 10:
        link = "https://www.khanacademy.org/ela/10th-grade-reading-and-vocabulary"
elif grade > 10 or grade == 1 and fav_sub == "language arts":
    rec = grammar
    link = "https://www.khanacademy.org/humanities/grammar"


# Khan Academy course recommendation.

if fav_sub == "computing" or fav_sub == "ecomonics" or \
fav_sub == "math" or fav_sub == "biology" or fav_sub == "chemistry" \
or fav_sub == "economics" or fav_sub == "history" or \
fav_sub == "test prep" or fav_sub == "language arts":
    print()
    print("We recommend the Khan Academy course: " + rec)
    if link != "":
        print("Link: " + link)
