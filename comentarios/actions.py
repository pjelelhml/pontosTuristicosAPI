def reprova_comentarios(modelAdmin, request, queryset):
    queryset.update(aprovado=False)

def aprova_comentarios(modelAdmin, request, queryset):
    queryset.update(aprovado=True)

reprova_comentarios.short_description = 'Reprovar comentarios'
aprova_comentarios.short_description = 'Aprovar comentários'