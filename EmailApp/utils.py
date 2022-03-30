def GetEmailSubject(formfields):
    subject = ''
    for formfield in formfields:
        field_name = formfield[0]
        field_value = formfield[1][0]
        subject += f'{field_name}:{field_value},                                                                                                                '
    return subject