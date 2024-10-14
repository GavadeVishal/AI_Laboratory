def ask_question(question):
    response = input(question + " (yes/no): ").strip().lower()
    return response == 'yes'

def engineering_guidance():
    print("Expert System for Engineering Field Guidance")

    if ask_question("Do you enjoy working with circuits and electronics?"):
        if ask_question("Are you interested in designing digital systems or embedded devices?"):
            recommendation = "You should consider studying Electronics or Computer Engineering."
        else:
            recommendation = "You should consider studying Electrical Engineering."
    elif ask_question("Do you enjoy coding and software development?"):
        if ask_question("Are you interested in artificial intelligence or machine learning?"):
            recommendation = "You should consider studying Computer Science or AI Engineering."
        else:
            recommendation = "You should consider studying Software Engineering."
    elif ask_question("Do you like designing machines or mechanical systems?"):
        if ask_question("Are you interested in robotics or automation?"):
            recommendation = "You should consider studying Mechatronics or Robotics Engineering."
        else:
            recommendation = "You should consider studying Mechanical Engineering."
    elif ask_question("Do you enjoy working on construction or infrastructure projects?"):
        if ask_question("Are you interested in urban development or sustainable construction?"):
            recommendation = "You should consider studying Civil or Environmental Engineering."
        else:
            recommendation = "You should consider studying Structural Engineering."
    else:
        recommendation = "Your preferences are unclear. Explore different branches of engineering to find your interest."

    print("\nRecommendation: " + recommendation)

if __name__ == "__main__":
    engineering_guidance()
