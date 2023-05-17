def solution(id_pw, db):
    for db_id, db_pw in db:
        if id_pw[0] == db_id:
            if id_pw[1] == db_pw:
                return "login"
            return "wrong pw"
    return "fail"        