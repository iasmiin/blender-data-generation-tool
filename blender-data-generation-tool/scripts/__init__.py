bl_info = {
    "name": "Ferramenta de Geração de Dados Sintéticos",
    "blender": (3, 0, 0),
    "category": "Object",
    "version": (1, 0),
    "author": "Seu Nome",
    "description": "Ferramenta para geração de dados sintéticos aumentados no Blender.",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
}

from . import main

def register():
    main.register()

def unregister():
    main.unregister()