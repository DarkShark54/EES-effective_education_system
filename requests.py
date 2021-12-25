def client_authorization(data_base=None, data=None):
    data_base.connection_to_base()
    text_request = """SELECT teacher.id as AUTORIZED
                    FROM teacher
                    WHERE teacher.fio = {fio} AND teacher.password = {password};""".format(fio=data[0],
                                                                                           password=data[1])
    records = data_base.post_request(text_request)
    data_base.close_to_base()
    return records


def get_client_data(data_base=None, data=None):
    data_base.connection_to_base()
    text_request = """SELECT teaching_class.id_subject, subject.name AS name_subject, teaching_class.class
                    FROM teaching_class LEFT JOIN subject ON id_subject = subject.id
                    WHERE teaching_class.id_teacher = {teacher_id};""".format(teacher_id=data)
    records = data_base.post_request(text_request)
    data_base.close_to_base()
    dict_of_subj_classes = {}
    for record in records:
        if str(record[0]) + ' ' + record[1] in dict_of_subj_classes.keys():
            dict_of_subj_classes[str(record[0]) + ' ' + record[1]].append(record[2])
        else:
            dict_of_subj_classes[str(record[0]) + ' ' + record[1]] = [record[2]]
    return dict_of_subj_classes


def get_subj_theme(data_base=None, data=None):
    data_base.connection_to_base()
    text_request = """SELECT theme.id AS theme_id, 
                             theme.name AS theme_name,
                CASE WHEN theme.id_parent IS NULL THEN 'parent' ELSE 'son' END AS kinship,
                CASE WHEN themeP IS NULL THEN NULL ELSE themeP.id END as parent_id,
                CASE WHEN themeP IS NULL THEN NULL ELSE themeP.name END AS parent_name
                FROM theme LEFT JOIN subject On theme.id_subject = subject.id 
                           LEFT JOIN theme AS themeP ON theme.id_parent = themeP.id
                WHERE subject.id = {subj_id}""".format(subj_id=data)
    records = data_base.post_request(text_request)
    data_base.close_to_base()
    dict_of_theme_subtopic = {}
    for record in records:
        if record[2] == "parent" and not (str(record[0]) + ' ' + record[1] in dict_of_theme_subtopic.keys()):
            dict_of_theme_subtopic[str(record[0]) + ' ' + record[1]] = []
        elif record[2] == "son" and str(record[3]) + ' ' + record[4] in dict_of_theme_subtopic.keys():
            dict_of_theme_subtopic[str(record[3]) + ' ' + record[4]].append(str(record[0]) + ' ' + record[1])
        elif record[2] == "son" and not (str(record[3]) + ' ' + record[4] in dict_of_theme_subtopic.keys()):
            dict_of_theme_subtopic[str(record[3]) + ' ' + record[4]] = []
            dict_of_theme_subtopic[str(record[3]) + ' ' + record[4]].append(str(record[0]) + ' ' + record[1])
    return dict_of_theme_subtopic


def get_st_marks(data_base=None, data=None):
    data_base.connection_to_base()
    text_request = """SELECT 
                    achievement.id_stud, student.fio, achievement.mark
                    FROM 
                    achievement LEFT JOIN student on student.id = achievement.id_stud
                    WHERE 
                    achievement.id_theme = {id_theme} AND student.class = '{class_name}'""".format(id_theme=data[0],
                                                                                                   class_name=data[1])
    records = data_base.post_request(text_request)
    data_base.close_to_base()
    return records


requests_list = {"GET": {"data_client": get_client_data, "subj_theme": get_subj_theme, "students_marks": get_st_marks},
                 "POST": {"authorization": client_authorization}}


