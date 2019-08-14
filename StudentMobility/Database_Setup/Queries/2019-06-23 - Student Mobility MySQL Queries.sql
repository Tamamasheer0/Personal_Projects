-- Initialize Student Mobility Database --
USE student_mobility;


-- [Query #1] Select All Records From 'Students' Table --
SELECT * FROM students;

-- [Query #2] Select All Records From 'Schools' Table -- 
SELECT * FROM schools;

-- [Query #3] Select All Records From 'Student_Records' Table --
SELECT * FROM records;

-- [Query #4] Select All Records From 'Student_Programs --
SELECT* FROM programs;

-- [Query #5] Count All Records From 'Students' Table --
SELECT COUNT(*) FROM students;

-- [Query #6] Count All Records From 'Student_Records' Table --
SELECT COUNT(*) as total_student_records
FROM records;

-- [Query #7] Select All Student ID's & Grade Level From School Selected School --
SELECT * 
FROM records
WHERE student_school_id = 40;

/* [Query #8]
Select Students Based:
	- School
    - Single Exit Reason
*/ 
SELECT student_id, grade_level
FROM records
WHERE (school_id = 40) AND
	  (exit_reason = 230);

-- [Query #9] List Studetents Who Are Enrolled In School Programs -- 
SELECT sr.id, sr.program_id, sr.grade_level
FROM records as sr
WHERE sr.student_program_id != 'N/A';

-- [Query #10] Counts # of Students Enrolled in School Programs --
SELECT COUNT(sr.student_id) as student_enrollemnt
FROM records as sr
WHERE sr.program_id != 'N/a';

/* [Query #10]
Count the Student Enrollment in Student Programs
Sort Them Highest to Lowest
*/
SELECT sp.program_id,
COUNT(sr.student_id) as program_enrollment
FROM records as sr
INNER JOIN programs as sp
		ON sp.id = sr.program_id
GROUP BY sp.program_id
ORDER BY program_enrollment DESC;


 /*
 
		*** TO DELETE STUDENT MOBILITY DATABASE AND ALL RECORDS ***
						(Uncomment Query to Use)
                        
DROP DATABASE IF EXISTS student_mobility;


*/

DROP DATABASE IF EXISTS student_mobility;


