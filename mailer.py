def send_mail(to, subject, body, test_mode=True):
    if test_mode:
        print(f"📧 TEST MAIL naar {to}: {subject}")
        return
    # Voeg hier SMTP code toe voor live mails
