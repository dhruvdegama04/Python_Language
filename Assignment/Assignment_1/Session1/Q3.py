"""3.Write a Python script called app_use_cases.py that prints three real-life 
apps you use daily and, for each, prints one way Python could be used in their backend 
or data analysis.
"""

def display_app_use_cases():
    apps = {
        "Instagram": "Backend web services and API routing powered by the Django framework.",
        "Spotify": "Data pipelines and machine learning algorithms for personalized music recommendations.",
        "Netflix": "Data analytics and A/B testing infrastructure to optimize video streaming and content delivery."
    }
    
    print("=== Real-Life Apps & Python Backend/Data Analysis Use Cases ===\n")
    for app_name, python_usage in apps.items():
        print(f"App: {app_name}")
        print(f"Python Role: {python_usage}\n")

if __name__ == "__main__":
    display_app_use_cases()