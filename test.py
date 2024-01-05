class Feedback():
    def __init__(self, id,rating, comments, user_id, event_id):
        self.id = id
        self.rating = rating
        self.comments = comments
        self.user_id = user_id
        self.event_id = event_id

    def get_id(self):
        return self.id
    
    def get_rating(self):
        return self.rating

    def get_comments(self):
        return self.comments

    def get_user_id(self):
        return self.user_id

    def get_event_id(self):
        return self.event_id
    
    def set_rating(self, rating):
        self.rating = rating

    def set_comments(self, comments):
        self.comments = comments

    def set_user_id(self, user_id):
        self.user_id = user_id

    def set_event_id(self, event_id):
        self.event_id = event_id

    def __str__(self):
        return "Rating: " + str(self.rating) + " Comments: " + self.comments + " User ID: " + str(self.user_id) + " Event ID: " + str(self.event_id)
    

class Event():
    def __init__(self, event_id, event_name,user_id, date_time, description):
        self.event_id = event_id
        self.event_name = event_name
        self.user_id = user_id
        self.date_time = date_time
        self.description = description
        self.feedback: [Feedback] = []

    def get_event_id(self):
        return self.event_id
    
    def get_event_name(self):
        return self.event_name

    def get_user_id(self):
        return self.user_id

    def get_date_time(self):
        return self.date_time
    
    def get_description(self):
        return self.description

    def set_event_id(self, event_id):
        self.event_id = event_id

    def set_event_name(self, event_name):
        self.event_name = event_name

    def set_user_id(self, user_id):
        self.user_id = user_id

    def set_date_time(self, date_time):
        self.date_time = date_time

    def set_description(self, description):
        self.description = description

    def __str__(self):
        return "Event ID: " + str(self.event_id) + " Event Name: " + self.event_name + " User ID: " + str(self.user_id) + " Date and Time: " + str(self.date_time) + " Description: " + self.description
    
    def submit_feedback(self, feedback):
        self.feedback.append(feedback)

    def get_feedback(self):
        return self.feedback

    def get_avg_rating(self):
        sum = 0
        for f in self.feedback:
            sum += f.get_rating()
        return sum/len(self.feedback)    
    
    def delete_feedback_entry(self, feedback_id):
    # Delete the specified feedback entry
        for f in self.feedback:
            if f.get_id() == feedback_id:
                self.feedback.remove(f)
                return True
        return False

    
class User():
    def __init__(self, user_id, user_name, user_email):
        self.user_id = user_id
        self.user_name = user_name
        self.user_email = user_email

    def get_user_id(self):
        return self.user_id

    def get_user_name(self):
        return self.user_name

    def get_user_email(self):
        return self.user_email

    def set_user_id(self, user_id):
        self.user_id = user_id

    def set_user_name(self, user_name):
        self.user_name = user_name

    def set_user_email(self, user_email):
        self.user_email = user_email

    def __str__(self):
        return "User ID: " + str(self.user_id) + " User Name: " + self.user_name + " User Email: " + self.user_email
    

class EventManager:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def get_most_popular_event(self) -> Event:
        if not self.events:
            return None  

        max_avg_rating = float('-inf')
        most_popular_event = None

        for event in self.events:
            avg_rating = event.get_avg_rating()
            if avg_rating > max_avg_rating:
                max_avg_rating = avg_rating
                most_popular_event = event

        return most_popular_event
    
    def get_least_popular_event(self) -> Event:
        if not self.events:
            return None  

        min_avg_rating = float('inf')
        least_popular_event = None

        for event in self.events:
            avg_rating = event.get_avg_rating()
            if avg_rating < min_avg_rating:
                min_avg_rating = avg_rating
                least_popular_event = event

        return least_popular_event


