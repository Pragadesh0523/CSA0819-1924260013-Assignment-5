def valid_email(email):
    email = email.strip()

    if email.count('@') != 1:
        return False

    user, domain = email.split('@')

    return (
        len(user) > 0 and
        '.' in domain and
        not domain.startswith('.') and
        not domain.endswith('.')
    )