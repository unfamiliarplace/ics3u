# Email
# https://dmoj.ca/problem/ecoo19r2p1
# Solution B

def sanitize_email(email: str) -> str:
    """
    Return a sanitized version of the given email address.
    
    Sanitization means:
    - Lowercase the email.
    - Remove any dots before the @ sign.
    - If there is a + followed by any sequence before the @ sign,
      the + and following sequence should be removed.
      
    >>> sanitize_email('foo@bar.com')
    'foo@bar.com'
    >>> sanitize_email('fO.o+baz123@bAR.com')
    'foo@bar.com'
    """
    email = email.lower()

    # Separate the @ symbol to the end
    at_onwards = email[email.index('@'):]
    
    # Clean up the part up to the @
    up_to_at = ''
    
    for char in email:

        # If we hit one of these stop
        if char in ['+', '@']:
            break

        # Otherwise add anything but . to our clean version
        elif char != '.':
            up_to_at += char
    
    # Re-add from the @ to the end
    email = up_to_at + at_onwards
    return email

# There are 10 datasets, meaning the whole program should be wrapped in range(10)
for _ in range(10):
    n_emails = int(input())
    emails = set()
    
    for _ in range(n_emails):
        email = input()
        email = sanitize_email(email)
        emails.add(email)
    
    print(len(emails))
