import os


def generate_invitations(template, attendees):
    """
    Checks the type of input.
    """
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(i, dict) for i in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return
    
    """
    Checks if template is not empty and if yes prints an error.
    """
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    file_number = 1
    for attendee in attendees:
        output_content = template.format(
            name=attendee.get('name', 'N/A'),
            event_title=attendee.get('event_title', 'N/A'),
            event_date=attendee.get('event_date', 'N/A'),
            event_location=attendee.get('event_location', 'N/A')
        )
        
        """
        Writes to a file.
        """
        output_filename = f"output_{file_number}.txt"
        with open(output_filename, 'w') as file:
            file.write(output_content)
        print(f"Generated file: {output_filename}")
        file_number += 1

"""
Example usage.
"""
template = """Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team"""

"""
list of attendees.
"""
attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

generate_invitations(template, attendees)
