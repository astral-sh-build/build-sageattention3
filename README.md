# build-sageattention3

Pre-built Linux wheels for [SageAttention3](https://github.com/thu-ml/SageAttention)'s Blackwell
implementation, across Python, PyTorch, CUDA, and CPU architectures.

## Installation

Following the PyTorch convention, artifacts are published to a separate index for each CUDA
version. Each wheel has a local version suffix that identifies the CUDA and PyTorch versions it
was built against, such as `sageattn3==2.2.0+cu.12.8.torch.2.10`, and requires the
matching PyTorch release. SageAttention3 requires CUDA 12.8 or later and targets
Blackwell GPUs with compute capability 12.0 or later.

Pre-built wheels are available on [Astral's GPU indexes](https://wheels.astral.sh/index.html).
For example, to install a CUDA 12.8 build:

```console
$ uv add sageattn3 --index astral-cu128=https://wheels.astral.sh/simple/cu128/
```

This configures the index and uses it as the source for `sageattn3`:

```toml
[tool.uv.sources]
sageattn3 = { index = "astral-cu128" }

[[tool.uv.index]]
name = "astral-cu128"
url = "https://wheels.astral.sh/simple/cu128/"
```

Or, with `uv pip`:

```console
$ uv pip install --index https://wheels.astral.sh/simple/cu128/ sageattn3
```

## GPU tests

The `tests/` directory contains a locked uv project that installs the published CUDA 12.8 wheel from the Astral index
alongside its matching CUDA-enabled PyTorch build. Run the tests on a Modal GPU with:

```console
$ modal run tests/modal_app.py
```

Modal installs the locked dependencies in its Linux image and runs the pytest
suite on an NVIDIA B200. The wheel is not installed on the local machine.

## Supported versions

Wheels are available for the following `sageattn3` versions:

- [`2.2.0`](https://github.com/astral-sh-build/build-sageattention3/releases/tag/v2.2.0-r1)

The latest release, SageAttention3 2.2.0, publishes pre-built wheels for the following combinations:

| PyTorch | Python    | `x86_64` CUDA    | `aarch64` CUDA   |
| ------- | --------- | ---------------- | ---------------- |
| 2.8.0   | 3.13      | 12.8, 12.9       | 12.9             |
| 2.9.1   | 3.13      | 12.8, 12.9, 13.0 | 12.8, 12.9, 13.0 |
| 2.10.0  | 3.13–3.14 | 12.8, 12.9, 13.0 | 12.8, 12.9, 13.0 |
| 2.11.0  | 3.13–3.14 | 12.8, 12.9, 13.0 | 12.8, 12.9, 13.0 |
| 2.12.1  | 3.13–3.14 | 13.0, 13.2       | 13.0, 13.2       |

## License

build-sageattention3 is licensed under the [Apache License, Version 2.0](LICENSE).

<div align="center">
  <a target="_blank" href="https://astral.sh" style="background:none">
    <img src="https://raw.githubusercontent.com/astral-sh/ruff/main/assets/svg/Astral.svg" alt="Made by Astral">
  </a>
</div>
