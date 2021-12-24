import view as v

requests_list = {"GET": {"data_client": v.get_client_data, "subj_theme": v.get_subj_theme, "students_marks": v.get_st_marks},
                 "POST": {"authorization": v.client_authorization}}

