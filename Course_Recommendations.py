# Math
def mathCourseRecommendation(grade, grade_math, high_math):
    if grade >= 1 and grade <= 8:
        # Sets suffix to match the grade number.
        match grade:
            case 1:
                suf = "st"
                link = "https://www.khanacademy.org/math/cc-1st-grade-math"
            case 2:
                suf = "nd"
                link = "https://www.khanacademy.org/math/cc-2nd-grade-math"
            case 3:
                suf = "rd"
                link = "https://www.khanacademy.org/math/cc-third-grade-math"
            case 4:
                suf = "th"
                link = "https://www.khanacademy.org/math/cc-fourth-grade-math"
            case 5:
                suf = "th"
                link = "https://www.khanacademy.org/math/cc-fifth-grade-math"
            case 6:
                suf = "th"
                link = "https://www.khanacademy.org/math/cc-sixth-grade-math"
            case 7:
                suf = "th"
                link = "https://www.khanacademy.org/math/cc-seventh-grade-math"
            case 8:
                suf = "th"
                link = "https://www.khanacademy.org/math/cc-eighth-grade-math"
        rec = str(grade) + suf + grade_math
    if grade >=9:
        rec = high_math
        link = "https://www.khanacademy.org/math/trigonometry"

# Science
def scienceCourseRecommendation(grade, fav_sub, mid_sci, high_sci):
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

# Language Arts
def languageartsCourseRecommendation(grade, read, vocab, grammar):
    if grade >= 2 and grade <= 5:
        # Sets suffix to math the grade number.
        match grade:
            case 2:
                suf = "nd"
                link = "https://www.khanacademy.org/ela/cc-2nd-reading-vocab"
            case 3:
                suf = "rd"
                link = "https://www.khanacademy.org/ela/cc-3rd-reading-vocab"
            case 4:
                suf = "th"
                link = "https://www.khanacademy.org/ela/cc-4th-reading-vocab"
        rec = str(grade) + suf + read
    elif grade > 6 and grade <= 10:
        suf = "th"
        rec = str(grade) + suf + vocab
        # Links for grades four to ten.
        match grade:
            case 5:
                link = "https://www.khanacademy.org/ela/cc-5th-reading-vocab"
            case 6:
                link = "https://www.khanacademy.org/ela/new-6th-grade-reading-and-vocabulary"
            case 7:
                link = "https://www.khanacademy.org/ela/cc-7th-reading-vocab"
            case 8:
                link = "https://www.khanacademy.org/ela/8th-grade-reading-and-vocabulary"
            case 9:
                link = "https://www.khanacademy.org/ela/cc-9th-reading-vocab"
            case 10:
                link = "https://www.khanacademy.org/ela/10th-grade-reading-and-vocabulary"
    elif grade > 10 or grade == 1:
        rec = grammar
        link = "https://www.khanacademy.org/humanities/grammar"