# Recommends a Khan Academy coures based of grade level and favorite subject.
# Only for grades 1 to 12.

# Course options to choose from for recommendations.

import streamlit as st
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


st.title("Khan Academy Course Recommendation")

# Collect user attributes to inform recommendation.

# Collect user's grade.
inputGrade=st.selectbox(
    'Grade: ',
    ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
)
grade = int(inputGrade)

# Collect user's favorite subject.
options = [
    'Biology', 'Chemistry', 'Computing', 'Economics', 'History', 'Language Arts',
    'Life Skills', 'Math', 'Physics', 'Test Prep'
    ]
inputFavSub=st.selectbox('Favorite Subject: ', options)
fav_sub = (inputFavSub)


# Make a course recommendation based on the user's attributes.
rec = ""
link = ""

match fav_sub:
    # Computing
    case "Computing":
        rec = comp
        link = "https://www.khanacademy.org/computing/pixar"
    # Life Skills
    case "Life Skills":
        rec = life_skills
        link = "https://www.khanacademy.org/college-careers-more/financial-literacy"
    # Math
    case "Math":
        rec, link = mathCourseRecommendation(grade, grade_math, high_math)
    # Science
    case "Biology":
         rec, link = scienceCourseRecommendation(grade, fav_sub, mid_sci, high_sci)
    case "Chemistry":
         rec, link = scienceCourseRecommendation(grade, fav_sub, mid_sci, high_sci)
    case "Physics":
         rec, link = scienceCourseRecommendation(grade, fav_sub, mid_sci, high_sci)
    # Economics
    case "Economics":
        rec = economics
        link = "https://www.khanacademy.org/economics-finance-domain/core-finance"
    # History
    case "History":
        rec = hist
        link = "https://www.khanacademy.org/humanities/world-history"
    # Test Prep
    case "Test Prep":
        rec = test
        link = "https://www.khanacademy.org/test-prep/mcat"
    # Language Arts
    case "Language Arts":
         rec, link = languageartsCourseRecommendation(grade, read, vocab, grammar)


# Khan Academy course recommendation.
st.subheader("Recommendation")
st.write(f"We recommend the Khan Academy course: {rec}")
if link != "":
    st.write(f"Link: {link}")
