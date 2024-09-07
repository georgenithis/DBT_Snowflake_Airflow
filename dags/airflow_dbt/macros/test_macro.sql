{% macro test_macro(execute=True) %}

    {% set test_var = var('aws_secret_key') %}
    {% if execute %}
        {{ print(test_var) }}
    {% endif %}
{% endmacro %}
