# xorjson

`xorjson` is a fork of [`orjson`](https://github.com/ijl/orjson) with the following changes:

- Smaller CI/CD to ease fork maintenance - not all platforms supported
- Default to str for Unknown objects as keys when using `OPT_NON_STR_KEYS` ([#454](https://github.com/ijl/orjson/pull/454))

[![artifact](https://github.com/timkpaine/xorjson/actions/workflows/artifact.yaml/badge.svg?branch=main&event=push)](https://github.com/timkpaine/xorjson/actions/workflows/artifact.yaml)
[![PyPI](https://img.shields.io/pypi/l/xorjson.svg)](https://pypi.python.org/pypi/xorjson)
