# build-sageattention3

Pre-built Linux wheels for [SageAttention3](https://github.com/thu-ml/SageAttention)'s Blackwell
implementation, across Python, PyTorch, CUDA, and CPU architectures.

## Installation

Following the PyTorch convention, artifacts are published to a separate index for each CUDA
version. Each wheel has a local version suffix that identifies the CUDA, PyTorch, and C++ ABI it
was built against, such as `sageattn3==2.2.0+cu12.8torch2.10.0cxx11abiTRUE`, and requires the
matching PyTorch release. SageAttention3 requires CUDA 12.8 or later and targets Blackwell GPUs.

Pre-built wheels are available on [Astral's GPU indexes](https://pub-ca5ccdc72d7a4f9e9f2af5929bdf5083.r2.dev/index.html).
For example, to install a CUDA 12.8 build:

```console
$ uv add sageattn3 --index astral-cu128=https://pub-ca5ccdc72d7a4f9e9f2af5929bdf5083.r2.dev/simple/cu128/
```

This configures the index and uses it as the source for `sageattn3`:

```toml
[tool.uv.sources]
sageattn3 = { index = "astral-cu128" }

[[tool.uv.index]]
name = "astral-cu128"
url = "https://pub-ca5ccdc72d7a4f9e9f2af5929bdf5083.r2.dev/simple/cu128/"
```

Or, with `uv pip`:

```console
$ uv pip install --index https://pub-ca5ccdc72d7a4f9e9f2af5929bdf5083.r2.dev/simple/cu128/ sageattn3
```

## Supported versions

Wheels are available for the following `sageattn3` versions:

- [`2.2.0`](https://github.com/astral-sh-build/build-sageattention3/releases/tag/v2.2.0-r1)

The latest release, SageAttention3 2.2.0, publishes pre-built wheels for the following combinations:

| PyTorch | Python | `x86_64` CUDA    | `aarch64` CUDA   |
| ------- | ------ | ---------------- | ---------------- |
| 2.7.1   | 3.13   | 12.8             | 12.8             |
| 2.8.0   | 3.13   | 12.8, 12.9       | 12.9             |
| 2.9.0   | 3.14   | 12.8, 12.9, 13.0 | 12.8, 12.9, 13.0 |
| 2.10.0  | 3.14   | 12.8, 12.9, 13.0 | 12.8, 12.9, 13.0 |

## License

build-sageattention3 is licensed under the [Apache License, Version 2.0](LICENSE).

<div align="center">
  <a target="_blank" href="https://astral.sh" style="background:none">
    <img src="https://raw.githubusercontent.com/astral-sh/ruff/main/assets/svg/Astral.svg" alt="Made by Astral">
  </a>
</div>
