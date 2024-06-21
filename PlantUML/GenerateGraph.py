import requests

plantuml_code = """
@startuml
Alice -> Bob: Authentication Request
Bob --> Alice: Authentication Response
@enduml
"""

# Kroki server URL
url = "https://kroki.io/plantuml/png"

# Send the diagram code
response = requests.post(url, data=plantuml_code.encode("utf-8"))

# Save the image
with open("diagram.png", "wb") as file:
    file.write(response.content)

print("Diagram saved as diagram.png")
