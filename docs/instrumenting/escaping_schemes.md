---
title: UTF-8 metric and label name escaping schemes
nav_title: UTF-8 escaping schemes
sort_rank: 7
---

## Abstract

* goal
  * escaping schemes / used by Prometheus | generate metric & label names / contain characters -- outside the -- legacy character set
    * legacy character set -- (a-zA-Z0-9\_:) --
    * specified -- via -- `escaping` parameter | `-H Accept` & `-H Content-Type`

## Introduction

* escaping scheme
  * negotiated | scraping
    * -> how metric producers should format their metric names

## Escaping Schemes

### No Escaping (allow-utf-8)

* **Header Value**: `escaping=allow-utf-8`
* **Behavior**:
  - Metric & label names
    - MUST be UTF-8 strings
  - if names appear | 
    - double quotes | exposition format -> `\`, `\n` and `"` MUST be escaped with `\`
    - unquoted | exposition format -> `\` and `\n` MUST be escaped with `\`
  - ⚠️requirements⚠️
    - producer & consumer support UTF-8 names

### Underscore Escaping (underscores)

* **Header Value**: `escaping=underscores`
* **Behavior**:
  - character / NOT | legacy character set -> replace with `_`
  - first character MUST be: letter, underscore, or colon
  - Subsequent characters MUST be: letters, numbers, underscores, or colons.
  - _Example:_ `metric.name/with/slashes` -> `metric_name_with_slashes`

### Dots Escaping (dots)

* **Header Value**: `escaping=dots`
* **Behavior**:
  - `.` -> MUST be replaced with `_dot_`
  - `_` -> MUST be replaced with `__`
  - OTHER NON-legacy characters MUST be replaced with `_`
  - FIRST character MUST be: letter, underscore, or colon.
  - Subsequent characters MUST be: letters, numbers, underscores, or colons.
  - _Example:_ `metric.name.with.dots` -> `metric_dot_name_dot_with_dot_dots`

### Value Encoding Escaping (values)

* **Header Value**: `escaping=values`
* **Behavior**:
  - name MUST be prefixed with `U__`
  - EACH character / NOT legacy character set -> MUST be replaced with `_relatedUnicodePointHexadecimal_`
  - `_` MUST be replaced with `__`
  - _Example:_ `metric.name` -> `U__metric_2E_name`

## Default Behavior

* == NO escaping scheme is specified | `-H Accept`
* `underscores`

## Security Considerations

1. BEFORE applying escaping, Targets MUST validate input names 
2. validate escaping scheme
  * Reason:🧠prevent injection attacks🧠
3. `allow-utf-8` scheme MUST only be used | producer & consumer support UTF-8 names
