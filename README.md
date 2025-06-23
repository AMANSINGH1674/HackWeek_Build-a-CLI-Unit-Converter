# CLI Unit Converter

A simple Python CLI tool to convert temperature between Celsius and Fahrenheit.

## Usage

```bash
python unit_converter.py <value> --to <unit>
```

- `<value>`: The temperature value to convert (float or int).
- `--to <unit>`: The unit to convert to. Must be either `celsius` or `fahrenheit`.

### Examples

Convert 100 Celsius to Fahrenheit:
```bash
python unit_converter.py 100 --to fahrenheit
```

Convert 32 Fahrenheit to Celsius:
```bash
python unit_converter.py 32 --to celsius
``` 