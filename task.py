from crewai import Task
from agents import doctor, verifier, nutritionist, exercise_specialist

help_patients = Task(
    description=(
        "Review the uploaded blood test report and summarize the key medical findings."
    ),
    expected_output="A clear medical summary highlighting any significant observations.",
    agent=doctor,
    async_execution=False,
)

nutrition_analysis = Task(
    description=(
        "Based on the blood test report, provide tailored nutrition recommendations."
    ),
    expected_output="A list of personalized nutrition recommendations.",
    agent=nutritionist,
    async_execution=False,
)

exercise_planning = Task(
    description=(
        "Recommend a suitable exercise plan considering the health status in the report."
    ),
    expected_output="A detailed exercise plan customized to the individual's health.",
    agent=exercise_specialist,
    async_execution=False,
)

verification = Task(
    description=(
        "Review all recommendations and verify their consistency and safety."
    ),
    expected_output="A verification summary confirming all advice is consistent and safe.",
    agent=verifier,
    async_execution=False,
)
