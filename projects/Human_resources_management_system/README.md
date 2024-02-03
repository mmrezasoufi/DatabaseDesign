# Human Resource Management System

# ERD
![hrms ER Diagram](https://raw.githubusercontent.com/ArmanLK/DatabaseDesign/main/projects/Human_resources_management_system/hrms_diagram.png)

# Normalization
Every table besides `buildings_has_departmend`, `personels_has_meetings` and `courses_has_personels` has an integer id as their primarly key and they don't have any other condidate keys. for those other three table mentioned they are all either created by only keys or there is the score value with has only functional dependancy `course_id personel_id -> score` and is only dependent to it's primarly key.

With arguments mentioned above we only need to prove this shema is in 3rd Normal Form.

There is no functional dependencies between non-prime atributes, so schema is in 3rd Normal Form and thus is in BCNF
