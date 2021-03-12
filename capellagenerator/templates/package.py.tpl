#print('{{ element.name }}.__init__.py loading')
{% if auto_register_package -%}
    from pyecore.resources import global_registry
{%- endif %}
from .{{ element.name }} import getEClassifier, eClassifiers
from .{{ element.name }} import name, nsURI, nsPrefix, eClass
{% if element.eClassifiers -%}
    from .{{ element.name }} import {{ element.eClassifiers  | map(attribute='name') | sort | join(', ') }}
{%- endif %}
from . import {{ element.name }}

{%- if element.eSuperPackage %}
from .. import {{ element.eSuperPackage.name }}
{% endif %}

{%- for sub in element.eSubpackages %}
from . import {{ sub.name }}
{% endfor %}

__all__ = [{{ element.eClassifiers | map(attribute='name') | sort | map('pyquotesingle') | join(', ')  }}]

eSubpackages = [{{ element.eSubpackages  | map(attribute='name') | sort |  join(', ') }}]
eSuperPackage = {{ element.eSuperPackage.name | default('None') }}
{{ element.name }}.eSubpackages = eSubpackages
{{ element.name }}.eSuperPackage = eSuperPackage

otherClassifiers = [{{ element.eClassifiers | select('kind', ecore.EDataType) | map(attribute='name') | join(', ') }}]

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
{% if auto_register_package %}
register_packages = [{{ element.name }}] + eSubpackages
for pack in register_packages:
    global_registry[pack.nsURI] = pack

{% endif %}
#print('{{ element.name }}.__init__.py loaded')
