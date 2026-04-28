#students registration in Robotics event

robotics = {"Amit", "Riya", "Kiran", "Neha"}
#students registration in AI workshop
ai = {"Neha","Karan","Pooja","Rohit"}

print("Robotics:",robotics)
print("AI Workshop:",ai)

#students registered in both events
both_events = robotics&ai
print("Students registered in both events:",both_events)
#students only in robotics
only_robotics = robotics-ai
print("Students only in Robotics:",only_robotics)
#students only in AI workshop
only_ai = ai-robotics       
print("Students only in AI Workshop:",only_ai)
#combine all participants(union)
all_students = robotics|ai
print("All students registered in either event:",all_students)