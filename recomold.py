import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Expanded and balanced course data
course_data = {
    'Course Name': [
        'Python for Engineers', 'Data Structures in C', 'Basic Civil Engineering',
        'Electrical Circuits 101', 'Thermodynamics Intro', 'Java Foundations',
        'Embedded Systems Basics', 'Intro to Robotics', 'Basic CAD Drawing',
        'Cybersecurity Essentials', 'Software Testing Basics', 'Advanced Python Programming',
        'Complex Electrical Systems', 'Advanced Dynamics', 'Java Advanced Techniques',
        'Robotics and AI', 'Advanced CAD Techniques', 'Network Security Principles',
        'Cloud Solutions for Engineers', 'Machine Learning for Robotics',
        'Structural Analysis', 'Concrete Technology', 'Construction Management Fundamentals',
        'Power System Fundamentals', 'Electrical Machine Design', 'Control Systems',
        'Fluid Mechanics', 'Heat Transfer', 'Advanced Machine Design', 'Finite Element Analysis'
    ],
    'Description': [
        'Learn Python programming applied in engineering tasks',
        'Explore essential data structures for technical problem-solving in C',
        'Understand the foundational concepts in civil engineering',
        'Introduction to electrical circuits for beginners',
        'Learn the basic principles of thermodynamics in mechanical engineering',
        'Build a strong foundation in Java programming tailored for engineers',
        'Get started with the fundamentals of designing embedded systems',
        'Explore the basics of robotics and automation',
        'Learn the essentials of mechanical design using CAD tools',
        'Understand the basics of cybersecurity tailored for engineers',
        'Introduction to the principles and practices of software testing',
        'Develop advanced Python applications for complex engineering problems',
        'Design and analyze complex electrical systems and circuits',
        'Study advanced concepts in mechanics and dynamics for mechanical engineers',
        'Learn advanced Java programming techniques with engineering applications',
        'Integrate artificial intelligence with robotics for advanced automation',
        'Master complex mechanical drawings and functionalities in CAD',
        'Explore deep network security strategies to protect engineering data',
        'Deploy and manage cloud computing solutions for engineering projects',
        'Apply machine learning techniques in robotics and automation',
        'Basics of structural engineering analysis',
        'Technological aspects of concrete, an essential construction material',
        'Essentials of project management in construction settings',
        'Basic principles and applications of power systems',
        'Design principles of electrical machinery',
        'Fundamentals of automatic control systems for engineers',
        'Core concepts of fluid dynamics in mechanical contexts',
        'Essential heat transfer principles for thermal engineering',
        'Advanced concepts and techniques in machine design',
        'Introduction to finite element methods for engineers'
    ],
    'Difficulty': [
        'Beginner', 'Beginner', 'Beginner',
        'Beginner', 'Beginner', 'Beginner',
        'Intermediate', 'Intermediate', 'Intermediate',
        'Intermediate', 'Intermediate', 'Intermediate',
        'Advanced', 'Advanced', 'Advanced',
        'Advanced', 'Advanced', 'Advanced',
        'Beginner', 'Beginner', 'Beginner',
        'Intermediate', 'Intermediate', 'Intermediate',
        'Advanced', 'Advanced', 'Advanced',
        'Beginner', 'Intermediate', 'Advanced'
    ],
    'Stream': [
        'Computer Science', 'Computer Science', 'Civil',
        'Electrical', 'Mechanical', 'Computer Science',
        'Electronics', 'Robotics', 'Mechanical',
        'Computer Science', 'Computer Science', 'Computer Science',
        'Electrical', 'Mechanical', 'Computer Science',
        'Robotics', 'Mechanical', 'Network',
        'Computer Science', 'Robotics',
        'Civil', 'Civil', 'Civil',
        'Electrical', 'Electrical', 'Electrical',
        'Mechanical', 'Mechanical', 'Mechanical', 'Mechanical'
    ],
    'Rating': [
        4.5, 4.0, 4.2,
        4.5, 4.3, 4.4,
        4.2, 4.6, 4.5,
        4.1, 4.3, 4.8,
        4.7, 4.9, 4.5,
        4.8, 4.6, 4.7,
        4.4, 4.9,
        4.3, 4.5, 4.4,
        4.4, 4.7, 4.3,
        4.4, 4.6, 4.8, 4.7
    ],
    'Udemy Link': [
        'https://udemy.com/course/example' for _ in range(30)  # Placeholder link repeated for all courses
    ]
}

