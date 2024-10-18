----Selecting username from user table (to display on profile page)----

SELECT 'username'
FROM user
WHERE 
user_id = ''

----Selecting name from tutor (to display on tutor profile page)----

SELECT 'name'
FROM tutor
WHERE 
tutor_id = ''

----Deleting account (tutor and learner)----

DELETE 
FROM user 
WHERE user_id = ''

----Create Account----

INSERT INTO user (user_id, username, name, profile_pic, email, password)
VALUES ('','','','','')


----Delete Course----

DELETE 
FROM course 
WHERE course_id = ''


----Create new course (rating and enrolled will always start at 0)

INSERT INTO course (course_id, course_name, price, sessions, picture, course_rating, enrolled, tutor_id)
VALUES ('','','')


----Ordering courses by rating----

SELECT course_name, course_rating, picture
FROM course
ORDER BY course_rating DESC


----Ordering courses by number of learners enrolled----

SELECT course_name, course_rating, picture, COUNT(enrolled)
FROM course
ORDER BY COUNT(enrolled) DESC


---Ordering courses by price of course----

SELECT course_name, course_rating, picture, COUNT(price)
FROM course 
ORDER BY COUNT(price) DESC


----Updating number of enrolled after new learner joins course----

ALTER TABLE course 


----Updating number of enrolled after new learner leaves course, is removed from course or deletes their account----


ALTER TABLE course 
