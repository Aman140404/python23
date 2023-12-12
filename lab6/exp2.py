class student:
    def per(m1, m2, m3):
        tot = m1+m2+m3
        per = ((tot)/300)*100
        if per >= 33:
            return ("pass")
        else:
            return ("fail")


print(student.per(33, 64, 45))