# Create a DataFrame from the sample data
df = pd.DataFrame(course_data)

# Streamlit app
st.title("Engineering Course Recommendation System")

# Check if user is an engineering student
user_is_student = st.sidebar.checkbox("Are you an engineering student?")
if user_is_student:
    st.sidebar.header("User Profile")
    stream = st.sidebar.selectbox("Which engineering stream do you belong to?", df['Stream'].unique())

    # Function to determine difficulty level based on exam score
    def get_difficulty_level(score):
        if score >= 15:
            return "Professional"
        elif score >= 10:
            return "Intermediate"
        else:
            return "Beginner"

    # Exam page
    st.subheader("Take The Exam To Understand Your Difficulty Level")
    score = st.slider("What score did you get in the exam?", min_value=0, max_value=20, step=1)
    difficulty_level = get_difficulty_level(score)

    # Filter courses based on the user's selections and difficulty level
    filtered_courses = df[(df['Stream'] == stream) & (df['Difficulty'] == difficulty_level)]

    # Display recommended courses
    st.subheader("Recommended Courses")
    if not filtered_courses.empty:
        for idx, course in filtered_courses.iterrows():
            st.write(f"{idx + 1}. [{course['Course Name']}]({course['Udemy Link']}) - {course['Description']}")
    else:
        st.write("No courses found that match your criteria. Try different keywords or adjust your filters.")

    # Adding a bar chart for course ratings within the selected stream and level
    if not filtered_courses.empty:
        st.subheader("Course Ratings")
        st.bar_chart(filtered_courses.set_index('Course Name')['Rating'])

    # Add Google Form links based on the selected stream
    st.subheader("Take The Exam")
    st.write("Please take the exam to understand your difficulty level:")
    if stream == 'Computer Science':
        st.markdown("[Exam Form for Computer Science](https://docs.google.com/forms/d/e/1FAIpQLSf7JpNAbRik-BjKf3R4sgXCm-bfylo4YL0mFZpjMWw1UGEbaA/viewform?embedded=true)")
    elif stream == 'Civil':
        st.markdown("[Exam Form for Civil Engineering](https://forms.gle/hcFJquE2dXqYBcnF9)")
    elif stream == 'Electrical':
        st.markdown("[Exam Form for Electrical Engineering](https://forms.gle/do5DmDf2hPnQhBXh7)")
    elif stream == 'Mechanical':
        st.markdown("[Exam Form for Mechanical Engineering](https://forms.gle/rMwcWL8zNgK6BHVT7)")
    elif stream == 'Electronics':
        st.markdown("[Exam Form for Electronics](https://forms.gle/SCKqBNGk1BUCfmda6)")
    elif stream == 'Robotics':
        st.markdown("[Exam Form for Robotics](https://forms.gle/CjDnncdCqww3oiqp8)")
    elif stream == 'Network':
        st.markdown("[Exam Form Networking](https://forms.gle/VrMTeauvdunHD6jJ9)")
else:
    st.write("This portal is dedicated to engineering students.")

# Growth curve for each course over the past 5 years
if user_is_student:
    st.title("Course Enrollment Over Time")
    years = np.arange(2019, 2024)
    for domain in df['Stream'].unique():
        st.subheader(f"Growth Curve for {domain}")
        plt.figure(figsize=(12, 8))
        for course in df[df['Stream'] == domain]['Course Name']:
            enrollment = np.random.randint(100, 1000, size=5)  # Random enrollment data for each course
            plt.plot(years, enrollment, marker='o', label=course)

        plt.xlabel("Year")
        plt.ylabel("Enrollment")
        plt.title(f"Course Enrollment Over Time - {domain}")
        plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
        plt.grid(True)
        st.pyplot(plt)