def main():
    # creating users    
    user1 = User(1, "user1","user1@gmail.com")
    user2 = User(2, "user2","user2@gmail.com")
    user3 = User(3, "user3","user3@gmail.com")

    # creating events
    event1 = Event(1, "event1", 1, "2024-01-02 12:00:00", "event1 description")
    event2 = Event(2, "event2", 2, "2024-01-03 12:30:00", "event2 description")
    event3 = Event(3, "event3", 3, "2024-01-04 13:00:00", "event3 description")

    # creating feedback entries
    feedback1 = Feedback(1, 4, "feedback1", 1, 1)
    feedback2 = Feedback(2, 5, "feedback2", 2, 1)
    feedback3 = Feedback(3, 3, "feedback3", 3, 1)
    feedback4 = Feedback(4, 5, "feedback4", 1, 1)
    feedback5 = Feedback(5, 5, "feedback5", 2, 1)
    feedback6 = Feedback(6, 1, "feedback6", 3, 2)
    feedback7 = Feedback(7, 4, "feedback7", 1, 2)
    feedback8 = Feedback(8, 2, "feedback8", 2, 2)
    feedback9 = Feedback(9, 3, "feedback9", 3, 2)
    feedback10 = Feedback(10, 5, "feedback10", 1, 2)
    feedback11 = Feedback(11, 3, "feedback11", 2, 3)
    feedback12 = Feedback(12, 5, "feedback12", 3, 3)
    feedback13 = Feedback(13, 1, "feedback13", 1, 3)
    feedback14 = Feedback(14, 2, "feedback14", 2, 3)
    feedback15 = Feedback(15, 5, "feedback15", 3, 3)


    # adding events to event manager
    event_manager = EventManager()
    event_manager.add_event(event1)
    event_manager.add_event(event2)
    event_manager.add_event(event3)


    # adding feedback entries to events
    event1.submit_feedback(feedback1)
    event1.submit_feedback(feedback2)
    event1.submit_feedback(feedback3) 
    event1.submit_feedback(feedback4)
    event1.submit_feedback(feedback5)

    event2.submit_feedback(feedback6)
    event2.submit_feedback(feedback7)
    event2.submit_feedback(feedback8)
    event2.submit_feedback(feedback9)
    event2.submit_feedback(feedback10)

    event3.submit_feedback(feedback11)
    event3.submit_feedback(feedback12)
    event3.submit_feedback(feedback13)
    event3.submit_feedback(feedback14)
    event3.submit_feedback(feedback15)

    # printing out the users
    print("Users:")
    print(user1)
    print(user2)
    print(user3)

    # printing out the events
    print("\nEvents:")
    print(event1)
    print(event2)
    print(event3)

    # printing out the feedback entries in the events
    print("\nEvent 1 Feedback:")
    for f in event1.get_feedback():
        print(f)

    print("\nEvent 2 Feedback:")
    for f in event2.get_feedback():
        print(f)

    print("\nEvent 3 Feedback:")
    for f in event3.get_feedback():
        print(f)

    # printing out the average rating for the events        
    print(f"\nEvent 1 Average Rating: {event1.get_avg_rating()}")
    print(f"\nEvent 2 Average Rating: {event2.get_avg_rating()}")
    print(f"\nEvent 3 Average Rating: {event3.get_avg_rating()}")

    # deleting the feedback entry
    event1.delete_feedback_entry(1)
    event2.delete_feedback_entry(10)
    event3.delete_feedback_entry(15)

    # printing out the feedback entries in the events
    print("\nEvent 1 Feedback after removing feedback:")
    for f in event1.get_feedback():
        print(f)

    print("\nEvent 2 Feedback after removing feedback:")
    for f in event2.get_feedback():
        print(f)

    print("\nEvent 3 Feedback after removing feedback:")
    for f in event3.get_feedback():
        print(f)


    # printing out the average rating for the events
    print(f"\nEvent 1 Average Rating after removing feedback: {event1.get_avg_rating()}")
    print(f"\nEvent 2 Average Rating after removing feedback: {event2.get_avg_rating()}")
    print(f"\nEvent 3 Average Rating after removing feedback: {event3.get_avg_rating()}")

    # printing out the most popular event
    print(f"\nMost Popular Event: {event_manager.get_most_popular_event().get_event_name()} with average rating of {event_manager.get_most_popular_event().get_avg_rating()}")

    # printing out the least popular event
    print(f"\nLeast Popular Event: {event_manager.get_least_popular_event().get_event_name()} with average rating of {event_manager.get_least_popular_event().get_avg_rating()}")


if __name__ == "__main__":
    main()