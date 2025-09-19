# Recommends a Khan Academy coures based of grade level and favorite subject.
# Only for grades 1 to 12.

# Course options to choose from for recommendations.

from Course_Recommendations import languageartsCourseRecommendation, mathCourseRecommendation, scienceCourseRecommendation


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

match fav_sub:
    # Computing
    case "computing":
        rec = comp
        link = "https://www.khanacademy.org/computing/pixar"
    # Life Skills
    case "life skills":
        rec = life_skills
        link = "https://www.khanacademy.org/college-careers-more/financial-literacy"
    # Math
    case "math":
        mathCourseRecommendation(grade, grade_math, high_math)
    # Science
    case "science":
        scienceCourseRecommendation(grade, fav_sub, mid_sci, high_sci)
    # Economics
    case "economics":
        rec = economics
        link = "https://www.khanacademy.org/economics-finance-domain/core-finance"
    # History
    case "history":
        rec = hist
        link = "https://www.khanacademy.org/humanities/world-history"
    # Test Prep
    case "test prep":
        rec = test
        link = "https://www.khanacademy.org/test-prep/mcat"
    # Language Arts
    case "language arts":
        languageartsCourseRecommendation(grade, read, vocab, grammar)


# Khan Academy course recommendation.

if fav_sub == "computing" or fav_sub == "ecomonics" or \
fav_sub == "math" or fav_sub == "biology" or fav_sub == "chemistry" \
or fav_sub == "economics" or fav_sub == "history" or \
fav_sub == "test prep" or fav_sub == "language arts":
    print()
    print("We recommend the Khan Academy course: " + rec)
    if link != "":
        print("Link: " + link)
