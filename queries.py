"""
queries.py
All 10 SQL queries for the Flight Booking System.

Team Name: [Your Team Name]
Student Numbers: [4395764, ...]
"""

QUERIES = {

    # ─────────────────────────────────────────────
    # SIMPLE QUERIES (2)
    # ─────────────────────────────────────────────

    "Q1 (Simple): List All Passengers Ordered by Surname": """
        SELECT passenger_id, first_name, surname, email_address, primary_phone
        FROM PASSENGER
        ORDER BY surname ASC, first_name ASC;
    """,

    "Q2 (Simple): Flights Departing from Cape Town (CPT)": """
        SELECT flight_number, departure_date_time, arrival_airport_code, base_fare
        FROM FLIGHT
        WHERE departure_airport_code = 'CPT'
        ORDER BY departure_date_time ASC;
    """,

    # ─────────────────────────────────────────────
    # MEDIUM QUERIES (4)
    # ─────────────────────────────────────────────

    "Q3 (Medium): Booking Details with Passenger and Flight Info": """
        SELECT
            b.booking_id,
            CONCAT(p.first_name, ' ', p.surname) AS passenger_name,
            f.flight_number,
            f.departure_date_time,
            b.fare_paid,
            b.booking_status
        FROM BOOKING b
        INNER JOIN PASSENGER p ON b.passenger_id = p.passenger_id
        INNER JOIN FLIGHT f ON b.flight_number = f.flight_number
        ORDER BY b.booking_date DESC;
    """,

    "Q4 (Medium): Number of Bookings per Flight": """
        SELECT
            f.flight_number,
            f.departure_date_time,
            COUNT(b.booking_id) AS total_bookings,
            SUM(b.fare_paid) AS total_revenue
        FROM FLIGHT f
        LEFT JOIN BOOKING b ON f.flight_number = b.flight_number
        GROUP BY f.flight_number, f.departure_date_time
        ORDER BY total_bookings DESC;
    """,

    "Q5 (Medium): Average Fare Paid per Airline": """
        SELECT
            al.airline_name,
            COUNT(b.booking_id) AS total_bookings,
            ROUND(AVG(b.fare_paid), 2) AS average_fare,
            MAX(b.fare_paid) AS highest_fare
        FROM AIRLINE al
        INNER JOIN AIRCRAFT ac ON al.airline_id = ac.airline_id
        INNER JOIN FLIGHT f ON ac.aircraft_id = f.aircraft_id
        INNER JOIN BOOKING b ON f.flight_number = b.flight_number
        GROUP BY al.airline_name
        ORDER BY average_fare DESC;
    """,

    "Q6 (Medium): Passengers with More Than One Booking": """
        SELECT
            p.passenger_id,
            CONCAT(p.first_name, ' ', p.surname) AS passenger_name,
            p.email_address,
            COUNT(b.booking_id) AS number_of_bookings
        FROM PASSENGER p
        INNER JOIN BOOKING b ON p.passenger_id = b.passenger_id
        GROUP BY p.passenger_id, p.first_name, p.surname, p.email_address
        HAVING COUNT(b.booking_id) > 1
        ORDER BY number_of_bookings DESC;
    """,

    # ─────────────────────────────────────────────
    # COMPLEX QUERIES (4)
    # ─────────────────────────────────────────────

    "Q7 (Complex): Passengers Who Booked the Most Expensive Flight": """
        SELECT
            p.passenger_id,
            CONCAT(p.first_name, ' ', p.surname) AS passenger_name,
            f.flight_number,
            b.fare_paid
        FROM PASSENGER p
        INNER JOIN BOOKING b ON p.passenger_id = b.passenger_id
        INNER JOIN FLIGHT f ON b.flight_number = f.flight_number
        WHERE b.fare_paid = (
            SELECT MAX(fare_paid) FROM BOOKING
        )
        ORDER BY passenger_name ASC;
    """,

    "Q8 (Complex): Airlines with Total Baggage Revenue Above 300": """
        SELECT
            al.airline_name,
            COUNT(DISTINCT bg.baggage_id) AS total_bags,
            SUM(bg.baggage_charge) AS total_baggage_revenue,
            ROUND(AVG(bg.baggage_charge), 2) AS average_baggage_fee
        FROM AIRLINE al
        INNER JOIN AIRCRAFT ac ON al.airline_id = ac.airline_id
        INNER JOIN FLIGHT f ON ac.aircraft_id = f.aircraft_id
        INNER JOIN BOOKING b ON f.flight_number = b.flight_number
        INNER JOIN BAGGAGE bg ON b.booking_id = bg.booking_id
        GROUP BY al.airline_name
        HAVING SUM(bg.baggage_charge) > 300
        ORDER BY total_baggage_revenue DESC;
    """,

    "Q9 (Complex): Flights Priced Above Their Departure Airport Average": """
        SELECT
            f.flight_number,
            f.departure_airport_code,
            ap.airport_name,
            f.base_fare,
            (SELECT ROUND(AVG(f2.base_fare), 2)
             FROM FLIGHT f2
             WHERE f2.departure_airport_code = f.departure_airport_code) AS airport_avg_fare
        FROM FLIGHT f
        INNER JOIN AIRPORT ap ON f.departure_airport_code = ap.airport_code
        WHERE f.base_fare > (
            SELECT AVG(f2.base_fare)
            FROM FLIGHT f2
            WHERE f2.departure_airport_code = f.departure_airport_code
        )
        ORDER BY f.departure_airport_code, f.base_fare DESC;
    """,

    "Q10 (Complex): Upcoming Flight Revenue Summary": """
        SELECT
            f.flight_number,
            ap.airport_name AS departure_airport,
            f.departure_date_time,
            COUNT(DISTINCT b.booking_id) AS confirmed_passengers,
            COALESCE(SUM(b.fare_paid), 0) AS ticket_revenue,
            COALESCE(SUM(bg.baggage_charge), 0) AS baggage_revenue,
            COALESCE(SUM(b.fare_paid), 0) + COALESCE(SUM(bg.baggage_charge), 0) AS total_revenue
        FROM FLIGHT f
        INNER JOIN AIRPORT ap ON f.departure_airport_code = ap.airport_code
        LEFT JOIN BOOKING b ON f.flight_number = b.flight_number
            AND b.booking_status = 'Confirmed'
        LEFT JOIN BAGGAGE bg ON b.booking_id = bg.baggage_id
        WHERE f.departure_date_time > NOW()
        GROUP BY f.flight_number, ap.airport_name, f.departure_date_time
        HAVING COUNT(DISTINCT b.booking_id) > 0
        ORDER BY total_revenue DESC;
    """,
}