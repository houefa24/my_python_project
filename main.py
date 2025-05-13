def hello(name="GitHub Actions", lastname=None):
    if not isinstance(name, str):
        raise TypeError("Le nom doit être une chaîne")
    
    if lastname:
        return f"Hello, {name} {lastname} !"
    
    return f"Hello, {name} !"