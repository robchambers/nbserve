{%- extends 'full.tpl' -%}

{% block input_group -%}
{% endblock input_group %}

{% block in_prompt -%}
{%- endblock in_prompt %}

{% block empty_in_prompt -%}
{%- endblock empty_in_prompt %}

{% block output %}
{{ super.super() }}
{% endblock output %}