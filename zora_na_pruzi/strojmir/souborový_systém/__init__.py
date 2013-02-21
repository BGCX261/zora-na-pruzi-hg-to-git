
def změním_příponu(jméno,  přípona):
    import os
    return '{}.{}'.format(os.path.splitext(jméno)[0],  přípona)
