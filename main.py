def hello(name="GitHub Actions", lastname=None):
    if not isinstance(name, str):
        raise TypeError("Le nom doit être une chaîne")

    # Supprime ou commente cette ligne après le test de gestion d'erreur
    # raise ValueError("Erreur volontaire")  
    if lastname:
        return f"Hello, {name} {lastname} !"
    
    return f"Hello, {name} !"  # Assure-toi d'avoir l'espace avant le point d'exclamation
