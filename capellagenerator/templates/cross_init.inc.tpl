{% macro insertion(classes) -%}
{% for c in classes %}
{{ c | pyfqn }}.eClass,
{%- endfor %}
{%- endmacro %}
#print('{{ element.name }}.cross_init starting')



{% if not element.eSuperPackage %}
    {%- for e in element | all_contents(ecore.EReference) | rejectattr('eOpposite') %}
{{ e.eContainingClass | pyfqn }}.{{ e | derivedname }}.eType ={{ e.eType | pyfqn }}
    {%- endfor %}
    {%- with opposites = element | all_contents(ecore.EReference) | selectattr('eOpposite') | list %}
        {%- for e in opposites %}
{{ e.eContainingClass | pyfqn }}.{{ e | derivedname }}.eType = {{ e.eType| pyfqn }}
            {%- if e is opposite_before_self(opposites) %}
{{ e.eContainingClass | pyfqn }}.{{ e | derivedname }}.eOpposite = {{ e.eOpposite.eContainingClass | pyfqn }}.{{ e.eOpposite | derivedname }}
            {%- endif %}
        {%- endfor %}
    {%- endwith %}
{%- endif %}

{% for c, inheritances in circular_inheritances.items() %}
{{ c | pyfqn }}._staticEClass = False
{{ c | pyfqn }}.eClass.eSuperTypes.extend(({{ insertion(c.eSuperTypes) }}
))
{% endfor %}

#print('{{ element.name }}.cross_init done')
