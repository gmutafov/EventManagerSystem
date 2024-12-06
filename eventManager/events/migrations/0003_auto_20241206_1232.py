# Generated by Django 5.1.3 on 2024-12-06 10:32
from datetime import datetime

from django.db import migrations

def populate_data(apps, schema_editor):

    Event = apps.get_model('events', 'Event')

    events = [
        (1, 'Tech Summit 2024', 'A gathering of tech enthusiasts to explore emerging technologies.',
         '2024-12-10 09:00:00', 'London, United Kingdom', 2, 'https://example.com/image1.jpg', 1, 1),
        (2, 'Art Gala', 'A showcase of contemporary art from local artists.', '2024-12-15 18:00:00', 'Paris, France', 2,
         'https://example.com/image2.jpg', 2, 2),
        (3, 'Music Fiesta', 'Enjoy live music performances from renowned bands.', '2025-01-20 19:30:00','New York, USA',
            2, 'https://example.com/image3.jpg', 3, 3),
        (4, 'Startup Pitch Night', 'Pitch your ideas to top investors and mentors.', '2025-03-05 14:00:00',
         'Berlin, Germany', 2, 'https://example.com/image4.jpg', 4, 4),
        (5, 'Gaming Championship', 'A gaming event for e-sports enthusiasts.', '2025-02-14 10:00:00', 'Tokyo, Japan', 2,
         'https://example.com/image5.jpg', 5, 5),
        (6, 'Community Meetup', 'Meet local professionals and expand your network.', '2025-01-12 17:00:00',
         'Toronto, Canada', 2, 'https://example.com/image6.jpg', 6, 1),
        (7, 'Health & Wellness Workshop', 'Explore ways to maintain mental and physical health.', '2025-03-17 11:00:00',
         'Sydney, Australia', 2, 'https://example.com/image7.jpg', 7, 2),
        (8, 'Food Fest', 'Indulge in delicious cuisines from around the world.', '2025-04-22 13:00:00', 'Rome, Italy', 2,
            'https://example.com/image8.jpg', 8, 3),
        (9, 'Book Fair 2025', 'Discover new books and meet your favorite authors.', '2025-05-10 10:00:00',
         'Buenos Aires, Argentina', 2, 'https://example.com/image9.jpg', 9, 4),
        (10, 'Education Expo', 'An event showcasing opportunities in education.', '2025-06-18 09:30:00',
         'London, United Kingdom', 2, 'https://example.com/image10.jpg', 10, 5),
        (11, 'AI Conference', 'Discuss advancements in artificial intelligence.', '2025-07-19 14:00:00',
         'San Francisco, USA', 2, 'https://example.com/image11.jpg', 11, 1),
        (12, 'Film Festival', 'Watch and celebrate movies from around the world.', '2025-08-23 16:00:00',
         'Cannes, France', 2, 'https://example.com/image12.jpg', 12, 2),
        (13, 'Car Expo', 'A display of the latest innovations in automobiles.', '2025-09-12 12:00:00','Munich, Germany',
            2, 'https://example.com/image13.jpg', 13, 3),
        (14, 'Science Fair', 'Showcase groundbreaking science projects.', '2025-10-06 10:30:00', 'Tokyo, Japan', 2,
         'https://example.com/image14.jpg', 14, 4),
        (15, 'Fashion Show', 'A runway event featuring new trends in fashion.', '2025-11-11 18:30:00', 'Milan, Italy',
         2, 'https://example.com/image15.jpg', 15, 5),
        (16, 'Tech Fair', 'Technology companies display the latest gadgets and software.', '2025-12-10 11:00:00',
         'Seoul, South Korea', 2, 'https://example.com/image16.jpg', 16, 6),
        (17, 'Historical Reenactment', 'Live-action representation of historical events.', '2026-01-15 15:00:00',
         'Athens, Greece', 2, 'https://example.com/image17.jpg', 17, 7),
        (18, 'Literature Fest', 'Interactive sessions with best-selling authors.', '2026-03-21 12:30:00',
         'Dublin, Ireland', 2, 'https://example.com/image18.jpg', 18, 8),
        (19, 'Start-Up Week', 'Week-long conference for entrepreneurs.', '2026-05-18 09:00:00', 'New York, USA', 2,
         'https://example.com/image19.jpg', 19, 9),
        (20, 'Coding Hackathon', 'Solve problems and build applications in a day.', '2026-07-09 10:00:00',
         'Berlin, Germany', 2, 'https://example.com/image20.jpg', 20, 10),
        (21, 'International Food Expo', 'Taste dishes from cultures around the world.', '2026-08-12 14:00:00',
         'Mexico City, Mexico', 2, 'https://example.com/image21.jpg', 21, 1),
        (22, 'Jazz Night', 'Enjoy a night of smooth jazz music.', '2026-09-22 20:00:00', 'New Orleans, USA', 2,
         'https://example.com/image22.jpg', 22, 2),
        (23, 'Summer Carnival', 'A fun-filled event with games, rides, and food.', '2026-10-07 10:00:00',
         'Rio de Janeiro, Brazil', 2, 'https://example.com/image23.jpg', 23, 3),
        (24, 'Startup Bootcamp', 'Workshops and seminars for aspiring entrepreneurs.', '2026-11-04 09:00:00',
         'London, United Kingdom', 2, 'https://example.com/image24.jpg', 24, 4),
        (25, 'Digital Marketing Summit', 'Learn the latest strategies in digital marketing.', '2026-12-15 11:30:00',
         'Los Angeles, USA', 2, 'https://example.com/image25.jpg', 25, 5),
        (26, 'Mobile App Expo', 'Showcasing the most innovative mobile apps.', '2027-01-25 10:00:00', 'Dubai, UAE', 1,
         'https://example.com/image26.jpg', 26, 6),
        (27, 'Green Living Expo', 'Learn about sustainable living practices.', '2027-02-18 13:00:00',
         'Vancouver, Canada', 2, 'https://example.com/image27.jpg', 27, 7),
        (28, 'Space Exploration Conference', 'Exploring the future of space travel and research.','2027-03-22 09:00:00',
            'Houston, USA', 2, 'https://example.com/image28.jpg', 28, 8),
        (29, 'Comic Con', 'Meet comic book creators and see exclusive releases.', '2027-04-14 14:00:00',
         'San Diego, USA', 2, 'https://example.com/image29.jpg', 29, 9),
        (30, 'Virtual Reality Expo', 'Experience the latest in virtual reality technology.', '2027-05-10 12:00:00',
         'Los Angeles, USA', 2, 'https://example.com/image30.jpg', 30, 10),
        (31, 'Blockchain Summit', 'Discover the potential of blockchain technology.', '2027-06-02 09:30:00',
         'Zurich, Switzerland', 2, 'https://example.com/image31.jpg', 31, 1),
        (32, 'Drone Racing Championship', 'Witness high-speed drone races.', '2027-07-20 15:00:00', 'Las Vegas, USA',
            2,'https://example.com/image32.jpg', 1, 2),
        (33, 'Luxury Car Show', 'See the latest luxury vehicles from top brands.', '2027-08-11 10:00:00',
         'Monaco, Monaco', 2, 'https://example.com/image33.jpg', 33, 3),
        (34, 'Tech Conference', 'Explore the latest in technology and innovation.', '2027-09-03 08:30:00',
         'Singapore, Singapore', 2, 'https://example.com/image34.jpgHere', 30, 5)
    ]
    for event in events:
        Event.objects.create(
            title=event[1],
            description=event[2],
            date=event[3],
            location=event[4],
            created_by_id=event[5],
            created_at=datetime.now(),
            updated_at=datetime.now(),
            image=event[6],
            venue_id=event[7],
            organizer_id=event[8]
        )
    Venue = apps.get_model('common', 'Venue')
    Organizer = apps.get_model('common', 'Organizer')

    venues = [
        ('Grand Hall', 'Downtown City, City A', 500, '2024-12-01 09:00:00'),
        ('Expo Center', 'Central Park, City B', 800, '2025-01-15 08:00:00'),
        ('Skyline Arena', 'Skyline Drive, City C', 1000, '2025-02-01 10:00:00'),
        ('Tech Dome', 'Tech Park, City D', 400, '2025-03-05 09:30:00'),
        ('City Pavilion', 'City Plaza, City E', 600, '2025-04-12 11:00:00'),
        ('Convention Center', 'Expo Park, City F', 1200, '2025-05-08 12:00:00'),
        ('Oceanview Hall', 'Seaside Blvd, City G', 300, '2025-06-20 13:00:00'),
        ('Parkside Arena', 'Green Park, City H', 700, '2025-07-14 10:00:00'),
        ('Royal Theatre', 'Old Town, City I', 550, '2025-08-22 17:00:00'),
        ('Cultural Center', 'Civic Square, City J', 450, '2025-09-10 14:00:00'),
        ('Music Dome', 'Music Square, City K', 850, '2025-10-01 18:00:00'),
        ('Art Pavilion', 'Art District, City L', 500, '2025-11-05 09:00:00'),
        ('The Sports Complex', 'Sports Street, City M', 1300, '2025-12-01 11:00:00'),
        ('Tech Hub', 'Tech Valley, City N', 600, '2026-01-15 09:30:00'),
        ('Central Hall', 'Main Street, City O', 400, '2026-02-20 10:00:00'),
        ('The Summit', 'Hilltop Road, City P', 300, '2026-03-10 12:30:00'),
        ('The Grand Arena', 'City Plaza, City Q', 1200, '2026-04-15 09:00:00'),
        ('City Conference Center', 'City Center, City R', 1000, '2026-05-05 14:00:00'),
        ('Mountain View Amphitheater', 'Mountain Road, City S', 700, '2026-06-10 13:00:00'),
        ('Waterfront Hall', 'Harbor Bay, City T', 500, '2026-07-20 12:00:00'),
        ('The Innovation Hub', 'Innovation Street, City U', 400, '2026-08-15 10:00:00'),
        ('Sky High Center', 'Skyline Avenue, City V', 600, '2026-09-01 14:00:00'),
        ('Riverfront Plaza', 'River Road, City W', 800, '2026-10-05 09:00:00'),
        ('The Arena', 'Broadway St, City X', 1100, '2026-11-10 11:00:00'),
        ('City Arts Center', 'City Park, City Y', 500, '2026-12-01 13:00:00'),
        ('The Workshop Center', 'Industrial Avenue, City Z', 300, '2027-01-20 09:00:00'),
        ('Beachfront Pavilion', 'Coastal Road, City A2', 350, '2027-02-15 10:00:00'),
        ('Festival Grounds', 'Festival Park, City B2', 900, '2027-03-12 14:00:00'),
        ('Star Theater', 'Star Avenue, City C2', 650, '2027-04-18 15:00:00'),
        ('The Greenhouse', 'Greenwood St, City D2', 500, '2027-05-01 16:00:00'),
        ('The Sports Arena', 'Game Street, City E2', 1200, '2027-06-12 10:00:00'),
        ('City Hall Auditorium', 'City Hall, City F2', 400, '2027-07-19 11:00:00'),
        ('The Blue Sky Venue', 'Blue Hills, City G2', 700, '2027-08-25 09:00:00'),
        ('The Lighthouse', 'Lighthouse Point, City H2', 350, '2027-09-05 14:00:00'),
        ('City Park Auditorium', 'Park Road, City I2', 650, '2027-10-20 13:00:00'),
        ('Sunset Hall', 'Sunset Boulevard, City J2', 400, '2027-11-07 12:00:00'),
        ('The Exhibition Center', 'Exhibit Street, City K2', 800, '2027-12-12 10:00:00'),
        ('The Legacy Venue', 'Legacy Road, City L2', 500, '2028-01-17 11:00:00'),
        ('Crystal Clear Arena', 'Crystal Road, City M2', 750, '2028-02-28 13:00:00'),
        ('The Event Hub', 'Event Avenue, City N2', 1000, '2028-03-25 14:00:00'),
        ('Pine Ridge Arena', 'Pine Road, City O2', 450, '2028-04-10 12:00:00'),
        ('The Discovery Center', 'Discovery Avenue, City P2', 600, '2028-05-05 15:00:00'),
        ('Sunshine Pavilion', 'Sunshine Street, City Q2', 500, '2028-06-18 10:00:00'),
        ('The Bright Arena', 'Bright Road, City R2', 700, '2028-07-22 12:00:00'),
        ('The Royal Pavilion', 'Royal Square, City S2', 850, '2028-08-15 13:00:00'),
        ('Ocean Breeze Hall', 'Ocean Avenue, City T2', 400, '2028-09-10 11:00:00'),
        ('The Crystal Auditorium', 'Crystal Avenue, City U2', 600, '2028-10-04 14:00:00'),
        ('The Event Dome', 'Event Street, City V2', 1000, '2028-11-01 15:00:00'),
        ('The Galaxy Hall', 'Galaxy Road, City W2', 900, '2028-12-15 13:00:00')
    ]

    organizers = [
        (1, 'John Smith', 'john.smith@email.com', 'An experienced event organizer specializing in tech conferences.'),
        (2, 'Jane Doe', 'jane.doe@email.com', 'Founder of ArtWave, a platform for promoting contemporary art events.'),
        (3, 'Sarah Johnson', 'sarah.johnson@email.com',
         'Event planner with a passion for music festivals and live events.'),
        (4, 'Michael Brown', 'michael.brown@email.com',
         'Expert in organizing startup events and entrepreneur networking.'),
        (5, 'Emily Davis', 'emily.davis@email.com', 'Organizes e-sports tournaments and gaming championships.'),
        (6, 'David Wilson', 'david.wilson@email.com',
         'Community-focused event organizer, specializing in local meetups and networking.'),
        (7, 'Olivia Taylor', 'olivia.taylor@email.com',
         'Wellness advocate, organizing health and fitness workshops and expos.'),
        (8, 'James Anderson', 'james.anderson@email.com',
         'Curator of food festivals, bringing global cuisines to local communities.'),
        (9, 'Amelia Thomas', 'amelia.thomas@email.com',
         'Book lover and event planner for literary festivals and author meetups.'),
        (10, 'Daniel Jackson', 'daniel.jackson@email.com',
         'Education-focused event organizer, specializing in expos and academic conferences.'),
        (11, 'Matthew White', 'matthew.white@email.com',
         'AI and tech conference specialist with years of event coordination experience.'),
        (12, 'Charlotte Harris', 'charlotte.harris@email.com',
         'Film festival organizer with a focus on indie and global cinema.'),
        (13, 'Benjamin Clark', 'benjamin.clark@email.com',
         'Automobile exhibition organizer, focusing on cutting-edge automotive innovations.'),
        (14, 'Sophia Lewis', 'sophia.lewis@email.com',
         'Science event organizer, passionate about showcasing innovation and research.'),
        (15, 'Ethan Walker', 'ethan.walker@email.com',
         'Fashion show producer, curating the latest trends and designer collections.'),
        (16, 'Lily Hall', 'lily.hall@email.com',
         'Technology event planner with a focus on exhibitions and tech conferences.'),
        (17, 'Henry Allen', 'henry.allen@email.com',
         'Historical reenactment event organizer, dedicated to preserving cultural heritage.'),
        (18, 'Grace Young', 'grace.young@email.com',
         'Literature festival director, bringing together authors, poets, and readers.'),
        (19, 'Lucas King', 'lucas.king@email.com',
         'Entrepreneurship-focused event planner for startup weeks and business incubators.'),
        (20, 'Mia Scott', 'mia.scott@email.com',
         'Hackathon event organizer, fostering innovation through coding and collaboration.'),
        (21, 'Noah Adams', 'noah.adams@email.com',
         'Global food festival organizer, exploring diverse cultures through cuisine.'),
        (22, 'Isabella Carter', 'isabella.carter@email.com',
         'Jazz night curator, creating intimate music experiences for enthusiasts.'),
        (23, 'Alexander Mitchell', 'alexander.mitchell@email.com',
         'Summer carnival organizer, focusing on fun and interactive outdoor experiences.'),
        (24, 'Ella Perez', 'ella.perez@email.com',
         'Workshops and bootcamp event organizer, helping entrepreneurs grow their businesses.'),
        (25, 'Jack Roberts', 'jack.roberts@email.com',
         'Marketing summit planner, creating opportunities for digital marketing professionals.'),
        (26, 'Avery Evans', 'avery.evans@email.com',
         'Mobile app expo coordinator, bringing innovation and app development to the spotlight.'),
        (27, 'Madison Green', 'madison.green@email.com',
         'Sustainability expo organizer, promoting green living and environmental awareness.'),
        (28, 'Joshua Turner', 'joshua.turner@email.com',
         'Space exploration conference organizer, dedicated to the future of space science.'),
        (29, 'Chloe Morgan', 'chloe.morgan@email.com',
         'Comic convention organizer, uniting fans and creators in the comic book world.'),
        (30, 'Mason Lee', 'mason.lee@email.com',
         'Virtual reality expo organizer, showcasing the latest VR technology and experiences.'),
        (31, 'Logan Perez', 'logan.perez@email.com',
         'Blockchain summit coordinator, focused on the future of decentralized technologies.'),
        (32, 'Zoe Carter', 'zoe.carter@email.com',
         'Drone racing event coordinator, combining technology and sports in thrilling races.'),
        (33, 'Jackson Hall', 'jackson.hall@email.com',
         'Luxury car show organizer, featuring high-end automotive brands and exclusive models.'),
        (34, 'Lily Wilson', 'lily.wilson@email.com',
         'Luxury events organizer, focusing on exclusive brands and products.'),
        (35, 'Samuel Clark', 'samuel.clark@email.com',
         'Interactive events planner, specializing in hands-on experiences for attendees.'),
        (36, 'Nora Martinez', 'nora.martinez@email.com',
         'Technology exhibitions and conferences organizer, exploring new gadgets and trends.'),
        (37, 'Oliver Lee', 'oliver.lee@email.com',
         'Gaming events planner, hosting large-scale tournaments and fan gatherings.'),
        (38, 'Sophia King', 'sophia.king@email.com',
         'International food events coordinator, showcasing culinary talent from around the world.'),
        (
        39, 'Liam Davis', 'liam.davis@email.com', 'Event organizer for high-profile tech expos and startup showcases.'),
        (40, 'Ella Robinson', 'ella.robinson@email.com',
         'Health and wellness retreat planner, focused on mental and physical well-being.'),
        (41, 'Samuel Harris', 'samuel.harris@email.com',
         'Photography exhibitions organizer, curating collections of visual art from photographers.'),
        (42, 'Charlotte Martin', 'charlotte.martin@email.com',
         'Cultural and arts festival organizer, celebrating the creative arts in all forms.'),
        (43, 'Isaac Young', 'isaac.young@email.com',
         'Smart city and tech innovation event planner, bringing together urban planners and tech experts.'),
        (44, 'Scarlett White', 'scarlett.white@email.com',
         'Educational workshop organizer, teaching students and professionals through engaging seminars.'),
        (45, 'Benjamin Lee', 'benjamin.lee@email.com',
         'Crafts fair organizer, offering handmade and unique artisan goods to the public.'),
        (46, 'Ella Harris', 'ella.harris@email.com',
         'Cultural exchange event planner, facilitating international dialogue through events.'),
        (47, 'David Clark', 'david.clark@email.com',
         'Health and fitness expo organizer, focusing on wellness and active living.'),
        (48, 'Ella Allen', 'ella.allen@email.com',
         'Gala event planner, organizing high-profile charity and fundraising galas.'),
        (49, 'Charlotte Johnson', 'charlotte.johnson@email.com',
         'Sustainable living event coordinator, dedicated to green practices and eco-friendly products.'),
        (50, 'Henry Martin', 'henry.martin@email.com',
         'Tech conference coordinator, bringing tech experts together for innovation and networking.')
    ]

    for venue in venues:
        Venue.objects.create(
            name=venue[0],
            location=venue[1],
            capacity=venue[2],
            available_from=venue[3]
        )

    for organizer in organizers:
        Organizer.objects.create(
            name=organizer[1],
            contact_info=organizer[2],
            bio=organizer[3]
        )

class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_event_image'),
    ]

    operations = [ migrations.RunPython(populate_data)]
