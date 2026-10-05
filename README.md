# quant-foundations

Primer proyecto de autoaprendizaje centrado en los fundamentos de las finanzas cuantitativas.

Todo el código usa datos públicos o simulados.

## Estructura

- `src/qf/`: código reutilizable (paquete `qf`)
- `notebooks/`: notebooks de estudio y experimentos
- `tests/`: tests con pytest

## Instalación

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate    |    macOS/Linux: source .venv/bin/activate
pip install -e ".[dev]"   # dependencias de pyproject.toml
```

## Uso

Ejecutar los tests:

```bash
pytest
```

Abrir los notebooks:

```bash
jupyter notebook notebooks/
```
